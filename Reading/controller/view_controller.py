from django.shortcuts import HttpResponse
from django.shortcuts import render

# 测试用的controller

user_list = []
def index(request):
    # return HttpResponse("Hello Word")
    # return render(request,'index.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        temp = {'user': username, 'pwd': password}
        user_list.append(temp)
    return render(request, 'index.html', {'data': user_list})