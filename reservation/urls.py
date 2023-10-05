from django.urls import path

from reservation import views

urlpatterns = [
    path('create_reservation/', views.ReservationCreateView.as_view(), name='create_reservation'),
    path('list_of_reservations/', views.ReservationListView.as_view(), name='list-of-reservations'),
    path('update_reservation/<int:pk>/', views.ReservationUpdateView.as_view(), name='update-reservation'),
    path('delete_reservation/<int:pk>/', views.ReservationDeleteView.as_view(), name='delete-reservation'),
    path('detail_reservation/<int:pk>/', views.ReservationDetailView.as_view(), name='detail-reservation'),
]
