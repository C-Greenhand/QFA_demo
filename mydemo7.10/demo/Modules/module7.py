from datetime import datetime
from demo.models import FACTORY_PRICE,ASSET_PRICE,WEIGHT,ASSET_TYPE,ASSET_VARITY,FACTORY_TYPE,COMMON_INFORMATION,BOND


class M7(object):

    def calculate_time1():
        target=ASSET_PRICE.objects.filter(asset_varity_id=1).get(date='2018-05-07').price
        time_now = datetime.now()
        return time_now

    def calculate_time2():
        item=ASSET_VARITY.objects.get(id=1)
        target=item.all_prices
        time_now = datetime.now()
        return time_now


