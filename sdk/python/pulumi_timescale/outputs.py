# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities
from . import outputs

__all__ = [
    'ServiceTimeouts',
    'GetProductsProductResult',
    'GetProductsProductPlanResult',
    'GetServiceResourceResult',
    'GetServiceResourceSpecResult',
    'GetServiceSpecResult',
    'GetVpcsVpcResult',
    'GetVpcsVpcPeeringConnectionResult',
    'GetVpcsVpcPeeringConnectionPeerVpcResult',
]

@pulumi.output_type
class ServiceTimeouts(dict):
    def __init__(__self__, *,
                 create: Optional[str] = None):
        """
        :param str create: A string that can be [parsed as a duration](https://pkg.go.dev/time#ParseDuration) consisting of numbers and unit suffixes, such as "30s" or "2h45m". Valid time units are "s" (seconds), "m" (minutes), "h" (hours).
        """
        if create is not None:
            pulumi.set(__self__, "create", create)

    @property
    @pulumi.getter
    def create(self) -> Optional[str]:
        """
        A string that can be [parsed as a duration](https://pkg.go.dev/time#ParseDuration) consisting of numbers and unit suffixes, such as "30s" or "2h45m". Valid time units are "s" (seconds), "m" (minutes), "h" (hours).
        """
        return pulumi.get(self, "create")


@pulumi.output_type
class GetProductsProductResult(dict):
    def __init__(__self__, *,
                 description: str,
                 id: str,
                 name: str,
                 plans: Sequence['outputs.GetProductsProductPlanResult']):
        """
        :param str id: The ID of this resource.
        """
        pulumi.set(__self__, "description", description)
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "plans", plans)

    @property
    @pulumi.getter
    def description(self) -> str:
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The ID of this resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def plans(self) -> Sequence['outputs.GetProductsProductPlanResult']:
        return pulumi.get(self, "plans")


@pulumi.output_type
class GetProductsProductPlanResult(dict):
    def __init__(__self__, *,
                 id: str,
                 memory_gb: int,
                 milli_cpu: int,
                 price: float,
                 product_id: str,
                 region_code: str):
        """
        :param str id: The ID of this resource.
        """
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "memory_gb", memory_gb)
        pulumi.set(__self__, "milli_cpu", milli_cpu)
        pulumi.set(__self__, "price", price)
        pulumi.set(__self__, "product_id", product_id)
        pulumi.set(__self__, "region_code", region_code)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The ID of this resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="memoryGb")
    def memory_gb(self) -> int:
        return pulumi.get(self, "memory_gb")

    @property
    @pulumi.getter(name="milliCpu")
    def milli_cpu(self) -> int:
        return pulumi.get(self, "milli_cpu")

    @property
    @pulumi.getter
    def price(self) -> float:
        return pulumi.get(self, "price")

    @property
    @pulumi.getter(name="productId")
    def product_id(self) -> str:
        return pulumi.get(self, "product_id")

    @property
    @pulumi.getter(name="regionCode")
    def region_code(self) -> str:
        return pulumi.get(self, "region_code")


@pulumi.output_type
class GetServiceResourceResult(dict):
    def __init__(__self__, *,
                 id: str,
                 spec: 'outputs.GetServiceResourceSpecResult'):
        """
        :param str id: Service ID is the unique identifier for this service
        """
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "spec", spec)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Service ID is the unique identifier for this service
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def spec(self) -> 'outputs.GetServiceResourceSpecResult':
        return pulumi.get(self, "spec")


@pulumi.output_type
class GetServiceResourceSpecResult(dict):
    def __init__(__self__, *,
                 enable_ha_replica: bool,
                 memory_gb: int,
                 milli_cpu: int):
        pulumi.set(__self__, "enable_ha_replica", enable_ha_replica)
        pulumi.set(__self__, "memory_gb", memory_gb)
        pulumi.set(__self__, "milli_cpu", milli_cpu)

    @property
    @pulumi.getter(name="enableHaReplica")
    def enable_ha_replica(self) -> bool:
        return pulumi.get(self, "enable_ha_replica")

    @property
    @pulumi.getter(name="memoryGb")
    def memory_gb(self) -> int:
        return pulumi.get(self, "memory_gb")

    @property
    @pulumi.getter(name="milliCpu")
    def milli_cpu(self) -> int:
        return pulumi.get(self, "milli_cpu")


