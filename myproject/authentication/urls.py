from django.urls import path
from . import views
urlpatterns=[
	path('',views.login_view, name=' login_view'),
	path('register/', views.register, name='register'),
	path('homepage/',views.show_homepage, name = 'Home'),
	path('logout/',views.logout_view,name = 'logout_view'),
]
