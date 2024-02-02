from django.db import models


class Model(models.Model):
    name = models.CharField(max_length=100)
    size = models.CharField(max_length=100)
    price_factor = models.DecimalField(max_digits=10, decimal_places=2)
    developer = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Provider(models.Model):
    name = models.CharField(max_length=100)
    url = models.URLField()
    pricing_url = models.URLField()
    pricing_tag_type = models.CharField(max_length=100)
    pricing_tag_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class SignUp(models.Model):
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email


class Price(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    model = models.ForeignKey(Model, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.price
