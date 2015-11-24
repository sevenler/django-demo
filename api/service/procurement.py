
#!/usr/bin/env python
#coding=utf8
#description     
#采购流程的操作  具体请看 https://tower.im/projects/41a9c99283014f68b96b534ac88d4af2/ 的流程设计图
#author          :songwei
#email			 :songwei@ujipin.cn
#date            :20151024
#==============================================================================
class Procurement():

	#新建采购单
	# kwargs 包括采购单信息、采购明细信息
	# 返回采购单
	def create(**kwargs):
		pass

	#提交采购单审核
	# 输入采购单号
	# 返回采购单, 状态会修改
	def submit(procurement_id):
		pass

	#采购单一审
	# 输入采购单号
	# 返回采购单, 状态会修改
	def audit_first(procurement_id):
		pass

	#采购单二审
	# 输入采购单号
	# 返回采购单, 状态会修改
	def audit_seconed(procurement_id):
		pass

	#生成付款单
	#根据采购单的状态判断是否生成付款单
	#返回采购单，采购单中会有相关的付款单, 状态也会修改
	def make_payment(procurement_id):
		pass

	#支付付款单
	#根据付款单进行支付
	#返回付款单
	def pay(payment_id):
		pass

	#生成接货单
	#输入采购单号
	#返回接货单
	def make_receipt(procurement_id):
		pass


	#
	#
	#

