import os
import pytesseract
import glob
import time
from PIL import Image
from pdf_conversion import txt_to_pdf
from img_preprocessing import img_preprocessing
from docx_conversion import txt_to_docx

#https://realpython.com/creating-modifying-pdf/#creating-pdf-files-with-python-and-reportlab

#Print available OCR language
#print(pytesseract.get_languages(config=''))

txt_start_file = "start.txt"
text_result = ''
path_in = '/workspace/data/input/test_images/'
path_out = '/workspace/data/input/test_images_bw/'
path_config = "/workspace/data/"

#Wait txt file to start
there_is_txt = 0
while(there_is_txt < 1):
	there_is_txt = len(glob.glob(path_config + txt_start_file))
	time.sleep(1)

# Image preproccessing
img_preprocessing(path_in, path_out, 135)
print('PREPROCESSING finished')

# OCR
file_list = sorted(glob.glob(path_out + '*'),key=os.path.getmtime)
idx = 1
for f in file_list:
  ocr = pytesseract.image_to_string(Image.open(f),lang='ita')
  text_result = text_result + '\n' + str(idx) +'-PHOTO:' + f + '\n' + ocr
  idx = idx + 1

print('OCR finished')
#Write txt file
with open("/workspace/data/output/output.txt", "w+") as f:
  print(text_result, file=f)
os.chmod("/workspace/data/output/output.txt",0o777)
print('TXT finished')
# Convert txt -> pdf
txt_to_pdf('/workspace/data/output/output.txt','/workspace/data/output/output.pdf')
print('PDF finished')
txt_to_docx('/workspace/data/output/output.txt','/workspace/data/output/output.docx')
print('DOCX finished')

# Delete txt file 
path = os.path.join(path_config, txt_start_file)  
os.remove(path_config + txt_start_file)

print ("The file has been removed")
