import urllib.parse
import os
import subprocess
import time

phone = "94761651626"                # intl format, no plus, no spaces
msg = "Hello from Python 👋"         # your message
url = f"whatsapp://send?phone={phone}&text={urllib.parse.quote(msg)}"

# Try 1: os.startfile (most reliable on Windows)
try:
    os.startfile(url)  # opens WhatsApp Desktop with the chat prefilled
except Exception as e:
    print("startfile failed:", e)
    # Try 2: 'start' via cmd (sometimes works when startfile doesn't)
    try:
        subprocess.run(['cmd', '/c', 'start', '', url], check=True)
    except Exception as e2:
        print("cmd start failed:", e2)
        print("\nTroubleshooting:")
        print("  • Make sure WhatsApp Desktop is installed and logged in.")
        print("  • Reinstall WhatsApp Desktop so the whatsapp:// protocol is registered.")
        print("  • Check phone number format (e.g., 9476XXXXXXX).")
        print("  • Test in Run dialog (Win+R): whatsapp://send?text=hi")
