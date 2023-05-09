import graphene

__all__ = (
    'IPAddressesMixin',
    'VLANGroupsMixin',
    'L2VPNTerminationsMixin',
)


class IPAddressesMixin:
    ip_addresses = graphene.List('ipam.graphql.types.IPAddressType')

    def resolve_ip_addresses(self, info):
        return self.ip_addresses.restrict(info.context.user, 'view')


class VLANGroupsMixin:
    vlan_groups = graphene.List('ipam.graphql.types.VLANGroupType')

    def resolve_vlan_groups(self, info):
        return self.vlan_groups.restrict(info.context.user, 'view')


class L2VPNTerminationsMixin:
    l2vpn_terminations = graphene.List('ipam.graphql.types.L2VPNTerminationType')

    def resolve_l2vpn_terminations(self, info):
        return self.l2vpn_terminations.restrict(info.context.user, 'view')
