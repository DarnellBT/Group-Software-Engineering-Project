from django.urls import path

from . import views

urlpatterns = [
    path('account/', views.dashboard, name='dashboard'),
    path('account/challenges/', views.challenges, name='challenges'),
    path('account/change-username/', views.change_uname, name='change-uname'),
    path('account/change-name/', views.change_name, name='change-name'),
    path('account/change-password/', views.change_password, name='change-password'),
    path('logout/', views.logout_dashboard, name="logout"),
    path('account/edit-account/', views.edit_account, name='edit_account'),
    path('account/rewards/', views.rewards, name='rewards')
]
