#!/usr/bin/env python

KU_PREFIX = 'ota'

LIBRARIES = '''\
大田区	大田図書館	ota
大田区	大森南図書館	omoriminami
大田区	大森東図書館	omorihigashi
大田区	大森西図書館	omorinishi
大田区	入新井図書館	iriarai
大田区	馬込図書館	magome
大田区	池上図書館	ikegami
大田区	久が原図書館	kugahara
大田区	洗足池図書館	senzokuike
大田区	浜竹図書館	hamatake
大田区	羽田図書館	haneda
大田区	六郷図書館	rokugo
大田区	下丸子図書館	shimomaruko
大田区	多摩川図書館	tamagawa
大田区	蒲田図書館	kamata
大田区	蒲田駅前図書館	kamataekimae
大田区	大田文化の森情報館	omoribunkanomori
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
