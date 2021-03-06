from django.core.validators import MinValueValidator
from django.db import models
from django.contrib.auth.models import User
# from django.core.validators import RegexValidator

class Order(models.Model):
    items = models.ManyToManyField('Item', through="Count")
    user = models.ForeignKey('Profile')
    timestamp = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField()
    submit = models.BooleanField()

    def cost_of_order(self):
        pass

    def __str_(self):
        return "Order for {}".format(self.user)

class Count(models.Model):
    item = models.ForeignKey("Item")
    order = models.ForeignKey(Order)
    count = models.IntegerField()

    def __str__(self):
        return "Item {} - Amount {}".format(self.item, self.count)


class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=12, validators=[MinValueValidator(0.00)])
    timestamp = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return "{} - Price: {} ".format(self.name, self.price)


class Category(models.Model):
    items = models.ManyToManyField(Item)
    name = models.CharField(max_length=30)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}".format(self.name)

class Menu(models.Model):
    categories = models.ManyToManyField(Category)
    display = models.BooleanField()
    timestamp = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=30)

    def __str__(self):
        return "{} - {} - {}".format(self.categories, self.display, self.name)

class Click(models.Model):
    item = models.ForeignKey(Item, null=True)
    category = models.ForeignKey(Category, null=True)
    menu = models.ForeignKey(Menu, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

# make Order.user = models.OneToOne(CommonUser) need to change later
class Profile(models.Model):
    user = models.OneToOneField(User, null=True)
    phone = models.CharField(blank=False, max_length=17)
    staff = models.BooleanField(default=False)
    customer = models.BooleanField(default=True)
    owner = models.BooleanField(default=False)

    def __str__(self):
        return 'user.id: {}, username: {}, phone number: {}'.format(self.user.id,
                                                             self.user,
                                                             self.phone)

    class Meta:
        ordering = ['id']
        verbose_name = 'id'
        verbose_name_plural = 'id'

    def __str__(self):
        return "{}".format(self.user)
# default user.customer is set to True for MVP and authentiction

class Comment(models.Model):
    user = models.ForeignKey(Profile)
    timestamp = models.DateTimeField(auto_now_add=True)
    comment = models.CharField(max_length=300)
    recommend = models.BooleanField(default=True)

    def __str__(self):
        return "{}".format(self.user)

    class Meta: #thank you Paul and Joel (displays comments newest first
        ordering = ["-timestamp"]