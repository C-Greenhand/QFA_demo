from demo.models import ASSET_PRICE,FACTORY_PRICE,ZZ_500S

"""
本模块用于将多张价格表（比如：al_nh，j_nh，cu_nh，j_nh，zz_500s）合并为一张历史价格表（比如：ASSET_PRICE）
"""


class M4(object):

    # 参数为原数据集记录数组，品种/类型id，操作类型（是填充资产历史价格表，还是填充因子历史价格表）
    def get_price_by_dataSet(List,varity_or_type_id,operation_type):

        if(operation_type=='asset'):
            for item in List:
                asset_price=ASSET_PRICE();
                asset_price.date=item.date
                asset_price.price = item.close
                asset_price.asset_varity_id = varity_or_type_id
                asset_price.save()
        else:
            for item in List:
                factory_price=FACTORY_PRICE();
                factory_price.date=item.date
                factory_price.price = item.close
                factory_price.factory_type_id = varity_or_type_id
                factory_price.save()




