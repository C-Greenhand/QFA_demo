from datetime import datetime
from django.db import models

# Create your models here.

# 因子类型表：存储因子类型名
class FACTORY_TYPE(models.Model):
    name=models.CharField(max_length=64,default='null') # 因子类型名称
    exchange_rate=models.DecimalField(max_digits=15,decimal_places=3,default=0) # 因子价格变化率

    def __str__(self):
        return self.name

# 因子历史价格表：存储因子历史价格信息
class FACTORY_PRICE(models.Model):
    factory_type = models.ForeignKey('FACTORY_TYPE', on_delete=models.CASCADE) # 因子类型（外键）
    date = models.DateField()  # 日期
    price=models.DecimalField(max_digits=15,decimal_places=3,default=0) # 价格

# 资产类型表，注意不含债券
class ASSET_TYPE(models.Model):
    name = models.CharField(max_length=64,default='null') # 资产类型名称
    ratio = models.DecimalField(max_digits=15, decimal_places=3,default=0)  # 资产占比
    cap = models.DecimalField(max_digits=15, decimal_places=3,default=0)  # 资产值

    def __str__(self):
        return self.name

# 资产品种表
class ASSET_VARITY(models.Model):
    name=models.CharField(max_length=64,default='null') # 资产品种名称
    asset_type = models.ForeignKey('ASSET_TYPE', on_delete=models.CASCADE,related_name='varity_type') # 资产类型（外键）
    amount = models.DecimalField(max_digits=15, decimal_places=3,default=0) # 持仓数量
    cap=models.DecimalField(max_digits=15, decimal_places=3,default=0) # 资产值

    @property
    def all_prices(self):
        return price_varity.all()



# 由于债券的占比，收益计算方式特殊，所以专门设置一表进行存储
class BOND(models.Model):
    ratio=models.DecimalField(max_digits=15,decimal_places=3,default=0) # 债券占比
    cap = models.DecimalField(max_digits=15, decimal_places=3,default=0)  # 债券资产值

# 资产历史价格表：存储资产历史价格信息
class ASSET_PRICE(models.Model):
    date = models.DateField()  # 日期
    price=models.DecimalField(max_digits=15,decimal_places=3) # 价格
    asset_varity = models.ForeignKey('ASSET_VARITY',on_delete=models.CASCADE, related_name='price_varity') # 资产品种（外键）

# 权重表，注意不含因子与债券的关系
class WEIGHT(models.Model):
    factory_type = models.ForeignKey('FACTORY_TYPE', on_delete=models.CASCADE) # 因子类型（外键）
    asset_type = models.ForeignKey('ASSET_TYPE', on_delete=models.CASCADE) # 资产类型（外键）
    value=models.DecimalField(max_digits=15,decimal_places=3,default=0) # 权重值


# 公共信息表
class COMMON_INFORMATION(models.Model):
    time_space=models.IntegerField(default=0) # 时间单元
    sum_cap=models.DecimalField(max_digits=15,decimal_places=3,default=0) # 各项资产总市值
    start_date=models.DateField() # 起始日期
    end_date = models.DateField() # 终止日期
    income=models.DecimalField(max_digits=15,decimal_places=3,default=0) # 收益

# PMI表
class PMI(models.Model):
    date=models.DateField()
    close=models.DecimalField(max_digits=15,decimal_places=3)

# 布伦特原油表
class BRENT(models.Model):
    date=models.DateField()
    close=models.DecimalField(max_digits=15,decimal_places=3)

# 利率表
class INTEREST_RATE(models.Model):
    date=models.DateField()
    close=models.DecimalField(max_digits=15,decimal_places=3)

# 汇率表
class FX_RATE(models.Model):
    date=models.DateField()
    close=models.DecimalField(max_digits=15,decimal_places=3)

# 期货南华铜表
class CU_NH(models.Model):
   date=models.DateField()
   close=models.DecimalField(max_digits=15,decimal_places=3)

# 期货南华铝表
class AL_NH(models.Model):
    date=models.DateField()
    close=models.DecimalField(max_digits=15,decimal_places=3)

# 期货南华螺纹钢表
class RB_NH(models.Model):
    date=models.DateField()
    close=models.DecimalField(max_digits=15,decimal_places=3)

# 期货南华焦炭表
class J_NH(models.Model):
    date=models.DateField()
    close=models.DecimalField(max_digits=15,decimal_places=3)

# '000905'中证500指数类
class ZZ_500S(models.Model):
    date=models.DateField()
    close=models.DecimalField(max_digits=15,decimal_places=3,default=0)







