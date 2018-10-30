#!/usr/bin/env python

KU_PREFIX = 'sumida'

LIBRARIES = '''\
墨田区ひきふね図書館	hikihune
墨田区緑図書館	midori
墨田区立花図書館	tachibana
墨田区八広図書館	yahiro
墨田区東駒形コミュニティ会館図書室	higashikomagata
墨田区梅若橋コミュニティ会館図書室	umewakabashi
墨田区横川コミュニティ会館図書室	yokokawa
墨田区すみだ女性センター情報資料コーナー	sumida-women
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
        title, filename = line.split()

        filename = f'{KU_PREFIX}-{i:02d}-{filename}.md'

        with open(filename, 'w', encoding='utf8', newline='') as fout:
            fout.write(TEMPLATE.format(title=title, ku=KU_PREFIX))

if __name__ == '__main__':
    main()
