syncat
======

Command line interface similar to ``cat`` with syntax highlighting

Example
-------

::

    curl -s http://httpbin.org/get | syncat --json

Lexers
------

Due to the large number of lexers, the list of lexers is hidden in the
default ``-h``/``--help`` output. Use ``syncat --lexer-help`` to list
all lexers

Usage
-----

::

    usage: syncat [-h] [--style STYLE] [--lexer-help] [--lexer LEXER] [file]

    positional arguments:
      file           File to print with syntax highlighting. Defaults to stdin

    optional arguments:
      -h, --help     show this help message and exit
      --style STYLE  Syntax highlighting style. Choices:
                     abap
                     algol
                     algol_nu
                     arduino
                     autumn
                     borland
                     bw
                     colorful
                     default
                     emacs
                     friendly
                     fruity
                     igor
                     lovelace
                     manni
                     monokai
                     murphy
                     native
                     paraiso-dark
                     paraiso-light
                     pastie
                     perldoc
                     rainbow_dash
                     rrt
                     solarized256
                     tango
                     trac
                     vim
                     vs
                     xcode
      --lexer-help   List help and options for the --lexer argument
      --lexer LEXER  Lexer to use for syntax highlighting. Defaults to guessing
                     based on the file contents. Use --lexer-help for a list of
                     all lexers. Can be used in the form of --lexer LEXER or as
                     --LEXER such as --lexer json or --json
