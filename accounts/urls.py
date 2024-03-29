from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login', views.Login.as_view(), name='login'),
    path('logout', views.Logout.as_view(), name='logout'),
    path('signup', views.SignUp.as_view(), name='signup'),
    # path('profile/<username>', views.Profile.as_view(), name='profile'),
    # path('edit_profile/<username>', views.EditProfile.as_view(), name='edit-profile'),
    # path('<username>/avatar', views.get_avatar, name='get-avatar'),
    # path('panel/<username>', views.Panel.as_view(), name='panel'),
]
