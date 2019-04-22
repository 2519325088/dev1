#处理用户发出的请求，从urls.py中对应过来,
# 通过渲染templates中的网页可以将显示内容，
# 比如登陆后的用户名，用户请求的数据，输出到网页。

from django.shortcuts import render,redirect,reverse,get_object_or_404,get_list_or_404

from django.http import HttpResponse,HttpResponseRedirect,JsonResponse

from .models import BookInfo ,HeroInfo

from django.template import loader

# Create your views here.


def index(request):
    # respons={'dasdad':"najnai"}
    # return JsonResponse(respons)
    return render(request,'demo1/index.html',{'username':'lxl'})


def list(request):
    bookInfo=BookInfo.objects.all()
    return render(request,'demo1/list.html',{'lista':bookInfo})


def delete(request,id):
    BookInfo.objects.get(pk=id).delete()
    bookInfo = BookInfo.objects.all()
    return HttpResponseRedirect('/demo1/list/',{'bookk':bookInfo})

def hdelete(request,id):
    name=HeroInfo.objects.get(pk=id).hbook
    HeroInfo.objects.get(pk=id).delete()
    bname=BookInfo.objects.get(btitle=name)

    # return HttpResponse(bname.id)
    return HttpResponseRedirect('/demo1/detail/'+str(bname.id)+'/',{'bname':bname})


def addbook(request):

    return render(request,'demo1/addbook.html')

def addbend(request):
    bname=request.POST['bookname']
    b1=BookInfo()
    b1.btitle=bname
    b1.save()
    return HttpResponseRedirect('/demo1/list/')

def addhero(request,id):
    # book=get_object_or_404(BookInfo,PK=id)
    book=BookInfo.objects.get(pk=id)
    return render(request,'demo1/addhero.html', {'bookk': book})

def addend(request):
    hname=request.POST['username']
    hsex=request.POST['usersex']
    hskill = request.POST['userskill']
    userid=request.POST['userid']
    book=BookInfo.objects.get(pk=userid)
    hero=HeroInfo()
    hero.hname=hname
    if hsex:
        hero.hgender=True
    else:
        hero.hgender=False
    hero.hcontent=hskill
    hero.hbook=book
    print(hname,hsex,hskill,book)
    hero.save()
    return  HttpResponseRedirect('/demo1/detail/'+str(userid)+'/',{'bname':book})



def detail(request,id):
    try:
        name = BookInfo.objects.get(pk=id)
        return render(request, 'demo1/detail.html', {'bname': name})

    except Exception as e:
        print(e)


'''
创建模板文件夹 templates
配置模板目录 os.path.join（BASE_DIR,'templates'）
创建项目模板目录，创建模板


加载模板  temp=loader.get_template（）
使用变量渲染模板  result = temp.render（{}）
返回 HttpRoesponse(result)
'''