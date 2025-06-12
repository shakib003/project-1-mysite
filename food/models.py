from django.db import models

# Create your models here.

# models are the database schema, which defines the structure of your data.

class Item(models.Model):

    def __str__(self):
        # This method defines how the model is represented as a string.
        return self.item_name

    # Now we define the "fields" of the model.
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500, default="https://cdn.vectorstock.com/i/500p/42/11/creative-concept-of-brain-food-symbolized-vector-53434211.jpg")
 
