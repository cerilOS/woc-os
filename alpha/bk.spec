# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

extra_tree = Tree('./data', prefix = 'data')

a = Analysis(['ceril_undercover.py'],
             pathex=['D:\\Documents\\GitHub\\woc-os\\idea'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)

pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

exe = EXE(pyz,
          a.scripts,
          name='Ceril: Undercover !',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          icon = './undercover.ico',
          console=False )

coll - COLLECT(exe,
          a.binaries,
          a.zipfiles,
          a.datas,
          strip=False,
          upx=True,
          name='Ceril: Undercover !'
        )