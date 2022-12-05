from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Snack
# Create your tests here.

class Test(TestCase):
    def test_snack_list_page(self):
        url=reverse('snacks')   
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,'snack_list.html')

    def setUp(self):
        self.user= get_user_model().objects.create_user(
            username='test',
            email='test@test.com',
            password='test',
        )
        self.snack=Snack.objects.create(
            name='Test',
            purchaser=self.user,
            description='test',
            img_url='test.png',
        )

    def test_str_method(self):
        self.assertEqual(str(self.snack), 'Test')

    def test_snack_detail_page(self):
        url=reverse('snack_detail',args=[self.snack.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,'snack_detail.html')
    
    def test_snack_create_page(self):
        data={
            'name': 'Test2',
            'purchaser': self.user.id,
            'description': 'test2',
            "img_url": 'test2.png',
        }
        url=reverse('snack_create')
        response= self.client.post(path=url, data=data,follow=True)
        self.assertEqual(len(Snack.objects.all()), 2)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,'snack_detail.html')
        self.assertRedirects(response, reverse('snack_detail',args=[2]))

    def test_snack_update_page(self):
        data={
            'name': 'Test2',
            'purchaser': self.user.id,
            'description': 'test2',
            "img_url": 'test2.png',
        }
        url=reverse('snack_update',args=[self.snack.id])
        response= self.client.post(path=url, data=data,follow=True)
        self.assertEqual(Snack.objects.get(id=1).name, 'Test2')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,'snack_detail.html')
        self.assertRedirects(response, reverse('snack_detail',args=[1]))


