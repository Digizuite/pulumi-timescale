{ pkgs ? import <nixpkgs> {} }:
  pkgs.mkShell {
    # nativeBuildInputs is usually what you want -- tools you need to run
    nativeBuildInputs = [ pkgs.pulumi-bin pkgs.pulumictl pkgs.yarn-berry pkgs.buildPackages.python3 pkgs.python311Packages.setuptools ];
}
