from django.urls import path
from . import views


urlpatterns = [
    path('signup/', views.SignupClassView.as_view(),name='signup'),
    path('login/', views.LoginClassView.as_view(),name='login'),
    path('logout/', views.LogoutClassView.as_view(),name='logout'),
    path('password-reset/', views.PasswordResetView.as_view(),name='password_reset'),
    path('password-reset-done/', views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password-change/',views.PasswordChangeView.as_view(),name='password_change'),
    path('password-change-done/',views.PasswordChangeDoneView.as_view(),name='password_change_confirm')
]