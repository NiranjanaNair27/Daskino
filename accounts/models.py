from django.db import models
from django.contrib.auth.models import User
class Cinema(models.Model):
    cinema=models.AutoField(primary_key=True)
    role=models.CharField(max_length=30,default='cinema_manager')
    cinema_name=models.CharField(max_length=50)
    phoneno=models.CharField(max_length=15)
    city=models.CharField(max_length=100)
    address=models.CharField(max_length=100)
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.cinema_name

class Movie(models.Model):
    movie=models.AutoField(primary_key=True)
    movie_name=models.CharField(max_length=50)
    movie_trailer=models.CharField(max_length=300, default="null")
    movie_rdate=models.CharField(max_length=20, default="null")
    movie_des=models.TextField()
    movie_rating=models.DecimalField(max_digits=3, decimal_places=1)
    movie_poster=models.ImageField(upload_to='movies/poster', default="movies/poster/not.jpg")
    movie_genre=models.CharField(max_length=50,default="Action | Comedy | Romance")
    movie_duration=models.CharField(max_length=10, default="2hr 45min")

    def __str__(self):
        return self.movie_name

class Shows(models.Model):
    shows=models.AutoField(primary_key=True)
    cinema=models.ForeignKey('Cinema',on_delete=models.CASCADE, related_name='cinema_show')
    movie=models.ForeignKey('Movie',on_delete=models.CASCADE, related_name='movie_show')
    time=models.CharField(max_length=100)
    date=models.CharField(max_length=15, default="")
    price=models.IntegerField()

    def __str__(self):
        return self.cinema.cinema_name +" | "+ self.movie.movie_name +" | "+ self.time

class Bookings(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    shows = models.ForeignKey(Shows, on_delete=models.CASCADE)
    useat = models.CharField(max_length=100)

# class theatre(models.Model):
#    theatre_id=models.IntegerField(primary_key=True)
#    theatre_name=models.CharField(max_length=30)
#    location=models.CharField(max_length=50)
#    no_of_halls=models.IntegerField()
#    total_seats=models.IntegerField()

# class refreshments(models.Model):
    # item_id=models.IntegerField(primary_key=True)
    # item_name=models.CharField(max_length=20)
    # stock=models.IntegerField()
    # size=models.CharField(max_length=10)
    
# class discount(models.Model):
#       movie_id1=models.IntegerField()
#       theatre_id5=models.IntegerField()
#       original_price=models.IntegerField()
#       discount_offered=models.IntegerField()
#       ticket_id3=models.ForeignKey(tickets,on_delete=models.CASCADE)
#       class Meta:
#         constraints=[models.UniqueConstraint(fields=['movie_id1','theatre_id5'],name='combination_unique2')]

    @property
    def useat_as_list(self):
        return self.useat.split(',')
    def __str__(self):
        return self.user.username +" | "+ self.shows.movie.movie_name +" | "+ self.useat

