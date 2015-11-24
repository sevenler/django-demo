#!/usr/bin/env python
#coding=utf8
#description     :This will create a header for a python script.
#author          :songwei
#email			 :songwei@ujipin.cn
#date            :20151024
#==============================================================================
from django.db import models

from base_model import BaseModel,BaseModelManager

class OperationRecordManager(BaseModelManager):
	pass	

#操作日志记录表
#具体的说明会写到 utils/operation_record.py 中
class OperationRecord(BaseModel):
	user_id = models.CharField(max_length=36)   #操作用户id
	model = models.CharField(max_length=200)   #数据表
	operation = models.CharField(max_length=200)   #操作
	date = models.DateTimeField(auto_now_add=True)   #操作时间
	before = models.IntegerField()   #操作前的状态
	after = models.IntegerField()   #操作后的状态
	description = models.CharField(max_length=2000)   #操作补充描述 description 字段算是日志的一个补充说明

	objects = OperationRecordManager()