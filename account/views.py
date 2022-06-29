from Frameworks.router import Path
from Frameworks.response import HttpResponse, RenderResponse, JsonResponse

def print_received(request):
    print(request.query_string)
    print(request.method)
    if request.method == 'POST':
        name = request.post.get('name')
        passord = request.post.get('pass')
        print(name, passord)

    
    return RenderResponse(request,"index.html")



def json_point(request):
    
    data = [{'hello': 'hi', 'there':'me'},
    {'name': 'John', 'age': 15},
    {'name': 'Ama', 'age': 18},
    {'name': 'Someone', 'age': 20},

    ]
    return JsonResponse(request,data)



def test(request):

    return RenderResponse(request,"test.html")
