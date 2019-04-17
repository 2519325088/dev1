#处理用户发出的请求，从urls.py中对应过来,
# 通过渲染templates中的网页可以将显示内容，
# 比如登陆后的用户名，用户请求的数据，输出到网页。

from django.shortcuts import render

from django.http import HttpResponse

from .models import BookInfo ,HeroInfo

from django.template import loader

# Create your views here.


def index(request):
    # indextem=loader.get_template('demo1/index.html')
    # cont = {'username':'lxl'}
    # result = indextem.render(cont)
    # return HttpResponse(result)

    # print("请求",request)
    # return HttpResponse("首页")
    return render(request,'demo1/index.html',{'username':'lxl'})


def list(request):
    # print("请求",request)
    # return HttpResponse("list")
    bookInfo=BookInfo.objects.all()
    return render(request,'demo1/list.html',{'lista':bookInfo})




# def list1(request,id):
#     print("请求",request)
#     return HttpResponse("list"+str(id))


def detail(request,id):

    name = BookInfo.objects.get(pk=id)
    # return HttpResponse('11')
    return render(request,'demo1/detail.html',{'bname':name})

    # try:
    #     name = BookInfo.objects.get(pk=int(id)).btitle
    #     return HttpResponse(name+"详情页")
    #
    # except Exception as e:
    #     print(e)


'''
创建模板文件夹 templates
配置模板目录 os.path.join（BASE_DIR,'templates'）
创建项目模板目录，创建模板


加载模板  temp=loader.get_template（）
使用变量渲染模板  result = temp.render（{}）
返回 HttpRoesponse(result)
'''