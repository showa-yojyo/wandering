#!/usr/bin/env python

KU_PREFIX = 'setagaya'

LIBRARIES = '''\
世田谷区	中央図書館	central	http://www.city.setagaya.lg.jp/shisetsu/1214/1266/d00120590.html
世田谷区	梅丘図書館	umegaoka	http://www.city.setagaya.lg.jp/shisetsu/1214/1266/d00135291.html
世田谷区	世田谷図書館	setagaya	http://www.city.setagaya.lg.jp/shisetsu/1214/1266/d00131133.html
世田谷区	砧図書館	kinuta	http://www.city.setagaya.lg.jp/shisetsu/1214/1266/d00067046.html
世田谷区	奥沢図書館	okusawa	http://www.city.setagaya.lg.jp/shisetsu/1214/1266/d00120858.html
世田谷区	玉川台図書館	tamagawadai	http://www.city.setagaya.lg.jp/shisetsu/1214/1266/d00067048.html
世田谷区	代田図書館	daita	http://www.city.setagaya.lg.jp/shisetsu/1214/1266/d00144187.html
世田谷区	烏山図書館	karasuyama	http://www.city.setagaya.lg.jp/shisetsu/1214/1266/d00067050.html
世田谷区	下馬図書館	shimouma	http://www.city.setagaya.lg.jp/shisetsu/1214/1266/d00145332.html
世田谷区	深沢図書館	fukasawa	http://www.city.setagaya.lg.jp/shisetsu/1214/1266/d00067052.html
世田谷区	桜丘図書館	sakuragaoka	http://www.city.setagaya.lg.jp/shisetsu/1214/1266/d00067053.html
世田谷区	尾山台図書館	oyamadai	http://www.city.setagaya.lg.jp/shisetsu/1214/1266/d00067054.html
世田谷区	上北沢図書館	kamikitazawa	http://www.city.setagaya.lg.jp/shisetsu/1214/1266/d00139357.html
世田谷区	粕谷図書館	kasuya	http://www.city.setagaya.lg.jp/shisetsu/1214/1266/d00067056.html
世田谷区	鎌田図書館	kamata	http://www.city.setagaya.lg.jp/shisetsu/1214/1266/d00151189.html
世田谷区	経堂図書館	kyodo	http://www.city.setagaya.lg.jp/shisetsu/1214/1266/d00067058.html
世田谷区	松沢図書室	matsuzawa	http://www.city.setagaya.lg.jp/shisetsu/1214/1267/d00122479.html
世田谷区	池尻図書室	ikejiri	http://www.city.setagaya.lg.jp/shisetsu/1214/1267/d00122482.html
世田谷区	野毛図書室	noge	http://www.city.setagaya.lg.jp/shisetsu/1214/1267/d00122480.html
世田谷区	希望丘図書室	kibogaoka	http://www.city.setagaya.lg.jp/shisetsu/1214/1267/d00122481.html
世田谷区	喜多見図書室	kitami	http://www.city.setagaya.lg.jp/shisetsu/1214/1267/d00122348.html
世田谷区	図書館カウンター三軒茶屋	sangenjaya	http://www.city.setagaya.lg.jp/shisetsu/1214/1268/d00141624.html
世田谷区	図書館カウンター二子玉川	futakotamagawa	http://www.city.setagaya.lg.jp/shisetsu/1214/1268/d00138312.html
'''

TEMPLATE = '''\
---
title: {title}
published: false
---

TODO: {{{{ page.title }}}}について記述する。

{{% include libraries/{ku}-office-hours.html
    library_name="{library_name}"
    library_url="{library_url}" %}}
'''

def main():
    for i, line in enumerate(LIBRARIES.splitlines()):
        if not line:
            continue
        ward, name, filename, url = line.split()
        title = ward + name
        filename = f'{KU_PREFIX}-{i:02d}-{filename}.md'

        with open(filename, 'w', encoding='utf8', newline='') as fout:
            fout.write(TEMPLATE.format(title=title, ku=KU_PREFIX,
            library_name=name,
            library_url=url))

if __name__ == '__main__':
    main()
