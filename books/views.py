from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from .serializers import BookSerializer
from .models import Book
from rest_framework import generics, status
from rest_framework.response import Response
from django.db.models import Q

class BookListAPIView(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer_data = BookSerializer(books, many=True).data
        data = {
            "status": f"Malumot yetib keldi. Soni  {len(books)}",
            "books": serializer_data,
            "Egasi": "Ogabek"
        }

        return Response(data)

class BookCreateAPIView(APIView):

    def post(self, request):
        data = request.data

        print("data -> ", data)
        title = data["title"]

        if Book.objects.filter(price__gte=500000):
            serializer = BookSerializer(data=data)
            # print(type(data))
            print("serializer: ", serializer)
            if serializer.is_valid():
                print("OKKKKK")

                serializer.save()
                print("O1111")
                data = {
                    "status": "Malumotlar saqlandi",
                    "data": serializer.data
                }

                return Response(data)
            else:
                data = {
                    "status": "malumotlar yaroqli emas"
                }
                return Response(data)
        else:
            data = {
                "status": "afsus",
                "message": "Bunday malumotni saqlay olmaymiz."
            }
            return Response(data)

class BookDetailAPIView(APIView):
    def get(self, request, pk):
        book = Book.objects.get(id=pk)
        serializer = BookSerializer(book).data

        data = {
            "status": "Okk",
            "book": serializer
        }

        return Response(data)

class BookUpdateAPIView(APIView):
    def put(self, request, pk):
        book = get_object_or_404(Book.objects.all(), id=pk)
        data = request.data
        serilazer = BookSerializer(instance=book, data=data, partial=True)

        if serilazer.is_valid(raise_exception=True):
            serilazer.save()

            return Response({
                "status": "Yaxshi",
                "message": f"Kitob {serilazer.data} muvaffaqiyatli o'zgartirildi."
            })

class BookDeleteAPIVIew(APIView):
    def delete(self, request, pk):
        try:
            book = Book.objects.get(id=pk)
            book.delete()
            return Response({
                "status": True,
                "message": "Kitob o'chirildi."
            }, status=status.HTTP_200_OK)
        except Exception:
            return Response({
                "status": False,
                "message": "Kitob topilmadi"
            }, status=status.HTTP_400_BAD_REQUEST )


class BookListCreateAPI(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetailUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer



# class BookRetriveUpadateAPI(generics.RetrieveUpdateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#
# class BookDeleteRetrieveAPI(generics.RetrieveDestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#
# class BookListAPI(generics.ListAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#
# class BookCreateAPI(generics.CreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#
#
# class BookDetailAPI(generics.RetrieveAPIView):
#     # lookup_field = "id"
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#
# class BookUpdateAPI(generics.UpdateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#
#
# class BookDeleteAPI(generics.DestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer