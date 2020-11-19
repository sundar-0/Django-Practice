# from django.shortcuts import render,HttpResponse
# class MyMiddleware:
#     def __init__(self,get_response):
#         self.get_response=get_response
#         print("One Time Configuration and Initialization")
    
#     def __call__(self,request):
#         print("Before the view is called")
#         response=self.get_response(request)
#         print("After the view is called")
#         return response
#     # def process_view(request,**args,**kwargs):
#     #     print("This is Process view-Before Calling View")
#     #     return None   
#     def process_exception(self,request,exception):
#         print("Exception Occured..")
#         msg=exception
#         return HttpResponse(msg)
    