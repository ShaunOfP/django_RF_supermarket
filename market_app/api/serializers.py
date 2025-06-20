from rest_framework import serializers
from market_app.models import Market, Seller, Product


class MarketSerializer(serializers.ModelSerializer):
    sellers = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = Market
        fields = ['id', 'name', 'location',
                  'description', 'net_worth', 'sellers']

    def validate_name(self, value):
        errors = []
        if 'X' in value:
            errors.append('no X in location')
        if 'Y' in value:
            errors.append('no Y in location')
        if errors:
            raise serializers.ValidationError(errors)
        return value


class MarketHyperlinkedSerializer(MarketSerializer, serializers.HyperlinkedModelSerializer):
    sellers = None

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop('fields', None)

        # Instantiate the superclass normally
        super().__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)

    class Meta:
        model = Market
        fields = ['id', 'url', 'name', 'location', 'description', 'net_worth']


class SellerSerializer(serializers.ModelSerializer):
    markets = MarketSerializer(many=True, read_only=True)
    market_ids = serializers.PrimaryKeyRelatedField(
        queryset=Market.objects.all(), many=True, write_only=True, source='markets')

    market_count = serializers.SerializerMethodField()

    class Meta:
        model = Seller
        fields = ['id', 'name', 'market_ids',
                  'market_count', 'markets', 'contact_info']

    def get_market_count(self, obj):
        return obj.markets.count()


class ProductSerializer(serializers.ModelSerializer):
    market = MarketSerializer(many=False, read_only=True)
    market_id = serializers.PrimaryKeyRelatedField(
        queryset=Market.objects.all(), many=False, write_only=True, source='market')
    seller = SellerSerializer(many=False, read_only=True)
    seller_id = serializers.PrimaryKeyRelatedField(
        queryset=Seller.objects.all(), many=False, write_only=True, source='seller')

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price',
                  'market', 'market_id', 'seller', 'seller_id']


# class ProductsDetailSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(max_length=255)
#     description = serializers.CharField()
#     price = serializers.DecimalField(max_digits=50, decimal_places=2)
#     market = MarketSerializer(many=False, read_only=True)
#     seller = SellersDetailSerializer(many=False, read_only=True)


# class ProductsCreateSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=255)
#     description = serializers.CharField()
#     price = serializers.DecimalField(max_digits=50, decimal_places=2)
#     market = serializers.PrimaryKeyRelatedField(queryset=Market.objects.all())
#     seller = serializers.PrimaryKeyRelatedField(queryset=Seller.objects.all())

#     def create(self, validated_data):
#         product = Product.objects.create(**validated_data)
#         return product
