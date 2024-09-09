import tkinter as tk

# Dictionary for text replacement
replacement_dict = {
    'a': '🅰', 'b': '🅱', 'c': '🅲', 'd': '🅳', 'e': '🅴', 'f': '🅵', 'g': '🅶',
    'h': '🅷', 'i': '🅸', 'j': '🅹', 'k': '🅺', 'l': '🅻', 'm': '🅼', 'n': '🅽',
    'o': '🅾', 'p': '🅿', 'q': '🆀', 'r': '🆁', 's': '🆂', 't': '🆃', 'u': '🆄',
    'v': '🆅', 'w': '🆆', 'x': '🆇', 'y': '🆈', 'z': '🆉',
    ' ': ' ',  # Include space for handling spaces
    '0': '⓪', '1': '⓵', '2': '⓶', '3': '⓷', '4': '⓸', '5': '⓹', '6': '⓺', '7': '⓻', '8': '⓼', '9': '⓽',
    '!': '❗', '@': 'Ⓐ', '#': '＃', '$': '＄', '%': '％', '^': '＾' 
}

def on_key_press(event):
    # Get the typed character
    char = event.char.lower()

    # If the character is in the dictionary, replace it
    if char in replacement_dict:
        replaced_char = replacement_dict[char]
        output_text.insert(tk.END, replaced_char)

def clear_output():
    # Clear the output text area
    output_text.delete("1.0", tk.END)
    # Clear the input text area
    input_text.delete("1.0", tk.END)

# Create the main window
window = tk.Tk()
window.title("Text Converter")

# Create input and output text areas
input_text = tk.Text(window, height=5, width=30)
input_text.pack()

output_text = tk.Text(window, height=5, width=30)
output_text.pack()

# Create a clear button
clear_button = tk.Button(window, text="Clear", command=clear_output)
clear_button.pack()

# Bind the key press event to the input text area
input_text.bind("<KeyPress>", on_key_press)

# Start the GUI event loop
window.mainloop()