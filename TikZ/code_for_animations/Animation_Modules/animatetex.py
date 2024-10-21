"""
File name: animatetex.py
Author: Jasper Nice
Purpose:
    This module simplifies the creation of LaTeX animations by 
    condensing the code required to:
        1. Create a blank PDF.
        2. Run and append the output of a LaTeX file to this PDF for
           each iteration of the animation.
        3. Remove the initial blank page after the loop terminates.
    The core functionalities are encapsulated in three versatile 
    functions:
        1. animatetex.before_loop()
        2. animatetex.during_loop()
        3. animatetex.after_loop()
Credit: 
    I acknowledge the use of AI, which assisted me in finding various
    syntaxes to achieve this goal. However, I did substantial work on 
    the earlier iterations myself.
"""

import subprocess
import shutil
import os
from pypdf import PdfReader, PdfWriter
from reportlab.pdfgen import canvas
import sys

def before_loop():
    """
    Purpose:
        Executes tasks required before running LaTeX. This includes 
        setting path destinations and creating an initial blank PDF.
    
    Parameters: None
    Returns: None
    """
    file_names()
    make_merged()
    make_temp()
    append_pdfs(merged_pdf, pdf_file, temp_pdf)
    rename_pdf()

def file_names():
    """
    Purpose:
        Sets the file names for the entire operation.
    
    Parameters: None
    Returns: None
    """
    global TeX_file, pdf_file, output_directory, merged_temp, merged_pdf
    output_directory = os.path.abspath(os.path.join(\
        os.path.dirname(__file__), '..'))
    TeX_file = os.path.join(output_directory, "TeX_file.tex")
    pdf_file = os.path.join(output_directory, "TeX_file.pdf")
    merged_temp = 'TeX_file_merged_output_temp.pdf'
    merged_pdf = 'TeX_file_merged_output.pdf'

def make_merged():
    """
    Purpose:
        Initializes the path for the merged output PDF.
    
    Parameters: None
    Returns: None
    """
    global merged_pdf
    merged_pdf = os.path.join(output_directory, merged_pdf)

def make_temp():
    """
    Purpose:
        Creates a temporary PDF file, which serves as a placeholder for 
        each iteration's output before merging it into the final PDF.
    
    Parameters: None
    Returns: None
    """
    global temp_pdf
    temp_pdf = os.path.join(output_directory, merged_temp)
    
    c = canvas.Canvas(temp_pdf)
    c.save()  # Creates an empty PDF for future appending.

def during_loop():
    """
    Purpose:
        Compiles the LaTeX file and appends its output to the merged
        PDF. This function generates a new temporary PDF for each 
        iteration, allowing the accumulated outputs to be merged in 
        the final document.
    
    Parameters: None
    Returns: None
    """
    # Runs the LaTeX compilation.
    compile_tex_to_pdf()
    # Prepares a new temporary PDF for the current iteration's output.
    make_temp() 
    # Merges the current output with the accumulated PDF.
    append_pdfs(merged_pdf, pdf_file, temp_pdf) 
    # Updates the merged PDF name to reflect the latest changes.
    rename_pdf()  

def compile_tex_to_pdf():
    """
    Purpose:
        Compiles the LaTeX file using LuaLaTeX, generating a PDF 
        output that is ready to be merged with the existing PDFs.
    
    Parameters: None
    Returns: None
    """
    subprocess.run(['lualatex', '-output-directory', output_directory,\
                     TeX_file])

def append_pdfs(pdf1, pdf2, output_pdf):
    """
    Purpose:
        Combines two PDF files into a single output PDF. 
        This function appends the output PDF generated from the LaTeX 
        compilation (`pdf2`) to the accumulated output PDF (`pdf1`), 
        effectively consolidating all animation frames into one final 
        document.

    Parameters:
        pdf1 (str): The path of the accumulated output PDF, which 
        contains all previously merged content.
        pdf2 (str): The path of the newly generated PDF from the 
        LaTeX compilation, representing the latest iteration of the 
        animation.
        output_pdf (str): The path where the merged PDF will be saved, 
        which will include the combined content of both `pdf1` and 
        `pdf2`.

    Returns: None
    """
    # Determine the appropriate Ghostscript command
    if sys.platform.startswith('win'):
        command = 'gswin64c'  # For Windows users
    else:
        command = 'gs'  # For Unix-like systems (Linux, macOS)

    subprocess.run([command, '-dBATCH', '-dNOPAUSE', '-q',\
                     '-sDEVICE=pdfwrite', '-sOutputFile=' + output_pdf,\
                          os.path.abspath(pdf1), os.path.abspath(pdf2)])

def rename_pdf():
    """
    Purpose:
        Renames the temporary PDF to the final merged output PDF, 
        ensuring that the most recent changes are preserved.
    
    Parameters: None
    Returns: None
    """
    shutil.move(temp_pdf, merged_pdf)

def after_loop():
    """
    Purpose:
        Removes the first blank page from the final merged PDF and 
        cleans up temporary LaTeX files that are no longer needed.
    
    Parameters: None
    Returns: None
    """
    remove_first_page(merged_pdf, os.path.join(output_directory,\
                                                'final_output.pdf'))
    clean_up()

def remove_first_page(input_pdf, output_pdf):
    """
    Purpose:
        Removes the first page from the input PDF and saves the result
        as a new PDF, typically to eliminate the initial blank page 
        created during the process.
    
    Parameters:
        input_pdf (str): The path of the input PDF from which to remove
        the first page.
        output_pdf (str): The path where the output PDF will be saved.
    
    Returns: None
    """
    pdf_reader = PdfReader(input_pdf)
    pdf_writer = PdfWriter()
    # Skips the first page.
    for page_num in range(1, len(pdf_reader.pages)):
        pdf_writer.add_page(pdf_reader.pages[page_num])
    with open(output_pdf, 'wb') as output_file:
        pdf_writer.write(output_file)

def clean_up():
    """
    Purpose:
        Removes all temporary LaTeX files generated during the process,
        ensuring that no unnecessary files remain.
    
    Parameters: None
    Returns: None
    """
    for ext in ['tex', 'pdf', 'aux', 'log', 'nav', 'out', 'snm', 'toc']:
        try:
            os.remove(os.path.join(output_directory, f'TeX_file.{ext}'))
        except FileNotFoundError:
            pass
    try:
        os.remove(merged_pdf)
    except FileNotFoundError:
        pass
