from django.urls import path
from .views import SnackListView,SnackDetailView,HomePage,snackCreateView,snackDeleteView,snackUpdateView
urlpatterns = [
    path('',HomePage.as_view(), name='home'),
    path('snacks/',SnackListView.as_view(), name='snacks'),
    path('snacks/<int:pk>',SnackDetailView.as_view(), name='snack_detail'),
    path('snacks/create/',snackCreateView.as_view(), name='snack_create'),
    path('snacks/<int:pk>/update/',snackUpdateView.as_view(), name='snack_update'),
    path('snacks/<int:pk>/delete/',snackDeleteView.as_view(), name='snack_delete'),
    
]