#!/usr/bin/env python
#coding=utf8
#description     :This will create a header for a python script.
#author          :songwei
#email			 :songwei@ujipin.cn
#date            :20151024
#==============================================================================
from django.db import models

from api.utils.id_generator import Generator
from base_model import BaseModel,BaseModelManager

class ProcurementManager(BaseModelManager):
	def create(self, **kwargs):
		return self.model(procurement_id = Generator.genarateId(), **kwargs)
#采购单
class Procurement(BaseModel):
	title = models.CharField(max_length=200)   #采购标题 
	expenses = models.FloatField(default=0)  #采购费用
	launch_user_id = models.CharField(max_length=36) #采购发起人
	procurement_id = models.CharField(max_length=36)  #采购单号，自动生成

	objects = ProcurementManager()

	def __unicode__(self):
		return "procurement://" + str(self.procurement_id)



class ProcurementEntryManager(BaseModelManager):
	def create(self, **kwargs):
		return self.model(entry_id = Generator.genarateId(), **kwargs)
#采购明细
class ProcurementEntry(BaseModel):
	product_id = models.CharField(max_length=36)   #采购商品id
	price = models.FloatField(default=0)    #采购价格
	number = models.IntegerField(default=0)  #采购数量
	entry_id = models.CharField(max_length=36)  #采购明细id，自动生成

	objects = ProcurementEntryManager()
