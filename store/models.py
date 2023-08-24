from django.db import models
from category.models import Category
from django.urls import reverse
# Create your models here.


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100,unique=True)
    images = models.ImageField(upload_to='photos/products')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField()
    description = models.TextField(max_length=1000)
    stock  = models.IntegerField()
    is_available = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now_add=True)



    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])
    



    def __str__(self):
        return self.product_name
    


class VariationManager(models.Manager):
    def colors(self):
        return super(VariationManager, self).filter(category_variation='color', is_active=True)
    
    def sizes(self):
        return super(VariationManager, self).filter(category_variation='size',is_active=True)
    





category_variation_choices = (
    ('color','color'),
    ('size', 'size'),

)
    
class Variation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    category_variation = models.CharField(max_length=100, choices=category_variation_choices)
    variation_value = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)


    objects = VariationManager()


    def __str__(self):
        return self.variation_value
    


    