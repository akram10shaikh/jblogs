"""jblogs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from blog import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('posts_data/<int:id>',views.posts_data,name='posts_data'),
    path('cat_data/<int:id>',views.cat_data,name='cat_data'),
    path('cats/',views.cats,name='cats'),
    path('about/',views.about,name='about'),
    path('login/',views.login1,name='login1'),
    path('user_data/',views.user_data,name='user_data'),
    path('log_out/',views.log_out,name='log_out'),
    path('second_base/',views.second_base,name='second_base'),
    path('login_user/',views.login_user,name='login_user'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('add_cat/',views.add_cat,name='add_cat'),
    path('add_post',views.add_post,name='add_post'),
    path('delete/',views.delete_page,name='delete_page'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('delete_post/<int:id>',views.delete_post,name='delete_post'),
    path('delete_data/<int:id>', views.delete_data, name='delete_data'),
    path('edit_data/',views.edit_data,name='edit_data'),
    path('edit_cat/',views.edit_cat,name='edit_cat'),
    path('cat_edit/<int:id>',views.cat_edit,name='cat_edit'),
    path('cat_data_edit/',views.cat_data_edit,name='cat_data_edit'),
    path('delete_cat/<int:id>/',views.delete_cat,name='delete_cat'),
    path('delete_cat_data/<int:id>/',views.delete_cat_data,name='delete_cat_data'),




]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
