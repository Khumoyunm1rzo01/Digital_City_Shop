from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    email = models.EmailField()
    company_name = models.CharField(max_length=255)
    card = models.IntegerField(null=True, blank=True)
    type = models.IntegerField(
        choices=(
            (1, 'Director'),
            (2, 'User'),
        ), default=1
    )
    news = models.BooleanField(default=False)
    contact_number = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    def __str__(self):
        return self.username


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Color(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    rating = models.IntegerField(default=0)
    text = models.TextField()
    img_1 = models.ImageField(upload_to='images/product/')
    img_2 = models.ImageField(upload_to='images/product/', null=True, blank=True)
    img_3 = models.ImageField(upload_to='images/product/', null=True, blank=True)
    img_4 = models.ImageField(upload_to='images/product/', null=True, blank=True)
    sku = models.IntegerField()
    category = models.ManyToManyField(Category)
    on_sale = models.BooleanField(default=False)
    sale_percent = models.IntegerField(default=0)
    gmail = models.EmailField()
    fb = models.URLField()
    insta = models.URLField()
    tw = models.URLField()
    weight = models.FloatField()
    dimensions = models.CharField(max_length=255)
    colors = models.ManyToManyField(Color)
    material = models.CharField(max_length=255)


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    rating = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.PROTECT, related_name='product1')

class Review(models.Model):
    review = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    rating = models.IntegerField()
    star = models.IntegerField(choices=(
        (1, '1'), 
        (2, '2'), 
        (3, '3'), 
        (4, '4'), 
        (5, '5'),
    ), default=0)
    date = models.DateField(auto_now=True)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)


class Info(models.Model):
    ln = models.URLField()
    fb = models.URLField()
    insta = models.URLField()
    tw = models.URLField()


class Subject(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    message = models.TextField()


class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    date = models.DateField()
    img = models.ImageField(upload_to='images/blog')
    text = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.PROTECT)

    def __str__(self):
        return self.text


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    website = models.URLField(blank=True, null=True)
    comment = models.CharField(max_length=255)


class Reply(models.Model):
    reply_to = models.ForeignKey(Comment, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    website = models.URLField(blank=True, null=True)
    comment = models.CharField(max_length=255)


class Cookies(models.Model):
    text = models.CharField(max_length=255)


class Privacy_Policy(models.Model):
    text = models.TextField()
    Security_text = models.CharField(max_length=255)
    Cookies = models.ManyToManyField(Cookies)


class About(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()


class Requirements(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Top_Trends(models.Model):
    img = models.ImageField(upload_to='images/top_trends/')
    text = models.CharField(max_length=255)
    requirements = models.ManyToManyField(Requirements, blank=True)


class Delivery_Options(models.Model):
    name = models.CharField(max_length=255)


class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    total_price = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    date = models.DateField(auto_now=True)
    status = models.BooleanField(default=False)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.IntegerField()
    delivery_options = models.ForeignKey(Delivery_Options, on_delete=models.PROTECT)
    deliver_address = models.CharField(max_length=255)
    shipping = models.BooleanField(default=False)


class Shipping_Detail(models.Model):
    types = models.CharField(max_length=2555)
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    post_code = models.IntegerField()

    def __str__(self):
        return self.types

class Cart(models.Model):
    product = models.ManyToManyField(Product)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    total = models.IntegerField()
    

class CartDetail(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.PROTECT)
    subtotal = models.IntegerField()
    shipping = models.ForeignKey(Shipping_Detail, on_delete=models.PROTECT)


class BillingDetails(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    postcode = models.CharField(max_length=255)
    city = models.CharField(max_length=255)


class Wishlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
