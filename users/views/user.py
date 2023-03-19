from django.shortcuts import render, redirect
from users import models

from users.utils.pagenation import Pagenation

from users.utils.form import UserModelForm


# 用户
def user_list(request):
    user_list = models.UserInfo.objects.all()
    page_object = Pagenation(request, user_list)
    context = {
        "user_list": page_object.page_queryset,
        "page_string": page_object.html()
    }
    return render(request, 'user_list.html', context)


# 添加用户
def user_add(request):
    if request.method == "GET":
        new_dict = {
            "gender_lsit": models.UserInfo.gender_choices,
            "darpar_list": models.Department.objects.all()
        }
        return render(request, 'user_add.html', new_dict)
    user = request.POST.get("name")
    pwd = request.POST.get("pwd")
    age = request.POST.get("age")
    accout = request.POST.get("count")
    ctime = request.POST.get("time")
    sex = request.POST.get("sex")
    bu = request.POST.get("bu")

    models.UserInfo.objects.create(name=user, password=pwd,
                                   age=age, account=accout,
                                   create_time=ctime,
                                   gender=sex, depart_id=bu)
    return redirect('/user_list/')


# 添加用户
def new_user_add(request):
    if request.method == "GET":
        form = UserModelForm()
        return render(request, 'new_user_add.html', {"form": form})
    form = UserModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/user_list/')


# 更新用户
def user_re(request, nid):
    row_object = models.UserInfo.objects.filter(id=nid).first()
    if request.method == "GET":
        form = UserModelForm(instance=row_object)
        return render(request, 'user_re.html', {"form": form})
    form = UserModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect("/user_list/")


# 删除用户
def user_delete(request, nid):
    models.UserInfo.objects.filter(id=nid).delete()
    return redirect("/user_list/")
