{
  lib,
  buildPythonApplication,
  pythonOlder,
  poppler-qt5,
  black,
  flake8,
  git,
  isort,
  mypy,
}:

buildPythonApplication {
  pname = "splendid-invoice";
  version = "0.0.0";

  disabled = pythonOlder "3.8";

  src = ./.;

  dependencies = [
    poppler-qt5
  ];

  checkInputs = [
    black
    flake8
    isort
    mypy
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
