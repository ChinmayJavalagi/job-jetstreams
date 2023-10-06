{ pkgs }: {
  deps = [
      pkgs.python39Packages.pip
      pkgs.bashInteractive
      pkgs.python39Full
      pkgs.python39Packages.flask
  ];
}