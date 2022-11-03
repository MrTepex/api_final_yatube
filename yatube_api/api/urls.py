from django.urls import include, path

from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

v1_router = DefaultRouter()
v1_router.register(r'v1/posts', PostViewSet, basename='posts')
v1_router.register(r'v1/groups', GroupViewSet, basename='groups')
v1_router.register(r'v1/follow', FollowViewSet, basename='follow')
v1_router.register(r'v1/posts/(?P<post_id>\d+)/comments', CommentViewSet,
                   basename='comments')


urlpatterns = [
    path('', include(v1_router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
