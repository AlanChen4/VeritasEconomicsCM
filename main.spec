# -*- mode: python ; coding: utf-8 -*-
from PyInstaller.utils.hooks import collect_dynamic_libs

block_cipher = None

hidden_imports = [
    'fiona',
    'fiona.schema',
    'fiona._shim',
    'geopandas.datasets',
    'gdal',
    'pandas._libs.tslibs.timedeltas',
    'pyproj',
    'pytest',
    'rtree',
    'scipy',
    'scipy.spatial.transform._rotation_groups',
    'sklearn',
    'sklearn.utils._weight_vector',
    'shapely',
    'shapely.geometry',
]

a = Analysis(['main.py'],
             binaries=collect_dynamic_libs('rtree'),
             datas=[('./data', 'data')],
             hiddenimports=hidden_imports,
             hookspath=['./hooks'],
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
          [],
          exclude_binaries=True,
          name='main',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False
          )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               upx_exclude=[],
               name='main')
