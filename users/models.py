from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class AccountManager(BaseUserManager):
    def create_user(self, password=None, **kwargs):
        if not kwargs.get('username'):
            raise ValueError('Users must have a username.')
        
        account = self.model(username=kwargs.get('username'))
        account.set_password(password)
        account.save()
        return account
    
    def create_superuser(self, password, **kwargs):
        account = self.create_user(password=None, **kwargs)
        account.is_admin = True
        account.save()
        return account
    
class Account(AbstractBaseUser):
    username = models.CharField(max_length=40, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    is_admin = models.BooleanField(default=False)
    
    objects = AccountManager()
    
    #REQUIRED_FIELDS = ['username']
    USERNAME_FIELD = 'username'
    
    def __unicode__(self):
        return self.username
   
    

