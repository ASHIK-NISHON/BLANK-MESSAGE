import tkinter as tk
from tkinter import ttk, messagebox
import pyperclip

def generate_enters():
    try:
        # Get number of lines from entry
        num_lines = int(lines_entry.get())
        if num_lines <= 0:
            messagebox.showerror("Error", "Please enter a positive number!")
            return
            
        # Generate Braille Pattern Blank characters
        blanks = "\u2800\n" * num_lines  # U+2800 is the Braille Pattern Blank
        
        # Display in text widget
        text_area.delete(1.0, tk.END)
        text_area.insert(1.0, blanks)
        
        # Enable copy button
        copy_button.config(state=tk.NORMAL)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number!")

def copy_to_clipboard():
    try:
        # Get text from text area
        text = text_area.get(1.0, tk.END)
        
        # Count the number of lines
        line_count = text.count('\n')
        
        # Copy to clipboard
        pyperclip.copy(text)
        
        # Show success message
        messagebox.showinfo("Success", f"{line_count} Braille blanks have been copied to clipboard!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to copy to clipboard: {str(e)}")

def clear_text():
    text_area.delete(1.0, tk.END)
    copy_button.config(state=tk.DISABLED)

# Create main window
root = tk.Tk()
root.title("Braille Blanks Generator")
root.geometry("600x400")
root.resizable(True, True)

# Create main frame
main_frame = ttk.Frame(root, padding="10")
main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Configure grid weights
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
main_frame.columnconfigure(1, weight=1)
main_frame.rowconfigure(1, weight=1)

# Title
title_label = ttk.Label(main_frame, text="Braille Blanks Generator", font=("Arial", 16, "bold"))
title_label.grid(row=0, column=0, columnspan=3, pady=(0, 10))

# Buttons frame
buttons_frame = ttk.Frame(main_frame)
buttons_frame.grid(row=1, column=0, sticky=(tk.W, tk.N, tk.S), padx=(0, 10))

# Lines entry frame
entry_frame = ttk.Frame(buttons_frame)
entry_frame.grid(row=0, column=0, pady=(0, 10), sticky=(tk.W, tk.E))

# Number of lines label and entry
lines_label = ttk.Label(entry_frame, text="Number of lines:")
lines_label.grid(row=0, column=0, padx=(0, 5))

lines_entry = ttk.Entry(entry_frame, width=10)
lines_entry.grid(row=0, column=1)
lines_entry.insert(0, "1000")  # Default value

# Generate button
generate_button = ttk.Button(buttons_frame, text="Generate Braille Blanks", command=generate_enters)
generate_button.grid(row=1, column=0, pady=(0, 10), sticky=(tk.W, tk.E))

# Copy button
copy_button = ttk.Button(buttons_frame, text="Copy to Clipboard", command=copy_to_clipboard, state=tk.DISABLED)
copy_button.grid(row=2, column=0, pady=(0, 10), sticky=(tk.W, tk.E))

# Clear button
clear_button = ttk.Button(buttons_frame, text="Clear", command=clear_text)
clear_button.grid(row=3, column=0, sticky=(tk.W, tk.E))

# Text area with scrollbar
text_frame = ttk.Frame(main_frame)
text_frame.grid(row=1, column=1, sticky=(tk.W, tk.E, tk.N, tk.S))

text_area = tk.Text(text_frame, wrap=tk.NONE, width=50, height=20)
text_scrollbar_y = ttk.Scrollbar(text_frame, orient=tk.VERTICAL, command=text_area.yview)
text_scrollbar_x = ttk.Scrollbar(text_frame, orient=tk.HORIZONTAL, command=text_area.xview)
text_area.configure(yscrollcommand=text_scrollbar_y.set, xscrollcommand=text_scrollbar_x.set)

text_area.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
text_scrollbar_y.grid(row=0, column=1, sticky=(tk.N, tk.S))
text_scrollbar_x.grid(row=1, column=0, sticky=(tk.W, tk.E))

text_frame.columnconfigure(0, weight=1)
text_frame.rowconfigure(0, weight=1)

# Instructions
instructions = ttk.Label(main_frame, text="Enter the number of lines desired, click 'Generate Braille Blanks' to create invisible spaces, then 'Copy to Clipboard' to copy them.", 
                         wraplength=400, foreground="gray")
instructions.grid(row=2, column=0, columnspan=2, pady=(10, 0))

# Start the GUI
root.mainloop()