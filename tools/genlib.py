#!/usr/bin/env python

KU_PREFIX = 'chuo'

LIBRARIES = '''\
中央区	京橋図書館	kyobashi
中央区	日本橋図書館	nihonbashi
中央区	月島図書館	tsukishima
'''

TEMPLATE = '''\
---
title: {title}
published: false
---

TODO: {{{{ page.title }}}}について記述する。

{{% include libraries/{ku}-office-hours.html %}}
'''

def main():
    for i, line in enumerate(LIBRARIES.splitlines()):
        if not line:
            continue
        ward, name, filename = line.split()
        title = ward + name
        filename = f'{KU_PREFIX}-{i:02d}-{filename}.md'

        with open(filename, 'w', encoding='utf8', newline='') as fout:
            fout.write(TEMPLATE.format(title=title, ku=KU_PREFIX))

if __name__ == '__main__':
    main()
