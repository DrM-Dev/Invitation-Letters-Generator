#Invite Letters 3.0   by    Dr.M-Dev
#========================imports
import template_name_merger
#+++++

#=================
from tkinter import *
#=================
import sys
import os
#=================
from pypdf import *
from fpdf import *

################## CONS:
WHITE = "#ffffff"
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
font_n = "Courier"

################## globals
finish_step1 = False
# Defaults
names_list = []
#
names_set_up = False
#
font_name = "Times New Roman" #font used in ------> template letter.pdf





print('''                                                                                                                                                  
                                                              ...::::.      ...::::::::    :.      .:.   
  5@@@@@@@@B!    &@@@@@@@&G:        ^G&@@@&P#@@@@B~          J@@@@@@@@@G.   #@@@@@@@@@@   .@@B    7@@?   
  G@@~::::J@@!   @@#     B@@.      :@@G::~&@@!::Y@@~         J@@~    ^@@B   #@@.           !@@J  .@@B    
  G@@     .@@Y   @@@    5&@#       ~@@!   B@&   :@@?         J@@:     &@#   #@@BBBBBBB      P@@: #@@.    
  7BP     .@@J   PBGGGGGB@@B       :BB^   B@&   :@@?         ~GP.     &@#   JGPYYYYYYY       &@# @@!     
  Y&&^....?@@7   #&P     J@@:  ##  ^&&~   B@&   ^@@?         ?@@7:  :7@@P   Y@& ......       ^@@@@P      
  P@@@@@@@@&?    &@B     ?@@:  ##  ~@@!   B@&   :@@?         ?@@@@@@@@#J    J&@@@@@@@@?       ?@@B  


                                                             !J!:                                                                
                                                              ^G@@&P7:                                                           
                                         .~7YGB#&&&&&&&#BG5?~:  .Y@@@@&G^                                                        
                                    :?P&@@@@@@@@@@@@@@@@@@@@@@@&G?J@@@@@&                                                        
                                .!G@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@P   ...                                                 
                              ~B@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@BG&&@@@@                                              
                            ?&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&                                             
                          7@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&#GYP#&J                                            
                        .B@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@!                                                
                       :&@@@@@@@@@@@@@@@@J7@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@P                                               
                      .@@@@@@@@@@@@@@@@#:  ^&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@G                                              
                      #@@@@@@@@@@@@@@&7      P@@@@@@@@@@@@@B&@@@@@@@&@@#&@@@@@@@@@@J                                             
                     !@@@@@@@@@@@@@&?         ^#@@@@&&@@@@@@#PPGB##? B@5#@#@@@@@@@@@:                                            
                     B@@@@@@@@@@@G~             ^B@@@&GG#@@@@@@@#~   .&#J@Y&@@@@@@@@G                                            
                     @@@@@@@@@@~                  .?#@@@&BGPGBBJ      .#5G&J@@@@@@@@@.                                           
                   .@@@@@@@@@7      !PB##B4^        .^JG#&&P:  ^4B###P4?!~!?@@@@@@@@^                                           
                   .@@@@@@@@#      !4~.. .~4^                 ~4~....~4^    #@@@@@@@^   .~                                      
               ~BJ :@@@@@@@@BJYYYYYYJJJJYJJJJJJJ?!.     .!?JYYYJJYYYJJJYYYYY&@@@@@@@P7: .G#?.                                   
            .?BG^  &@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@?...5@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@?  .Y#5:                                 
          :5BJ.    @@@@@@@@@&PJJJJJJ????JJJJ5&@@@@@@@@@@@@@@@GYJJ??????JJJJJYB@@@@@@@@@Y     7BB~                               
        !GG~       .YGG@@@@B        ...       G@@@@@@@@@@@@@:     .::.        !@@@@&GP7        ^G#?                             
     .JB5:             &@@@Y      4P..P@G.    7@@@@@@@@@@@@&    ^:^B@@@P.      @@@@~             .J#5.                          
     J@J               &@@@5     G@@4Y&@@&    ?@@@@?::^#@@@&   ~@4^B@@@@#     .@@@@~              ^#&:                          
      .5#J.            &@@@5     ?@@@@@@@P    7@@@@.   ?@@@&   .@@@@@@@@Y     .@@@@~           .J#P:                            
        .?#P:          #@@@G      .JGBBY:     5@@@&    ^@@@@.    ?B&&#P^      :@@@@~         ^PBJ.                              
           ~BB!        7@@@@5.              :P@@@@J     #@@@&!.             .!&@@@&        7BG~                                 
             :5#J.      ?@@@@@@@@@@@@@@@@@@@@@@@@J      .#@@@@@@&&&&&&&@&&@@@@@@@B.     :5BY.                                   
               .J#!      .7G&&@@@@@@@@@@@@@@&&G7.         ^5#&@@@@@@@@@@@@@@@&BJ:       7!                                      


 ''')

