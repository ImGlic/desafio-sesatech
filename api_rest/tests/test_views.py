from rest_framework import status
from rest_framework.test import APITestCase
from api_rest.models import Products, Sale, ProductSale

class APITestCaseExample(APITestCase):

    def setUp(self):
        self.product1 = Products.objects.create(name="Celular 1", price=1800.00, description="Lorenzo Ipsulum")
        self.product2 = Products.objects.create(name="Celular 2", price=3200.00, description="Lorem ipsum dolor")

    def test_create_sale(self):
       
        url = '/api/sales/'
        data = {
            "total": 5000.00,
            "Products": [self.product1.id, self.product2.id]
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Sale.objects.count(), 1)
        self.assertEqual(Sale.objects.get().total, 5000.00)

   
    def test_list_sales(self):
        url = '/api/sales/list/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

