from rest_framework import generics

from fidback.models import Fidback
from fidback.serlizers import FidbackSerlizer
from rest_framework.permissions import AllowAny, IsAuthenticated

from users.permissions import IsOwnerOrStaff

"Вьюшки для выполнения механизма CRUD(отзывы)"


class FidbackCreateAPIView(generics.CreateAPIView):
    serializer_class = FidbackSerlizer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        new_author = serializer.save()
        new_author.author = self.request.user
        new_author.save()


class FidbackListAPIView(generics.ListAPIView):
    serializer_class = FidbackSerlizer
    queryset = Fidback.objects.all()
    permission_classes = [IsAuthenticated]


class FidbackRetrivAPIView(generics.RetrieveAPIView):
    serializer_class = FidbackSerlizer
    queryset = Fidback.objects.all()
    permission_classes = [IsOwnerOrStaff]


class FidbackUpdateAPIView(generics.UpdateAPIView):
    serializer_class = FidbackSerlizer
    queryset = Fidback.objects.all()
    permission_classes = [IsOwnerOrStaff]


class FidbackDestroyAPIView(generics.DestroyAPIView):
    queryset = Fidback.objects.all()
    permission_classes = [IsOwnerOrStaff]
