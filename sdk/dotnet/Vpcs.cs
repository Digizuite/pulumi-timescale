// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Timescale
{
    /// <summary>
    /// Schema for a VPC. Import can be done using your VPCs name
    /// </summary>
    [TimescaleResourceType("timescale:index/vpcs:Vpcs")]
    public partial class Vpcs : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The IPv4 CIDR block
        /// </summary>
        [Output("cidr")]
        public Output<string> Cidr { get; private set; } = null!;

        [Output("created")]
        public Output<string> Created { get; private set; } = null!;

        [Output("errorMessage")]
        public Output<string> ErrorMessage { get; private set; } = null!;

        /// <summary>
        /// VPC Name is the configurable name assigned to this vpc. If none is provided, a default will be generated by the provider.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        [Output("projectId")]
        public Output<string> ProjectId { get; private set; } = null!;

        [Output("provisionedId")]
        public Output<string> ProvisionedId { get; private set; } = null!;

        /// <summary>
        /// The region for this VPC.
        /// </summary>
        [Output("regionCode")]
        public Output<string> RegionCode { get; private set; } = null!;

        [Output("status")]
        public Output<string> Status { get; private set; } = null!;

        [Output("timeouts")]
        public Output<Outputs.VpcsTimeouts> Timeouts { get; private set; } = null!;

        [Output("updated")]
        public Output<string> Updated { get; private set; } = null!;


        /// <summary>
        /// Create a Vpcs resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Vpcs(string name, VpcsArgs args, CustomResourceOptions? options = null)
            : base("timescale:index/vpcs:Vpcs", name, args ?? new VpcsArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Vpcs(string name, Input<string> id, VpcsState? state = null, CustomResourceOptions? options = null)
            : base("timescale:index/vpcs:Vpcs", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Vpcs resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Vpcs Get(string name, Input<string> id, VpcsState? state = null, CustomResourceOptions? options = null)
        {
            return new Vpcs(name, id, state, options);
        }
    }

    public sealed class VpcsArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The IPv4 CIDR block
        /// </summary>
        [Input("cidr", required: true)]
        public Input<string> Cidr { get; set; } = null!;

        /// <summary>
        /// VPC Name is the configurable name assigned to this vpc. If none is provided, a default will be generated by the provider.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The region for this VPC.
        /// </summary>
        [Input("regionCode", required: true)]
        public Input<string> RegionCode { get; set; } = null!;

        [Input("timeouts")]
        public Input<Inputs.VpcsTimeoutsArgs>? Timeouts { get; set; }

        public VpcsArgs()
        {
        }
        public static new VpcsArgs Empty => new VpcsArgs();
    }

    public sealed class VpcsState : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The IPv4 CIDR block
        /// </summary>
        [Input("cidr")]
        public Input<string>? Cidr { get; set; }

        [Input("created")]
        public Input<string>? Created { get; set; }

        [Input("errorMessage")]
        public Input<string>? ErrorMessage { get; set; }

        /// <summary>
        /// VPC Name is the configurable name assigned to this vpc. If none is provided, a default will be generated by the provider.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("projectId")]
        public Input<string>? ProjectId { get; set; }

        [Input("provisionedId")]
        public Input<string>? ProvisionedId { get; set; }

        /// <summary>
        /// The region for this VPC.
        /// </summary>
        [Input("regionCode")]
        public Input<string>? RegionCode { get; set; }

        [Input("status")]
        public Input<string>? Status { get; set; }

        [Input("timeouts")]
        public Input<Inputs.VpcsTimeoutsGetArgs>? Timeouts { get; set; }

        [Input("updated")]
        public Input<string>? Updated { get; set; }

        public VpcsState()
        {
        }
        public static new VpcsState Empty => new VpcsState();
    }
}
