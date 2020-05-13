from django.db import models
from django.urls import reverse
from hitcount.models import HitCountMixin, HitCount########new
from django.contrib.contenttypes.fields import GenericRelation########new
from django.utils.encoding import python_2_unicode_compatible##new

# Create your models here.

class event(models.Model):
    title = models.CharField(max_length=255)
    img=models.ImageField(upload_to='pics/')
    Date= models.DateField()
    description = models.TextField()
    address=models.CharField(max_length=30,null=True)


    class meta:
        ordering =['Date']

    def __str__(self):
        return self.title
@python_2_unicode_compatible#new
class music(models.Model):
    title=models.CharField(max_length=20,null=True)
    singer_name = models.CharField(max_length=30)
    date = models.DateField()
    musicfile = models.FileField(upload_to='music/')
    img= models.ImageField(upload_to='pics/',blank="True")
    hit_count_generic=GenericRelation(HitCount,object_id_field='object.pk',related_query_name='hit_count_generic_relation')#new:to count the number of hits

    def __str__(self):
        return self.singer_name
    def get_absolute_url(self):
        return reverse('mix')

