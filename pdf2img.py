import os
from tqdm import tqdm
from pdf2image import convert_from_path
import pypdfium2 as pdfium

# images = convert_from_path("111000 Emails  List.pdf")
# for i in tqdm(len(images)):
#     images[i].save('pages/page'+str(i+1)+".jpg", "JPEG")

filepath = "111000 Emails  List.pdf"
pdf = pdfium.PdfDocument(filepath)

for i in tqdm(range(len(pdf))):
    page = pdf[i]
    pil_image = page.render(scale=1).to_pil()
    pil_image.save("pages/page_"+str(i+1)+".jpg")