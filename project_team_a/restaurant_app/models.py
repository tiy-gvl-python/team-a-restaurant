from django.db import models
from django.contrib.auth.models import User

class Order(models.Model):
    items = models.ManyToManyField('Item')
    user = models.ForeignKey(User)
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

    def __str__(self):
        return "{}-{}-{}".format(self.name, self.price, self.timestamp)


class Category(models.Model):
    items = models.ManyToManyField(Item)
    name = models.CharField(max_length=30)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{}-{}-{}".format(self.items, self.name, self.timestamp)


# make Order.user = models.OneToOne(CommonUser) need to change later
class CommonUser(models.Model):
    user = models.OneToOneField(User)

    class Meta:
        abstract = True


class Owner(CommonUser):
    restaurant = models.CharField(max_length=50)
    is_owner = models.BooleanField(default=True)
    status = models.CharField(max_length=6, default='Owner')

    def __str__(self):
        return "Status: {}, Restaurant: {},  Is owner".format(self.status, self.restaurant)


class Staff(CommonUser):
    restaurant = models.CharField(max_length=50)
    job_title = models.CharField(max_length=20)
    is_staff = models.BooleanField(default=False)
    status = models.CharField(max_length=6, default='Staff')

    def __str__(self):
        return '{}'.format(self.restaurant, self.job_title)


class Customer(CommonUser):
    is_customer = models.BooleanField(default=True)
    status = models.CharField(max_length=10,default='Customer')

    def __str__(self):
        return 'Status: {} is customer'.format(self.status)









