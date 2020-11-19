from django.contrib.auth.signals import user_logged_in,user_logged_out,user_login_failed
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_init,post_init,pre_save,post_save,pre_delete,post_delete
from django.core.signals import request_started,request_finished,got_request_exception
# """1.Login And Logout Signals"""
# @receiver(user_logged_in,sender=User)
# def login_success(sender,request,user,**kwargs):
#     print(".....Logged In Signal.......")
#     print("sender:",sender)
#     print("Request:",request)
#     print("User:",user)
#     print(f'**kwargs: {kwargs}')  
# #user_logged_in.connect(login_success,sender=User)

# @receiver(user_logged_out,sender=User)
# def logout_success(sender,request,user,**kwargs):
#     print(".....Logged Out Signal.......")
#     print("sender:",sender)
#     print("Request:",request)
#     print("User:",user)
#     print(f'**kwargs: {kwargs}')  

# @receiver(user_login_failed)
# def login_failed(sender,credentials,request,**kwargs):
#     print(".....Logged In Failed Signal.......")
#     print("sender:",sender)
#     print("Credentials:",credentials)
#     print("Request:",request)
#     print(f'**kwargs: {kwargs}')  


# """ 2.Model Signals"""
# @receiver(pre_init,sender=User)
# def preInit(sender,args,**kwargs):
#     print("...Pre Init Signal....")
#     print("sender:",sender)
#     print("Arguments:",args)
#     print(f'**kwargs: {kwargs}')  
# @receiver(post_init,sender=User)
# def postInit(sender,instance,**kwargs):
#     print("...Post Init Signal....")
#     print("sender:",sender)
#     print("Instance",instance)
#     print(f'**kwargs: {kwargs}')  

# @receiver(pre_save,sender=User)
# def preSave(sender,instance,**kwargs):
#     print("...Pre Save Signal....")
#     print("sender:",sender)
#     print("Instance",instance)
#     print(f'**kwargs: {kwargs}')  

# @receiver(post_save,sender=User)
# def postSave(sender,instance,created,**kwargs):
#     if created:
#         print('............')
#         print('Post Save signal')
#         print('sender',sender)
#         print('instance',instance)
#         print('created',created)
#         print(f'**kwargs: {kwargs}')  
#     else:
#         print('............')
#         print('Update Post Save Signal')
#         print('sender',sender)
#         print('instance',instance)
#         print(f'**kwargs: {kwargs}')  


# """3.Request/Response Signals"""
# @receiver(request_started)
# def startRequest(sender,environ,**kwargs):
#     print('....start  Request......')
#     print('Sender',sender)
#     print('Environ',environ)
#     print(f'**kwargs: {kwargs}')  
# @receiver(request_finished)
# def finishRequest(sender,**kwargs):
#     print('Sender',sender)
#     print(f'**kwargs: {kwargs}')  
