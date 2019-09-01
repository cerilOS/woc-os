# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['ceril_undercover.py'],
             pathex=['D:\\Documents\\GitHub\\woc-os\\alpha'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None,
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

for d in a.datas:
    if 'pyconfig' in d[0]:
        a.datas.remove(d)
        break

a.datas +=[('undercover.ico','D:\\Documents\\GitHub\\woc-os\\alpha\\data\\icon\\undercover.ico','DATA'),
            ('01.jpg','D:\\Documents\\GitHub\\woc-os\\alpha\\data\\img\\01.jpg','DATA'),
            ('02.jpg','D:\\Documents\\GitHub\\woc-os\\alpha\\data\\img\\02.jpg','DATA'),
            ('03.jpg','D:\\Documents\\GitHub\\woc-os\\alpha\\data\\img\\03.jpg','DATA'),
            ('04.jpg','D:\\Documents\\GitHub\\woc-os\\alpha\\data\\img\\04.jpg','DATA'),
            ('05.jpg','D:\\Documents\\GitHub\\woc-os\\alpha\\data\\img\\05.jpg','DATA'),
            ('06.jpg','D:\\Documents\\GitHub\\woc-os\\alpha\\data\\img\\06.jpg','DATA'),
            ('07.jpg','D:\\Documents\\GitHub\\woc-os\\alpha\\data\\img\\07.jpg','DATA'),
            ('08.jpg','D:\\Documents\\GitHub\\woc-os\\alpha\\data\\img\\08.jpg','DATA'),
            ('09.jpg','D:\\Documents\\GitHub\\woc-os\\alpha\\data\\img\\09.jpg','DATA'),
            ('10.jpg','D:\\Documents\\GitHub\\woc-os\\alpha\\data\\img\\10.jpg','DATA'),
            ('11.jpg','D:\\Documents\\GitHub\\woc-os\\alpha\\data\\img\\11.jpg','DATA'),
            ('12.jpg','D:\\Documents\\GitHub\\woc-os\\alpha\\data\\img\\12.jpg','DATA'),
            ('13.jpg','D:\\Documents\\GitHub\\woc-os\\alpha\\data\\img\\13.jpg','DATA'),
            ('14.jpg','D:\\Documents\\GitHub\\woc-os\\alpha\\data\\img\\14.jpg','DATA'),
            ('15.jpg','D:\\Documents\\GitHub\\woc-os\\alpha\\data\\img\\15.jpg','DATA'),
            ('16.jpg','D:\\Documents\\GitHub\\woc-os\\alpha\\data\\img\\16.jpg','DATA'),
            ('17.jpg','D:\\Documents\\GitHub\\woc-os\\alpha\\data\\img\\17.jpg','DATA'),
            ('18.jpg','D:\\Documents\\GitHub\\woc-os\\alpha\\data\\img\\18.jpg','DATA'),
            ('19.jpg','D:\\Documents\\GitHub\\woc-os\\alpha\\data\\img\\19.jpg','DATA'),
            ('20.jpg','D:\\Documents\\GitHub\\woc-os\\alpha\\data\\img\\20.jpg','DATA'),
]

pyz = PYZ(a.pure, a.zipped_data,

             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          exclude_binaries=False,
          name='Ceril_The_Undercover.exe',
          debug=False,
          bootloader_ignore_signals=False,
          strip=None,
          upx=True,
          icon = 'D:\\Documents\\GitHub\\woc-os\\alpha\\data\\icon\\undercover.ico',
          console=False )
