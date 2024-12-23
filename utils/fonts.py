def font_helvetica(text, current_font, font_choice) -> None:
    text.config(font="Helvetica")
    current_font.set("Helvetica")
    font_choice.set("Helvetica")

def font_courier(text, current_font, font_choice) -> None:
    text.config(font="Courier")
    current_font.set("Courier")
    font_choice.set("Courier")