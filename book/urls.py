from django.urls import include, path
from rest_framework import routers

from book import views


router = routers.DefaultRouter()
router.register(r'books', views.BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
