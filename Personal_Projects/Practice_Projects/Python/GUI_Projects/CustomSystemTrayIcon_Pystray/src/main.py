"""
    Date: Wed-12-June-2024

    This is so cool! It takes the image and creates the tray icon in my taskbar.
    Then calls the function when I click on it!

    Usefulness:

    This is useful if one has a program that runs in the background...
    like scripts that:
        1.  scrape a website
        2.  to run a script that listens for stock price updates or backs up something.
    One will want it to run windowless, but just showing the tray icon, instead of the whole
    window.
    The tray icon can then be used to control options or display the full window.

"""
import pystray
#  Use PIL.Image or from PIL import Image
#   But prefer PIL.Image because other graphics libraries like tkinter and opencv also have
#   an image class or image submodule.
import PIL.Image

#   Load Image
image = PIL.Image.open("resources/generator.png")


#   This function is called when one clikcs on this item of the tray icon menu
#   `icon` is the full Icon object
#   `item` is the item clicked.
def on_click_tray_icon_item(icon, item):
    if str(item) == "Say Yo!":
        print("Yo! World!")
    elif str(item) == "Exit":
        icon.stop()
    elif str(item) == "Subitem 1":
        print("Sub 1")
    else:
        print("Not implemented yet!")
        


icon = pystray.Icon("Ezer", image, menu=pystray.Menu(
    pystray.MenuItem("Say Yo!", on_click_tray_icon_item),
    pystray.MenuItem("Exit", on_click_tray_icon_item),
    pystray.MenuItem("Submenu", pystray.Menu(
        pystray.MenuItem("Subitem 1", on_click_tray_icon_item),
        pystray.MenuItem("Subitem 2", on_click_tray_icon_item)
    ))
))

icon.run()