#=================
# make sure to install:
# import pymupdf
# import pymupdf_fonts
# #-----------------
# then import:
import fitz  # PyMuPDF


finished_extraction = False

#+++++++++++++++++++++++++++++++++++++++++++++++++++++
def extract_everything(pdf_path,target_name,output_dir):
    global finished_extraction
    is_extraction_complete = finished_extraction

    #########################
    # 1.Open the PDF
    doc = fitz.open(pdf_path)
    #      X--------X       #
    if is_extraction_complete:
        doc.close() #making sure it's closed
        return True #to make letters_generated = True and ending the process :)
    #########################
    old_name = "[name]"
    new_name = target_name

    # ________________________________________
    # Iterate through pages
    for page in doc:
        #-------------------------------#perform modifications
        ####
        # ---------------------------------------------marking old name
        text_instances = page.search_for(old_name)
        # ---------------------------------------------marking old name
        for area in text_instances:
            # mark area for redaction (since we can't remove a text directly)
            page.add_redact_annot(area, fill=None)
        # Apply redactions removal to remove it <#---------------removing old name
        page.apply_redactions(0)

        #----------------------------------------------ADDING THE NEW NAME
        for inst in text_instances:
            #    ------    #
            page.insert_text(
                inst.bl, #<---------you can change this bottom-left position
                new_name,
                fontname = "tibo",
                fontsize=18,
                color=(0, 0, 0) #black
            )
    #if you are a dev, here are other names for fonts in "fitz" PyMuPDF-package:
    #fonts:
    #Helvetica
    # helv - normal
    # heit - italic
    # hebo - bold
    # hebi - bold italic
    #
    #Courier
    # cour - normal
    # coit - italic
    # cobo - bold
    # cobi - bold italic
    #
    #Times-Roman
    # tiro - normal
    # tiit - italic
    # tibo - bold
    # tibi - bold italic

    #directions:
    # rect.tl(top - left),
    # rect.tr(top - right),
    # rect.bl(bottom - left),
    # rect.br(bottom - right).

    # @@@@@@@@@@@@@
    doc.save(output_dir) #saving the new doc!!!! :)
    # DEBUG
    return print(f"-->added{new_name} and made it go to {output_dir}*************")
    #@@@@@@@@@@@@@
