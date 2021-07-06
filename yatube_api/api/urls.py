from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import permissions
from .views import CommentViewSet, PostViewSet, GroupViewSet, FollowViewSet
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf.urls import url
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


router = DefaultRouter()
router.register(r'posts/(?P<post_id>\d+)/comments',
                CommentViewSet, basename='CommentViewSet')
router.register('posts', PostViewSet, basename='PostView')
router.register('group', GroupViewSet, basename='GroupView')
router.register('follow', FollowViewSet, basename='FollowView')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/token/',
         TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('v1/token/refresh/',
         TokenRefreshView.as_view(), name='token_refresh'),
]

schema_view = get_schema_view(
   openapi.Info(
      title="Cats API",
      default_version='v1',
      description="Документация для приложения cats проекта проекта Kittygram",
      # terms_of_service="URL страницы с пользовательским соглашением",
      contact=openapi.Contact(email="admin@kittygram.ru"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns += [
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0),
        name='schema-redoc'),
]
