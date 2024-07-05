from django.urls import path
from .views import BookViewSet,UserViewSet,TransactionViewSet,BookDetail,UserDetail,TransactionDetail

urlpatterns = [
    path('bookapp/', BookViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('bookapp/book/<int:pk>/', BookDetail.as_view()),
    path('user/', UserViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('user/<int:pk>/', UserDetail.as_view()),
    path('transaction/', TransactionViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('transaction/<int:pk>/', TransactionDetail.as_view())
]