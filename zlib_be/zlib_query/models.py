# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Books(models.Model):
    zlibrary_id = models.IntegerField(primary_key=True)
    date_added = models.TextField()
    date_modified = models.TextField()
    extension = models.TextField()
    filesize = models.BigIntegerField(blank=True, null=True)
    filesize_reported = models.BigIntegerField()
    md5 = models.CharField(max_length=32, blank=True, null=True)
    md5_reported = models.CharField(max_length=32)
    title = models.TextField()
    author = models.TextField()
    publisher = models.TextField()
    language = models.TextField()
    series = models.TextField()
    volume = models.TextField()
    edition = models.TextField()
    year = models.TextField()
    pages = models.TextField()
    description = models.TextField()
    cover_url = models.TextField()
    in_libgen = models.IntegerField()
    pilimi_torrent = models.CharField(max_length=50, blank=True, null=True)
    unavailable = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'books'


class Isbn(models.Model):
    zlibrary_id = models.IntegerField(primary_key=True)
    isbn = models.CharField(max_length=13)

    class Meta:
        managed = True
        db_table = 'isbn'
        unique_together = (('isbn', 'zlibrary_id'), ('zlibrary_id', 'isbn'),)
