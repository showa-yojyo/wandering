#!/usr/bin/env python

KU_PREFIX = 'meguro'

LIBRARIES = '''\
目黒区	八雲中央図書館	yakumochuo
目黒区	大橋図書館	ohashi
目黒区	中目黒駅前図書館	nakameguroekimae
目黒区	目黒区民センター図書館	meguro-center
目黒区	守屋図書館	moriya
目黒区	目黒本町図書館	megurohoncho
目黒区	洗足図書館	senzoku
目黒区	緑が丘図書館	midorigaoka
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
