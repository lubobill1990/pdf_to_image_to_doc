# write all png files under res/ to a docx file

import os
import glob
from docx import Document
from docx.shared import Mm, Inches

import sys

# Create a new Document
doc = Document()

# Directory containing the PNG files
dir_path = 'res/'

all_png_files = glob.glob('res/*.png')
# sort the png files by name
all_png_files.sort(key=lambda f: int(''.join(filter(str.isdigit, f))))

section = doc.sections[0]
# set the margin of the document to 0
section.left_margin = Inches(0.13)
section.right_margin = Inches(0.13)
section.top_margin = Inches(0)
section.bottom_margin = Inches(0.0)
# get the page width
width = section.page_width
# Traverse the directory
for filename in all_png_files:
    # Add each PNG file to the Document
    doc.add_picture(filename, width=Inches(8.2))

# Save the Document
doc.save('output.docx')
