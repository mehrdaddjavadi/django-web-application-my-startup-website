from django.contrib.gis.db import models
from django.utils import timezone
from account.models import Account
from django.urls import reverse






class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,self).get_queryset().filter(status='published')

class Post(models.Model):

    # def get_absolute_url(self):
    #     return reverse('articles:post_detail',
    #                     args=[self.publish.year,
    #                     self.publish.month,
    #                     self.publish.day, self.slug])

    def get_absolute_url(self):
        return reverse('articles:post_detail',
                        args=[ self.slug])


    # def get_absolute_url(self):
    #     return reverse("articles:post_detail",
    #                      kwargs={"year":self.publish.year,
    #                      "month":self.publish.month,
    #                      "day":self.publish.day,
    #                      "post": self.slug})
    


    STATUS_CHOICES = (
        ('draft', 'پیش نویس'),
        ('published', 'منتشر شده'),
        )
    title = models.CharField(max_length=250, 
                            verbose_name='عنوان',)
    slug = models.SlugField(max_length=250,
                            unique_for_date='publish', 
                            allow_unicode=True, 
                            verbose_name='آدرس لینک',)

    author = models.ForeignKey(Account,
                                on_delete=models.CASCADE,
                                related_name='blog_posts',
                                verbose_name='نویسنده',)
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                            choices=STATUS_CHOICES,
                            default='draft')
    cover_image=models.CharField(max_length=250,blank=True, null=True)
   


    objects = models.Manager() # The default manager.
    published = PublishedManager() # Our custom manager.

    class Meta:
        # ordering = ('-publish',)
         ordering = ('publish',)


    def __str__(self):
        return self.title


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)


