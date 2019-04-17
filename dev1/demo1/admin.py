#后台，可以用很少量的代码就拥有一个强大的后台。

from django.contrib import admin
from .models import BookInfo,HeroInfo
# Register your models here.

class HeroInfoInline(admin.StackedInline):
    model = HeroInfo
    # 关联个数
    extra = 1
# class BookInfoInline(admin.StackedInline):
#     model = BookInfo
#     # 关联个数
#     extra = 1



class BookInfoAdmin(admin.ModelAdmin):
    # 显示字段，可以点击列头进行排序
    list_display = ['id','bname','bpub_date']
    # 过滤字段，过滤框会出现在右侧
    list_filter = ['btitle','bpub_date']
    # 搜索字段，搜索框会出现在上侧
    search_fields = ['btitle','bpub_date']
    # 分页，分页框会出现在下侧
    list_per_page = 3

    inlines = [HeroInfoInline]

class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ['id','pname','sex','skill']
    list_filter = ['hname','hgender','hcontent']
    search_fields = ['hname','hgender','hcontent']
    list_per_page = 3


admin.site.register(BookInfo,BookInfoAdmin)
admin.site.register(HeroInfo,HeroInfoAdmin)
'''
需要将特定的数据模型注册  才能在后台管理
'''
