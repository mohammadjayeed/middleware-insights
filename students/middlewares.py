from django.http import HttpResponse
# function based middlware

def custom_function_middleware(get_response):
    print('this is a one time conf')

    def middleware(request):
        print('this executed FBM before the view happened')
        response = get_response(request)
        # response = HttpResponse('this is the response from function based middleware')
        print('this executed FBM after the view happened')
        return response
    return middleware


# class based middlware
class CustomClassBasedMiddlware:
    def __init__(self,get_response):
        self.get_response = get_response

        print('this is a one time conf')

    def __call__(self,request):
        print('this executed before the view')
        print(request.path)
        response = self.get_response(request)
        # response = HttpResponse('this is the response from class based middleware')
        print('this executed after the view')
        return response
    
    def process_view(self,request,view_func,view_args,view_kwargs):
        print("hook called just before calling the view")
        # print(request.method)
        # print(view_func.__name__)
        return None
    
    def process_exception(self,request,exception):
        print(exception)
        print('hook called the process exception')
        return None
    
    def process_template_response(self, request,response):
        print('hook called just after the view is executed')
        response.context_data['process_template_response'] = 'called from ptr hook'
        response.context_data['name'] = 'jayeed overwritten jayeed'
        return response
