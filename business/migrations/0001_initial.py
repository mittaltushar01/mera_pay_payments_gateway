# Generated by Django 3.0.6 on 2020-05-16 17:59

from decimal import Decimal
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('phone', models.IntegerField(null=True, unique=True)),
                ('wallet', models.DecimalField(decimal_places=2, default=Decimal('1000'), max_digits=64, null=True)),
                ('profile_type', models.CharField(max_length=50, null=True)),
                ('credit_number', models.IntegerField(default=1000, null=True)),
                ('debit_number', models.IntegerField(default=10000, null=True)),
                ('debit_balance', models.IntegerField(default=50000, null=True)),
                ('credit_balance', models.IntegerField(default=50000, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='BusinessProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('business_name', models.CharField(max_length=100, unique=True)),
                ('register_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('pan_number', models.IntegerField(unique=True)),
                ('pan_name', models.CharField(max_length=100)),
                ('address', models.TextField(max_length=200)),
                ('pincode', models.IntegerField()),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('business_url_endpoint', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField(default=0, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(blank=True, upload_to='image')),
                ('description', models.CharField(default='No Description Added', max_length=100)),
                ('business_profile', models.ManyToManyField(blank=True, related_name='business_of_services', to='business.BusinessProfile')),
                ('price', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='business.Price')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=0)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('time', models.TimeField(default=django.utils.timezone.now)),
                ('by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='by_profile', to=settings.AUTH_USER_MODEL)),
                ('service', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='business.Service')),
                ('to', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='to_profile', to='business.BusinessProfile')),
            ],
        ),
        migrations.AddField(
            model_name='businessprofile',
            name='service',
            field=models.ManyToManyField(blank=True, related_name='services_of_business', to='business.Service'),
        ),
        migrations.AddField(
            model_name='businessprofile',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
