from tkinter import filedialog

def save_as(text) -> None:
    t = text.get("1.0", "end-1c")
    save_location = filedialog.asksaveasfilename()
    file1 = open(save_location, 'w+')
    file1.write(t)
    file1.close()