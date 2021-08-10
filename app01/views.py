from django.shortcuts import render, HttpResponse


def index(request):
    import datetime
    now = datetime.datetime.now()
    ctime = now.strftime("%Y-%m-%d %X")
    return render(request, "index.html", {"ctime": ctime})


def year_archive(request):
    return None


def month_archive(request):
    return None


def article_detail(request):
    return None