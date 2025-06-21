from rest_framework.response import Response
from .serializers import MarketSerializer, SellerSerializer, ProductSerializer, SellerListSerializer
from market_app.models import Market, Seller, Product
from rest_framework.views import APIView
from rest_framework import mixins, generics, viewsets
from django.shortcuts import get_object_or_404


# class MarketsView(generics.ListCreateAPIView):
#     queryset = Market.objects.all()
#     serializer_class = MarketSerializer


# class MarketSingleView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Market.objects.all()
#     serializer_class = MarketSerializer


class MarketViewSet(viewsets.ModelViewSet):
    queryset = Market.objects.all()
    serializer_class = MarketSerializer


class SellerOfMarketList(generics.ListCreateAPIView):
    serializer_class = SellerListSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        market = Market.objects.get(pk=pk)
        return market.sellers.all()

    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        market = Market.objects.get(pk=pk)
        serializer.save(markets=[market])


# class SellersView(generics.ListCreateAPIView):
#     queryset = Seller.objects.all()
#     serializer_class = SellerSerializer


# class SellerSingleView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Seller.objects.all()
#     serializer_class = SellerSerializer


class SellerViewSet(viewsets.ModelViewSet):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer


# class ProductsView(generics.ListCreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer


# class ProductViewSetOld(viewsets.ViewSet):
#     queryset = Product.objects.all()

#     def list(self, request):
#         serializer = ProductSerializer(self.queryset, many=True)
#         return Response(serializer.data)

#     def retrieve(self, request, pk=None):
#         product = get_object_or_404(self.queryset, pk=pk)
#         serializer = ProductSerializer(product)
#         return Response(serializer.data)

#     def create(self, request):
#         serializer = ProductSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)

#     def destroy(self, request, pk=None):
#         product = get_object_or_404(self.queryset, pk=pk)
#         serializer = ProductSerializer(product)
#         product.delete()
#         return Response(serializer.data)
#  wurde ersetzt durch ModelViewSet


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    #ModelViewSet vereint z.B. MarketsView und MarketSingleView in einer Class