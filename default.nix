{
  lib,
  buildPythonApplication,
  pythonOlder,
  setuptools,
  poppler-qt5,
  xsdata,
  black,
  flake8,
  git,
  isort,
  mypy,
}:

let

  src = ./.;

  pyproject = builtins.fromTOML (builtins.readFile "${src}/pyproject.toml");

in

buildPythonApplication {
  pname = "splendid-invoice";
  inherit (pyproject.project) version;
  pyproject = true;

  disabled = pythonOlder "3.9";

  inherit src;

  build-system = [
    setuptools
  ];

  dependencies = [
    poppler-qt5
    xsdata
  ];

  checkInputs = [
    black
    flake8
    isort
    mypy
    # xsdata[cli]
    (xsdata.overridePythonAttrs (prevAttrs: {
      dependencies = (prevAttrs.dependencies or [ ]) ++ prevAttrs.optional-dependencies.cli;
    }))
  ];

  nativeCheckInputs = [
    git
  ];

  pythonImportsCheck = [ "splendid_invoice" ];

  meta = with lib; {
    inherit (pyproject.project) description;
    license = licenses.gpl2Plus;
    maintainers = with maintainers; [ schnusch ];
  };
}
