from django.urls import path

from .import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.index, name="index"),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path("logout", views.logout, name="logout"),
    path("problems", views.form, name="problems"),
    path("contactus", views.contactus, name="contactus"),
    path("team_register", views.team_register, name="team_register"),
    path("profile", views.profile, name="profile"),
    path('editprofile/<int:reg_pk>/', views.editprofile , name = "editprofile"),
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name="password_reset.html"),name="reset_password"),
    path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(template_name="password_reset_sent.html"),name="password_reset_done"),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_form.html"),name="password_reset_confirm"),
    path('reset_password_complete/',auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_done.html"),name="password_reset_complete"),
    #path("team_detail", views.team_detail, name="team_detail"),

    ]
