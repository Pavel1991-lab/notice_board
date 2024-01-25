from fidback.apps import FidbackConfig
from django.urls import path
from fidback.views import FidbackCreateAPIView, FidbackListAPIView, FidbackRetrivAPIView, FidbackUpdateAPIView, \
    FidbackDestroyAPIView

app_name = FidbackConfig.name

urlpatterns = [
   path('create/', FidbackCreateAPIView.as_view(), name='fidback-create'),
   path('', FidbackListAPIView.as_view(), name='fidback-list'),
   path('<int:pk>/', FidbackRetrivAPIView.as_view(), name='fidback-retriv'),
   path('update/<int:pk>/', FidbackUpdateAPIView.as_view(), name='fidback-update'),
   path('delete/<int:pk>/', FidbackDestroyAPIView.as_view(), name='fidback-delete'),
]