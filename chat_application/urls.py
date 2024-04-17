from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from rest_framework.routers import DefaultRouter

from server.views import SeverListViewSet
from webchat.consumer import MyConsumer

router = DefaultRouter()
router.register("api/server/", SeverListViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/docs/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/docs/schema/swagger-ui/', SpectacularSwaggerView.as_view(), name='swagger-ui'),
] + router.urls

websocket_urlpatterns = [
    path("ws/test", MyConsumer.as_asgi())
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
