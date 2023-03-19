from django.shortcuts import render, redirect
from users import models


# 部门
def depart_list(request):
    Depart_list = models.Department.objects.all()
    return render(request, 'depart_list.html', {"Depart_list": Depart_list})


# 添加部门
def depart_add(request):
    if request.method == "GET":
        return render(request, 'depart_add.html')
    title = request.POST.get("title")
    models.Department.objects.create(title=title)

    return redirect("/depart_list/")


# 删除部门
def depart_delete(request):
    nid = request.GET.get('nid')
    models.Department.objects.filter(id=nid).delete()
    return redirect("/depart_list/")


# 更新部门
def depart_re(request, nid):
    if request.method == "GET":
        row_object = models.Department.objects.filter(id=nid).first()
        return render(request, 'depart_re.html', {"row_object": row_object})
    title = request.POST.get("title")
    models.Department.objects.filter(id=nid).update(title=title)
    return redirect("/depart_list/")
