from tkinter import *
from tkinter import ttk, colorchooser , messagebox

hex_colour = '#FFFFFF'

def rgb_to_hex(rgb):
    r, g, b = rgb
    return f'#{r:02x}{g:02x}{b:02x}'

def choose_color():
    color = colorchooser.askcolor()[1]  
    if color:
        hex_colour = color
        label_color.config(background=hex_colour)  
        label_hex.config(text=hex_colour)  

def convert():
    r = int(entry_r.get())
    g = int(entry_g.get())
    b = int(entry_b.get())
    rgb_color = (r, g, b)
    hex_color = rgb_to_hex(rgb_color)
    label_hex.config(text=hex_color)
    label_color.config(background=hex_color)  

def focus_next_entry(event):
    current_widget = event.widget
    if current_widget == entry_b:
        button_convert.invoke()
    else:
        current_widget.tk_focusNext().focus()
    return "break"

def copy_text(event):
    root.clipboard_clear()
    root.clipboard_append(label_hex.cget("text"))
    messagebox.showinfo('Copy' , 'copied successfully')

root = Tk()
root.title("RGB to Hex Converter")
root.geometry('460x140+800+100')
root.iconbitmap('D://rgb.ico')
root.resizable(False , False)

style = ttk.Style()
style.configure("TButton", padding=6)

label_r = ttk.Label(root, text="R:")
label_r.grid(row=0, column=0, pady=5)
entry_r = ttk.Entry(root)
entry_r.grid(row=0, column=1)

label_g = ttk.Label(root, text="G:")
label_g.grid(row=0, column=2, pady=5)
entry_g = ttk.Entry(root)
entry_g.grid(row=0, column=3)

label_b = ttk.Label(root, text="B:")
label_b.grid(row=0, column=4, pady=5)
entry_b = ttk.Entry(root)
entry_b.grid(row=0, column=5)

button_convert = ttk.Button(root, text="Convert", command=convert)
button_convert.grid(row=1, column=0, columnspan=8, pady=10)

entry_r.bind("<Return>" , focus_next_entry)
entry_g.bind("<Return>", focus_next_entry)
entry_b.bind("<Return>", focus_next_entry)

label_color = ttk.Label(root, text="", background=hex_colour, width=3 , borderwidth = 1, relief='solid')
label_color.grid(row=3, column=0, columnspan=8)
label_color.bind("<Button-1>", lambda event: choose_color())

label_hex = Label(root, text=hex_colour, cursor="hand2")
label_hex.grid(row=2, column=0 , columnspan=8)
label_hex.bind("<Button-1>", copy_text)

root.mainloop()