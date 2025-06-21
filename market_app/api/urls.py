from django.urls import path
from .views import MarketsView, MarketSingleView, SellerView, products_view, sellers_single_view

urlpatterns = [
    path('market/', MarketsView.as_view()),
    path('market/<int:pk>/', MarketSingleView.as_view(), name="market-detail"),
    path('seller/', SellerView.as_view()),
    path('seller/<int:pk>/', sellers_single_view, name='seller_single'),
    path('product/', products_view)
]
