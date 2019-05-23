from django.conf.urls import url

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator

from Fieldchoice.notifications.consumers import NotificationsConsumer
# from Fieldchoice.notifications.routing import notifications_urlpatterns
# from Fieldchoice.messager.routing import messager_urlpatterns

application = ProtocolTypeRouter({
    "websocket": AllowedHostsOriginValidator(
        AuthMiddlewareStack(
            URLRouter([
                url(r'^notifications/$', NotificationsConsumer),
                
            ])
        ),
    ),
})
