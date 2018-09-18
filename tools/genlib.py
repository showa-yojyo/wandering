#!/usr/bin/env python

KU_PREFIX = 'toshima'

LIBRARIES = '''\
中央図書館	central
駒込図書館	komagome
上池袋図書館	kamiikebukuro
千早図書館	chihaya
巣鴨図書館	sugamo
池袋図書館	ikebukuro
目白図書館	mejiro
雑司が谷図書貸出コーナー	zoushigaya
'''

TEMPLATE = '''\
---
title: {title}
---

TODO: {{ page.title }}について記述する。

{% include libraries/{ku}-office-hours.html %}
'''

def main():
    for i, line in enumerate(LIBRARIES.splitlines()):
        title, filename = line.split('\t')

        filename = f'{KU_PREFIX}-{i:02d}-{filename}.md'

        with open(filename, 'w', encoding='utf8', newline='') as fout:
            fout.write(TEMPLATE.format(title=title, ku=KU_PREFIX))

if __name__ == '__main__':
    main()
