#!/usr/bin/env python
#coding=utf8
#description     操作日志记录
#记录的大致原则是  谁在什么时间 操作了 什么内容，操作前是什么状态，操作后是什么状态
# TODO  before after 的定义怎么做？ 肯定不仅仅记录表的状态变化
# 状态 ＋ 详情的记录description  这个详情的记录description 让业务逻辑处理的时候定义
# 举例子来说：
#  新建采购单的时候，需要记录  张三 在2015.10.9 10:00:10 创建了  采购单， 
#  之前是空， 之后是新建的状态。description 可以为空 
#  
#  采购单审核的时候，需要记录  财务张总监  在 2015.10.10 10:00:10 二审 采购单
#  之前是一审通过 之后是财务审核通过。  description 可以记录 生成的付款单号 是 123456
#  如果出现了exception, 也请用这个description字段来记录,例如付款写入失败了，回滚了数据库状态这样的情况
#  
#  description 字段算是日志的一个补充说明
#author          :songwei
#email			 :songwei@ujipin.cn
#date            :20151024
#==============================================================================
from erp.models.operation_record import OperationRecord as ormodel
import datetime

class OperationRecord():

	# model 数据表  定义采购单、入库单等等
	# operation 操作   创建、一审、二审采购单、支付采购单等等
	#  date  操作时间   默认当前时间
	#  before  操作前的状态
	#  before  操作后的状态
	#  description  日志的补充说明   长度限制2000的英文字符
	@staticmethod
	def record(model, operation, date = datetime.datetime.now(), before = -1, after = -1, description = ""):
		user_id = "user19900928"
		return ormodel.objects.create(user_id = user_id, 
				model = model,
				operation = operation,
				date = date,
				before = before,
				after = after,
				description = description).save();
		