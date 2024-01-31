
import os
import sys
import re
import glob

# for each pdf file under this directory
for pdf in glob.glob('*.pdf'):
    print(pdf)
    # get the file name without extension
    name = os.path.splitext(pdf)[0]
    # get the number at the beginning of the file name
    num = re.search(r'^\d+', name).group()
    # format the number to 3 digits
    num = num.zfill(3)
    print(num)
    # call pdftoppm -png -cropbox pdf_file_name output_file_name
    os.system('pdftoppm -png -cropbox "{}" "res/{}"'.format(pdf, num))
