from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    context = p.chromium.launch_persistent_context(
        user_data_dir="whatsapp_session",
        headless=False
    )

    page = context.pages[0] if context.pages else context.new_page()

    page.goto("https://web.whatsapp.com")

    print("WhatsApp Web abierto.")
    input("Cuando estés dentro de WhatsApp, presiona ENTER...")

    print("URL:", page.url)
    print("Título:", page.title())

    input("Presiona ENTER para cerrar...")

    context.close()