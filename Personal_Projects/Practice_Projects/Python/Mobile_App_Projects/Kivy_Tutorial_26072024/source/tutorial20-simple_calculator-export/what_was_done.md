#   Date: 31-July-2024

This tutorial demonstrates how to convert the calculator app into an exe file.

It does this using pyinstaller.

First, after installing pytinstaller with `pip install pyinstaller`, run the command:
    `pyinstaller <name_of_source_py_file> -w`
This does just this: It prepares packages for the final exported exe file.
It produces a SPEC file.
This file needs to be edited.
#   Changes to be made:
    1.  Add dependencies at the top of the file:
        from kivy_deps import sdl2, glew
    2.  below the `pyz` specification, type:
        `a.datas += [('Code\\<name_of_kv_file.kv>',
                    'C:\\<dir>\\<to>\\<kv_file>',
                    'DATA')]`


Check other.txt in export/calc_deji-31072024

Afterwards, move the kv file into the same directory as the generated executable
        