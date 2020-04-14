from django.conf.urls import url, include
from . import views
from django.urls import path, re_path

app_name = 'crm'
urlpatterns = [
               path('', views.home, name='home'),
               re_path(r'^home/$', views.home, name='home'),
               path('crochethook_list', views.crochethook_list, name='crochethook_list'),
               path('crochethook/create/', views.crochethook_new, name='crochethook_new'),
               path('crochethook/<int:pk>/edit/', views.crochethook_edit, name='crochethook_edit'),
               path('crochethook/<int:pk>/delete/', views.crochethook_delete, name='crochethook_delete'),
               path('yarn_list', views.yarn_list, name='yarn_list'),
               path('yarn/create/', views.yarn_new, name='yarn_new'),
               path('yarn/<int:pk>/edit/', views.yarn_edit, name='yarn_edit'),
               path('yarn/<int:pk>/delete/', views.yarn_delete, name='yarn_delete'),
               path('gift_list', views.gift_list, name='gift_list'),
               path('gift/create/', views.gift_new, name='gift_new'),
               path('gift/<int:pk>/edit/', views.gift_edit, name='gift_edit'),
               path('gift/<int:pk>/delete/', views.gift_delete, name='gift_delete'),
               path('crochethook/<int:pk>/summary/', views.summary, name='summary'),
]