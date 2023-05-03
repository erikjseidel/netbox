import django_tables2 as tables

from dcim.models import *
from netbox.tables import NetBoxTable, columns
from tenancy.tables import TenancyColumnsMixin

__all__ = (
    'VirtualLinkTable',
)


class VirtualLinkTable(TenancyColumnsMixin, NetBoxTable):
    id = tables.Column(
        linkify=True,
        verbose_name='ID'
    )
    status = columns.ChoiceFieldColumn()
    device_a = tables.Column(
        accessor=tables.A('interface_a__device'),
        linkify=True
    )
    interface_a = tables.Column(
        linkify=True
    )
    device_b = tables.Column(
        accessor=tables.A('interface_b__device'),
        linkify=True
    )
    interface_b = tables.Column(
        linkify=True
    )
    tags = columns.TagColumn(
        url_name='dcim:virtuallink_list'
    )

    class Meta(NetBoxTable.Meta):
        model = VirtualLink
        fields = (
            'pk', 'id', 'status', 'device_a', 'interface_a', 'device_b', 'interface_b', 'tenant',
            'tenant_group', 'description', 'tags', 'created', 'last_updated',
        )
        default_columns = (
            'pk', 'id', 'status', 'device_a', 'interface_a', 'device_b', 'interface_b', 'description',
        )