print("******** WELCOME TO Invite Letters 3.0    -   By: Dr.m DEV *********")

#==========================================================================================================
#==========================================================================================================
#==========================================================================================================
#==========================================================================================================
################## SETUP:
window = Tk()
window.minsize(700,700)
window.maxsize(705,705)
window.title("Invite Letters Gen 1.0")
################## Positions:
######titles:
title_x = 140
title_y = 450
#error title placement:
error_title_place_x = title_x - 50
error_title_place_y = title_y
#prompt placement
promx = 50
promy = 490
##################
#####-----------------------------------titles / labels:
how_title = Label(text="", font=(font_n, 14, "bold"))
how_title.place(x=1000, y=1000)
#
note1 = Label(
    text="",
    font=(font_n, 10, "bold"), justify="left")
note1.place(x=1000, y=1000)
#####-----------------------------------buttons:
next_button_0 = Button(text="Next", font=(font_n,10,"bold"), justify="left")
next_button_0.place(x=1000,y=1000)
#
next_button_1 = Button(text="Next", font=(font_n,10,"bold"), justify="left")
next_button_1.place(x=1000,y=1000)
#
next_button_2 = Button(text="Next", font=(font_n, 10, "bold"), justify="left")
next_button_2.place(x=1000,y=1000)
#####-----------------------------------NOTES:
note0 = Label(text="⚠️IMPORTANT NOTE️", font=(font_n, 14, "bold"))
note2 = Label(
    text="2- Make sure to have list of names inside-> [invited names.txt]\n\nor you may encounter an error!\npress Next to proceed",
    font=(font_n, 10, "bold"), justify="left")



##################File_reader/writer
file_writer = PdfWriter() #pypdf-class
# Add a blank A4 page (width and height in points: 1/72 inch)
file_writer.add_blank_page(width=595, height=842)


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++Adding Canvas:
# CANVAS:
ex_canvas = Canvas(width=640,height=420, background="black",highlightthickness=0)
ex_canvas.place(x=30,y=10)
######~~~~~~~~~~~~~~~~~~~~~~~~
#images:
try:
    intro_image = PhotoImage(file="images/intro.png")
    template_image = PhotoImage(file="images/template letter.png")
    template_error_image = PhotoImage(file="images/template letter error.png")
    invited_n_image = PhotoImage(file="images/invited names.png")
    invited_n_image_error = PhotoImage(file="images/invited names error.png")
    final_image = PhotoImage(file="images/final.png")
    #####display:
    display = ex_canvas.create_image(640/2,420/2, image=intro_image)
    #####change display-debug:
    # ex_canvas.itemconfig(display, image=template_image)

######~~~~~~~~~~~~~~~~~~~~~~~~
except FileNotFoundError:
    no_image = Label(text="!!!! NO IMAGE !!!!\n\nthe\"images folder\" was:\nremoved/relocated", fg="white", bg="black", font=(font_n, 20, "bold"), justify="center")
    no_image.place(x=170,y=100)
except TclError:
    no_image = Label(text="!!!! NO IMAGE !!!!\n\nthe\"images folder\" was:\nremoved/relocated", fg="white", bg="black", font=(font_n, 20, "bold"), justify="center")
    no_image.place(x=170,y=100)
except NameError:
    no_image = Label(text="!!!! NO IMAGE !!!!\n\nthe\"images folder\" was:\nremoved/relocated", fg="white", bg="black", font=(font_n, 20, "bold"), justify="center")
    no_image.place(x=170,y=100)










#########################################################################
#####===================================================#####MAIN CODE
def start_code():
    #globals:
    global names_list
    global finish_step1
    global names_set_up
    ######################
    #image:
    ex_canvas.itemconfig(display, image=invited_n_image)
    ######################
    next_button_0.place(x=10000, y=10000)
    #
    how_title.place(x=10000, y=10000)
    note1.place(x=10000, y=10000)
    start_button.place(x=10000, y=10000)
    ######################
    next_button_1.config(text="Next", font=(font_n,10,"bold"), justify="left", command=next_button1)
    next_button_1.place(x=30,y=600)
    ############
    # finish_step1 = False(global)
    names_set_up = False
    ############
    #_________________________________STEP1
    note0.config(text="⚠️IMPORTANT NOTE", font=(font_n, 14, "bold"))
    note0.place(x=error_title_place_x, y=error_title_place_y)
    #
    note2.config(
        text="2- Make sure to have list of names (at least 3) \ninside-> [invited names.txt]\n\nor you may encounter an error!\npress Next to proceed",
        font=(font_n, 10, "bold"), justify="left")
    note2.place(x=promx, y=promy)



