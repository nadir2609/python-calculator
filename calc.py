import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("300x400")
root.resizable(False, False)

# Entry to display input/output
entry = tk.Entry(root, font=("Arial", 24), borderwidth=2, relief="solid", justify="right")
entry.pack(fill="both", ipadx=8, ipady=15, padx=10, pady=10)

# Add a frame for buttons
btn_frame = tk.Frame(root)
btn_frame.pack()

# Button layout
buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('0', '.', 'C', '+'),
    ('=',)
]

# Store expression
expression = ""

# Button click logic
def on_click(symbol):
    global expression
    if symbol == 'C':
        expression = ""
    elif symbol == '=':
        try:
            expression = str(eval(expression))
        except:
            expression = "Error"
    else:
        expression += symbol
    entry.delete(0, tk.END)
    entry.insert(0, expression)

# Create and place buttons
for row in buttons:
    row_frame = tk.Frame(btn_frame)
    row_frame.pack(expand=True, fill='both')
    for btn in row:
        button = tk.Button(
            row_frame, text=btn, font=("Arial", 18),
            padx=10, pady=10,
            command=lambda b=btn: on_click(b)
        )
        button.pack(side="left", expand=True, fill='both')

# Start GUI loop
root.mainloop()
