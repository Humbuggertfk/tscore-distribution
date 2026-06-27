# T-Score Bell Curve Tool — Distribution

This repository contains build scripts and instructions for creating distribution packages of the **T-Score Bell Curve Tool** desktop application.

## 🎯 Overview

The T-Score Bell Curve Tool is a standalone desktop application for visualizing and analyzing T-score distributions. This repository automates the creation of:

- **macOS `.dmg`** — Professional disk image with drag-and-drop installer
- **macOS `.app`** — Standalone application bundle
- **Windows `.exe`** — Standalone executable

## 📦 Quick Start

### For macOS Users (Building .dmg)

```bash
# 1. Clone this repository
git clone https://github.com/Humbuggertfk/tscore-distribution.git
cd tscore-distribution

# 2. Make the build script executable
chmod +x build_dmg.sh

# 3. Run the script
./build_dmg.sh
```

Your `.dmg` will be created in the current directory: `TScoreTool.dmg`

### For Detailed Instructions

See **[BUILD_INSTRUCTIONS.md](BUILD_INSTRUCTIONS.md)** for:
- Prerequisites and setup
- Platform-specific build steps
- Troubleshooting
- Distribution guidelines

## 📋 What's Inside

| File | Purpose |
|------|---------|
| `build_dmg.sh` | Automated macOS .dmg builder |
| `BUILD_INSTRUCTIONS.md` | Complete build documentation |
| `.gitignore` | Excludes build artifacts from version control |

## 🔧 Requirements

- **macOS** (for building `.dmg`)
- **Python 3.9+**
- **PyInstaller** (`pip install pyinstaller`)

## 📚 Documentation

- **[BUILD_INSTRUCTIONS.md](BUILD_INSTRUCTIONS.md)** — Full build guide for all platforms
- **[build_dmg.sh](build_dmg.sh)** — Commented build script

## 💬 License

This repository is for distributing the T-Score Bell Curve Tool. See the main project repository for license details.

## 👤 Author

**Humbuggertfk**

---

**Last Updated:** 2026-06-27
