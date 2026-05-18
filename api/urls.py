from django.urls import path
from .views import RegisterView, LoginView, UserDataView, AdminDashboardStatsView

urlpatterns = [
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/login/', LoginView.as_view(), name='login'),
    path('auth/user/', UserDataView.as_view(), name='user_data'),
    path('admin-stats/', AdminDashboardStatsView.as_view(), name='admin_stats'),
]
