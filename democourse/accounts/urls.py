from django.urls import path, include
from .serialiser import *
from rest_framework.routers import DefaultRouter
from .views import *

# Routers provide an easy way of automatically determining the URL conf.
router = DefaultRouter()

router.register('users', UserViewSet, basename='user')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', HomeView.as_view(), name='index'),
    path('product', ProductView.as_view(), name='product'),
    path('customers', CustomersView.as_view(), name='product'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns += router.urls