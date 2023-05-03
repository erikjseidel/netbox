from django.db import migrations, models
import django.db.models.deletion
import wireless.models


class Migration(migrations.Migration):

    dependencies = [
        ('dcim', '0161_cabling_cleanup'),
        ('dcim', '0135_tenancy_extensions'),
        ('dcim', '0162_unique_constraints'),
    ]

    operations = [
        migrations.AddField(
            model_name='interface',
            name='virtual_link',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='dcim.virtuallink'),
        ),
        migrations.AlterField(
            model_name='virtuallink',
            name='interface_a',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='dcim.interface'),
        ),
        migrations.AlterField(
            model_name='virtuallink',
            name='interface_b',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='+', to='dcim.interface'),
        ),
    ]
