from rest_framework import status
from rest_framework.test import APITestCase
from users.models import User

from notice.models import Notice

"Тесты на проверку функционала CRUD для обьявлений"


class NoticeModelTest(APITestCase):

    def setUp(self) -> None:
        pass

    def test_create_hotice(self):
        'Тестирование создания урока'
        user = User.objects.create(email='sotnikov.pavel.91@mail.ru', last_name='sotn',
                                   first_name='pavel', phone=89109005811, password='123')
        self.client.force_authenticate(user)

        data = {
            "title": "Продам мопед",
            "price": 10000,
            "description": "Хорошое состояние"

        }
        response = self.client.post(
            '/notice/create/',

            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertTrue(
            Notice.objects.exists()
        )

    def test_list_hotice(self):
        user = User.objects.create(email='sotnikov.pavel.91@mail.ru', last_name='sotn',
                                   first_name='pavel', phone=89109005811, password='123')

        self.client.force_authenticate(user)

        Notice.objects.create(
            title="Продам мопед",
            price=10000,
            description="Хорошое состояние",
        )

        response = self.client.get(
            '/notice/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_get_pk_notice(self):
        user = User.objects.create_user(email='sotnikov.pavel.91@mail.ru', last_name='sotn',
                                        first_name='pavel', phone=89109005811, password='123'
                                        )

        self.client.force_authenticate(user)

        notice = Notice.objects.create(
            title="Продам мопед",
            price=10000,
            description="Хорошое состояние",
            author=user
        )

        response = self.client.get(
            f'/notice/{notice.id}/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_update_notice(self):
        user = User.objects.create_user(email='sotnikov.pavel.91@mail.ru', last_name='sotn',
                                        first_name='pavel', phone=89109005811, password='123')
        self.client.force_authenticate(user)

        notice = Notice.objects.create(
            title="Продам мопед",
            price=10000,
            description="Хорошое состояние",
            author=user
        )

        new_title = 'updated'
        new_description = 'updated_description'

        response = self.client.put(
            f'/notice/update/{notice.id}/',
            {
                "title": new_title,
                "price": 1200,
                "description": new_description,
            }
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        updated_hotice = Notice.objects.get(id=notice.id)
        self.assertEqual(updated_hotice.title, new_title)
        self.assertEqual(updated_hotice.description, new_description)

    def test_delete_notice(self):
        user = User.objects.create_user(email='sotnikov.pavel.91@mail.ru', last_name='sotn',
                                        first_name='pavel', phone=89109005811, password='123')
        self.client.force_authenticate(user)

        notice = Notice.objects.create(
            title="Продам мопед",
            price=10000,
            description="Хорошое состояние",
            author=user
        )

        response = self.client.delete(
            f'/notice/delete/{notice.id}/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_204_NO_CONTENT
        )

        # Проверяем, что урок был удален
        with self.assertRaises(Notice.DoesNotExist):
            Notice.objects.get(id=notice.id)
