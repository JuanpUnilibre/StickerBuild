from pywinauto import Desktop

windows = Desktop(backend="uia").windows()

for i, window in enumerate(windows):
    try:
        print(f"{i} | {window.window_text()}")
    except:
        pass