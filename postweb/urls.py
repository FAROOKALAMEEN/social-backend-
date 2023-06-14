from django.urls import path
from postweb import views

urlpatterns=[
    path('signup/',views.SignUpView.as_view(),name="reg"),
    path('',views.LogInView.as_view(),name="login"),
    path('home/',views.HomeView.as_view(),name="home"),
    path('createprofile/',views.ProfileCreateView.as_view(),name="profile_create"),
    path('profile/',views.ProfileView.as_view(),name="profile_detail")

]