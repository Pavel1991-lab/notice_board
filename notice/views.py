from django_filters.rest_framework import DjangoFilterBackend
from requests import Response
from rest_framework import generics

from notice.models import Notice
from notice.serlizers import NoticeSerlizer
from rest_framework.permissions import AllowAny, IsAuthenticated
from users.permissions import IsOwnerOrStaff

from notice.filters import NoticeFilter


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
    filter_backends = (DjangoFilterBackend,)  # Подключаем библотеку, отвечающую за фильтрацию к CBV
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



class NoticeSearchView(generics.ListAPIView):
    queryset = Notice.objects.all()
    serializer_class = NoticeSerlizer

    def post(self, request):
        title = request.data.get('title', None)
        if title is not None:
            queryset = Notice.objects.filter(title__icontains=title)
            serializer = NoticeSerlizer(queryset, many=True)
            return Response(serializer.data)
        else:
            return Response({'message': 'Please provide a title'})





