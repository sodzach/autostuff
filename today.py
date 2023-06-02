import pyperclip
from datetime import date

# Get the current date
current_date = date.today().strftime("%d/%m/%Y")

# Copy the current date to the clipboard
pyperclip.copy(current_date)

# Print a confirmation message
print("Current date copied to clipboard: " + current_date)


# import datetime
# from tkinter import *
#
# # Get the current date
# current_date = datetime.date.today().strftime("%d/%m/%Y")
#
# r = Tk()
# r.clipboard_clear()
# r.clipboard_append(current_date)
# r.after(100, r.destroy)
# r.mainloop()