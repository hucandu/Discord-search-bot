from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from django.views import defaults as default_views
from rest_framework.schemas import get_schema_view
from rest_framework.renderers import OpenAPIRenderer, JSONOpenAPIRenderer
from discord_search_bot import __version__

urlpatterns = [
    # Domain Root
    path(
        "",
        default_views.permission_denied,
        kwargs={"exception": Exception("Permission Denied")},
        name="home"
    ),
    path(  # noqa F405
        "openapi",
        get_schema_view(  # noqa F405
            url="http://discordsearchbot.tk/",  # noqa F405
            title="Discord Search BOT",  # noqa F405
            description="Discord Search BOT",  # noqa F405
            version=__version__,  # noqa F405
            renderer_classes=(JSONOpenAPIRenderer, OpenAPIRenderer,)  # noqa F405
        ),  # noqa F405
        name="discord_search_bot-schema",  # noqa F405
    ),
    # Example Url Config
    # Your stuff: custom urls includes go here
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
