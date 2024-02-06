from rest_framework import status
from rest_framework.test import APITestCase
from users.models import User
from fidback.models import Fidback
from notice.models import Notice

"Тесты на проверку функционала CRUD для отзывов"


class FidbackModelTest(APITestCase):

    def setUp(self) -> None:
        pass

    def test_create_fidback(self):
        'Тестирование создания урока'
        user = User.objects.create(email='sotnikov.pavel.91@mail.ru', last_name='sotn',
                                   first_name='pavel', phone=89109005811, password='123')
        self.client.force_authenticate(user)

        notice = Notice.objects.create(
            id=1,
            title="Продам мопед",
            price=10000,
            description="Хорошое состояние",
        )

        data = {
            "text": "Хороший мопед",
            "ad": notice.id,
        }

        response = self.client.post(
            '/fidback/create/',

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

        response = self.client.get(
            '/fidback/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_get_pk_fidback(self):
        user = User.objects.create_user(email='sotnikov.pavel.91@mail.ru', last_name='sotn',
                                        first_name='pavel', phone=89109005811, password='123'
                                        )

        self.client.force_authenticate(user)

        notice = Notice.objects.create(
            id=1,
            title="Продам мопед",
            price=10000,
            description="Хорошое состояние",
            author=user
        )

        fidback = Fidback.objects.create(
            text="Хороший мопед",
            ad=notice,
            author=user
        )

        response = self.client.get(
            f'/fidback/{fidback.id}/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

    def test_update_fidback(self):
        user = User.objects.create_user(email='sotnikov.pavel.91@mail.ru', last_name='sotn',
                                        first_name='pavel', phone=89109005811, password='123')
        self.client.force_authenticate(user)

        notice = Notice.objects.create(
            id=1,
            title="Продам мопед",
            price=10000,
            description="Хорошое состояние",
            author=user
        )

        fidback = Fidback.objects.create(
            text="Хороший мопед",
            ad=notice,
            author=user
        )

        text = 'new_text'

        response = self.client.put(
            f'/fidback/update/{fidback.id}/',
            {
                "text": text,
                "ad": notice.id
            }
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK
        )

        updated_fidback = Fidback.objects.get(id=fidback.id)
        self.assertEqual(updated_fidback.text, text)

    def test_delete_notice(self):
        user = User.objects.create_user(email='sotnikov.pavel.91@mail.ru', last_name='sotn',
                                        first_name='pavel', phone=89109005811, password='123')
        self.client.force_authenticate(user)

        notice = Notice.objects.create(
            id=1,
            title="Продам мопед",
            price=10000,
            description="Хорошое состояние",
            author=user
        )

        fidback = Fidback.objects.create(
            text="Хороший мопед",
            ad=notice,
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
