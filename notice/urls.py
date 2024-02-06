from django.urls import path
from notice.apps import NoticeConfig

from notice.views import NoticeCreateAPIView, NoticeListAPIView, NoticeRetrivAPIView, NoticeUpdateAPIView, \
    NoticeDestroyAPIView

app_name = NoticeConfig.name

urlpatterns = [
    path('create/', NoticeCreateAPIView.as_view(), name='notice-create'),
    path('', NoticeListAPIView.as_view(), name='notice-list'),
    path('<int:pk>/', NoticeRetrivAPIView.as_view(), name='notice-retriv'),
    path('update/<int:pk>/', NoticeUpdateAPIView.as_view(), name='notice-update'),
    path('delete/<int:pk>/', NoticeDestroyAPIView.as_view(), name='notice-delete'),
]
