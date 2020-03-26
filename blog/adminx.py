#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import xadmin
from xadmin import views
from xadmin.plugins.auth import UserAdmin

from .models import Blog, Conment, Category, Tagprofile, Message


class BaseSetting:
    """
    后台修改需要的配置
    """
    enable_themes = True  # 开启主题功能
    use_bootswatch = True


class GlobalSettings:
    """
    后台修改
    """
    site_title = '博客后台管理'
    site_footer = '博客后台管理'
    menu_style = 'accordion'  # 开启分组折叠


class BlogAdmin:
    list_display = ['title', 'category', 'author', 'add_time', 'read_nums', 'conment_nums', 'tag']
    list_filter = ['title', 'category', 'author', 'read_nums', 'conment_nums', 'tag']
    search_fields = ['title', 'category', 'author', 'add_time', 'read_nums', 'conment_nums', 'tag']
    readonly_fields = ['add_time', 'read_nums', 'conment_nums', 'edit_time']
    style_fields = {'content': 'ueditor'}


class ConmentAdmin:
    model = Conment


class CategoryAdmin:
    model = Category


class TagAdmin:
    model = Tagprofile


class MessageAdmin:
    model=Message


# xadmin.site.register(views.BaseAdminView, BaseSetting)
# # xadmin.site.register(views.CommAdminView, GlobalSettings)
# # xadmin.site.register(Blog, BlogAdmin)
# # xadmin.site.register(Conment, ConmentAdmin)
# # xadmin.site.register(Category, CategoryAdmin)
# # xadmin.site.register(Tagprofile, TagAdmin)
# # xadmin.site.register(Message, MessageAdmin)
xadmin.site.register(Blog, BlogAdmin)
xadmin.site.register(Tagprofile,TagAdmin)
xadmin.site.register(Message,MessageAdmin)
xadmin.site.register(Category, CategoryAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)


