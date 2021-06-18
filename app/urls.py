from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from core import views
from cart.api import UserAPI, ProductAPI, PaymentAPI, OrderAPI

from .router import router


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('home/', views.HomeView.as_view(), name='home'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('cart/', include('cart.urls', namespace='cart')),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('apis/',include(router.urls), name='apis'),
    path('api/user', UserAPI.as_view(), name="api_create_user"),
    path('api/productos', ProductAPI.as_view(), name="api_productos"),
    path('api/payment', PaymentAPI.as_view(), name="api_payment"),
    path('api/order', OrderAPI.as_view(), name="api_order"),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)