// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Timescale.Outputs
{

    [OutputType]
    public sealed class GetVpcsVpcPeeringConnectionResult
    {
        public readonly string ErrorMessage;
        /// <summary>
        /// The ID of this resource.
        /// </summary>
        public readonly int Id;
        public readonly ImmutableArray<Outputs.GetVpcsVpcPeeringConnectionPeerVpcResult> PeerVpcs;
        public readonly string Status;
        public readonly int VpcId;

        [OutputConstructor]
        private GetVpcsVpcPeeringConnectionResult(
            string errorMessage,

            int id,

            ImmutableArray<Outputs.GetVpcsVpcPeeringConnectionPeerVpcResult> peerVpcs,

            string status,

            int vpcId)
        {
            ErrorMessage = errorMessage;
            Id = id;
            PeerVpcs = peerVpcs;
            Status = status;
            VpcId = vpcId;
        }
    }
}
