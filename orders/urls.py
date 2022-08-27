from django.urls import path

from .views import HelloOrderView

urlpatterns = [
    path('', HelloOrderView.as_view()),
]