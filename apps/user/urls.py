# django
from django.urls import path
# third
# own
from apps.user.views import Home, Login, Logout, AddUser

urlpatterns = [
    path('', Home.as_view(), name='base_home_user'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('add_user/', AddUser.as_view(), name='add_user'),
]