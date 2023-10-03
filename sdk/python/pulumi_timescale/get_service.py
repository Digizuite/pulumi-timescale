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
    'GetServiceResult',
    'AwaitableGetServiceResult',
    'get_service',
    'get_service_output',
]

@pulumi.output_type
class GetServiceResult:
    """
    A collection of values returned by getService.
    """
    def __init__(__self__, created=None, id=None, name=None, region_code=None, resources=None, spec=None, vpc_id=None):
        if created and not isinstance(created, str):
            raise TypeError("Expected argument 'created' to be a str")
        pulumi.set(__self__, "created", created)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if region_code and not isinstance(region_code, str):
            raise TypeError("Expected argument 'region_code' to be a str")
        pulumi.set(__self__, "region_code", region_code)
        if resources and not isinstance(resources, list):
            raise TypeError("Expected argument 'resources' to be a list")
        pulumi.set(__self__, "resources", resources)
        if spec and not isinstance(spec, dict):
            raise TypeError("Expected argument 'spec' to be a dict")
        pulumi.set(__self__, "spec", spec)
        if vpc_id and not isinstance(vpc_id, int):
            raise TypeError("Expected argument 'vpc_id' to be a int")
        pulumi.set(__self__, "vpc_id", vpc_id)

    @property
    @pulumi.getter
    def created(self) -> str:
        """
        Created is the time this service was created.
        """
        return pulumi.get(self, "created")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Service ID is the unique identifier for this service
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Service Name is the configurable name assigned to this resource. If none is provided, a default will be generated by the provider.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="regionCode")
    def region_code(self) -> str:
        """
        Region Code is the physical data center where this service is located.
        """
        return pulumi.get(self, "region_code")

    @property
    @pulumi.getter
    def resources(self) -> Sequence['outputs.GetServiceResourceResult']:
        return pulumi.get(self, "resources")

    @property
    @pulumi.getter
    def spec(self) -> 'outputs.GetServiceSpecResult':
        return pulumi.get(self, "spec")

    @property
    @pulumi.getter(name="vpcId")
    def vpc_id(self) -> int:
        """
        VPC ID this service is linked to.
        """
        return pulumi.get(self, "vpc_id")


class AwaitableGetServiceResult(GetServiceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetServiceResult(
            created=self.created,
            id=self.id,
            name=self.name,
            region_code=self.region_code,
            resources=self.resources,
            spec=self.spec,
            vpc_id=self.vpc_id)


def get_service(id: Optional[str] = None,
                vpc_id: Optional[int] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetServiceResult:
    """
    Service data source


    :param str id: Service ID is the unique identifier for this service
    :param int vpc_id: VPC ID this service is linked to.
    """
    __args__ = dict()
    __args__['id'] = id
    __args__['vpcId'] = vpc_id
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('timescale:index/getService:getService', __args__, opts=opts, typ=GetServiceResult).value

    return AwaitableGetServiceResult(
        created=pulumi.get(__ret__, 'created'),
        id=pulumi.get(__ret__, 'id'),
        name=pulumi.get(__ret__, 'name'),
        region_code=pulumi.get(__ret__, 'region_code'),
        resources=pulumi.get(__ret__, 'resources'),
        spec=pulumi.get(__ret__, 'spec'),
        vpc_id=pulumi.get(__ret__, 'vpc_id'))


@_utilities.lift_output_func(get_service)
def get_service_output(id: Optional[pulumi.Input[str]] = None,
                       vpc_id: Optional[pulumi.Input[Optional[int]]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetServiceResult]:
    """
    Service data source


    :param str id: Service ID is the unique identifier for this service
    :param int vpc_id: VPC ID this service is linked to.
    """
    ...
