# Generated by Django 2.1.5 on 2019-02-28 14:55

import bridge_lti.utils
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('api', '0001_initial'),
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='BridgeUser',
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
                ('roles', models.CharField(help_text='User <a target="_blank" href="https://www.imsglobal.org/specs/ltiv1p1p1/implementation-guide#toc-22">LTI roles</a> (comma separated).', max_length=255)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'bridge user',
                'verbose_name_plural': 'bridge users',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='LtiConsumer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, unique=True)),
                ('provider_key', models.CharField(max_length=255)),
                ('provider_secret', models.CharField(max_length=255)),
                ('lti_metadata', models.CharField(blank=True, max_length=255, null=True)),
                ('host_url', models.URLField(max_length=255, null=True)),
                ('is_active', models.BooleanField(default=False, help_text='Are its sources available for Instructors?')),
                ('source_type', models.CharField(choices=[('base', 'Base Source'), ('edx', 'edX Source'), ('dart', 'Dart Source')], default='edx', max_length=100)),
                ('available_in_groups', models.ManyToManyField(related_name='group_source', to='auth.Group', verbose_name='source in groups')),
                ('o_auth_client', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='api.OAuthClient')),
            ],
            options={
                'verbose_name': 'Content Source',
                'verbose_name_plural': 'Content Sources',
            },
        ),
        migrations.CreateModel(
            name='LtiProvider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consumer_name', models.CharField(max_length=255, unique=True)),
                ('consumer_key', models.CharField(db_index=True, default=bridge_lti.utils.short_token, max_length=32, unique=True)),
                ('consumer_secret', models.CharField(default=bridge_lti.utils.short_token, max_length=32, unique=True)),
                ('expiration_date', models.DateField(blank=True, null=True, verbose_name='Consumer key expiration date')),
                ('lms_metadata', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'verbose_name': 'LMS Platform',
                'verbose_name_plural': 'LMS Platforms',
            },
        ),
        migrations.CreateModel(
            name='LtiUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(db_index=True, max_length=255)),
                ('course_id', models.CharField(blank=True, max_length=255, null=True)),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('bridge_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('lti_consumer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bridge_lti.LtiProvider')),
            ],
            options={
                'verbose_name': 'LTI User',
                'verbose_name_plural': 'LTI Users',
            },
        ),
        migrations.CreateModel(
            name='OutcomeService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lis_outcome_service_url', models.CharField(max_length=255)),
                ('lms_lti_connection', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='bridge_lti.LtiProvider')),
            ],
            options={
                'verbose_name': 'outcome service',
                'verbose_name_plural': 'outcome services',
            },
        ),
        migrations.AlterUniqueTogether(
            name='ltiuser',
            unique_together={('lti_consumer', 'user_id')},
        ),
    ]
