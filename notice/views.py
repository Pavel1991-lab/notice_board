from django_filters.rest_framework import DjangoFilterBackend
from requests import Response
from rest_framework import generics
from notice.models import Notice
from notice.serlizers import NoticeSerlizer
from rest_framework.permissions import AllowAny, IsAuthenticated
from users.permissions import IsOwnerOrStaff
from notice.filters import NoticeFilter

"Вьюшки для выполнения механизма CRUD(обьявления)"


class NoticeCreateAPIView(generics.CreateAPIView):
    serializer_class = NoticeSerlizer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_author = serializer.save()
        new_author.author = self.request.user
        new_author.save()


class NoticeListAPIView(generics.ListAPIView):
    serializer_class = NoticeSerlizer
    queryset = Notice.objects.all()
    permission_classes = [AllowAny]
    filter_backends = (DjangoFilterBackend,)
    filterset_class = NoticeFilter


class NoticeRetrivAPIView(generics.RetrieveAPIView):
    serializer_class = NoticeSerlizer
    queryset = Notice.objects.all()
    permission_classes = [IsOwnerOrStaff]


class NoticeUpdateAPIView(generics.UpdateAPIView):
    serializer_class = NoticeSerlizer
    queryset = Notice.objects.all()
    permission_classes = [IsOwnerOrStaff]


class NoticeDestroyAPIView(generics.DestroyAPIView):
    queryset = Notice.objects.all()
    permission_classes = [IsOwnerOrStaff]
