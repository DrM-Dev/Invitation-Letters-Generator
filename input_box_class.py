import customtkinter
from tkinter import messagebox


def open_input_dialog():
    # Create and display the input dialog window

    # 2. Pass 'root' as the master to stop the flashing window glitch
    dialog = customtkinter.CTkInputDialog(
        text="Please enter your text here:",
        title="Input Required",
    )
    #_____________________________
    # dialog.iconbitmap("images/saved_cake_bitmap.ico")

    #_____________________________Getting input:
    user_input = dialog.get_input()
    ##########
    # Handle the user's action
    if user_input is not None:
        if user_input.strip() == "":
            messagebox.showinfo(title="No Name Entered", message="Please write a birthday date name to remove!")
            return ""
        else:
            messagebox.showinfo(title="Target Acquired", message=f"Birthday entry [{user_input}] will be deleted!")
            return user_input
    else:
        messagebox.showinfo(title="Deletion Canceled", message="Nothing was deleted, retuning to note book browser :)")
        return ""

open_input_dialog()