#!/usr/bin/env python

KU_PREFIX = 'katsushika'

LIBRARIES = '''\
葛飾区	中央図書館	central
葛飾区	立石図書館	tateishi
葛飾区	お花茶屋図書館	ohanajaya
葛飾区	上小松図書館	kamikomatsu
葛飾区	亀有図書館	kameari
葛飾区	水元図書館	mizumoto
葛飾区	鎌倉図書館	kamakura
葛飾区	四つ木地区図書館	yotsugi
葛飾区	西水元地区図書館	nishimizumoto
葛飾区	青戸地区図書館	aoto
葛飾区	奥戸地区図書館	okudo
葛飾区	こすげ地区図書館	kosuge
葛飾区	新宿図書センター	nijuku
葛飾区	男女平等推進センター図書資料室	gender-equality
葛飾区	新宿図書サービスコーナー	nijuku-service
葛飾区	リリオ亀有図書サービスカウンター	kameari-service
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
