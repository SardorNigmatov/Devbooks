from django.db import models

class AuthorModel(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    date_of_birth = models.DateField()
    date_of_death = models.DateField(null=True,blank=True)
    country = models.CharField(max_length=200,default='Uzbekistan')
    genre = models.CharField(max_length=200)
    bio = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='imge/',blank=True,null=True)


    def __str__(self):
        full_name = f"{self.first_name} {self.last_name}"
        return full_name


    class Meta:
        db_table = 'author'


class BookModel(models.Model):
    title = models.CharField(max_length=200)
    pages = models.IntegerField()
    year = models.DateField()
    price = models.DecimalField(max_digits=7,decimal_places=2,default=0)
    genre = models.CharField(max_length=200)
    author = models.ForeignKey(AuthorModel,on_delete=models.CASCADE)
    about_book = models.CharField(max_length=5000)
    image = models.ImageField(upload_to='imge/',blank=True,null=True)

    def __str__(self):
        return self.title


    class Meta:
        db_table = 'books'





