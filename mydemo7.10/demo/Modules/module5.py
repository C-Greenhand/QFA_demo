from datetime import datetime
from demo.models import ASSET_PRICE,FACTORY_PRICE,ASSET_VARITY,FACTORY_TYPE
import pandas as pd

"""
本模块负责与日期处理有关的操作
"""

class M5(object):

    # 判断表的日期数据有无周六周日
    def get_weekend(List):
        weekends=[]
        for item in List:
            if item.date.weekday()==5 or item.date.weekday()==6:
                weekends.append(item)
        return weekends

    # 剔除表中的周六周日记录
    def exclude_weekend(operate_type):
        if operate_type=='asset':
            for item in ASSET_PRICE.objects.all():
                if item.date.weekday()==5 or item.date.weekday()==6:
                    item.delete()
        else:
            for item in FACTORY_PRICE.objects.all():
                if item.date.weekday() == 5 or item.date.weekday() == 6:
                    item.delete()

    # 获取公共时间范围数组（不含周六周日），用以填充历史价格表
    def get_date_range(beginDate, endDate):


        # 获得完整日期范围，注意beginDate, endDate是形如‘20160601’或者'2016-0601'的字符串
        date_l = [datetime.strftime(x, '%Y-%m-%d') for x in list(pd.date_range(start=beginDate, end=endDate))]

        # 剔除周六周日
        date_2=[]
        for item in date_l:
            date=datetime.strptime(item, '%Y-%m-%d')
            if date.weekday()!=5 and date.weekday()!=6:
                date_2.append(item)

        return date_2 # 注意date_2为字符串数组

    # 根据公共日期范围为历史价格表填充缺省日期（非周六周日）记录
    def fill_date(operae_type):
        """
        pperation_type为'asset':对资产历史价格表进行处理
                      为'factory':对资产历史价格表进行处理
        """
        date_list=M5.get_date_range('20110418','20181228')

        if operae_type=='asset':
            for item in ASSET_VARITY.objects.all():
                varity_id=item.id
                asset_list=ASSET_PRICE.objects.filter(asset_varity_id=varity_id).order_by('date')
                current_price=asset_list.first().price
                for item2 in date_list:
                    date=datetime.strptime(item2, '%Y-%m-%d')

                    # 该日期记录缺省，且非周六周日,则插入新记录
                    if asset_list.filter(date=item2).count()==0 and date.weekday()!=5 and date.weekday()!=6:
                        asset_price = ASSET_PRICE();
                        asset_price.date = item2
                        asset_price.price = current_price
                        asset_price.asset_varity_id = varity_id
                        asset_price.save()

                    # 该日期记录存在，则更新current_price
                    if asset_list.filter(date=item2).count()==1:
                        current_price=asset_list.get(date=item2).price

        if operae_type=='factory':
            for item in FACTORY_TYPE.objects.all():
                type_id=item.id
                factory_list=FACTORY_PRICE.objects.filter(factory_type_id=type_id).order_by('date')
                current_price=factory_list.first().price
                for item2 in date_list:
                    date=datetime.strptime(item2, '%Y-%m-%d')

                    # 该日期记录缺省，且非周六周日,则插入新记录
                    if factory_list.filter(date=item2).count()==0 and date.weekday()!=5 and date.weekday()!=6:
                        factory_price = FACTORY_PRICE();
                        factory_price.date = item2
                        factory_price.price = current_price
                        factory_price.factory_type_id = type_id
                        factory_price.save()

                    # 该日期记录存在，则更新current_price
                    if factory_list.filter(date=item2).count()==1:
                        current_price=factory_list.get(date=item2).price


    # 将时间范围按照固定时间单元（以天计）进行划分，生成测试时间数组
    def get_test_date_range(beginDate, endDate,time_sapce):

        # 获取完整的时间列表
        date_list1=M5.get_date_range(beginDate, endDate)

        # 根据时间单元对date_list1进行处理

        date_list2=[]
        for index in range(len(date_list1)):
            if index%time_sapce==0:
                date_list2.append(date_list1[index])

        return date_list2





























