from django.db import models
from django.urls import reverse

# Create your models here.
WORK = (
    ('S', 'String Replacement'),
    ('C', 'Cleaning'),
    ('P', 'Part Replacement'),
    ('F', 'Fret Level & Polish'),
    ('A', 'Full Setup'),
)

class Guitar(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    description = models.TextField(max_length=250)
    year = models.IntegerField()


    def __str__(self):
        return self.model
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'guitar_id': self.id})

class Maintenance(models.Model):
    date = models.DateField('maintenance date')
    
    work = models.CharField(
        max_length=1,
        choices=WORK,
        default=WORK[0][0])

    guitar = models.ForeignKey(Guitar, on_delete=models.CASCADE)

    def __str__(self):
    # Nice method for obtaining the friendly value of a Field.choice
        return f"{self.get_work_display()} on {self.date}"

    class Meta:
        ordering = ['-date']