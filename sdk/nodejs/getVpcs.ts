// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

export function getVpcs(opts?: pulumi.InvokeOptions): Promise<GetVpcsResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("timescale:index/getVpcs:getVpcs", {
    }, opts);
}

/**
 * A collection of values returned by getVpcs.
 */
export interface GetVpcsResult {
    /**
     * The ID of this resource.
     */
    readonly id: string;
    readonly vpcs: outputs.GetVpcsVpc[];
}
export function getVpcsOutput(opts?: pulumi.InvokeOptions): pulumi.Output<GetVpcsResult> {
    return pulumi.output(getVpcs(opts))
}
