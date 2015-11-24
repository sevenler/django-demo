#!/usr/bin/env python
#coding=utf8
#description     :base model for all models
#author          :songwei
#email			 :songwei@ujipin.cn
#date            :20151024
# ID generator 用于创建各种单号
#==============================================================================
import uuid

class Generator:

	@staticmethod
	def genarateId():
		return str(uuid.uuid4())