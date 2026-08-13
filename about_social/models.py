from django.db import models

# Create your models here.

class About(models.Model):
    about_heading = models.CharField(max_length=100)
    about_description = models.TextField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.about_heading
    
    class Meta:
            verbose_name_plural = 'About'
            

class SocialMedia(models.Model):
    social_media = models.CharField(max_length=30)
    link = models.URLField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
        
    def __str__(self):
        return self.social_media