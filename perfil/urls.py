from django.urls import path
from .views import RegisterView, RegisterList, RetrieveUser, InfoUser, UpdateUser
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('registro/', RegisterView.as_view(), name='register_view'),
    path('lista/', RegisterList.as_view(), name='register_list'),
    path('username/<str:username>', RetrieveUser.as_view(), name='username'),
    path('info_user/<int:pk>', InfoUser.as_view(), name='info_user'),
    path('update_user/<int:pk>', UpdateUser.as_view(), name='update_user'),
]
