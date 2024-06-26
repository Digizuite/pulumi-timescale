// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package timescale

import (
	"github.com/digizuite/pulumi-timescale/sdk/go/timescale/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func LookupVpcs(ctx *pulumi.Context, opts ...pulumi.InvokeOption) (*LookupVpcsResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupVpcsResult
	err := ctx.Invoke("timescale:index/getVpcs:getVpcs", nil, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of values returned by getVpcs.
type LookupVpcsResult struct {
	// The ID of this resource.
	Id   string       `pulumi:"id"`
	Vpcs []GetVpcsVpc `pulumi:"vpcs"`
}
