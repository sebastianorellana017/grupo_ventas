from cart.viewsets import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Product',ProductViewSet)
router.register('ColorVariation',ColourVariationViewSet)
router.register('ordenitem',OrderItemViewSet)
router.register('payment', PaymentViewSet)
router.register('order', OrderViewSet)
router.register('category', CategoryViewSet)
router.register('SizeVariation', SizeVariationViewSet)
router.register('Address', AddressViewSet)

