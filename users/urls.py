from django.urls import path
from . import views

urlpatterns = [
  path('register/', views.register, name='register'),
  path('login/', views.login_view, name='login'),
  path('logout/', views.logout_view, name='logout'),
  path('profile/<username>', views.profile_view, name='profile'),
   path('activate/<uidb64>/<token>', views.activate, name='activate')
  # ... other URL patterns
]