import os
import django
from django.urls import path
from django.core.asgi import get_asgi_application
from channels.http import AsgiHandler
from channels.routing import ProtocolTypeRouter, URLRouter, get_default_application
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'motion_capture_web_server.settings')

django_asgi_app = get_asgi_application()

from web_server_application.consumers import WebSocketTestConsumer

application = ProtocolTypeRouter({
    'http': django_asgi_app,
    'websocket': AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter([
                path("whole/", WebSocketTestConsumer.as_asgi())
            ])
        )
    )
})

