#后台，可以用很少量的代码就拥有一个强大的后台。

from django.contrib import admin
from .models import BookInfo,HeroInfo
# Register your models here.
admin.site.register(BookInfo)
admin.site.register(HeroInfo)


'''
需要将特定的数据模型注册  才能在后台管理
'''
