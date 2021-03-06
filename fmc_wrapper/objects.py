"""
FMC API Rest Objects

"""
from .object_mixins import _FmcApiObject, AcpNameToUuid, NatIdField, RegkeyField, NameField, NameWithSpaceField, ModeField, DefaultActionField, ActionField, UuidField, ValueField, UrlField, DescriptionField, SourceNetworkField, DestNetworkField, HostnameField, InterfaceModeField


class SecurityZone(ModeField, NameField, InterfaceModeField, DescriptionField, _FmcApiObject):
    """
    Need: name, mode
    Optional: desc
    """
    type_ = 'SecurityZone'
    api_url = 'object/securityzones'

    def valid_for_post(self):
        if self.name and self.mode:
            return True

    """
        json_data = {
            "type": "SecurityZone",
            "name": zone['name'],
            "description": zone['desc'],
            "interfaceMode": zone['mode'],
        }
    """


class NetworkObject(ModeField, NameField, UuidField, DescriptionField, ValueField, _FmcApiObject):
    """
    Need: name, value
    Optional: desc
    """
    type_ = 'Network'
    api_url = 'object/networks'
    
    def valid_for_post(self):
        if self.name and self.value:
            return True


class UrlObject(NameWithSpaceField, DescriptionField, ValueField, UuidField, UrlField, _FmcApiObject):
    """
    Need: name, value (AKA URL)
    Optional: desc
    """
    type_ = 'Url'
    api_url = 'object/urls'

    def valid_for_post(self):
        if self.name and self.url:
            return True


class AccessControlPolicy(NameWithSpaceField, UuidField, DescriptionField, DefaultActionField, _FmcApiObject):
    """
    Needs: name, defaultaction
    Optional: desc
    """
    type_ = 'AccessPolicy'
    api_url = 'policy/accesspolicies'

    def valid_for_post(self):
        if self.name and self.defaultaction:
            return True

    """
        json_data = {
            'type': "AccessPolicy",
            'name': policy['name'],
            'description': policy['desc'],
            'defaultaction': { 'action': policy['defaultaction'] }
        }
    """


class AccessControlPolicyRule(NameWithSpaceField, UuidField, SourceNetworkField, DestNetworkField, ActionField, AcpNameToUuid, _FmcApiObject):
    """
    Needs: name, action, acpuuid
    Optional: enabled, sendeventstofmc, logbegin, logend, ipspolicy, sourcezone, destzone, sourcenetwork, destnetwork, and many more!!!
    """

    type_ = 'AccessRule'
    acpuuid = ''
    api_url = 'policy/accesspolicies/' + acpuuid + 'accessrules'

    def valid_for_post(self):
        if self.name and self.action and self.acpuuid:
            return True

    def valid_for_get(self):
        if self.uuid and self.acpuuid:
            return True

    def valid_for_put(self):
        self.valid_for_get()

    def valid_for_delete(self):
        if self.uuid:
            return True


class Device(NameWithSpaceField, UuidField, RegkeyField, HostnameField, AcpNameToUuid, NatIdField, _FmcApiObject):
    """
    Needs: name, regkey, acpuuid
    Optional: license_caps, hostname
    """
    type_ = 'Device'
    api_url = 'devices/devicerecords'

    def valid_for_post(self):
        if self.name and self.regkey and self.acpuuid:
            return True
