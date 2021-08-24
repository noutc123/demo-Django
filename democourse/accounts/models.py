from django.db import models

# Create your models here.


class Custumer(models.Model):
    """
    Description: Model Description
    """
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    price = models.FloatField()
    email = models.CharField(max_length=200)
    data_created = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ('price',)
    pass

    def __str__(self):
        return f"{self.name}"




class Tag(models.Model):
    """
    Description: Model Description
    """
    name = models.CharField(max_length=200)

    class Meta:
        ordering = ('name',)
    pass

    def __str__(self):
        return f"{self.name}"


class Product(models.Model):
    """
    Description: Model Description
    """
    CATEGORY = [
        ('Indoor', 'Indoor'),
        ('Out Door', 'Out Door')
    ]
    name = models.CharField(max_length=200)
    price = models.FloatField()
    category = models.CharField(max_length=200, choices=CATEGORY)
    description = models.CharField(max_length=200)
    data_created = models.DateTimeField(auto_now_add=True, null=True)
    tags = models.ManyToManyField(Tag)

    class Meta:
        ordering = ('price', 'data_created',)

    def __str__(self):
        return f"{self.name}"


class Order(models.Model):
    """
    Description: Model Description
    """

    STATUS = [
        ('Pending', 'Pending'),
        ('Out for delivrery', 'Out for delivrery'),
        ('Delivred', 'Delivred'),
    ]
    customer = models.ForeignKey(
        Custumer, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, null=True, on_delete=models.SET_NULL)
    data_created = models.DateTimeField(auto_now_add=True, null=True)
    status = models.CharField(max_length=200, choices=STATUS)

    class Meta:
        ordering = ('data_created',)

    def __str__(self):
        return f"{self.product}"
