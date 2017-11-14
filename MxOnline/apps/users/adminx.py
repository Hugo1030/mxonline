import xadmin
from xadmin import views
from .models import EmailVerifyRecord, Banner


class BaseSetting(object): # 页面样式
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object): # 页头和页脚
    site_title = "开智后台管理系统"
    site_footer = '开智学堂'
    #menu_style = "accordion"


class EmailVerifyRecordAdmin(object): # 后台注册
    list_display = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type']
    list_filter = ['code', 'email', 'send_type', 'send_time']

class BannerAdmin(object): # 后台注册
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'image', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index', 'add_time']


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin) # 注册进入 xadmin
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
