from django.shortcuts import render
from django.http import request


def display_location(request):
    return render(request, 'display_location.html')


def loadpoints(request):
    type_val = request.GET.get('type')
    lat_val = request.GET.get('lat')
    lng_val = request.GET.get('lng')
    zoom_val = request.GET.get('zoom')

    print(lat_val, lng_val, zoom_val)

    context = {

        'data': 'http://36.255.71.1:8001/static/pharma.geojson' if type_val == '1' else (
            'http://36.255.71.1:8001/static/electrical.geojson' if type_val == '2' else 'http://36.255.71.1:8001/static/all.geojson'),
        'type': type_val if type_val else 0,
        'zoom': zoom_val if zoom_val else 6,
        'lat': lat_val if lat_val else 23.7645784,
        'lng': lng_val if lng_val else 90.3510153

    }
    print(context)
    return render(request, 'loadpoints.html', context)


def geodata(request):
    return render(request, 'loadpoints.html')


def filter(request):
    return render(request, 'filtertest.html')
def datadriven(request):
    return render(request, 'datadriven.html')
