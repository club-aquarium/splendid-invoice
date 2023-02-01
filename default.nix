{ lib
, buildPythonApplication
, poppler-qt5
, black
, flake8
, mypy
}:

buildPythonApplication {
  pname = "splendid-invoice";
  version = "0.0.0";

  src = ./.;

  propagatedBuildInputs = [ poppler-qt5 ];

  nativeBuildInputs = [
    black
    flake8
    mypy
  ];

  pythonImportsCheck = [ "splendid_invoice" ];

  meta = with lib; {
    description = "Parse PDF invoices from Splendid Drinks";
    license = licenses.gpl2Plus;
    maintainers = with maintainers; [ schnusch ];
  };
}
