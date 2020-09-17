with import <nixpkgs> {};

mkShell {
  DEBUG = true;
  buildInputs = [
    (python3.withPackages (ps: with ps; [
      requests
      pyyaml
      paramiko
    ]))
  ];
}
