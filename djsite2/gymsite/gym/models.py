from django.db import models
from django.contrib.auth.models import User
GenderChoice=(('M','Male'),('F', 'Female'))

CardDiscountChoice=((1, 10),(2, 20),(3, 30))
CardNameChoice =(('B', 'Bronze'), ('S', 'Silver'),('G', 'Gold'))
DayChoice =(('mon', 'Monday'),('tue', 'Tuesday'),('wed', 'Wednesday'),
            ('thu', 'Thursday'),('fri', 'Friday'),('sat', 'Saturday'),('sun', 'Sunday'))
ClubGymChoice = (('pool', 'SwimmingPool'),('gym', 'Gym'),('ring','BoxingRing'),('tatami','Tatami'))
LessonChoice = (('swim', 'Swimming'), ('bobu', 'BoduBuilding'),('yoga', 'Yoga'),('karate','Karate'),
                 ('sambo','Sambo'), ('judo', 'Judo'), ('box', 'Boxing'))
class Group(models.Model):
    name = models.CharField(max_length=50, verbose_name='GroupName')
    period_price = models.IntegerField()
    clients = models.ManyToManyField('Client')
    schedule = models.OneToOneField('Schedule', on_delete=models.PROTECT)
    def __str__(self):
        return self.name
class ClubCard(models.Model):
    name = models.CharField(max_length=10, choices=CardNameChoice, verbose_name='ClubCard')
    discount =models.IntegerField(choices=CardDiscountChoice)
    def __str__(self):
        return dict(CardNameChoice)[str(self.name)]
    def get_discount(self):
        return dict(CardDiscountChoice)[self.discount]
    class Meta:
        ordering = ['discount']
class Client(models.Model):
    name = models.CharField(max_length=50, verbose_name='ClientName')
    gender = models.CharField(max_length=1, choices=GenderChoice)
    card =models.ForeignKey('ClubCard', on_delete=models.PROTECT, verbose_name='DiscountCard')
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['name']
class Lesson(models.Model):
    subject_name = models.CharField(max_length=50, choices=LessonChoice, verbose_name='SubjectName')
    start_time = models.TimeField()
    end_time = models.TimeField()
    lesson_price = models.IntegerField()
    photo = models.ImageField(upload_to="photos/lessons", verbose_name='Photo', default=None)
    masters = models.ManyToManyField('Master')
    days = models.ManyToManyField('Day')
    lesson_gym = models.ForeignKey('ClubGym', on_delete=models.PROTECT,default=None, verbose_name='PlaceForConductingClasses')
    def __str__(self):
        return self.subject_name
    def get_subject_name(self):
        return dict(LessonChoice)[str(self.subject_name)]
    def get_related_masters(self):
        return self.masters.all()
    class Meta:
        ordering = ['subject_name', 'start_time']
class Master(models.Model):
    username = models.CharField(max_length=50,unique=True,default='NoneMaster', verbose_name='MasterName')
    subject_name = models.CharField(max_length=20, choices=LessonChoice,default='NoneSubject', verbose_name='SubjectName')
    password = models.CharField(max_length=100, default='***')
    email = models.EmailField(blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="photos/masters", verbose_name='Photo', default=None)
    # individual_students = models.ManyToManyField('Client', blank=True)
    def __str__(self):
        return self.username
    def get_subject_name(self):
        return dict(LessonChoice)[str(self.subject_name)]
    class Meta:
        ordering = ['username']
class Day(models.Model):
    name = models.CharField(max_length=10, choices=DayChoice)
    def __str__(self):
        return self.name
# Create your models here.
class Schedule(models.Model):
    weeks_count = models.IntegerField()
    lessons = models.ManyToManyField('Lesson')
    def __str__(self):
        return 'scedule '+str(self.pk)

class ClubGym(models.Model):
    name = models.CharField(max_length=20, choices=ClubGymChoice)
    floor = models.IntegerField()
    def __str__(self):
        return 'GymType '+str(self.name)
