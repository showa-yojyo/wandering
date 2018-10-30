#!/usr/bin/env python

KU_PREFIX = 'taito'

LIBRARIES = '''\
台東区中央図書館	central
台東区中央図書館浅草橋分室	central-branch-asakusabashi
台東区中央図書館谷中分室	central-branch-yanaka
台東区根岸図書館	negishi
台東区石浜図書館	ishihama
台東区くらまえオレンジ図書館	kuramae
台東区すこやかとしょしつ	sukoyaka
台東区東浅草なかよし図書館	higashiasakusa
'''

TEMPLATE = '''\
---
title: {title}
published: false
---

TODO: {{{{ page.title }}}}について記述する。

## 休館日

休館日は次のとおり：

* 第 3 木曜日（祝日の場合は翌日振替）
* 年末年始
* 特別整理期間

## 営業時間

営業時間は次のとおり：

* 月～土 9:00-20:00
* 日・祝 9:00-17:00
'''

def main():
    for i, line in enumerate(LIBRARIES.splitlines()):
        title, filename = line.split()

        filename = f'{KU_PREFIX}-{i:02d}-{filename}.md'

        with open(filename, 'w', encoding='utf8', newline='') as fout:
            fout.write(TEMPLATE.format(title=title, ku=KU_PREFIX))

if __name__ == '__main__':
    main()
