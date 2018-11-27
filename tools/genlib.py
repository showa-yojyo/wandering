#!/usr/bin/env python

KU_PREFIX = 'koto'

LIBRARIES = '''\
江東区	江東図書館	koto
江東区	深川図書館	hukagawa
江東区	東陽図書館	toyo
江東区	豊洲図書館	toyosu
江東区	東雲図書館	shinonome
江東区	古石場図書館	furuishiba
江東区	城東図書館	joto
江東区	亀戸図書館	kameido
江東区	砂町図書館	sunamachi
江東区	東大島図書館	higashiojima
江東区	白河こどもとしょかん	shirakawa-children
江東区	枝川図書サービスコーナー	edakawa
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
