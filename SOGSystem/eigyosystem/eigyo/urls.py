from django.urls import path, include
from eigyosystem.eigyo.login import views
from eigyosystem.eigyo.menu import views

app_name = 'eigyosystem'
urlpatterns = [
    # 売上
    path('login/', include('eigyosystem.eigyo.login.urls')),  # 登録
    # path('test/', views.test, name='test'),  # index
    # re_path(r'^user/(?P<pk>\d+)/test/$', views.test, name='test'),

    # 売上
    path('index/', include('eigyosystem.eigyo.menu.urls')),  # index
    path('uriage/', include('eigyosystem.eigyo.uriage.urls')),  # 売上管理
    path('yosan/', include('eigyosystem.eigyo.yosan.urls')),  # 売上管理
    # path('uriage_jisseki/', views.uriage_jisseki, name='uriage_jisseki'),  # 売上実績
    # path('uriage_chart/', views.uriage_chart, name='uriage_chart'),  # 売上実績
    # path('uriage_chart_total/', views.uriage_chart_total, name='uriage_chart_total'),  # 売上実績
    # path('yosan_chart/', views.yosan_chart, name='yosan_chart'),  # 売上実績

]