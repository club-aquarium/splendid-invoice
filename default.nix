{
  lib,
  buildPythonApplication,
  pythonOlder,
  poppler-qt5,
  xsdata,
  black,
  flake8,
  git,
  isort,
  mypy,
}:

buildPythonApplication {
  pname = "splendid-invoice";
  version = "0.0.0";

  disabled = pythonOlder "3.9";

  src = ./.;

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
    description = "Parse PDF invoices from Splendid Drinks";
    license = licenses.gpl2Plus;
    maintainers = with maintainers; [ schnusch ];
  };
}
