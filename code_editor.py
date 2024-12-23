import subprocess
from tkinter import *
from tkinter import filedialog, messagebox
import os

# Main Window Config
root = Tk()
root.title("Python Code Editor")
root.geometry('900x800')
root.resizable(False, False)

# Variables
scripts_list = []  # List to manage open scripts
current_script = None  # Track the currently opened script

# Function to Run Script and Show Output
def run_script():
    if not current_script:
        messagebox.showwarning("No Script", "No script is open to run.")
        return

    # Save current content to a temporary file
    temp_file = "temp_script.py"
    with open(temp_file, "w") as f:
        f.write(text.get(1.0, END))

    # Run the script using subprocess
    try:
        result = subprocess.run(
            ["python", temp_file],
            capture_output=True,
            text=True
        )
        # Display output in the output text area
        output_text.delete(1.0, END)
        output_text.insert(END, result.stdout)
        if result.stderr:
            output_text.insert(END, "\nERROR:\n" + result.stderr)
    except Exception as e:
        output_text.delete(1.0, END)
        output_text.insert(END, f"Error running script: {str(e)}")
    finally:
        if os.path.exists(temp_file):
            os.remove(temp_file)

# Function to Save the Current Script
def save_script():
    global current_script
    if current_script:
        # Overwrite the current script
        with open(current_script, "w") as f:
            f.write(text.get(1.0, END))
        messagebox.showinfo("File Saved", f"File saved to {current_script}")
    else:
        # Save as new script
        filepath = filedialog.asksaveasfilename(defaultextension=".py",
                                                filetypes=[("Python Files", "*.py")])
        if filepath:
            with open(filepath, "w") as f:
                f.write(text.get(1.0, END))
            messagebox.showinfo("File Saved", f"File saved to {filepath}")
            update_scripts_list(filepath)

# Function to Open a Script
def open_script():
    filepath = filedialog.askopenfilename(filetypes=[("Python Files", "*.py")])
    if filepath:
        with open(filepath, "r") as f:
            content = f.read()
        text.delete(1.0, END)
        text.insert(END, content)
        update_scripts_list(filepath)
        global current_script
        current_script = filepath

# Function to Remove a Script
def remove_script():
    global current_script
    selected_index = scripts_listbox.curselection()
    if selected_index:
        selected_file = scripts_list[selected_index[0]]
        scripts_listbox.delete(selected_index)
        scripts_list.remove(selected_file)
        if selected_file == current_script:
            text.delete(1.0, END)  # Clear the editor if the removed file was active
            current_script = None

# Function to Update Scripts List
def update_scripts_list(filepath):
    if filepath not in scripts_list:
        scripts_list.append(filepath)
        scripts_listbox.insert(END, os.path.basename(filepath))

# Function to Display Script When Selected
def on_script_select(event):
    global current_script
    selected_index = scripts_listbox.curselection()
    if selected_index:
        selected_file = scripts_list[selected_index[0]]
        with open(selected_file, "r") as f:
            content = f.read()
        text.delete(1.0, END)
        text.insert(END, content)
        current_script = selected_file

# Configure Main Layout
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# Frames
left_frame = Frame(root, width=200, bg="#0b546f", padx=10, pady=10)
left_frame.grid(row=0, column=0, sticky="ns")

right_frame = Frame(root, bg="white", padx=10, pady=10)
right_frame.grid(row=0, column=1, sticky="nsew")

# Text Editor
text = Text(right_frame, wrap='word', font=("Courier", 12), bg='white', fg='black')
text.pack(expand=True, fill='both', padx=5, pady=5)

# Output Window
output_label = Label(left_frame, text="Output", bg="#0b546f", fg="white")
output_label.pack()
output_text = Text(left_frame, height=10, bg="#07364a", fg="white", wrap='word')
output_text.pack(fill='x', padx=5, pady=5)

# Scripts List
scripts_label = Label(left_frame, text="Scripts", bg="#0b546f", fg="white")
scripts_label.pack()
scripts_listbox = Listbox(left_frame, bg="white", fg="black", height=10)
scripts_listbox.pack(fill='x', padx=5, pady=5)

# Bind Selection Event for Listbox
scripts_listbox.bind("<<ListboxSelect>>", on_script_select)

# Buttons
Button(left_frame, text="Run Script", fg='#07364a', command=run_script).pack(fill='x', pady=5)
Button(left_frame, text="Save Script", fg='#07364a', command=save_script).pack(fill='x', pady=5)
Button(left_frame, text="Open Script", fg='#07364a', command=open_script).pack(fill='x', pady=5)
Button(left_frame, text="Remove Script", fg='#07364a', command=remove_script).pack(fill='x', pady=5)

# Run the Application
root.mainloop()