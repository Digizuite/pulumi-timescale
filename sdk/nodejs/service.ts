// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

export class Service extends pulumi.CustomResource {
    /**
     * Get an existing Service resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ServiceState, opts?: pulumi.CustomResourceOptions): Service {
        return new Service(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'timescale:index/service:Service';

    /**
     * Returns true if the given object is an instance of Service.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Service {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Service.__pulumiType;
    }

    /**
     * Enable HA Replica
     */
    public readonly enableHaReplica!: pulumi.Output<boolean>;
    /**
     * The hostname for this service
     */
    public /*out*/ readonly hostname!: pulumi.Output<string>;
    /**
     * Memory GB
     */
    public readonly memoryGb!: pulumi.Output<number>;
    /**
     * Milli CPU
     */
    public readonly milliCpu!: pulumi.Output<number>;
    /**
     * Service Name is the configurable name assigned to this resource. If none is provided, a default will be generated by the provider.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * The Postgres password for this service. The password is provided once during service creation
     */
    public /*out*/ readonly password!: pulumi.Output<string>;
    /**
     * The port for this service
     */
    public /*out*/ readonly port!: pulumi.Output<number>;
    /**
     * The region for this service. Currently supported regions are us-east-1, eu-west-1, us-west-2, eu-central-1, ap-southeast-2
     */
    public readonly regionCode!: pulumi.Output<string>;
    /**
     * Deprecated: Storage GB
     *
     * @deprecated This field is ignored. With the new usage-based storage Timescale automatically allocates the disk space needed by your service and you only pay for the disk space you use.
     */
    public readonly storageGb!: pulumi.Output<number | undefined>;
    public readonly timeouts!: pulumi.Output<outputs.ServiceTimeouts | undefined>;
    /**
     * The Postgres user for this service
     */
    public /*out*/ readonly username!: pulumi.Output<string>;
    /**
     * The VpcID this service is tied to.
     */
    public readonly vpcId!: pulumi.Output<number | undefined>;

    /**
     * Create a Service resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: ServiceArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: ServiceArgs | ServiceState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as ServiceState | undefined;
            resourceInputs["enableHaReplica"] = state ? state.enableHaReplica : undefined;
            resourceInputs["hostname"] = state ? state.hostname : undefined;
            resourceInputs["memoryGb"] = state ? state.memoryGb : undefined;
            resourceInputs["milliCpu"] = state ? state.milliCpu : undefined;
            resourceInputs["name"] = state ? state.name : undefined;
            resourceInputs["password"] = state ? state.password : undefined;
            resourceInputs["port"] = state ? state.port : undefined;
            resourceInputs["regionCode"] = state ? state.regionCode : undefined;
            resourceInputs["storageGb"] = state ? state.storageGb : undefined;
            resourceInputs["timeouts"] = state ? state.timeouts : undefined;
            resourceInputs["username"] = state ? state.username : undefined;
            resourceInputs["vpcId"] = state ? state.vpcId : undefined;
        } else {
            const args = argsOrState as ServiceArgs | undefined;
            resourceInputs["enableHaReplica"] = args ? args.enableHaReplica : undefined;
            resourceInputs["memoryGb"] = args ? args.memoryGb : undefined;
            resourceInputs["milliCpu"] = args ? args.milliCpu : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["regionCode"] = args ? args.regionCode : undefined;
            resourceInputs["storageGb"] = args ? args.storageGb : undefined;
            resourceInputs["timeouts"] = args ? args.timeouts : undefined;
            resourceInputs["vpcId"] = args ? args.vpcId : undefined;
            resourceInputs["hostname"] = undefined /*out*/;
            resourceInputs["password"] = undefined /*out*/;
            resourceInputs["port"] = undefined /*out*/;
            resourceInputs["username"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const secretOpts = { additionalSecretOutputs: ["password"] };
        opts = pulumi.mergeOptions(opts, secretOpts);
        super(Service.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Service resources.
 */
export interface ServiceState {
    /**
     * Enable HA Replica
     */
    enableHaReplica?: pulumi.Input<boolean>;
    /**
     * The hostname for this service
     */
    hostname?: pulumi.Input<string>;
    /**
     * Memory GB
     */
    memoryGb?: pulumi.Input<number>;
    /**
     * Milli CPU
     */
    milliCpu?: pulumi.Input<number>;
    /**
     * Service Name is the configurable name assigned to this resource. If none is provided, a default will be generated by the provider.
     */
    name?: pulumi.Input<string>;
    /**
     * The Postgres password for this service. The password is provided once during service creation
     */
    password?: pulumi.Input<string>;
    /**
     * The port for this service
     */
    port?: pulumi.Input<number>;
    /**
     * The region for this service. Currently supported regions are us-east-1, eu-west-1, us-west-2, eu-central-1, ap-southeast-2
     */
    regionCode?: pulumi.Input<string>;
    /**
     * Deprecated: Storage GB
     *
     * @deprecated This field is ignored. With the new usage-based storage Timescale automatically allocates the disk space needed by your service and you only pay for the disk space you use.
     */
    storageGb?: pulumi.Input<number>;
    timeouts?: pulumi.Input<inputs.ServiceTimeouts>;
    /**
     * The Postgres user for this service
     */
    username?: pulumi.Input<string>;
    /**
     * The VpcID this service is tied to.
     */
    vpcId?: pulumi.Input<number>;
}

/**
 * The set of arguments for constructing a Service resource.
 */
export interface ServiceArgs {
    /**
     * Enable HA Replica
     */
    enableHaReplica?: pulumi.Input<boolean>;
    /**
     * Memory GB
     */
    memoryGb?: pulumi.Input<number>;
    /**
     * Milli CPU
     */
    milliCpu?: pulumi.Input<number>;
    /**
     * Service Name is the configurable name assigned to this resource. If none is provided, a default will be generated by the provider.
     */
    name?: pulumi.Input<string>;
    /**
     * The region for this service. Currently supported regions are us-east-1, eu-west-1, us-west-2, eu-central-1, ap-southeast-2
     */
    regionCode?: pulumi.Input<string>;
    /**
     * Deprecated: Storage GB
     *
     * @deprecated This field is ignored. With the new usage-based storage Timescale automatically allocates the disk space needed by your service and you only pay for the disk space you use.
     */
    storageGb?: pulumi.Input<number>;
    timeouts?: pulumi.Input<inputs.ServiceTimeouts>;
    /**
     * The VpcID this service is tied to.
     */
    vpcId?: pulumi.Input<number>;
}
