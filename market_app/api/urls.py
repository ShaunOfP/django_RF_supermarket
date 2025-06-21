from django.urls import path
from .views import MarketsView, MarketSingleView, SellerOfMarketList, SellersView, SellerSingleView, ProductsView

urlpatterns = [
    path('market/', MarketsView.as_view()),
    path('market/<int:pk>/', MarketSingleView.as_view(), name='market-detail'),
    path('market/<int:pk>/sellers/', SellerOfMarketList.as_view()),
    path('seller/', SellersView.as_view()),
    path('seller/<int:pk>/', SellerSingleView.as_view(), name='seller-detail'),
    path('product/', ProductsView.as_view())
]
