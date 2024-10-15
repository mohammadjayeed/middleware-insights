# function based middlware

def custom_function_middleware(get_response):
    print('this is a one time conf')

    def middlware(request):
        print('this executed before the view happened')
        response = get_response(request)
        print('this executed after the view happened')
        return response
    return middlware