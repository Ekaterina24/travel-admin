# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Adminuser(models.Model):
    id = models.UUIDField(primary_key=True)
    username = models.CharField(unique=True, max_length=50)
    password = models.CharField(max_length=128)

    class Meta:
        managed = False
        db_table = 'adminUser'

    def __str__(self):
        return f'{self.username}'


class Audio(models.Model):
    generatedid = models.AutoField(db_column='generatedId', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=255)
    desc = models.CharField(unique=True, max_length=255)
    status = models.CharField(max_length=255)
    placeid = models.CharField(db_column='placeId', max_length=255)  # Field name made lowercase.
    placegeneratedid = models.ForeignKey('Place', models.DO_NOTHING, db_column='placeGeneratedId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'audio'
        verbose_name = 'Аудио'
        verbose_name_plural = 'Аудио'

    def __str__(self):
        return f'{self.name}'


class City(models.Model):
    generatedid = models.AutoField(db_column='generatedId', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=255)
    latitude = models.DecimalField(max_digits=8, decimal_places=6)
    longitude = models.DecimalField(max_digits=8, decimal_places=6)

    class Meta:
        managed = False
        db_table = 'city'
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

    def __str__(self):
        return f'{self.name}'


class DayPlaces(models.Model):
    placeid = models.CharField(db_column='placeId', max_length=255)  # Field name made lowercase.
    datevisiting = models.CharField(db_column='dateVisiting', max_length=255)  # Field name made lowercase.
    tripidid = models.ForeignKey('Trip', models.DO_NOTHING, db_column='tripIdId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'day_places'
        verbose_name = 'Место на день'
        verbose_name_plural = 'Места на день'

    def __str__(self):
        return f'{self.placeid} {self.datevisiting}'


class Place(models.Model):
    generatedid = models.AutoField(db_column='generatedId', primary_key=True)  # Field name made lowercase.
    id = models.CharField(unique=True, max_length=255)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    addressid = models.CharField(db_column='addressId', max_length=255)  # Field name made lowercase.
    typeplace = models.CharField(db_column='typePlace', max_length=255)  # Field name made lowercase.
    subtypeplace = models.CharField(db_column='subTypePlace', max_length=255)  # Field name made lowercase.
    latitude = models.CharField(max_length=255)
    longitude = models.CharField(max_length=255)
    is_visited = models.BooleanField()
    is_favourite = models.BooleanField()
    updated_at = models.DateTimeField()
    cityidgeneratedid = models.ForeignKey(City, models.DO_NOTHING, db_column='cityIdGeneratedId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'place'
        verbose_name = 'Место'
        verbose_name_plural = 'Места'

    def __str__(self):
        return f'{self.name}'


class Review(models.Model):
    userid = models.IntegerField(db_column='userId')  # Field name made lowercase.
    placeid = models.CharField(db_column='placeId', max_length=255)  # Field name made lowercase.
    text = models.CharField(max_length=255)
    rating = models.IntegerField()
    date = models.DateTimeField()
    useridid = models.ForeignKey('User', models.DO_NOTHING, db_column='userIdId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'review'
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'

    def __str__(self):
        return f'{self.userid} {self.placeid}'


class SubUser(models.Model):
    typeid = models.IntegerField(db_column='typeId')  # Field name made lowercase.
    city = models.CharField(max_length=255)
    date = models.DateTimeField()
    useridid = models.ForeignKey('User', models.DO_NOTHING, db_column='userIdId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sub_user'
        verbose_name = 'Подписка поьзователя'
        verbose_name_plural = 'Подписки пользователя'

    def __str__(self):
        return f'{self.useridid} {self.date}'


class Trip(models.Model):
    city = models.CharField(max_length=255)
    date_start = models.CharField(max_length=255)
    date_finish = models.CharField(max_length=255)
    useridid = models.ForeignKey('User', models.DO_NOTHING, db_column='userIdId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'trip'
        verbose_name = 'Путешествие'
        verbose_name_plural = 'Путешествия'

    def __str__(self):
        return f'{self.city} {self.date_start}-{self.date_finish}'


class TypeSub(models.Model):
    period = models.IntegerField()
    price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'type_sub'
        verbose_name = 'Тип подписки'
        verbose_name_plural = 'Типы подписок'

    def __str__(self):
        return f'{self.period}'


class User(models.Model):
    username = models.CharField(unique=True, max_length=255)
    email = models.CharField(unique=True, max_length=255)
    password = models.CharField(max_length=255)
    salt = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    scores = models.IntegerField()
    createdat = models.DateTimeField(db_column='createdAt')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user'
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f'{self.username}'
