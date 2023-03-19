"""mydjango02 URL Configuration

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

from django.urls import path
from users.views import depart, user, pretty, admin, acount

urlpatterns = [
    # 部门管理
    path('depart_list/', depart.depart_list),
    path('depart_add/', depart.depart_add),
    path('depart_delete/', depart.depart_delete),
    path('<int:nid>/depart_re/', depart.depart_re),

    # 用户管理
    path('user_list/', user.user_list),
    path('user_add/', user.user_add),
    path('new_user_add/', user.new_user_add),
    path('<int:nid>/user_re/', user.user_re),
    path('<int:nid>/user_delete/', user.user_delete),

    # 靓号管理
    path('pretty_list/', pretty.pretty_list),
    path('pretty_add/', pretty.pretty_add),
    path('<int:nid>/pretty_re/', pretty.pretty_re),
    path('<int:nid>/pretty_delete/', pretty.pretty_delete),

    # 管理员
    path('admin_list/', admin.admin_list),
    path('admin_add/', admin.admin_add),
    path('<int:nid>/admin_re/', admin.admin_re),
    path('<int:nid>/admin_delete/', admin.admin_delete),

    path('login/', acount.login)
]
