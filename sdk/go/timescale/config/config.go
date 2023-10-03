// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package config

import (
	"github.com/digizuite/pulumi-timescale/sdk/go/timescale/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi/config"
)

var _ = internal.GetEnvOrDefault

// Access Key
func GetAccessKey(ctx *pulumi.Context) string {
	return config.Get(ctx, "timescale:accessKey")
}

// Access Token
func GetAccessToken(ctx *pulumi.Context) string {
	return config.Get(ctx, "timescale:accessToken")
}

// Project ID
func GetProjectId(ctx *pulumi.Context) string {
	return config.Get(ctx, "timescale:projectId")
}

// Secret Key
func GetSecretKey(ctx *pulumi.Context) string {
	return config.Get(ctx, "timescale:secretKey")
}