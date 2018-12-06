#!/usr/bin/env python

KU_PREFIX = 'minato'

LIBRARIES = '''\
港区	みなと図書館	minato
港区	三田図書館	mita
港区	麻布図書館	azabu
港区	赤坂図書館	akasaka
港区	高輪図書館	takanawa
港区	高輪図書館分室	takanawa-branch
港区	港南図書館	konan
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
