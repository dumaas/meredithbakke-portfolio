from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)
from dj_rest_auth.registration.views import VerifyEmailView
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title="Post API",
        default_version="v1",
        description="API for Mere's posts",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="christiangonzalezblack@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
  public=True,
  permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # Django admin
    path('admin/', admin.site.urls),

    # API
    path('api/v1/', include('posts.urls')),
    path('api-auth/', include('rest_framework.urls')),

    # JWT Authentication
    path('api-token/', TokenObtainPairView.as_view()),
    path('api-token-refresh/', TokenRefreshView.as_view()),

    # dj-rest-auth
    path('api/v1/dj-rest-auth/', include('dj_rest_auth.urls')),
    path('api/v1/dj-rest-auth/registration', include('dj_rest_auth.registration.urls')),
    path('api/v1/dj-rest-auth/account-confirm-email', VerifyEmailView.as_view(), name='account_email_verification_sent'),

    # swagger
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
