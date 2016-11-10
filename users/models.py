from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from random import choice
from string import ascii_lowercase, digits

# Create your models here.

class AccountManager(BaseUserManager):
    def create_user(self, password=None, **kwargs):
        #account = self.model(username=kwargs.get('username'))
        account = self.model(username=self.gen_random_username())
        account.set_password(password)
        account.save()
        return account
    
    def create_superuser(self, password, **kwargs):
        if not kwargs.get('username'):
            raise ValueError('Users must have a username.')
        #account = self.create_user(password=None, **kwargs)
        account = self.model(username=kwargs.get('username'))
        account.set_password(password)
        account.is_admin = True
        account.save()

        return account
        
    def gen_random_username(self):        
        username = ''.join([choice(ascii_lowercase+digits) for i in xrange(8)])
        
        username = '-'.join([username[start:start+4] for start in range(0, len(username), 4)])
        
        try:
            Account.objects.get(username=username)
            return self.gen_random_username()
        except Account.DoesNotExist:
            return username;
    
class Account(AbstractBaseUser):
    username = models.CharField(max_length=40, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    is_admin = models.BooleanField(default=False)
    
    objects = AccountManager()
    
    USERNAME_FIELD = 'username'
    
    def is_staff(self):
        return self.is_admin

    def __unicode__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def is_superuser(self, app_label):
        return self.is_superuser
   
    def get_short_name(self):
        return self.username 
