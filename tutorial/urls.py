from django.urls import include, path
from rest_framework import routers
from tutorial.posts import views as p_views
from tutorial.quickstart import views as q_views

router = routers.DefaultRouter()
router.register(r'users', q_views.UserViewSet)
router.register(r'groups', q_views.GroupViewSet)
router.register(r'posts', p_views.PostViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]