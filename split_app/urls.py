from django.urls import path
from split_app import views

urlpatterns = [
    path('',views.index,name='index'),
    path('home',views.index,name='index'),
    path('logout',views.logout,name='logout'),
    path('login',views.login,name='login'),
    path('signup',views.signup,name='signup'),
    path('page',views.page,name='page'),
    path('pay',views.pay,name='pay'),
    path('delete_paid/<bill_id>',views.delete_paid,name='delete_paid'),
]