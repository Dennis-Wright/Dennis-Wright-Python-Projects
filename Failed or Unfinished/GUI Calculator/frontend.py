import tkinter as tk
import backend
import logging

def initiate_tk():
    logging.info("Frontend.py - Initiating gui.")
    try:
        # Create window
        parent = tk.Tk()
        parent.title("GUI Calculator - By Dennis Wright")
        parent.geometry("315x510")
        parent.minsize(315, 510)

        # Configure grid resizing
        for col in range(4):
            parent.grid_columnconfigure(col, weight=1)
        for row in range(6):
            parent.grid_rowconfigure(row, weight=1)

        # Create variable storing current value to display
        global display 
        display = tk.StringVar()
        display.set("0")

        # Create display label
        display_label = tk.Label(
            parent,
            textvariable=display,
            font=("Arial", 24),
            anchor="w",
            bg="lightgray",
            padx=5
        )
        display_label.grid(row=0, column=0, columnspan=4, sticky="nsew")

        # Button layout
        button_layout = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
        ]

        # Create buttons
        for (text, row, column) in button_layout:
            button = tk.Button(
                parent,
                text=text,
                font=("Arial", 18),
                command=lambda t=text: update_display(t) if t != "=" else calculate_result(display)
            )
            button.grid(row=row, column=column, sticky="nsew")

        # Create clear button
        clear_button = tk.Button(
            parent,
            text="C",
            font=("Arial", 18),
            command=lambda: display.set("0")
        )
        clear_button.grid(row=5, column=0, columnspan=4, sticky="nsew")

        parent.bind('<KeyPress>', onKeyPress)

        logging.info("Frontend.py - GUI Initiated.")
        parent.mainloop()
    except Exception as e:
        logging.error(f"Frontend.py - Error initiating gui. '{e}'")
        raise SystemExit(1)
# End function

def onKeyPress(event):
    characters = ["1","2","3","4","5","6","7","8","9","0","+","-","*","/"]

    # Map keys that require Shift or special keys
    keysym_map = {
        "plus": "+",
        "minus": "-",
        "asterisk": "*",
        "slash": "/",
        "equal": "=",
        "Return": "=",      # Enter key triggers calculation
        "BackSpace": "BACK" # Backspace key
    }

    char = keysym_map.get(event.keysym, event.char)

    if char in characters:
        update_display(char)
    elif char == "=":
        calculate_result(display)
    elif char == "BACK":
        current = display.get()
        display.set(current[:-1])
    else:
        if event.keysym not in ["Shift_L", "Shift_R", "Control_L", "Control_R", "Alt_L", "Alt_R"]:
            display.set("Error. Invalid Input")
            logging.error(f"Frontend.py - User entered invalid key. {event.keysym} / {event.char}")
# End function

def update_display(value):
    try:
        logging.info("Frontend.py - Updating Display")
        current_text = display.get()
        if current_text == "0":
            display.set(value)
        else:
            display.set(current_text + value)
    except Exception as e:
        logging.error(f"Frontend.py - Error Updating Display '{e}'")
# End function

def calculate_result(t):
    try:
        display.set(backend.main(display.get()))
        logging.info("Frontend.py - Result Calculated")
    except Exception as e:
        display.set("Error")
        logging.error(f"Frontend.py - Error in calculation. {e}")
# End function
