# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Books(models.Model):
    book_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    author = models.CharField(max_length=45)
    publish = models.CharField(max_length=45)
    isbn = models.CharField(max_length=15)
    women10 = models.FloatField()
    women60 = models.FloatField()
    women50 = models.FloatField()
    women40 = models.FloatField()
    women30 = models.FloatField()
    women20 = models.FloatField()
    men30 = models.FloatField()
    men40 = models.FloatField()
    men50 = models.FloatField()
    men20 = models.FloatField()
    men60 = models.FloatField()
    men10 = models.FloatField()
    category = models.ForeignKey('Category', models.DO_NOTHING)
    url = models.CharField(max_length=255)
    story = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name

    class Meta:
        managed = False
        db_table = 'books'


class Category(models.Model):
    category_id = models.IntegerField(primary_key=True)
    category_name = models.CharField(max_length=45)

    def __str__(self):
        return self.category_name

    class Meta:
        managed = False
        db_table = 'category'


class Cossim(models.Model):
    book = models.ForeignKey(Books, models.DO_NOTHING, primary_key=True,related_name='%(class)s_a')
    book_id1 = models.ForeignKey(Books, models.DO_NOTHING, db_column='book_id1',related_name='%(class)s_b')
    sim = models.FloatField()

    class Meta:
        managed = False
        db_table = 'cossim'
        unique_together = (('book', 'book_id1'),)
