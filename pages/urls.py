from django.urls import path,include

from pages import views 

urlpatterns = [
    path('', views.home , name='home' ),
    path('book-appointment/', views.bookappointment , name='bookappointment' ),
    path('appointment-detail/<int:id>/', views.appointmentdetail, name='appointment_detail' ),
    path('appointment-delete/<int:id>/', views.appointmentdelete, name='appointmentdelete' ),
    path('dashboard/', views.dashboardPatiend , name='dashboard' ),
    path('dashboard-doctor/', views.dashboardDoctor, name='dashboardD' ),
]