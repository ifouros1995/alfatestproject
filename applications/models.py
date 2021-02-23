from django.db import models
from jsonfield import JSONField
from multiselectfield import MultiSelectField
from django.contrib.admin.widgets import AdminDateWidget

class Trial(models.Model):
	STATUS = (
				('Pending', 'Pending'),
				('Out for delivery', 'Out for delivery'),
				('Delivered', 'Delivered'),
				)

	name = models.CharField(max_length=200, null=True)
	status = models.CharField(max_length=200, null=True, choices=STATUS)



	def __str__(self):
		return self.name



class Customer(models.Model):
	name = models.CharField(max_length=200, null=True)
	phone = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200, null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)

	def __str__(self):
		return self.name


class Tag(models.Model):
	name = models.CharField(max_length=200, null=True)

	def __str__(self):
		return self.name

class Product(models.Model):
	CATEGORY = (
			('Indoor', 'Indoor'),
			('Out Door', 'Out Door'),
			)

	name = models.CharField(max_length=200, null=True)
	price = models.FloatField(null=True)
	category = models.CharField(max_length=200, null=True, choices=CATEGORY)
	description = models.CharField(max_length=200, null=True, blank=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	tags = models.ManyToManyField(Tag)

	def __str__(self):
		return self.name

class Order(models.Model):
	STATUS = (
			('Pending', 'Pending'),
			('Out for delivery', 'Out for delivery'),
			('Delivered', 'Delivered'),
			)

	customer = models.ForeignKey(Customer, null=True, on_delete= models.SET_NULL)
	product = models.ForeignKey(Product, null=True, on_delete= models.SET_NULL)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	status = models.CharField(max_length=200, null=True, choices=STATUS)
	note = models.CharField(max_length=1000, null=True)

	def __str__(self):
		return self.product.name



class Application(models.Model):

	MY_CHOICES = (('item_key1', 'Item title 1.1'),
              ('item_key2', 'Item title 1.2'),
              ('item_key3', 'Item title 1.3'),
              ('item_key4', 'Item title 1.4'),
              ('item_key5', 'Item title 1.5'))

	TESTS=(
	    ('ΥΓΕΙΑ', 'ΥΓΕΙΑ'),
	    ('ΠΛΑΣΤΙΚΟΤΗΤΑ', 'ΠΛΑΣΤΙΚΟΤΗΤΑ'),
	    ('ΕΙΣΚΟΜΙΣΗ ΜΗΤΡΩΝ', 'ΕΙΣΚΟΜΙΣΗ ΜΗΤΡΩΝ'),
		('ΘΡΑΥΣΗ ΔΟΚΙΜΙΩΝ', 'ΘΡΑΥΣΗ ΔΟΚΙΜΙΩΝ')
		)

	STATUS=(
		('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered')
		)


    #customer = models.ForeignKey(Customer, null=True, on_delete= models.SET_NULL)
	protocol_number = models.IntegerField()
	name = models.CharField(max_length=264,unique=True)
	address = models.CharField(max_length=264,unique=True)
	date = models.DateField(auto_now=True)
	tests = models.CharField(max_length=200, null=True, choices=TESTS)
	status = models.CharField(max_length=200, null=True, choices=STATUS)
	status_list = MultiSelectField(choices=MY_CHOICES,null=True)


	def __str__(self):
		return self.name
