from django.db import models
from ckeditor.fields import RichTextField

class Category(models.Model):
    title=RichTextField(max_length=50)
    
    
    def __str__(self):
        return f"{self.title}"
    
