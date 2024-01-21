{ lib
, buildPythonApplication
, pythonOlder
, poppler-qt5
, black
, flake8
, git
, mypy
}:

buildPythonApplication {
  pname = "splendid-invoice";
  version = "0.0.0";

  disabled = pythonOlder "3.8";

  src = ./.;

  propagatedBuildInputs = [ poppler-qt5 ];

  nativeCheckInputs = [
    black
    flake8
    git
    mypy
  ];

  pythonImportsCheck = [ "splendid_invoice" ];

  meta = with lib; {
    description = "Parse PDF invoices from Splendid Drinks";
    license = licenses.gpl2Plus;
    maintainers = with maintainers; [ schnusch ];
  };
}