@pulumi.output_type
class GetServiceSpecResult(dict):
    def __init__(__self__, *,
                 hostname: str,
                 port: int,
                 username: str):
        """
        :param str hostname: Hostname is the hostname of this service.
        :param int port: Port is the port assigned to this service.
        :param str username: Username is the Postgres username.
        """
        pulumi.set(__self__, "hostname", hostname)
        pulumi.set(__self__, "port", port)
        pulumi.set(__self__, "username", username)

    @property
    @pulumi.getter
    def hostname(self) -> str:
        """
        Hostname is the hostname of this service.
        """
        return pulumi.get(self, "hostname")

    @property
    @pulumi.getter
    def port(self) -> int:
        """
        Port is the port assigned to this service.
        """
        return pulumi.get(self, "port")

    @property
    @pulumi.getter
    def username(self) -> str:
        """
        Username is the Postgres username.
        """
        return pulumi.get(self, "username")


@pulumi.output_type
class GetVpcsVpcResult(dict):
    def __init__(__self__, *,
                 cidr: str,
                 created: str,
                 error_message: str,
                 id: int,
                 name: str,
                 peering_connections: Sequence['outputs.GetVpcsVpcPeeringConnectionResult'],
                 project_id: str,
                 provisioned_id: str,
                 region_code: str,
                 status: str,
                 updated: str):
        """
        :param int id: The ID of this resource.
        """
        pulumi.set(__self__, "cidr", cidr)
        pulumi.set(__self__, "created", created)
        pulumi.set(__self__, "error_message", error_message)
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "peering_connections", peering_connections)
        pulumi.set(__self__, "project_id", project_id)
        pulumi.set(__self__, "provisioned_id", provisioned_id)
        pulumi.set(__self__, "region_code", region_code)
        pulumi.set(__self__, "status", status)
        pulumi.set(__self__, "updated", updated)

    @property
    @pulumi.getter
    def cidr(self) -> str:
        return pulumi.get(self, "cidr")

    @property
    @pulumi.getter
    def created(self) -> str:
        return pulumi.get(self, "created")

    @property
    @pulumi.getter(name="errorMessage")
    def error_message(self) -> str:
        return pulumi.get(self, "error_message")

    @property
    @pulumi.getter
    def id(self) -> int:
        """
        The ID of this resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="peeringConnections")
    def peering_connections(self) -> Sequence['outputs.GetVpcsVpcPeeringConnectionResult']:
        return pulumi.get(self, "peering_connections")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> str:
        return pulumi.get(self, "project_id")

    @property
    @pulumi.getter(name="provisionedId")
    def provisioned_id(self) -> str:
        return pulumi.get(self, "provisioned_id")

    @property
    @pulumi.getter(name="regionCode")
    def region_code(self) -> str:
        return pulumi.get(self, "region_code")

    @property
    @pulumi.getter
    def status(self) -> str:
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def updated(self) -> str:
        return pulumi.get(self, "updated")


@pulumi.output_type
class GetVpcsVpcPeeringConnectionResult(dict):
    def __init__(__self__, *,
                 error_message: str,
                 id: int,
                 peer_vpcs: Sequence['outputs.GetVpcsVpcPeeringConnectionPeerVpcResult'],
                 status: str,
                 vpc_id: int):
        """
        :param int id: The ID of this resource.
        """
        pulumi.set(__self__, "error_message", error_message)
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "peer_vpcs", peer_vpcs)
        pulumi.set(__self__, "status", status)
        pulumi.set(__self__, "vpc_id", vpc_id)

    @property
    @pulumi.getter(name="errorMessage")
    def error_message(self) -> str:
        return pulumi.get(self, "error_message")

    @property
    @pulumi.getter
    def id(self) -> int:
        """
        The ID of this resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="peerVpcs")
    def peer_vpcs(self) -> Sequence['outputs.GetVpcsVpcPeeringConnectionPeerVpcResult']:
        return pulumi.get(self, "peer_vpcs")

    @property
    @pulumi.getter
    def status(self) -> str:
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> int:
        return pulumi.get(self, "vpc_id")


@pulumi.output_type
class GetVpcsVpcPeeringConnectionPeerVpcResult(dict):
    def __init__(__self__, *,
                 account_id: str,
                 cidr: str,
                 id: int,
                 region_code: str):
        """
        :param int id: The ID of this resource.
        """
        pulumi.set(__self__, "account_id", account_id)
        pulumi.set(__self__, "cidr", cidr)
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "region_code", region_code)

    @property
    @pulumi.getter(name="accountId")
    def account_id(self) -> str:
        return pulumi.get(self, "account_id")

    @property
    @pulumi.getter
    def cidr(self) -> str:
        return pulumi.get(self, "cidr")

    @property
    @pulumi.getter
    def id(self) -> int:
        """
        The ID of this resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="regionCode")
    def region_code(self) -> str:
        return pulumi.get(self, "region_code")

