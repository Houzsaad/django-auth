from django.contrib import admin
from django.urls import path, include

from rest_framework_simplejwt.views import(

TokenObtainPairView, 
TokenRefreshView,
)

from todosapp.views import TodoViewSet
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'todos', TodoViewSet, basename='todos')


urlpatterns = [
    path('admin/', admin.site.urls),

    path('firstapp', include('firstapp.urls')),

    path('accounts/', include('accounts.urls')),

    path('api-auth/', include('rest_framework.urls')),

    path('todosapp/', include('todosapp.urls')),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),



    path('api/', include(router.urls)),

]