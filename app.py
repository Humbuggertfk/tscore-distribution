"""
T-Score Bell Curve Tool — Desktop Launcher
==========================================
Starts a local HTTP server and opens the tool in the default browser.
Bundled by PyInstaller into a standalone app (Mac) or exe (Windows).
"""

import os, sys, socket, threading, webbrowser, time
from http.server import HTTPServer, SimpleHTTPRequestHandler

def resource_path(name):
    base = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base, name)

HTML_FILE = "tscore_pct_pivot_obs_norm.html"

def find_free_port():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("127.0.0.1", 0))
        return s.getsockname()[1]

class QuietHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=resource_path("."), **kwargs)
    def log_message(self, *a): pass
    def log_error(self, *a): pass

def main():
    port = find_free_port()
    url  = f"http://127.0.0.1:{port}/{HTML_FILE}"
    server = HTTPServer(("127.0.0.1", port), QuietHandler)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    time.sleep(0.5)
    webbrowser.open(url)
    print("=" * 55)
    print("  T-Score Bell Curve Tool is running.")
    print(f"  URL : {url}")
    print("  Close this window to stop the server.")
    print("=" * 55)
    try:
        while True: time.sleep(1)
    except KeyboardInterrupt:
        server.shutdown()

if __name__ == "__main__":
    main()
