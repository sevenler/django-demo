from django.test import TestCase
from api.models import Good, Brand

# Create your tests here.

class ModelTeseCase(TestCase):

	def setUp(self):
		b = Brand.objects.create(title = "new blance")
		b.save()
		Good.objects.create(title = "999", price = 999.5, brand = b.generated_id).save()

	def testAddModelData(self):
		self.assertEqual(1, 1)
