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

class GoodManager(BaseModelManager):

	def create(self, **kwargs):
		return self.model(generated_id = Generator.genarateId(), **kwargs)
	
class Good(BaseModel):
	title = models.CharField(max_length=200)
	price = models.FloatField(default=0)
	brand = models.CharField(max_length=36)
	generated_id = models.CharField(max_length=36)

	objects = GoodManager()

	def __unicode__(self):
		return "good://" + str(self.generated_id)


class BrandManager(BaseModelManager):
	pass

class Brand(BaseModel):
	title = models.CharField(max_length=200)
	icon = models.CharField(max_length=500)
	desc = models.CharField(max_length=1000)

	objects = BrandManager()
