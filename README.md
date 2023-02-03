# splendid-invoice

splendid-invoice is a command-line tool that parses PDF invoices from
[Splendid Drinks](https://www.splendid-drinks.com/) or
[Gustav Müller](https://www.gustav-mueller.de/) to CSV. Invoices from the latter
follow the [ZUGFeRD 1.0 standard](https://www.ferd-net.de/standards/zugferd-versionsarchiv/zugferd-1.0.html)
so it should be able to parse all of those.

## Installation

`pip install https://github.com/club-aquarium/splendid-invoice/archive/refs/heads/master.zip`

or

clone the repo and run `nix-shell`

### Dependencies

  * Python >= [3.8](https://docs.python.org/3/library/functools.html#functools.cached_property)
  * [popplerqt5](https://pypi.org/project/python-poppler-qt5/)

To run tests during build you also need:

  * [black](https://github.com/psf/black)
  * [flake8](https://flake8.pycqa.org/)
  * [mypy](https://mypy-lang.org/)

## Usage

### splendid-invoice

```
usage: splendid-invoice [-h] [-v] <invoice> [<invoice> ...]

Parse PDF invoices from Splendid Drinks or conforming to the ZUGFeRD 1.0 standard

positional arguments:
  <invoice>

optional arguments:
  -h, --help     show this help message and exit
  -v, --verbose  Print parsed PDF to standard error.
```

### splendid-mail

```
usage: splendid-mail [-h] -H HOST -l LOGIN (-p PASSWORD | --password-from-stdin) [-m MAILBOX] [-v] [--confirm] [--after AFTER] [-n N] [--git FILE] [-r]

Download PDF attachments from mailbox and feed them into splendid-invoice

optional arguments:
  -h, --help            show this help message and exit
  -H HOST, --host HOST  IMAP host
  -l LOGIN, --login LOGIN
                        IMAP login
  -p PASSWORD, --password PASSWORD
                        IMAP password
  --password-from-stdin
                        read IMAP password from stdin
  -m MAILBOX, --mailbox MAILBOX
                        mailbox sub-directory, be sure to quote properly
  -v, --verbose         Print parsed PDF to standard error.
  --confirm             Wait for user to press Enter after each PDF.

selection arguments:
  --after AFTER         Skip messages before AFTER. (format YYYY-MM-DD HH:MM:SS[+-]HH:MM)
  -n N, --max-count N   Stop after N messages.

git arguments:
  --git FILE            Write csv to git-tracked file FILE.
  -r, --reverse         When writing to a git-tracked file, append newer invoices to the top of the file.
```
