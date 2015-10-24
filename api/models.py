#!/usr/bin/env python
#description     :This will create a header for a python script.
#author          :songwei
#email			 :songwei@ujipin.cn
#date            :20151024
#notes           :两个类，一个商品类 Good， 一个品牌类 Brand。
#每个类都有一个字段 generated_id。这是自动生成的字段，这个字段用于对外唯一ID
#创建model对象请使用 model.objects.create() 来创建。这个方法中会自动生成 generated_id
#==============================================================================

from demo.models import BaseModel
from django.db import models
import uuid

class GoodManager(models.Manager):
	def create(self, **kwargs):
		return Good(generated_id = Common.genarateId(), **kwargs)

class Good(models.Model):
	created_time = models.DateTimeField(auto_now_add=True)
	edited_time = models.DateTimeField(auto_now_add=True)
	title = models.CharField(max_length=200)
	price = models.FloatField(default=0)
	brand = models.CharField(max_length=36)
	generated_id = models.CharField(max_length=36)

	objects = GoodManager()

	def __unicode__(self):
		return "good://" + self.generated_id


class BrandManager(models.Manager):
	def create(self, **kwargs):
		return Brand(generated_id = Common.genarateId(), **kwargs)

class Brand(models.Model):
	title = models.CharField(max_length=200)
	generated_id = models.CharField(max_length=36)
	icon = models.CharField(max_length=500)
	desc = models.CharField(max_length=1000)

	def __unicode__(self):
		return "brand://" + self.generated_id


class Common():

	@staticmethod
	def genarateId():
		return str(uuid.uuid4())
