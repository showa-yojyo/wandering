#!/usr/bin/env python

KU_PREFIX = 'arakawa'

LIBRARIES = '''\
ゆいの森あらかわ               central
南千住図書館                   minamisenju
尾久図書館                     ogu
町屋図書館                     machiya
日暮里図書館                   nippori
汐入図書サービスステーション   shioiri
冠新道図書サービスステーション kammurishindo
'''

TEMPLATE = '''\
---
title: {title}
---

TODO: {{{{ page.title }}}}について記述する。

{{% include libraries/{ku}-office-hours.html %}}
'''

def main():
    for i, line in enumerate(LIBRARIES.splitlines()):
        title, filename = line.split()

        filename = f'{KU_PREFIX}-{i:02d}-{filename}.md'

        with open(filename, 'w', encoding='utf8', newline='') as fout:
            fout.write(TEMPLATE.format(title=title, ku=KU_PREFIX))

if __name__ == '__main__':
    main()
