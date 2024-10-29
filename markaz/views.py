from django.http import Http404
from rest_framework.views import APIView
from .models import Xona, Oqituvchi, Oquvchilar, Fani
from .serializers import XonaSerializer, OqituvchiSerializer, OquvchiSerializer, FanSerializer
from rest_framework.response import Response
from rest_framework import generics
from django.db.models import  Q
from datetime import datetime
from rest_framework import status

from rest_framework.decorators import api_view

@api_view(["GET", "POST"])
def xona_list(request):

    if request.method == "GET":
        xonalar = Xona.objects.all()
        serialzer = XonaSerializer(xonalar, many=True).data
        print(serialzer)
        return Response(serialzer)

    if request.method == "POST":
        serializer = XonaSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)
        else:
            return Response(serializer.errors)

@api_view(["GET", "PUT", "DELETE"])

def xona_detail(request, pk):

    try:
        xona = Xona.objects.get(id=pk)
    except Xona.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        serialzier = XonaSerializer(xona)
        return Response(serialzier.data)

    elif request.method == "PUT":
        serialzier = XonaSerializer(xona, data=request.data)
        if serialzier.is_valid():
            serialzier.save()
            return Response(serialzier.data)
        else:
            return Response(serialzier.errors)
    elif request.method == "DELETE":
        xona.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)





#
# class XonaListAPI(APIView):
#     def get(self, request):
#         xonalar = Xona.objects.all()
#
#         serializer = XonaSerializer(xonalar, many=True).data
#
#         return Response(serializer)
#
#     def post(self, request):
#         data = request.data
#         serializer = XonaSerializer(data=data)
#
#         if serializer.is_valid():
#             serializer.save()
#             malumot = {
#                 "status": "Okk",
#                 "xabar": "malumot saqlandi"
#             }
#             return Response(malumot)
#         else:
#             return Response(serializer.errors)
#
# class XonaDetail(APIView):
#
#     def xonani_olish(self, pk):
#         try:
#             return Xona.objects.get(id=pk)
#         except Xona.DoesNotExist:
#             raise Http404
#
#         # return xona
#
#     def get(self, request, pk):
#         xona = self.xonani_olish(pk)
#         serializer = XonaSerializer(xona).data
#
#         return Response(serializer)
#
#     def put(self, request, pk):
#         xona = self.xonani_olish(pk)
#         serializer = XonaSerializer(xona, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk):
#         xona = self.xonani_olish(pk)
#         xona.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

class OqituvchiListAPIView(generics.ListAPIView):
    queryset = Oqituvchi.objects.all()
    serializer_class = OqituvchiSerializer

class FanListAPIView(generics.ListAPIView):
    queryset = Fani.objects.all()
    serializer_class = FanSerializer

class FanRetriveUpdateAPIView(generics.ListAPIView):
    queryset = Fani.objects.all()
    serializer_class = FanSerializer

class OquvchiListAPIView(generics.ListAPIView):
    queryset = Oqituvchi.objects.all()
    serializer_class = OquvchiSerializer


class XonaListAPIView(APIView):
    def get(self, request):
        xonalar = Xona.objects.all()
        serializer_data = XonaSerializer(xonalar, many=True).data
        data = {
            "status": "Ok",
            "xonalar": serializer_data
        }

        return Response(data)

class XonaCreateAPIView(APIView):
    def post(self, request):
        data = request.data
        xonaSerialzer = XonaSerializer(data=data)
        if xonaSerialzer.is_valid():
            xonaSerialzer.save()
            data = {
                "status": "OK",
                "malumot": f"{xonaSerialzer.data["nomi"]} saqlandi."
            }

        return Response(data)


class OqituvchiCreateAPIView(APIView):
    def post(self, request):
        data = request.data
        oqituvchiSerialzer = OqituvchiSerializer(data=data)
        if oqituvchiSerialzer.is_valid():
            oqituvchiSerialzer.save()
            data = {
                "status": "OK",
                "malumot": f"{oqituvchiSerialzer.data["ismi"]} saqlandi."
            }

        return Response(data)

class FanCreateAPIView(APIView):
    def post(self, request):
        data = request.data
        print("data-> ", data["oqituvchisi"])
        oqituvchiId = data["oqituvchisi"]
        juftmi = data["juftmi"]
        xonasi = data["xonasi"]
        darsVaqti = data["darsBoshlanishVaqti"]

        teachers = Fani.objects.filter(Q(oqituvchisi__exact=oqituvchiId) &
                                       Q(xonasi__exact=xonasi) & Q(darsBoshlanishVaqti__exact=darsVaqti)
                                       & Q(juftmi__exact=juftmi))
        # for teacher in teachers:

        print("bormi-> ", teachers)
        if teachers.count() == 0:
            print("saqlash mumkin")
        else:
            print("Saqlash mumkin emas ", teachers[0])
        # fanSerialzer = FanSerializer(data=data)
        # if fanSerialzer.is_valid():
        #     fanSerialzer.save()
        #     data = {
        #         "status": "OK",
        #         "malumot": f"{fanSerialzer.data["nomi"]} saqlandi."
        #     }

        return Response(data)


class OquvchiCreateAPIView(APIView):

    def post(self, request):
        data = request.data
        year = datetime.now().year
        tug_yil = int(data["tugSana"][:4])
        yoshi = (year - tug_yil)
        malumot = {}

        if yoshi > 15:
            oquvchiSerail = OquvchiSerializer(data=data)
            if oquvchiSerail.is_valid():
                pupil = oquvchiSerail.save()
                teacher = pupil.fani.oqituvchisi
                kursNarxi = int(pupil.fani.kursNarxi)
                soni = int(teacher.oquvchiSoni) + 1
                foiz = int(teacher.foiz)
                oylik = (soni * kursNarxi) * foiz
                teacher.oyligi = oylik
                teacher.oquvchiSoni = soni
                teacher.save()

                malumot = {
                    "status": "ok",
                    "malumot": f"{oquvchiSerail.data["ismi"]}saqlandi"
                }

        else:
            malumot = {
                "status": "fail",
                "malumot": "yoshi yetarli emas"
            }

        return Response(malumot)
