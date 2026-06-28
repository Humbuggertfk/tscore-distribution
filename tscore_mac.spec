# PyInstaller spec — Mac (.app bundle)
# Build on a Mac:  pyinstaller tscore_mac.spec
block_cipher = None
a = Analysis(
    ['app.py'], pathex=['.'], binaries=[],
    datas=[('tscore_pct_pivot_obs_norm.html', '.')],
    hiddenimports=[], hookspath=[], hooksconfig={},
    runtime_hooks=[], excludes=[], cipher=block_cipher, noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)
exe = EXE(pyz, a.scripts, [], exclude_binaries=True,
    name='TScoreTool', debug=False, bootloader_ignore_signals=False,
    strip=False, upx=True, console=True,
    codesign_identity=None, entitlements_file=None,
)
coll = COLLECT(exe, a.binaries, a.zipfiles, a.datas,
    strip=False, upx=True, upx_exclude=[], name='TScoreTool',
)
app = BUNDLE(coll, name='TScoreTool.app', icon=None,
    bundle_identifier='com.tscore.bellcurve',
    info_plist={
        'CFBundleName': 'T-Score Bell Curve Tool',
        'CFBundleDisplayName': 'T-Score Bell Curve Tool',
        'CFBundleVersion': '1.0.0',
        'CFBundleShortVersionString': '1.0.0',
        'NSHighResolutionCapable': True,
    },
)
