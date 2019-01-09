from django.urls import path
from . import views
from django.urls import include
from django.contrib.auth import views as auth_view
from . import views as core_views
from django.conf.urls import url



urlpatterns = [
	path('', views.home_page, name='home_page'),
    path('projects', views.post_list, name='post_list'),
    path('pricing', views.pricing_page, name='pricing_page'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('login/', views.login, name='login'),
    path('logout/', views.login, name='logout'),
    url(r'^signup/$', core_views.signup, name='signup'),
]

#Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]

