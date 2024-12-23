# Python-TextEditor
A simple Python Code Editor built with Tkinter that allows users to write, save, and run Python scripts. 

The application features a text editor, script management, and an output window for script results.

## Features
1. **Text Editor:** A basic editor for writing Python scripts with line wrapping and ```Courier``` font.
2. **Run Python Scripts:** Executes the current script and displays the output or errors in a dedicated output window.
3. **Script Management:**
- Open multiple Python files and manage them via a side panel.
- Save changes directly to existing files or create new ones.
- Remove scripts from the manager and clear the editor.
4. **Output Window:** Displays script outputs, including standard output and error messages.

## Prerequisites
- Python 3.12.1
- Tkinter (usually included with Python)

## Usage:
### Clone the Repository:
```
git clone https://github.com/finsherwell/Python-TextEditor.git
```

### Run the application:
```
python code_editor.py
```

### Use the GUI to:
- Write Python scripts in the editor.
- Save scripts with ```.py``` extensions.
- Open and switch between multiple scripts.
- Run the currently selected script and view outputs/errors.

### Buttons and Features
- **Run Script:** Executes the script displayed in the text editor.
- **Save Script:** Saves the current script to the existing file or as a new ```.py``` file.
- **Open Script:** Opens a Python file in the text editor and adds it to the script manager.
- **Remove Script:** Removes the selected script from the manager and clears the editor if active.

### Script Management Panel
- Displays the names of all opened scripts.
- Click on a script to load it into the text editor for editing.
- Changes to a script can be saved directly without requiring "Save As."

## File Structure
```code_editor.py:``` Main Python file containing the editor's logic and UI code.

## Limitations
- Does not support syntax highlighting.
- No auto-complete or advanced IDE features.

## Future Enhancements
**Shortcuts:**
I may add the following shortcuts for convenience:
1. Save Script: ```Ctrl+S```
2. Open Script: ```Ctrl+O```
3. Run Script: ```F5```

I am also considering adding:
- Python syntax highlighting using ```Pygments```.
- Debugging capabilities.
- Configuration for editor themes and fonts.
