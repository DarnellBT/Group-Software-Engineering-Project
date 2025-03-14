"""
URL configuration for ecoquest project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from about import views as contact_view
from challenge import views as challenge_view
from dashboard import views as dashboard_view
from django.contrib import admin
from django.urls import path
from leaderboard import views as leaderboard_view
from django.contrib.auth import views as auth_views
from login import views as login_view
from main import views as main_view
from map import views as map_view
from qrcodescan import views as qr_view
from quiz import views as quiz_view
from registration import views as register_view
from sustain import views as sus_view
from roleportals import views as role_view
from achievements import views as achievements_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', register_view.register, name='register'),
    path('login/', login_view.login_page, name='login'),
    path('home/', main_view.home, name='home'),
    path('account/', dashboard_view.dashboard, name='account'),
    path('', main_view.home, name='home'),
    path('map/', map_view.MapView.as_view(), name='map'),
    path('challenge/', challenge_view.challenge, name='challenge'),
    path('quiz/<int:id>/', quiz_view.quiz, name='quiz'),
    path('challenge/<int:id>/', challenge_view.challenge, name='challenge'),
    path('account/challenges/', dashboard_view.challenges, name='challenges'),
    path('account/change-username/', dashboard_view.change_uname, name='change-uname'),
    path('account/change-name/', dashboard_view.change_name, name='change-name'),
    path('account/change-password/', dashboard_view.change_password, name='change-password'),
    path('logout/', dashboard_view.logout_dashboard, name="logout"),
    path('leaderboard/', leaderboard_view.leaderboard_page, name='leaderboard'),
    path('qr-scanner/', qr_view.scanner, name='qr-scanner'),
    path('sustainability/', sus_view.sustain, name='sustainability'),
    path('contact/', contact_view.contact, name="contact"),
    path('quiz/<int:id>/results/', quiz_view.results, name='results'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='passwordResetForm.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='passwordResetDone.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='passwordResetConfirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='passwordResetComplete.html'), name='password_reset_complete'),
    path('admin-portal/', role_view.admin_portal, name='admin-portal'),
    path('gamekeeper-portal/', role_view.gamekeeper_portal, name="gamekeeper-portal"),
    path('achievements/', achievements_view.achievements, name="achievements"),
    path('admin-portal/edit-location/', role_view.admin_location, name='admin-location'),
    path('admin-portal/edit-quiz/', role_view.admin_quiz, name='admin-quiz'),
    path('admin-portal/edit-question/', role_view.admin_question, name='admin-question'),
    path('admin-portal/edit-challenge/', role_view.admin_challenge, name='admin-challenge'),
    path('admin-portal/edit-location/edit-location/<int:location_id>/', role_view.edit_location, name='edit_location'),
    path('admin-portal/edit-location/delete-location/<int:location_id>/', role_view.delete_location, name='delete_location'),
     path('admin-portal/edit-quiz/edit-quiz/<int:quiz_id>/', role_view.edit_quiz, name='edit_quiz'),
    path('admin-portal/edit-quiz/delete-quiz/<int:quiz_id>/', role_view.delete_quiz, name='delete_quiz'),
    path('admin-portal/edit-question/edit-question/<int:question_id>/', role_view.edit_question, name='edit_question'),
    path('admin-portal/edit-question/delete-question/<int:question_id>/', role_view.delete_question, name='delete_question'),
    path('admin-portal/edit-challenge/edit-challenge/<int:challenge_id>/', role_view.edit_challenge, name='edit_challenge'),
    path('admin-portal/edit-challenge/delete-challenge/<int:challenge_id>/', role_view.delete_challenge, name='delete_challenge'),
    path('account/edit-account/', dashboard_view.edit_account, name='edit_account'),
    path('home/privacy/', main_view.privacy, name='privacy'),
    path('account/rewards/', dashboard_view.rewards, name='rewards')
]
