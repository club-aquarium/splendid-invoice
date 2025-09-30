#!/usr/bin/env nix-shell
#!nix-shell -i bash -p ruff 'python3.pkgs.xsdata.overridePythonAttrs (oldAttrs: { dependencies = (oldAttrs.dependencies or [ ]) ++ oldAttrs.optional-dependencies.cli; })'
export PS4='$ '
set -eux
for schema in \
    minimum='ZF233_DE_01/Schema/0. Factur-X_1.07.3_MINIMUM/Factur-X_1.07.3_MINIMUM.xsd' \
    basicwl='ZF233_DE_01/Schema/1. Factur-X_1.07.3_BASICWL/Factur-X_1.07.3_BASICWL.xsd' \
    basic='ZF233_DE_01/Schema/2. Factur-X_1.07.3_BASIC/Factur-X_1.07.3_BASIC.xsd' \
    en16931='ZF233_DE_01/Schema/3. Factur-X_1.07.3_EN16931/Factur-X_1.07.3_EN16931.xsd' \
    extended='ZF233_DE_01/Schema/4. Factur-X_1.07.3_EXTENDED/Factur-X_1.07.3_EXTENDED.xsd' \
    d22b='ZF233_DE_01/Schema/5. CII D22B XSD/CrossIndustryInvoice_100pD22B.xsd' \
; do
    package="${schema%%=*}"
    path="${schema#*=}"

    # $package must not contain a slash
    [ -z "${package##*/*}" ] || rm -fr "generated/${package}"

    xsdata generate --package="generated.${package}" --structure-style=clusters --relative-imports "${path}"
    find "generated/${package}" -type f -name '*.py' -exec \
        sed -e '/^from xsdata.models.datatype import\b/ s/$/  # type: ignore[import-not-found]/' -i {} +
    ruff check --select I --fix --no-respect-gitignore "generated/${package}"
    ruff format --no-respect-gitignore "generated/${package}"
done
