from tkinter import *

from utils.fonts import font_courier, font_helvetica
from utils.file_save import save_as

# Main Window Config
root = Tk()
root.title("Python Text Editor")
root.geometry('900x800')
root.maxsize(900, 800)
root.minsize(600, 500)
root.config(bg='#066686')

# Configure Grid to Scale
root.columnconfigure(0, weight=1) # Left Frame takes some space
root.columnconfigure(1, weight=4) # Right Frame (text editor) scales more
root.rowconfigure(0, weight=1) # Allow vertical scaling

# Left Frame (Controls)
left_frame = Frame(root, bg='#0b546f', padx=10, pady=10)
left_frame.grid(row=0, column=0, sticky="ns")  # Sticky makes it stretch vertically

# Right Frame (Text Editor)
right_frame = Frame(root, bg='#066686', padx=10, pady=10)
right_frame.grid(row=0, column=1, sticky="nsew")  # Expands to fill space

# Text Widget in Right Frame
text = Text(right_frame, wrap='word', font=("Courier", 12), bg='#e0f5fe', fg='#0b546f')
text.pack(expand=True, fill='both', padx=5, pady=5)

# Save Button
save_button = Button(left_frame, text="Save", command=lambda: save_as(text), borderwidth=0)
save_button.pack(pady=10, fill='x')  # Fills horizontally in left frame

# Font Selection Variables
current_font = StringVar(value="Courier")  # Default font
font_choice = StringVar(value="Courier")  # Tracks the selected font

# Create the Menubutton
font_menu = Menubutton(
    left_frame,
    textvariable=current_font,  # Show the current font
    relief=RAISED,
    bg='#0b546f',
    fg='#066686',
    borderwidth=0,
    width=10  # Fixed width to prevent resizing
)
font_menu.menu = Menu(font_menu, tearoff=0)
font_menu["menu"] = font_menu.menu

# Add Checkbuttons for Fonts (Linked to `font_choice`)
font_menu.menu.add_radiobutton(
    label="Courier",
    variable=font_choice,
    value="Courier",
    command=font_courier(text, current_font, font_choice)
)
font_menu.menu.add_radiobutton(
    label="Helvetica",
    variable=font_choice,
    value="Helvetica",
    command=font_helvetica(text, current_font, font_choice)
)

font_menu.pack(pady=10, fill='x')

# Additional Controls Placeholder
Label(left_frame, text="File Manager", bg='#0b546f', fg='white').pack(pady=10, fill='x')
Button(left_frame, text="Open File", borderwidth=0, command=lambda: print("Open File")).pack(pady=5, fill='x')
Button(left_frame, text="New File", borderwidth=0, command=lambda: print("New File")).pack(pady=5, fill='x')

root.mainloop()