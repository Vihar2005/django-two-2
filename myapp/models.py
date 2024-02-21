from django.db import models

# Create your models here.
class User(models.Model):
	fname=models.CharField(max_length=100)
	lname=models.CharField(max_length=100)
	email=models.EmailField()
	mobile=models.PositiveIntegerField()
	address=models.TextField()
	gender=models.CharField(max_length=100)
	password=models.CharField(max_length=100)
	profile_pic=models.ImageField(upload_to="profile_pic/",default="")
	usertype=models.CharField(max_length=100,default="buyer")

	def __str__(self):
		return self.fname+" "+self.lname


class Product(models.Model):
	seller=models.ForeignKey(User,on_delete=models.CASCADE)
	product_brand=models.CharField(max_length=100)
	product_price=models.PositiveIntegerField()
	product_size=models.CharField(max_length=100)
	product_pic=models.ImageField(upload_to="product_pic/")


	def __str__(self):
		return self.seller.fname+" - "+self.product_brand
		

class Wishlist(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	product=models.ForeignKey(Product,on_delete=models.CASCADE)

	def __str__(self):
		return self.user.fname+ " - "+self.product.product_brand



class Cart(models.Model):
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	product=models.ForeignKey(Product,on_delete=models.CASCADE)
	product_price=models.PositiveIntegerField()
	product_qty=models.PositiveIntegerField()
	total_price=models.PositiveIntegerField()
	payment_status=models.BooleanField(default=False)

	def __str__(self):
		return self.user.fname+ " - "+self.product.product_brand


class Blog(models.Model):
	comment=models.CharField(max_length=100)
	name=models.CharField(max_length=50)
	email=models.EmailField()
	website=models.CharField(max_length=50)


	def __str__(self):
		return self.name
