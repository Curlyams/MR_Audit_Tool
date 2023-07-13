# -*- mode: python ; coding: utf-8 -*-


block_cipher = None


a = Analysis(
    ['Audit_Tool.py'],
    pathex=[],
    binaries=[],
    datas=[('icons/1x/*', 'icons/1x'), ('images/Layout/*', 'images/Layout'), ('C:\\Users\\bcurl\\Desktop\\MR_Audit_Tool\\Audit_Tool\\data\\modes.csv', '.'), ('C:\\Users\\bcurl\\Desktop\\MR_Audit_Tool\\Audit_Tool\\data\\PrivateProviders.csv', '.'), ('C:\\Users\\bcurl\\Desktop\\MR_Audit_Tool\\Audit_Tool\\data\\purpose_summary.csv', '.'), ('C:\\Users\\bcurl\\Desktop\\MR_Audit_Tool\\Audit_Tool\\data\\service_areas.csv', '.')],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='Audit_Tool',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['C:\\Users\\bcurl\\Desktop\\MR_Audit_Tool\\Audit_Tool\\icons\\1x\\auditing-icon-9.ico'],
)
