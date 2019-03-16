from django.db import models
from django.urls import reverse

# Create your models here.


# we will inherit all the functions of the Model class in Posts class
class Post(models.Model):

    # these are going to be present in every post that we create
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    summary = models.CharField(max_length=300)
    content = models.TextField()
    published = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

        def __unicode__(self):
            return u'%s'% self.title

    def get_absolute_url(self):
        return reverse('blog.views.post', args=[self.slug])
