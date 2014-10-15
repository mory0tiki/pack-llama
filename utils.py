import ast

def render_post_params(request, *args, **kwargs):
    result = None
    try:
        if request.is_ajax() or request.method != "POST":
            result = ast.literal_eval(request.body)
        else:
            if request.method == "POST":
                result = request.POST.dict()#ast.literal_eval(str(request.POST.dict()))
    except Exception as ex:
        print ex
    return result

