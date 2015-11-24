#!/usr/bin/env python
#coding=utf8
#description     :base model for all models
#author          :songwei
#email			 :songwei@ujipin.cn
#date            :20151024
#==============================================================================

from django.db import models

class BaseModelManager(models.Manager):
	def create(self, **kwargs):
		return self.model(**kwargs)

class BaseModel(models.Model):
    created_time = models.DateTimeField(auto_now_add=True)
    edited_time = models.DateTimeField(auto_now_add=True)
    id = models.AutoField(primary_key=True)

    objects = BaseModelManager()

    def __unicode__(self):
        name = self.__class__.__name__
        return name + "://" + str(self.id)

    class Meta:
        abstract=True # Set this model as Abstract