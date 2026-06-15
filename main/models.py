from django.db import models
from django.utils import timezone
import uuid



class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100, blank=True)
    bio = models.TextField(blank=True)
    # Store the relative path under `main/static/images/`, e.g. "person/john.webp"
    photo = models.CharField(max_length=255, blank=True, help_text="Relative path under main/static/images/ (e.g., 'person/john.webp')")
    # social links: replace twitter/github with instagram/facebook
    instagram_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    facebook_url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Note: no updated_at since we rely on manual path updates
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['created_at']


class ServiceCard(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.CharField(max_length=255, blank=True, help_text="Relative path under main/static/images/ (e.g., 'services/image.jpg')")
    # Optional link: if provided the frontend will render a button
    link_url = models.URLField(blank=True, help_text="Optional external URL for the card button")
    link_text = models.CharField(max_length=50, blank=True, help_text="Optional button text (e.g., 'Learn More')")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']  # Newest first
        verbose_name = 'News Card'
        verbose_name_plural = 'News Cards'


class Club(models.Model):
    """Model to manage clubs and activities."""
    name = models.CharField(max_length=150)
    description = models.TextField()
    icon = models.CharField(max_length=100, help_text="Bootstrap Icon class name (e.g., 'bi-cpu' for CPU icon)")
    link_url = models.URLField(blank=True, help_text="URL for the 'Explore Club' button (e.g., 'aipc.html' or external URL)")
    link_text = models.CharField(max_length=50, default="Explore Club", help_text="Button text")
    order = models.IntegerField(default=0, help_text="Display order on the page (lower numbers appear first)")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['order', 'name']
        verbose_name = 'Club'
        verbose_name_plural = 'Clubs'


class Faculty(models.Model):
    POSITION_CHOICES = [
        ('Head of Department', 'Head of Department'),
        ('Professor', 'Professor'),
        ('Associate Professor', 'Associate Professor'),
        ('Assistant Professor', 'Assistant Professor'),
        ('Lecturer', 'Lecturer'),
    ]
    
    name = models.CharField(max_length=150)
    position = models.CharField(max_length=50, choices=POSITION_CHOICES)
    photo = models.ImageField(upload_to='faculty/', blank=True, null=True)
    research_area = models.TextField(blank=True, help_text="Research areas the faculty member is working on")
    research_area_2 = models.TextField(blank=True, help_text="Additional research area")
    research_area_3 = models.TextField(blank=True, help_text="Additional research area")
    
    # Contact information
    linkedin_url = models.URLField(blank=True, help_text="LinkedIn profile URL")
    website_url = models.URLField(blank=True, help_text="Personal/research website URL")
    email = models.EmailField(blank=True, help_text="Email address")
    
    order = models.IntegerField(default=0, help_text="Display order on the page (lower numbers appear first)")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.name} - {self.position}"
    
    class Meta:
        ordering = ['order', 'name']
        verbose_name = 'Faculty Member'
        verbose_name_plural = 'Faculty Members'
