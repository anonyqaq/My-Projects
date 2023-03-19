from django.shortcuts import render, redirect
from users import models

from users.utils.pagenation import Pagenation

from users.utils.form import PrettyModelForm


# 靓号
def pretty_list(request):
    # for i in range(100):
    #     models.PrettyNum.objects.create(moblie="18888888888", price=100, level=1, status=1)
    pretty_dict = {}
    search_pretty = request.GET.get('q', "")
    if search_pretty:
        pretty_dict["moblie__contains"] = search_pretty
    # quest_list = int(request.GET.get('page', 1))
    # start = (quest_list - 1) * 10
    # end = quest_list * 10
    queryset = models.PrettyNum.objects.filter(**pretty_dict).order_by("-level")
    page_object = Pagenation(request, queryset)
    context = {
        "search_data": search_pretty,
        "queryset": page_object.page_queryset,
        "page_string": page_object.html()
    }

    # pretty_count = models.PrettyNum.objects.all().count()
    # pretty_count, div = divmod(pretty_count, 10)
    # if div:
    #     pretty_count += 1
    #
    # page_str_list = []
    # for i in range(1,pretty_count+1):
    #     ele = f'<li ><a href="?page={i}">{i}</a></li>'
    #     page_str_list.append(ele)
    # str_page = mark_safe("".join(page_str_list))
    return render(request, 'pretty_list.html', context)


def pretty_add(request):
    if request.method == "GET":
        form = PrettyModelForm()
        return render(request, 'pretty_add.html', {"form": form})
    form = PrettyModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect("/pretty_list/")


# 编辑靓号
def pretty_re(request, nid):
    row_object = models.PrettyNum.objects.filter(id=nid).first()
    if request.method == "GET":
        form = PrettyModelForm(instance=row_object)
        return render(request, 'pretty_re.html', {"form": form})
    form = PrettyModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect("/pretty_list/")


# 删除靓号
def pretty_delete(request, nid):
    models.PrettyNum.objects.filter(id=nid).delete()
    return redirect("/pretty_list/")
