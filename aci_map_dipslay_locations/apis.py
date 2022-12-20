import json

from django.db import connection
from rest_framework.views import APIView
from rest_framework.response import Response


class refreshApi(APIView):
    def get(self, request):
        return Response({'status': getData() + " data fetched !"})


def getData():
    all_data = []
    all_pharma = []
    all_electrical = []
    with connection.cursor() as cursor:
        cursor.execute("select * from [192.168.100.61].[GroupDashboard].[dbo].[CustomerTouchPoint]")
        row = cursor.fetchall()
        for r in row:
            all_data.append(
                {"type": "Feature",
                 "properties": {"id": r[0], "name": r[1], "business": r[8], "type": r[5],
                                "address": r[7] + ' , ' + r[6]},
                 "geometry": {"type": "Point", "coordinates": [r[3], r[2], 2.609]}}
            )
            if r[8] == 'Pharmaceuticals':
                all_pharma.append(
                    {"type": "Feature",
                     "properties": {"id": r[0], "name": r[1], "business": r[8], "type": r[5],
                                    "address": r[7] + ' , ' + r[6]},
                     "geometry": {"type": "Point", "coordinates": [r[3], r[2], 2.609]}})
            if r[8] == 'Electrical':
                all_electrical.append(
                    {"type": "Feature",
                     "properties": {"id": r[0], "name": r[1], "business": r[8], "type": r[5],
                                    "address": r[7] + ' , ' + r[6]},
                     "geometry": {"type": "Point", "coordinates": [r[3], r[2], 2.609]}})

        with open("static/all.geojson", "w") as outfile:
            outfile.write(json.dumps(
                {
                    "type": "FeatureCollection",
                    "crs": {"type": "name", "properties": {"name": "urn:ogc:def:crs:OGC:1.3:CRS84"}},
                    "features": all_data
                }, indent=4))
        with open("static/pharma.geojson", "w") as outfile:
            outfile.write(json.dumps(
                {
                    "type": "FeatureCollection",
                    "crs": {"type": "name", "properties": {"name": "urn:ogc:def:crs:OGC:1.3:CRS84"}},
                    "features": all_pharma
                }, indent=4))
        with open("static/electrical.geojson", "w") as outfile:
            outfile.write(json.dumps(
                {
                    "type": "FeatureCollection",
                    "crs": {"type": "name", "properties": {"name": "urn:ogc:def:crs:OGC:1.3:CRS84"}},
                    "features": all_electrical
                }, indent=4))
    return str(len(all_data)) + ' ' + str(len(all_pharma)) + ' ' + str(len(all_electrical)) + ' '
