from django.urls import path

from . import views

urlpatterns=[
	path('',views.index,name='index'),
	path('blood-test/',views.blood_test,name='blood_test'),
	path('result',views.blood_test,name='result')
	
]