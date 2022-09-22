from django.shortcuts import render
from mywatchlist.models import WatchList
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_mywatchlist(request):
    data_mywatchlist = WatchList.objects.all()
    context = {
        'list_tontonan': data_mywatchlist,
        'nama': 'Ahmad Fatahillah',
        'npm': '2106653741',
        'total_watched': 0,
        'status' : ""
    }

    for tontonan in data_mywatchlist:
        if tontonan.watched == "Watched":
            context['total_watched'] += 1

    if context['total_watched'] >= (len(data_mywatchlist))/2:
        context["status"] += "Selamat, Kamu sudah banyak menonton!"
    else:
        context["status"] += "Wah, kamu masih sedikit menonton :("

    return render(request, "mywatchlist.html", context)

def show_xml(request):
    data = WatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = WatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request, id):
    data = WatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = WatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")