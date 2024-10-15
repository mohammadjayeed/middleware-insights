# function based middlware

# def custom_function_middleware(get_response):
#     print('this is a one time conf')

#     def middlware(request):
#         print('this executed before the view happened')
#         response = get_response(request)
#         print('this executed after the view happened')
#         return response
#     return middlware


# class based middlware
class CustomClassBasedMiddlware:
    def __init__(self,get_response):
        self.get_response = get_response

        print('this is a one time conf')

    def __call__(self,request):
        print('this executed before the view')
        print(request.path)
        response = self.get_response(request)
        print('this executed after the view')
        return response