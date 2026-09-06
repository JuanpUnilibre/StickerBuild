from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)

    page = browser.new_page()

    page.goto("https://web.whatsapp.com")

    print("WhatsApp Web abierto.")
    print("Escanea el código QR si es necesario.")

    input("Presiona ENTER cuando WhatsApp esté listo...")

    print("Sesión lista.")

    input("Presiona ENTER para cerrar...")

    browser.close()