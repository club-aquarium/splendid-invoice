{
  pkgs ? import <nixpkgs> { },
}:
pkgs.python3.pkgs.callPackage ./. {
  # override buildPythonApplication with a call to mkShell
  buildPythonApplication =
    {
      dependencies,
      checkInputs,
      nativeCheckInputs,
      ...
    }:
    pkgs.mkShell {
      nativeBuildInputs = dependencies ++ checkInputs ++ nativeCheckInputs;
    };
}
