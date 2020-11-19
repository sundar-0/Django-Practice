def my_middleware(get_response):
    print("One time Configuration and Initialization")
    def my_function(request):
        print("Code Executed before view are called")
        response=get_response(request)
        print("Code Executed after view are called")
        return response
    return my_function