#########################################################################
#########################################################################
#error labels:
error_title2 = Label(text="🚫️ ERROR    🚫️\n", font=(font_n, 14, "bold"), justify="center")
error_prompt2 = Label(text="You seem to have deleted/relocated [template letter.pdf] file accidentally!"
                           "\nno worries, we made a new one for you, "
                           "\nyou can use any pdf-template of yours -> just name it \"template letter.pdf\""
                           "\n\nnow go write template for the invite letter in ->[template letter.pdf]\ngo ahead and press -> [Retry] to start over",
                      font=(font_n, 10, "bold"), justify="left")


def no_template_error_feedback():
    # DEBUGGGG
    print("NO TEMPLATE")
    error_title2.place(x=error_title_place_x, y=error_title_place_y)
    error_prompt2.place(x=promx, y=promy)
    # image:
    ex_canvas.itemconfig(display, image=template_error_image)
    ####
    # RETRY?
    next_button_1.place(x=1000, y=1000)  # remove the "next" button
    next_button_2.place(x=1000, y=1000)
    retry_button = Button(text="Retry?", font=(font_n, 10, "bold"), justify="left", command=retry)
    retry_button.place(x=30, y=600)
    ####
    # making a
    pdf_temp = FPDF()
    pdf_temp.add_page()
    pdf_temp.set_font("helvetica", size=12)
    # Writing example file:
    pdf_temp.cell(200, 10, text="Write a template here:")
    pdf_temp.ln(10)  # Move down by 10mm
    pdf_temp.cell(200, 10, text="and make sure to write \"[name]\"")
    pdf_temp.ln(10)
    pdf_temp.cell(200, 10, text="so this template can be used for every name in your [invited names.text]")
    ####
    # Save the file
    pdf_temp.output("template letter.pdf")
    # DEBUG
    print("TEMPLATE CREATED")
    # -------------------------------
    # ---------------old text-creator:
    # with open("template letter.pdf", "w") as invited_names_file:
    #     invited_names_file.write("EXAMPLE:\n\nDear [name]\n\n\n this is an invitation letter for you")


# =================================================================STAGE2
def filtering_names():
    global names_list
    global names_set_up
    ####
    global font_name
    ####
    letters_generated = False
    # ===[FILTER V2]=============================
    filter_n_list = []
    # ----------------
    for name in names_list:
        ####
    # ------------------------
        fixed_name = name.strip()
        ####
        filter_n_list.append(fixed_name)
    # ---------------#DEBUG
    print(filter_n_list)

    # ===[Fetching the letter template]=============================
    ####
    if names_set_up:
        # ------------------------
        error_title2.config(text="🚫️ ERROR    🚫️\n", font=(font_n, 14, "bold"), justify="center")
        error_prompt2.config(text="You seem to have deleted/relocated [template letter.pdf] file accidentally!"
                                   "\nno worries, we made a new one for you, "
                                   "\nyou can use any pdf-template of yours -> just name it \"template letter.pdf\""
                                   "\n\nnow go write template for the invite letter in ->[template letter.pdf]\ngo ahead and press -> [Retry] to start over",
                                    font=(font_n, 10, "bold"), justify="left")

        #____________________________
        try:
            pdf_path = r"template letter.pdf"
            #+++++++++++++++++++++++++
            #+++++++++++++++++++++++++
            for name in filter_n_list:
                output_directory = fr'output\invite_to_{name}.pdf'
                #----#
                template_name_merger.extract_everything(pdf_path=pdf_path,
                                                        target_name=name,
                                                        output_dir=output_directory,
                )
                #----x----x----x----x----x----x----x----x----x----x
            template_name_merger.finished_extraction = True
            ##################
            #letters_generated = True (that makes it true) and closes the doc file

            #===============ERRORS:
            error_title2.place(x=1000, y=1000)
            error_prompt2.place(x=1000, y=1000)
            ####
            letters_generated = True
            #|# debug
            #V#
            print(letters_generated)

        #########################
        except FileNotFoundError:
            no_template_error_feedback()



    #############################
    if letters_generated:
        final_resalt_title = Label(text="✅The letters have been generated!", font=(font_n, 14, "bold"))
        final_resalt_title.place(x=title_x,y=title_y)
        #final image:
        ex_canvas.itemconfig(display, image=final_image)
        # ---- # ---- # ---- #
        final_resalt = Label(
            text="you can find them in    -->   📁[output folder] :)",font=(font_n, 10, "bold"), justify="center")
        final_resalt.place(x=promx+85, y=promy)
        #
        # CODE-ENDS-HERE
        # EXIT? (not retry)
        #################
        exit_button = Button(text="Retry?", font=(font_n, 10, "bold"), justify="left", command=retry)
        exit_button.place(x=30, y=600)
        next_button_1.place(x=1000,y=1000)

#########################################################################
#RETRY:
def retry():
    """Restarts the current Python script."""
    python = sys.executable
    os.execl(python, python, *sys.argv)


