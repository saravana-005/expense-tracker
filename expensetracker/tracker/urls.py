from django.urls import path
from . import views
urlpatterns=[
    path('track/',views.expense_chart,name='add_expense'),
    path('',views.register_view,name='register'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('home/',views.home,name='home'),
    path('sheet/',views.sheet_view,name='sheet'),
    path('delete/<int:expense_id>/',views.delete,name='delete'),
]