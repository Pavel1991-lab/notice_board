from rest_framework.permissions import BasePermission

""""
 Пермишн, который проверяет, является ли пользователь владельцем объекта или является персоналом.)

    Для проверки разрешения, этот пермишн использует следующие правила:
    - Если пользователь является персоналом (staff), разрешение будет предоставлено.
    - Если пользователь не является персоналом, разрешение будет предоставлено только в том случае, если
      пользователь является автором объекта, с которым происходит взаимодействие.
"""


class IsOwnerOrStaff(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_staff:
            return True

        return request.user == view.get_object().author
