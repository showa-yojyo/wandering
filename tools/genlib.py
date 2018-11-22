#!/usr/bin/env python

KU_PREFIX = 'edogawa'

LIBRARIES = '''\
江戸川区	中央図書館	central
江戸川区	小岩図書館	koiwa
江戸川区	松江図書館	matsue
江戸川区	小松川図書館	komatsugawa
江戸川区	葛西図書館	kasai
江戸川区	西葛西図書館	nishikawai
江戸川区	東葛西図書館	higashikasai
江戸川区	篠崎図書館	shinozaki
江戸川区	東部図書館	tobu
江戸川区	篠崎子ども図書館	sinozaki-children
江戸川区	清新町コミュニティ図書館	seishincho
江戸川区	鹿骨コミュニティ図書館	shishibone
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
