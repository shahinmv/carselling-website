from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField
# Create your models here.
class Car(models.Model):

    city_choice = (
        ('Bakı','Bakı'),
        ('Gəncə','Gəncə'),
        ('Naxçıvan','Naxçıvan'),
        ('Xankəndi','Xankəndi'),
        ('Lənkəran','Lənkəran'),
        ('Mingəçevir','Mingəçevir'),
        ('Naftalan','Naftalan'),
        ('Sumqayıt','Sumqayıt'),
        ('Şəki','Şəki'),
        ('Şirvan','Şirvan'),
        ('Yevlax','Yevlax'),
    )

    fuel_choices = (
        ('Benzin','Benzin'),
        ('Dizel','Dizel'),
        ('Hybrid','Hybrid'),
        ('Qaz','Qaz'),
    )

    drive_choices = (
        ('Tam','Tam'),
        ('Arxa','Arxa'),
        ('Qabaq','Qabaq'),
    )
    new_choices = (
        ('Bəli','Beli'),
        ('Xeyr','Xeyr'),
    )

    featured_list = (
        ('Kruiz Kontrol','Kruiz Kontrol'),
        ('Arxa görüntü kamerası','Arxa görüntü kamerası'),
        ('Dəri salon', 'Dəri salon'),
        ('Parca salon', 'Parca salon'),
        ('Park radarı', 'Park radarı'),
        ('Lyuk', 'Lyuk'),
        ('Kondisioner', 'Kondisioner'),
        ('Auto Start Stop', 'Auto Start Stop'),
        ('Bluetooth', 'Bluetooth'),
        ('Airbag', 'Airbag'),
        ('Oturacaqların ventilyasiyası', 'Oturacaqların ventilyasiyası'),
        ('Oturacaqların isidilməsi', 'Oturacaqların isidilməsi'),

    )

    city = models.CharField(choices = city_choice, max_length= 100)
    car_title = models.CharField(max_length=255)
    car_model = models.CharField(max_length=255)
    year = models.IntegerField()
    body_style = models.CharField(max_length=255)
    color = models.CharField(max_length=255)
    engine = models.IntegerField()
    engine_hp = models.IntegerField()
    fuel = models.CharField(choices = fuel_choices, max_length= 100)
    mileage = models.IntegerField()
    transmission = models.CharField(max_length=255)
    drive_wheel = models.CharField(choices=drive_choices, max_length=255)
    no_of_owners = models.CharField(choices=new_choices, max_length=255)
    price = models.IntegerField()
    
    description = RichTextField()
    features = MultiSelectField(choices=featured_list)

    created_date = models.DateTimeField(default=datetime.now, blank = True)
    is_featured = models.BooleanField(default = False)

    car_photo1 = models.ImageField(upload_to= 'photos/%Y/%m/%d/',blank = True)
    car_photo2 = models.ImageField(upload_to= 'photos/%Y/%m/%d/',blank = True)
    car_photo3 = models.ImageField(upload_to= 'photos/%Y/%m/%d/',blank = True)
    car_photo4 = models.ImageField(upload_to= 'photos/%Y/%m/%d/',blank = True)
    car_photo5 = models.ImageField(upload_to= 'photos/%Y/%m/%d/',blank = True)

    def __str__(self):
        return self.car_title