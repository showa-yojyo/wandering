#!/usr/bin/env python

from argparse import ArgumentParser
from pathlib import Path
import sys

TEMPLATE = '''\
---
title: {title}
published: false
---

TODO: {{{{ page.title }}}}について記述する。

{{% include libraries/{ku}-office-hours.html monday='{monday}' office_type='{office_type}' %}}
'''

HOSTNAME = 'https://www.city.nerima.tokyo.jp'

def parse_args(args):
    """Parse the command line parameters."

    Returns:
        An instance of argparse.ArgumentParser that stores the command line
        parameters.
    """

    parser = ArgumentParser(description='TBW')
    parser.add_argument('ku', help='e.g. shibuya, shinjuku, shinagawa')
    return parser.parse_args(args or ['--help'])

def run(args):
    """The main function.

    Args:
        args: An instance of argparse.ArgumentParser parsed in the configure
        function.

    Returns:
        None.
    """

    dest_dir = Path(__file__).parent.joinpath('../_libraries')

    for i, line in enumerate(sys.stdin):
        line = line.strip()
        if not line:
            continue

        # e.g. hikarigaoka[TAB]練馬区[TAB]光が丘図書館[TAB]2[TAB]A[TAB]/shisetsu/bunka/lib/hikarigaoka.html
        filename, ward, name, monday, office_type, url_path = line.split()
        # e.g. 渋谷区渋谷図書館
        title = ward + name

        kwargs = dict(
            title=title, ku=args.ku, office_type=office_type,
            monday=monday, url_path=HOSTNAME + url_path)

        # e.g. ${dest_dir}/shibuya-00-central.md
        filename = dest_dir.joinpath(f'{args.ku}-{i:02d}-{filename}.md').resolve()

        with open(filename, 'w', encoding='utf8', newline='') as fout:
            fout.write(TEMPLATE.format(**kwargs))

def main(args=sys.argv[1:]):
    sys.exit(run(parse_args(args)))

if __name__ == '__main__':
    main()
