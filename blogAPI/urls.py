"""
URL configuration for blogAPI project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework_swagger.views import get_swagger_view
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Kitoblar dasturining API lari",
        default_version="v1",
        description="Bu API lar hammasi Kitoblarni malumotlarini olish",
        terms_of_service="demo.com",
        contact=openapi.Contact(email="nasriddinovmusojon852@gmail.com")
    )
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/v1/", include("books.urls")),
    path("api/v1/markaz/", include("markaz.urls")),
    path("api-auth/", include("rest_framework.urls")),
    path("api/v1/dj-rest-auth", include("dj_rest_auth.urls")),
    path("api/v1/dj-rest-auth/registration", include("dj_rest_auth.registration.urls")),
    path('swagger/', schema_view.with_ui(
        'swagger', cache_timeout=0), name="swagger-ui")
]
