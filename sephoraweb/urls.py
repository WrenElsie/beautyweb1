from django.urls import path, re_path
from . import views

# namespace
app_name = 'sephoraweb'

urlpatterns = [

    # 查看列表
    path('', views.BeautyList.as_view(), name='beauty_list'),

    # 查看详情, 如/sephoraweb/beauty/1/
    re_path(r'^beauty/(?P<pk>\d+)/$',
        views.BeautyDetail.as_view(), name='beauty_detail'),

    # 创建, 如：/sephoraweb/beauty/create/
    re_path(r'^beauty/create/$', views.BeautyCreate.as_view(), name='beauty_create'),

    # 编辑详情, 如: /sephoraweb/beauty/1/edit/
    re_path(r'^beauty/(?P<pk>\d+)/edit/$',
        views.BeautyEdit.as_view(), name='beauty_edit'),

    # 创建商品 ex.: /sephoraweb/beauty/1/goods/create/
    re_path(r'^beauty/(?P<pk>\d+)/goods/create/$',
            views.GoodCreate.as_view(), name='good_create'),

    # 编辑商品, ex.: /sephoraweb/beauty/1/goods/1/edit/
    re_path(r'^beauty/(?P<pkr>\d+)/goods/(?P<pk>\d+)/edit/$',
            views.GoodEdit.as_view(), name='good_edit'),

    # 查看商品信息 ex: /sephoraweb/beauty/1/goods/1/
    re_path(r'^beauty/(?P<pkr>\d+)/goods/(?P<pk>\d+)/$',
            views.GoodDetail.as_view(), name='good_detail'),

    # 创建评论, /sephoraweb/beauty/1/reviews/create/
    re_path(r'^beauty/(?P<pk>\d+)/reviews/create/$',
            views.review_create, name='review_create'),

]
