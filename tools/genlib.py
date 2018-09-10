#!/usr/bin/env python

LIBRARIES = '''\
北区中央図書館	central
北区中央図書館分室	central-branch
北区滝野川図書館	takinogawa
北区赤羽図書館	akabane
北区浮間図書館	ukima
北区赤羽西図書館	akabanenishi
北区昭和町図書館	showamachi
北区田端図書館	tabata
北区上十条図書館	kamijujo
北区赤羽北図書館	akabanekita
北区東田端図書館	hitashitabata
北区神谷図書館	kamiya
北区滝野川西図書館	takinogawahishi
北区豊島図書館	toshima
北区東十条図書館	higashijujo
'''

TEMPLATE = '''\
---
title: {title}
---

TODO: 図書館について記述する。

'''

def main():
    for i, line in enumerate(LIBRARIES.splitlines()):
        title, filename = line.split('\t')

        filename = f'kita-{i:02d}-{filename}.md'

        with open(filename, 'w', encoding='utf8', newline='') as fout:
            fout.write(TEMPLATE.format(title=title))

if __name__ == '__main__':
    main()
