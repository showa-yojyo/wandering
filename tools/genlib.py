#!/usr/bin/env python

KU_PREFIX = 'chiyoda'

LIBRARIES = '''\
千代田区	千代田図書館	chiyoda
千代田区	四番町図書館	yobancho
千代田区	日比谷図書文化館	hibiya
千代田区	昌平まちかど図書館	shohei
千代田区	神田まちかど図書館	kanda
千代田区	ちよだパークサイドプラザ区民図書室	park-side-plaza
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
