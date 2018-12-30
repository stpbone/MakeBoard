from django.urls import path
from . import views
from django.urls import include
from django.contrib.auth import views as auth_view


urlpatterns = [
	path('', views.home_page, name='home_page'),
    path('projects', views.post_list, name='post_list'),
    path('pricing', views.pricing_page, name='pricing_page'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]

#Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]