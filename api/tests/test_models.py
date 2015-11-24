#!/usr/bin/env python
#coding=utf8
#description     :This will create a header for a python script.
#author          :songwei
#email			 :songwei@ujipin.cn
#date            :20151024
#==============================================================================

from django.test import TestCase
from api.models.goods import Good, Brand

# Create your tests here.

class ModelTeseCase(TestCase):

	def setUp(self):
		b = Brand.objects.create(title = "new blance")
		b.save()
		Good.objects.create(title = "999", price = 999.5, brand = b.generated_id).save()
		Good.objects.create(title = "999", price = 100, brand = b.generated_id).save()

	def testAddModelData(self):
		self.assertEqual(1, 1)
		print Good.objects.all()

		#按照指定条件过滤  然后再做排序
		print Good.objects.filter(title = '999').order_by('price')
		
		#获取制定条件数据  get返回多个数据会报错哦
		good = Good.objects.get(price = 999.5)
		print good

		good.price = 1000
		good.save()

		print Good.objects.get(price = 1000)

		#在fitler结果列表中获取第一个结果
		print Good.objects.filter(title = '999')[0]





