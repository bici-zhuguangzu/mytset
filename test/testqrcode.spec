# -*- mode: python -*-
a = Analysis(['testqrcode.py'],
             pathex=['/Users/zhuguangzu/mytset'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='testqrcode',
          debug=False,
          strip=None,
          upx=True,
          console=True )
