from channels.routing import ProtocolTypeRouter, URLRouter
import os

from django.core.asgi import get_asgi_application
from chat_application import urls


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chat_application.settings')

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": URLRouter(urls.websocket_urlpatterns),
    }
)
