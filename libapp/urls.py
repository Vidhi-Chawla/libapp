from django.urls import path
from .views import BookViewSet,BookDetail,BookSelectView

urlpatterns = [
    path('libapp/', BookViewSet.as_view()),
    path('libapp/<int:pk>/', BookDetail.as_view()),
    path('libapp/select/', BookSelectView.as_view(),name='book-select')
]