# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


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

    class Meta:
        managed = False
        db_table = 'books'


class Category(models.Model):
    category_id = models.IntegerField(primary_key=True)
    category_name = models.CharField(max_length=45)

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


class Cossim2(models.Model):
    book = models.ForeignKey(Books, models.DO_NOTHING, primary_key=True,related_name='%(class)s_a')
    book_id1 = models.ForeignKey(Books, models.DO_NOTHING, db_column='book_id1',related_name='%(class)s_b')
    sim = models.FloatField()

    class Meta:
        managed = True
        db_table = 'cossim2'
        unique_together = (('book', 'book_id1'),)

class Cossim3(models.Model):
    book = models.ForeignKey(Books, models.DO_NOTHING, primary_key=True,related_name='%(class)s_a')
    book_id1 = models.ForeignKey(Books, models.DO_NOTHING, db_column='book_id1',related_name='%(class)s_b')
    sim = models.FloatField()

    class Meta:
        managed = True
        db_table = 'cossim3'
        unique_together = (('book', 'book_id1'),)

class Cossim4(models.Model):
    book = models.ForeignKey(Books, models.DO_NOTHING, primary_key=True,related_name='%(class)s_a')
    book_id1 = models.ForeignKey(Books, models.DO_NOTHING, db_column='book_id1',related_name='%(class)s_b')
    sim = models.FloatField()

    class Meta:
        managed = True
        db_table = 'cossim4'
        unique_together = (('book', 'book_id1'),)

class Cossim5(models.Model):
    book = models.ForeignKey(Books, models.DO_NOTHING, primary_key=True,related_name='%(class)s_a')
    book_id1 = models.ForeignKey(Books, models.DO_NOTHING, db_column='book_id1',related_name='%(class)s_b')
    sim = models.FloatField()

    class Meta:
        managed = True
        db_table = 'cossim5'
        unique_together = (('book', 'book_id1'),)
class Cossim6(models.Model):
    book = models.ForeignKey(Books, models.DO_NOTHING, primary_key=True,related_name='%(class)s_a')
    book_id1 = models.ForeignKey(Books, models.DO_NOTHING, db_column='book_id1',related_name='%(class)s_b')
    sim = models.FloatField()

    class Meta:
        managed = True
        db_table = 'cossim6'
        unique_together = (('book', 'book_id1'),)

class Cossim7(models.Model):
    book = models.ForeignKey(Books, models.DO_NOTHING, primary_key=True,related_name='%(class)s_a')
    book_id1 = models.ForeignKey(Books, models.DO_NOTHING, db_column='book_id1',related_name='%(class)s_b')
    sim = models.FloatField()

    class Meta:
        managed = True
        db_table = 'cossim7'
        unique_together = (('book', 'book_id1'),)

class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class UserAction(models.Model):
    session_id = models.CharField(primary_key=True, max_length=40)
    time = models.DateTimeField()
    user_action = models.CharField(max_length=15)
    category = models.IntegerField()
    book_no = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'user_action'


class UserTime(models.Model):
    session_id = models.CharField(primary_key=True, max_length=40)
    in_field = models.DateTimeField(db_column='in')  # Field renamed because it was a Python reserved word.
    last_action = models.DateTimeField()

    class Meta:
        managed = True
        db_table = 'user_time'
