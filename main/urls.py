from django.urls import path
from .views import CategoryView, PostView

urlpatterns = [
    path('post/', PostView.as_view(), name='post'),
    path('category/', CategoryView.as_view(), name='category')
]
