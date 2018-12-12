#!/usr/bin/env python

KU_PREFIX = 'shinagawa'

LIBRARIES = '''\
品川区	品川図書館	shinagawa
品川区	二葉図書館	futaba
品川区	荏原図書館	ebara
品川区	南大井図書館	minamioi
品川区	源氏前図書館	genjimae
品川区	ゆたか図書館	yutaka
品川区	大井図書館	oi
品川区	五反田図書館	gotanda
品川区	大崎図書館	osaki
品川区	八潮図書館	yashio
品川区	大井町サービスコーナー	oimachi
品川区	武蔵小山サービスコーナー	musashikoyama
品川区	大崎駅西口図書取次施設	osaki-station
品川区	目黒サービスコーナー	meguro
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
