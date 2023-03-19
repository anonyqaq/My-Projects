from django.shortcuts import render, redirect
from users import models
from users.utils.form import AdminModelForm, AdminEditModelForm


def admin_list(request):
    admin_list = models.Admin.objects.all()
    return render(request, 'admin_list.html', {"admin_list": admin_list})


def admin_add(request):
    if request.method == "GET":
        form = AdminModelForm()
        return render(request, 'test.html', {"form": form, "title": "新建管理员"})
    form = AdminModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/admin_list/')


def admin_re(request, nid):
    row_object = models.Admin.objects.filter(id=nid).first()
    if not row_object:
        return redirect('/admin_list')

    title = "编辑管理员"
    if request.method == "GET":
        form = AdminEditModelForm(instance=row_object)
        return render(request, 'test.html', {"form": form, "title": title})

    form = AdminEditModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/admin_list/')


def admin_delete(request, nid):
    models.Admin.objects.filter(id=nid).delete()
    return redirect('/admin_list/')
