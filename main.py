from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    context = p.chromium.launch_persistent_context(
        user_data_dir="whatsapp_session",
        headless=False,
        args=["--start-maximized"],
        no_viewport=True
    )

    page = context.pages[0] if context.pages else context.new_page()

    page.goto("https://web.whatsapp.com")

    input("Cuando WhatsApp esté cargado, presiona ENTER...")

    # Buscar el botón "Tú"
    tu = page.get_by_role("button", name="Tú")

    print("Botón 'Tú' encontrado:", tu.count())

    if tu.count() > 0:
        tu.click()
        print("✅ Se abrió el chat contigo.")
    else:
        print("❌ No se encontró el botón 'Tú'.")

    page.wait_for_timeout(2000)

    # Mostrar los botones que ahora existen
    botones = page.get_by_role("button")

    print("\nBOTONES DESPUÉS DE ABRIR EL CHAT:\n")

    for i in range(botones.count()):
        boton = botones.nth(i)

        try:
            print(
                i,
                "| texto:", boton.inner_text(),
                "| aria:", boton.get_attribute("aria-label"),
                "| title:", boton.get_attribute("title")
            )
        except:
            pass

    input("\nPresiona ENTER para cerrar...")
    context.close()