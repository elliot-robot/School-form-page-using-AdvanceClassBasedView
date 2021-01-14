from django.conf.urls import url
from basic_app import views
from django.urls import path

app_name = 'basic_app'


urlpatterns=[
    #path('',views.IndexView.as_view()),
    path('',views.SchoolListView.as_view(),name='list'),
    path('test/',views.test,name='test'),
    path('<int:pk>/',views.SchoolDetailView.as_view(),name='detail'),
    #path()

    #path('other/',views.other,name='other'),
    #path('relative/',views.relative,name='relative'),
]
