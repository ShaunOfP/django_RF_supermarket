from django.urls import path, include
from .views import SellerOfMarketList, MarketViewSet, SellerViewSet, ProductViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register(r'market', MarketViewSet)
router.register(r'seller', SellerViewSet)
router.register(r'product', ProductViewSet)



urlpatterns = [
    path('', include(router.urls)),
    # path('market/', MarketsView.as_view()),
    # path('market/<int:pk>/', MarketSingleView.as_view(), name='market-detail'),
    path('market/<int:pk>/sellers/', SellerOfMarketList.as_view()),
    # path('seller/', SellersView.as_view()),
    # path('seller/<int:pk>/', SellerSingleView.as_view(), name='seller-detail'),
]
