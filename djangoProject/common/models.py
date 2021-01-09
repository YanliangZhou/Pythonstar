from django.db import models
import datetime

# Create your models here.
# class Customer(models.Model):
#     #客户名称
#     name = models.CharField(max_length=200)
#
#     #联系电话
#     phonenumber = models.CharField(max_length=200)
#
#     #地址
#     address = models.CharField(max_length=200)
#
#
# class Medicine(models.Model):
#     # 药品名
#     name = models.CharField(max_length=200)
#     # 药品编号
#     sn = models.CharField(max_length=200)
#     # 描述
#     desc = models.CharField(max_length=200)


class Order(models.Model):
    # # 订单名
    # name = models.CharField(max_length=200,null=True,blank=True)

    # # Date
    # create_date = models.DateTimeField(default=datetime.datetime.now)
    # Date

    create_date = models.CharField(primary_key=True,max_length=200)

    # Open price
    open_price = models.CharField(max_length=200)

    # High price
    high_price = models.CharField(max_length=200)

    # Low price
    low_price = models.CharField(max_length=200)

    # Close price
    close_price = models.CharField(max_length=200)

    # Adj close price
    adj_close_price = models.CharField(max_length=200)

    # Volume
    volume = models.IntegerField()

    # # 客户
    # customer = models.ForeignKey(Customer,on_delete=models.PROTECT)

    # # 订单购买的药品，和Medicine表是多对多 的关系
    # medicines = models.ManyToManyField(Medicine, through='OrderMedicine')


# class OrderMedicine(models.Model):
#     order = models.ForeignKey(Order, on_delete=models.PROTECT)
#     medicine = models.ForeignKey(Medicine, on_delete=models.PROTECT)
#
#     # 订单中药品的数量
#     amount = models.PositiveIntegerField()


#
# from django.contrib import admin
# admin.site.register(Customer)
#
#
# # 国家表
# class Country(models.Model):
#     name = models.CharField(max_length=100)
#
# # 学生表， country 字段是国家表的外键，形成一对多的关系
# class Student(models.Model):
#     name    = models.CharField(max_length=100)
#     grade   = models.PositiveSmallIntegerField()
#     country = models.ForeignKey(Country,
#                                 on_delete=models.PROTECT)