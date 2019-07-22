from datetime import datetime
from demo.models import FACTORY_PRICE,ASSET_PRICE,WEIGHT,ASSET_TYPE,ASSET_VARITY,FACTORY_TYPE,COMMON_INFORMATION,BOND,HISTORICAL_RATIO
from demo.Modules.module6 import M6
from demo.Modules.module5 import M5
from decimal import Decimal
"""
本模块负责与资产有关的操作
"""

""" 
假设时间单元为N天，最后一天为M
day1   dayN    day2N......dayM-1  dayM   
f3     f3      f3         f3      f3
f1     f1      f1         f1
f2     f2      f2         f2

"""

class M1(object):

    # [f1] 更新资产占比
    def update_asset_ratio(former_date,current_date):

        # 根据权重公式生成各资产占比
        for item in ASSET_TYPE.objects.all():
            asset_ratio=0
            weights = WEIGHT.objects.filter(asset_type_id=item.id)
            for item2 in weights:

                # 计算exchange_rate
                factory_item = FACTORY_TYPE.objects.get(id=item2.factory_type_id)

                former_price = FACTORY_PRICE.objects.filter(factory_type_id=factory_item.id).get(date=former_date).price
                current_price=FACTORY_PRICE.objects.filter(factory_type_id=factory_item.id).get(date=current_date).price

                exchange_rate=(current_price-former_price)/former_price

                # 计算ratio
                asset_ratio+=exchange_rate*item2.value

            # 更新ratio
            ASSET_TYPE.objects.filter(id=item.id).update(ratio=asset_ratio)
            #ASSET_TYPE.objects.filter(id=item.id).update(ratio=0.02)

        for item in ASSET_TYPE.objects.all():

            # 占比为负，则说明不应该投资该资产，将占比赋值为0
            if item.ratio<0:
                ASSET_TYPE.objects.filter(id=item.id).update(ratio=0)

        #记录历史资产比例
        stock_ratio=ASSET_TYPE.objects.get(id=1).ratio
        futures_ratio=ASSET_TYPE.objects.get(id=2).ratio
        bond_ratio=1-stock_ratio-futures_ratio
        HISTORICAL_RATIO.objects.create(Stock_Ratio=stock_ratio,Futures_Ratio=futures_ratio,Bond_Ratio=bond_ratio)
        

    # [f2] 根据资产占比调整仓位，分配资金
    def position_adjust(current_date):

        # 获取总资本
        sum_cap = COMMON_INFORMATION.objects.get(id=1).sum_cap

        # 计算sum_ratio
        sum_ratio=0
        # 先计算期货和股票的总sum_ratio
        for item in ASSET_TYPE.objects.all():
            sum_ratio+=item.ratio

        # 调整不同类型资产的仓位
        for item2 in ASSET_TYPE.objects.all():

            # 计算新ratio，cap
            if sum_ratio>1:
                now_ratio=item2.ratio/sum_ratio
            else:
                now_ratio = item2.ratio
            now_cap = now_ratio * sum_cap

            # 计算该类型资产增值还是减值，用于指导不同资产品种的投资量动态调整
            cap_gap = now_cap-item2.cap

            # 更新ratio与cap
            ASSET_TYPE.objects.filter(id=item2.id).update(ratio=now_ratio)
            ASSET_TYPE.objects.filter(id=item2.id).update(cap=now_cap)

            templist = ASSET_VARITY.objects.filter(asset_type_id=item2.id)

            varity_count=ASSET_VARITY.objects.filter(asset_type_id=item2.id).count()

            # 若该类型资产增值，则由小至大调整属于该类型的不同品种资产投资金额
            if cap_gap>0:
                if varity_count==1:#等于1为中证500
                    varity_cap=ASSET_VARITY.objects.get(asset_type_id=item2.id).cap+cap_gap
                    ASSET_VARITY.objects.filter(asset_type_id=item2.id).update(cap=varity_cap)
                else:
                    M6.adjust(cap_gap,templist)

            else:
                cap_gap = -cap_gap
                if varity_count==1:
                    varity_cap=ASSET_VARITY.objects.get(asset_type_id=item2.id).cap-cap_gap
                    ASSET_VARITY.objects.filter(asset_type_id=item2.id).update(cap=varity_cap)

                else:
                    M6.adjust_reverse(cap_gap, templist)

            #更新各资产对应的数量
            for item3 in ASSET_VARITY.objects.filter(asset_type_id=item2.id):
                item_varity_price=ASSET_PRICE.objects.filter(asset_varity_id=item3.id).get(date=current_date).price
                item_varity_amount=item3.cap/item_varity_price
                ASSET_VARITY.objects.filter(asset_type_id=item2.id).filter(id=item3.id).update(amount=item_varity_amount)
                #print(item_varity_amount)

        # sum_ratio>1时，调整为1
        if sum_ratio>1:
            sum_ratio=1

        # 剩余即为债券所占比例，以此更新bond表
        bond_ratio=1-sum_ratio
        bond_cap=sum_cap*bond_ratio
        BOND.objects.all().update(ratio=bond_ratio)
        BOND.objects.all().update(cap=bond_cap)


    # [f3] 更新资产值
    def update_asset_cap(current_date,bond_date_list):

        # 计算各个类型及品种资产当前总值
        sum_cap=0
        for item in ASSET_TYPE.objects.all():
            item_type_cap=0
            for item2 in ASSET_VARITY.objects.filter(asset_type_id=item.id):
                item_varity_cap=ASSET_PRICE.objects.filter(asset_varity_id=item2.id).get(date=current_date).price*item2.amount

                # 更新ASSET_VARITY的cap
                ASSET_VARITY.objects.filter(id=item2.id).update(cap=item_varity_cap)
                item_type_cap += item_varity_cap

            # 更新ASSET_TYPE的cap
            ASSET_TYPE.objects.filter(id=item.id).update(cap=item_type_cap)#分别更新了股票和期货的资产总值
            sum_cap+=item_type_cap

        # 计算债券累计收益
        bond_sum_cap=BOND.objects.get(id=1).cap
        for item3 in bond_date_list:
            bond_date = datetime.strptime(item3, '%Y-%m-%d')
            bond_date_rate=FACTORY_PRICE.objects.filter(factory_type_id=3).get(date=bond_date).price
            bond_date_rate=bond_date_rate/365
            bond_sum_cap+=bond_sum_cap*bond_date_rate

        # 更新BOND的cap
        BOND.objects.filter(id=1).update(cap=bond_sum_cap)
        sum_cap+=bond_sum_cap

        # 计算收益
        former_sum_cap=COMMON_INFORMATION.objects.get(id=1).sum_cap
        income=sum_cap-10000000

        # 更新common_information表
        COMMON_INFORMATION.objects.all().update(sum_cap=sum_cap) # 更新资产总市值
        COMMON_INFORMATION.objects.all().update(income=income) # 更新收益


    # 运行历史回测
    def historical_backtest():

        # current_sum_cap = COMMON_INFORMATION.objects.get(id=1).sum_cap

        cap_list=[]

        # 获取开始日期和结束日期  
        start_date= COMMON_INFORMATION.objects.get(id=1).start_date      
        end_date= COMMON_INFORMATION.objects.get(id=1).end_date

        # 获取时间单元
        time_space=COMMON_INFORMATION.objects.get(id=1).time_space

        # 获取回测时间列表
        historical_date_list=M5.get_test_date_range(str(start_date),str(end_date),time_space)

        for index in range(len(historical_date_list)):

            # 第一天，不执行任何操作
            if index==0:
                former_date=historical_date_list[index] 

            # 中间过程：每到达一个时间单元，执行f3，f1，f2
            elif index<len(historical_date_list)-1:

                # 更新current_date
                current_date = historical_date_list[index]

                # 执行f3，f1，f2
                bond_date_list=M5.get_date_range(former_date,current_date)
                M1.update_asset_cap(current_date,bond_date_list)

                # 测试
                current_sum_cap=COMMON_INFORMATION.objects.get(id=1).sum_cap
                cap_list.append(current_sum_cap)

                M1.update_asset_ratio(former_date, current_date)
                M1.position_adjust(current_date)

                # 更新former_date
                former_date = current_date

            # 到达最后一个时间单元
            else:

                # 执行f3
                bond_date_list = M5.get_date_range(former_date, current_date)
                M1.update_asset_cap(current_date, bond_date_list)

                # 测试
                current_sum_cap=COMMON_INFORMATION.objects.get(id=1).sum_cap
                cap_list.append(current_sum_cap)

        return cap_list

    # 重置操作，用于下次历史回测前
    def reset_data():
        #清空HISTORICAL_RATIO表中内容
        temp_ratio=HISTORICAL_RATIO.objects.all()
        for i in temp_ratio:
            i.delete()
        # ASSET_TYPE表重置
        ASSET_TYPE.objects.all().update(cap=0,ratio=0)

        # ASSET_VARITY表重置
        ASSET_VARITY.objects.all().update(cap=0, amount=0)

        # BOND表重置
        BOND.objects.all().update(cap=10000000,ratio=1)

        # FACTORY_TYPE表重置
        FACTORY_TYPE.objects.all().update(exchange_rate=0)

        # COMMON_INFORMATION表重置
        COMMON_INFORMATION.objects.all().update(sum_cap=0,income=0)

        # 默认开始时间和结束时间分别为'2018-2-10'和'2018-12-28'
        default_start_date = datetime.strptime('2018-10-2', '%Y-%m-%d')
        default_end_date = datetime.strptime('2018-10-10', '%Y-%m-%d')
        COMMON_INFORMATION.objects.all().update(start_date=default_start_date,end_date=default_end_date)

        # 默认初始资本为1000万
        default_sum_cap=10000000
        COMMON_INFORMATION.objects.all().update(sum_cap=default_sum_cap)

        # 默认时间单元为3天
        default_time_space=3
        COMMON_INFORMATION.objects.all().update(time_space=default_time_space)







