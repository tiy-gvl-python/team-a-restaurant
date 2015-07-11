from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
# from django.core.validators import RegexValidator

class Order(models.Model):
    items = models.ManyToManyField('Item')
    user = models.ForeignKey('Profile')
    timestamp = models.DateTimeField(auto_now_add=True)
    completed = models.BooleanField()
    submit = models.BooleanField()

    def cost_of_order(self):
        pass

    def __str_(self):
        return"{}-{}-{}-{}-{}".format(self.items,
                                      self.user,
                                      self.timestamp,
                                      self.completed,
                                      self.submit)

class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return "{}-{}-{}".format(self.name, self.price, self.timestamp)


class Category(models.Model):
    items = models.ManyToManyField(Item)
    name = models.CharField(max_length=30)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}-{}-{}".format(self.items, self.name, self.timestamp)

class Menu(models.Model):
    categories = models.ManyToManyField(Category)
    display = models.BooleanField()
    timestamp = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=30)


    def __str__(self):
        return "{} - {} - {}".format(self.categories, self.display, self.name)

class Click(models.Model):
    item = models.ForeignKey(Item, null = True)
    category = models.ForeignKey(Category, null=True)
    menu = models.ForeignKey(Menu, null = True)
    timestamp = models.DateTimeField(auto_now_add=True)

# make Order.user = models.OneToOne(CommonUser) need to change later
class Profile(models.Model):
    user = models.OneToOneField(User, null=True)
    phone = PhoneNumberField(blank=False)
    staff = models.BooleanField(default=False)
    customer = models.BooleanField(default=False)
    owner = models.BooleanField(default=False)

    class Meta:
        ordering = ['user']
        verbose_name = 'user'
        verbose_name_plural = 'users'













