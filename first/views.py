from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.http import JsonResponse, HttpResponse
from django .shortcuts import render



from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from first.models import blog, post
from first.serializers import BlogSerializer


def Register(request):
    if request.method == 'GET':
        return render(request,'register.html')

    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        User.objects.create_user( username=username, password=password, email=email)
        return render(request,'login.html')


def login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            return render(request, 'blog.html')
        else:
            return render(request, 'login.html')


def insert(request):
    if request.method =='GET':
        return render(request, 'blog.html')
    else:
        a = request.POST.get('date')
        b = request.POST.get('blog')
        post.objects.create(date=a, blog=b)
        return render(request, 'blog.html')

def viewblog(request):
    ob=post.objects.all()
    return render(request,'viewblog.html',{'ob':ob})

@csrf_exempt
def blogpost(request):
    if request.method =='GET':
        obj = post.objects.all()
        serializerobj = BlogSerializer(obj,many=True)
        return JsonResponse(serializerobj.data,safe=False)
    else:
        data = JSONParser().parse(request)
        serializer = BlogSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.data,status=400)


@api_view(['GET','PUT'])
def blogpst(request,id):
 blg=post.objects.get(id=id)
 if request.method=='GET':
     serializer=BlogSerializer(blg)
     return JsonResponse(serializer.data)
 elif request.method=='PUT':
     data=JSONParser().parse(request)
     serializer=BlogSerializer(blg,data=data)
     if serializer.is_valid():
         serializer.save()
         return JsonResponse(serializer.data)
     return JsonResponse(serializer.errors,status=400)




