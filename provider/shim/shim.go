package shim

import (
	tfpf "github.com/hashicorp/terraform-plugin-framework/provider"
	"github.com/timescale/terraform-provider-timescale/internal/provider"
)

// Provider fix provider.Provider here to match whats in internal/provider
func Provider() tfpf.Provider {
	return provider.New("0.0.1")()
}
