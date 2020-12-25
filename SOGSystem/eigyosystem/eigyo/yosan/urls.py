from django.urls import path
from eigyosystem.eigyo.yosan import views

urlpatterns = [

    path('', views.yosan, name='yosan'),  # 売上管理
    # path('eigyosystem/', include('eigyosystem.eigyo.urls')),
    # # 売上
    # path('login/', views.logineigyo, name='logineigyo'),  # index
    # path('test/', views.test, name='test'),  # index
    # # re_path(r'^user/(?P<pk>\d+)/test/$', views.test, name='test'),
    #
    # # 売上
    # path('index/', views.index, name='index'),  # index
    # path('uriage/', views.uriage, name='uriage'),  # 売上管理
    # path('uriage_jisseki/', views.uriage_jisseki, name='uriage_jisseki'),  # 売上実績
    # path('uriage_chart/', views.uriage_chart, name='uriage_chart'),  # 売上実績
    # path('uriage_chart_total/', views.uriage_chart_total, name='uriage_chart_total'),  # 売上実績
    # path('yosan_chart/', views.yosan_chart, name='yosan_chart'),  # 売上実績

]