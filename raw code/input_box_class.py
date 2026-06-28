import customtkinter
from tkinter import messagebox

numbers_list = [0,1,2,3,4,5,6,7,8,9]
run_it = False

def open_input_dialog():
    global run_it
    # 2. Pass 'root' as the master to stop the flashing window glitch
    dialog = customtkinter.CTkInputDialog(
        text="14 is recommended, but depending on your template, you can increase it",
        title="Please enter your text size here:",
    )
    #_____________________________Getting input:
    user_input = dialog.get_input()
    ##########
    run_it = False
    ##########
    for char in list(user_input):
        if int(char) not in numbers_list:
            run_it = False
            messagebox.showinfo(title="No letters allowed!", message="Please write numbers only")
    #----
    if user_input.strip() == "":
        messagebox.showinfo(title="No Number Entered", message="Please write a fitting number")
        run_it = False
    #----
    else:
        run_it =True
    #___________________________
    if run_it:
        print(user_input)
        return int(user_input)
    else:
        run_it = False
        #----
        print(run_it)
        return run_it

# DEBUG:
# open_input_dialog()