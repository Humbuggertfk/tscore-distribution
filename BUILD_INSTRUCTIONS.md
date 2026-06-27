# T-Score Bell Curve Tool — Desktop App Build Instructions

## What You Get
Two standalone desktop applications — no Python required on the end-user machine.

| Platform | Output | How it works |
|----------|--------|--------------|
| **Mac** | `TScoreTool.app` | Double-click; opens in your default browser |
| **Mac Distribution** | `TScoreTool.dmg` | Disk image with drag-and-drop installer |
| **Windows** | `TScoreTool.exe` | Double-click; opens in your default browser |

---

## Prerequisites (do this once, on your own computer)

### 1 — Install Python 3.9 or later
- **Mac**: https://www.python.org/downloads/ — or `brew install python`
- **Windows**: https://www.python.org/downloads/ — ✅ check **"Add Python to PATH"**

### 2 — Install PyInstaller
```
pip install pyinstaller
```

---

## Building the Mac App

```bash
# In Terminal, navigate to this folder:
cd /path/to/tscore_desktop_src

# Build:
pyinstaller tscore_mac.spec

# Your app is at:
#   dist/TScoreTool.app
```

**Distribute:** Zip `dist/TScoreTool.app` and share it. No Python needed on the recipient's Mac.

**⚠️ Gatekeeper warning on first launch:**
Right-click the app → **Open** → click **Open**. One-time only.

---

## Building the Mac .dmg (Disk Image)

The `.dmg` provides a professional drag-and-drop installer experience. It includes a symlink to the Applications folder for easy installation.

### Prerequisites
- macOS (the `.dmg` can only be built on Mac)
- `build_dmg.sh` from this repository
- Python 3.9+ and PyInstaller (see Prerequisites above)

### Build Steps

```bash
# 1. Clone this repository (if you haven't already)
git clone https://github.com/Humbuggertfk/tscore-distribution.git
cd tscore-distribution

# 2. Copy the build files from tscore_desktop_src
#    (or ensure you have tscore_mac.spec, app.py, tscore_pct_pivot_obs_norm.html here)

# 3. Make the script executable
chmod +x build_dmg.sh

# 4. Run the build script
./build_dmg.sh
```

**Output:** `TScoreTool.dmg` in the current directory

### What the Script Does
1. ✅ Builds the `.app` with PyInstaller (if not already built)
2. ✅ Creates a staging directory
3. ✅ Copies `TScoreTool.app` into the DMG
4. ✅ Adds a symlink to `/Applications` for drag-and-drop installation
5. ✅ Generates `TScoreTool.dmg` using `hdiutil`
6. ✅ Cleans up temporary files

### Distributing the .dmg
- Upload `TScoreTool.dmg` to your distribution channel (GitHub Releases, website, etc.)
- Users download and open the `.dmg`
- They see the app and Applications folder
- Drag `TScoreTool.app` to Applications to install
- Launch from Applications or Spotlight

---

## Building the Windows Exe

```cmd
REM In Command Prompt, navigate to this folder:
cd C:\path\to\tscore_desktop_src

REM Build:
pyinstaller tscore_windows.spec

REM Your exe is at:
REM   dist\TScoreTool.exe
```

**Distribute:** Copy `dist\TScoreTool.exe` to any Windows PC. No Python needed.

**⚠️ SmartScreen warning on first launch:**
Click **More info** → **Run anyway**. One-time only.

---

## How It Works

1. `app.py` starts Python's built-in HTTP server on a random free local port.
2. Opens that URL in the default browser automatically.
3. PyInstaller bundles Python + `app.py` + the HTML into one executable.
4. On Mac, it wraps that into a `.app` bundle.
5. `build_dmg.sh` creates a distribution `.dmg` with Applications symlink.

---

## Updating the Tool

### For Mac App (.app)
1. Replace `tscore_pct_pivot_obs_norm.html` with the new version.
2. Run: `pyinstaller tscore_mac.spec`
3. The new `dist/TScoreTool.app` has the updated tool.

### For Mac Distribution (.dmg)
1. Update `tscore_pct_pivot_obs_norm.html`
2. Run: `./build_dmg.sh`
3. The new `TScoreTool.dmg` contains the updated app.

### For Windows Exe
1. Replace `tscore_pct_pivot_obs_norm.html` with the new version.
2. Run: `pyinstaller tscore_windows.spec`
3. The new `dist\TScoreTool.exe` has the updated tool.

---

## File Reference

| File | Purpose |
|------|---------|
| `app.py` | Python launcher script |
| `tscore_pct_pivot_obs_norm.html` | The complete T-Score tool |
| `tscore_mac.spec` | PyInstaller config for Mac |
| `tscore_windows.spec` | PyInstaller config for Windows |
| `build_dmg.sh` | Build script for macOS .dmg distribution |
| `requirements.txt` | Python dependencies |

---

## Troubleshooting

### `.dmg` won't build: "hdiutil: create failed"
- Ensure you're on macOS (`.dmg` requires native tools)
- Check that `dist/TScoreTool.app` exists
- Try: `rm -rf dist/build && ./build_dmg.sh`

### App won't launch on first run
- **Mac:** Right-click → Open → Open (Gatekeeper bypass)
- **Windows:** Click "More info" → "Run anyway" (SmartScreen bypass)

### Python not found
- Install Python 3.9+ from https://www.python.org/downloads/
- Verify: `python --version` or `python3 --version`

### PyInstaller not found
- Install: `pip install pyinstaller`
- Verify: `pyinstaller --version`
