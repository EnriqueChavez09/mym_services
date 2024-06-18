# Generated by Django 4.2.13 on 2024-06-18 22:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields
import simple_history.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('is_active', models.BooleanField(default=True, verbose_name='¿Activo?')),
                ('is_delete', models.BooleanField(default=False, verbose_name='¿Eliminado?')),
                ('order', models.PositiveIntegerField(default=1, verbose_name='Orden')),
                ('ruc_number', models.CharField(max_length=11, verbose_name='Número de RUC')),
                ('company_name', models.CharField(max_length=100, verbose_name='Razón Social')),
                ('address', models.CharField(max_length=100, verbose_name='Dirección')),
                ('district', models.CharField(max_length=100, verbose_name='Distrito')),
            ],
            options={
                'verbose_name': 'Empresa',
                'verbose_name_plural': 'Empresas',
                'ordering': ['company_name'],
            },
        ),
        migrations.RemoveField(
            model_name='user',
            name='name',
        ),
        migrations.AddField(
            model_name='user',
            name='created',
            field=model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created'),
        ),
        migrations.AddField(
            model_name='user',
            name='is_delete',
            field=models.BooleanField(default=False, verbose_name='¿Eliminado?'),
        ),
        migrations.AddField(
            model_name='user',
            name='modified',
            field=model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified'),
        ),
        migrations.AddField(
            model_name='user',
            name='order',
            field=models.PositiveIntegerField(default=1, verbose_name='Orden'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='Correo'),
        ),
        migrations.CreateModel(
            name='HistoricalContact',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('is_active', models.BooleanField(default=True, verbose_name='¿Activo?')),
                ('is_delete', models.BooleanField(default=False, verbose_name='¿Eliminado?')),
                ('order', models.PositiveIntegerField(default=1, verbose_name='Orden')),
                ('full_names', models.CharField(max_length=11, verbose_name='Nombres completos')),
                ('phone', models.CharField(max_length=100, verbose_name='Celular')),
                ('address', models.CharField(max_length=100, verbose_name='Dirección')),
                ('email', models.EmailField(max_length=254, verbose_name='Correo')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('company', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='users.company', verbose_name='Empresa')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Contacto',
                'verbose_name_plural': 'historical Contactos',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='HistoricalCompany',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('is_active', models.BooleanField(default=True, verbose_name='¿Activo?')),
                ('is_delete', models.BooleanField(default=False, verbose_name='¿Eliminado?')),
                ('order', models.PositiveIntegerField(default=1, verbose_name='Orden')),
                ('ruc_number', models.CharField(max_length=11, verbose_name='Número de RUC')),
                ('company_name', models.CharField(max_length=100, verbose_name='Razón Social')),
                ('address', models.CharField(max_length=100, verbose_name='Dirección')),
                ('district', models.CharField(max_length=100, verbose_name='Distrito')),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Empresa',
                'verbose_name_plural': 'historical Empresas',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('is_active', models.BooleanField(default=True, verbose_name='¿Activo?')),
                ('is_delete', models.BooleanField(default=False, verbose_name='¿Eliminado?')),
                ('order', models.PositiveIntegerField(default=1, verbose_name='Orden')),
                ('full_names', models.CharField(max_length=11, verbose_name='Nombres completos')),
                ('phone', models.CharField(max_length=100, verbose_name='Celular')),
                ('address', models.CharField(max_length=100, verbose_name='Dirección')),
                ('email', models.EmailField(max_length=254, verbose_name='Correo')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contacts', to='users.company', verbose_name='Empresa')),
            ],
            options={
                'verbose_name': 'Contacto',
                'verbose_name_plural': 'Contactos',
                'ordering': ['-created'],
            },
        ),
    ]