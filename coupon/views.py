from .models import Coupon
from .serializers import CouponSerializer
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.views import APIView

from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response


###
class CustomPagination(PageNumberPagination):
    page_size = 15


class CouponListCreate(generics.ListCreateAPIView):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    filterset_fields = ('user', 'code', "discount")
    search_fields = ('code',)
    pagination_class = CustomPagination


class CouponGetUpdate(generics.RetrieveUpdateAPIView):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer
    permission_classes = (AllowAny,)

class CouponDelete(generics.DestroyAPIView):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

class CouponGetCode(APIView):
    def get(self, request, code, format=None):
        try:
            c = Coupon.objects.get(code=code)
            serializer = CouponSerializer(c)
            return Response(serializer.data, status=200)
        except:
            d = {'status':'404','detail':'Something went wrong.'}
            return Response(d, status=404)