#!/usr/bin/env python

from argparse import ArgumentParser
from pathlib import Path
import sys

TEMPLATE = '''\
---
title: {title}
---

TODO: {{{{ page.title }}}}について記述する。

{{% include libraries/{ku}-office-hours.html
    holiday_monday_ordinal='{holiday_monday_ordinal}'
    hours_type='{hours_type}' %}}
'''

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

        # e.g. koishikawa[TAB]文京区[TAB]小石川図書館[TAB]3[TAB]long
        filename, ward, name, holiday_monday_ordinal, hours_type = line.split()

        kwargs = dict(
            title=ward + name,
            holiday_monday_ordinal=holiday_monday_ordinal,
            hours_type=hours_type,
            ku=args.ku,)

        # e.g. ${dest_dir}/bunkyo-00-masago.md
        filename = dest_dir.joinpath(f'{args.ku}-{i:02d}-{filename}.md').resolve()

        with open(filename, 'w', encoding='utf8', newline='') as fout:
            fout.write(TEMPLATE.format(**kwargs))

def main(args=sys.argv[1:]):
    sys.exit(run(parse_args(args)))

if __name__ == '__main__':
    main()
