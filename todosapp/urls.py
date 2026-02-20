from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import TodoViewSet, RegisterView
router = DefaultRouter()
router.register('todos', TodoViewSet, basename='todo')
urlpatterns = router.urls


urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name ='register')
]