# =================================================================STAGE1
def next_button1():
    # globals:
    global names_list
    global finish_step1
    #----
    global names_set_up
    #----
    global next_button_1
    #----
    global error_title_place_x
    global error_title_place_y
    ######################
    finish_step1 =True
    ######################
    note0.place(x=1000,y=1000)
    note2.place(x=1000,y=1000)
    # _________________________________
    if not names_set_up and finish_step1:
        next_button_1.place(x=1000, y=1000)
        ############################################
        ############################################
        error_title = Label(text="🚫️ ERROR    🚫️\n",
                            font=(font_n, 14, "bold"), justify="center")
        #----------------------
        warning_1 = Label(text="The file seems to be empty!!\n\nwrite a list of people in (at least 3)->\"invited names.txt\" file\n\n press -> [Retry] to start over",
                          font=(font_n, 10, "bold"), justify="left")
        #----------------------
        file_not_found = Label(
            text="You seem to have deleted/relocated the [invited names.txt] file accidentally!"
                 "\nno worries, we made a new one for you"
                 "\n\ngo write a list of people to invite in"
                 "\n->[invited names.txt] (at least3)", font=(font_n, 10, "bold"), justify="left")
        # CHECK:
        #
        ############################################
        ############################################
        try:
            f = open("invited names.txt", "r")  # opened_file
            names_list = f.readlines()
            ####
            if len(names_list) >= 3:
                print(f"list of invited names{names_list}")
                names_set_up = True
                filtering_names()
                # ----
                error_title.place(x=10000, y=10000)
                warning_1.place(x=10000, y=10000)
                file_not_found.place(x=10000, y=10000)
            else:
                error_title.place(x=error_title_place_x,y=error_title_place_y)
                warning_1.place(x=promx, y=promy)
                file_not_found.place(x=10000, y=10000)
                #DEBUG
                print("NO NAMES")
                #################
                #RETRY?
                retry_button = Button(text="Retry?", font=(font_n, 10, "bold"), justify="left", command=retry)
                retry_button.place(x=30, y=600)
            # ----
            # -------------------------------
            # ----
            if names_set_up and finish_step1:
                # STAGE2
                # note3 = Label
                #
                next_button_2.config(text="Next", font=(font_n, 10, "bold"), justify="left", command=next_button1)
                next_button_2.place(x=30, y=600)
        # -------------------------------------------
        except FileNotFoundError:
            error_title.place(x=error_title_place_x,y=error_title_place_y)
            warning_1.place(x=10000, y=10000)
            file_not_found.place(x=promx, y=promy)
            #
            ex_canvas.itemconfig(display, image=invited_n_image_error)
            #
            with open("invited names.txt", "w") as invited_names_file:
                invited_names_file.write("person1\nperson2\nperson3")
            #
            #this window will be closed in 10sec so you can
            # window.destroy()  # <!> end-code
            #
            # DEBUG
            print("NO FILE")
            print("END")
            #################
            # RETRY?
            retry_button = Button(text="Retry?", font=(font_n, 10, "bold"), justify="left", command=retry)
            retry_button.place(x=30, y=600)



#####===================================================#####start-GUI
#_________________________________NOTE1
def note_1_display():
    ######################
    ex_canvas.itemconfig(display, image=template_image)
    ######################
    how_title.config(text="📓How to use - invite letters generator", font=(font_n,14,"bold"))
    how_title.place(x=title_x,y=title_y)
    #
    note1.config(text="1- Write a template invite letter to the people you want to invite in\n->[template letter.pdf]\n\n⚠️️make sure to mark the names of people as\n->\"[name]\"(with square brackets)\nor they won't be detected and replaced ", font=(font_n,10,"bold"), justify="left")
    note1.place(x=promx,y=promy)
    #
    #Next BUTTON
    next_button_0.config(text="Next", fg="black", bg=WHITE,font=("font_n",10,"bold"), command=start_code)
    next_button_0.place(x=30, y=600)
    #____________________
    start_button.place(x=1000,y=1000)
    welcome_prompt.place(x=1000,y=1000)
    welcome_title.place(x=1000,y=1000)


#--------------------------------code start:
welcome_title = Label(text="WELCOME TO\nInvite Letters Generator", font=(font_n,14,"bold"), justify="center")
welcome_title.place(x=title_x+80,y=title_y)
#
welcome_prompt = Label(text="Press -> [Next] for how-to use it :) ", font=(font_n,10,"bold"), justify="left")
welcome_prompt.place(x=promx,y=promy+40)
#
#ask to start code
#BUTTON
start_button = Button(text="START?", fg="black", bg=WHITE,font=("font_n",10,"bold"), command=note_1_display)
start_button.place(x=700/2, y=600)
start_button.focus()

################END
window.mainloop()
