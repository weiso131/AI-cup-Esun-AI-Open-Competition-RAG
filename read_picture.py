"""
in Linux

pip install pytesseract
sudo apt update
sudo apt install tesseract-ocr
"""

from PIL import Image
import pytesseract
import pdfplumber
import io
import os

def get_text_from_images_in_pdf(pdf_path):
    extracted_text = []  # This will hold the extracted text from all images in the PDF
    
    # Open the PDF file with pdfplumber
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            # Extract images from the current page
            imgBlobs = []
            images = page.images
            for img in images:
                img_blob = img['stream'].get_data()  # Get the image data as a blob
                imgBlobs.append(img_blob)
            
            # For each image blob, use pytesseract to extract text
            for i in range(len(imgBlobs)):
                imgBlob = imgBlobs[i]
                try:
                    # Convert the image blob into a PIL image
                    im = Image.open(io.BytesIO(imgBlob))
                    # Use pytesseract to extract text from the image
                    

                    text = pytesseract.image_to_string(im, lang='chi_tra')  # You can specify other languages here
                    extracted_text.append(text)  # Append the extracted text to the list
                
                except Exception as e:
                    print(f"Error extracting text from image: {e}, path: {pdf_path}, page: {i}")
                    break
    
    return extracted_text  # Return all the extracted text from the images in the PDF





FINANCE_PATH = "競賽資料集/reference/finance"


picture_pdf_list = [1, 5, 11, 30, 85, 87, 88, 96, 98, 123, 125, 134, 141, 179, 183, 190, 207, 226, 263, 277, 278, 288, 310, 318, 338, 345, 352, 360, 362, 369, 377, 381, 382, 384, 399, 417, 418, 420, 422, 423, 431, 432,
                     459, 475, 487, 489, 499, 515, 524, 531, 534, 561, 571, 589, 615, 629, 652, 656, 670, 675, 681,
                    1031,1022,1001,1002,1004,1005,979,968,938,932,911,902,885,884,883,881,846,856,827,824,822,810,781,759,754,753,745,703]

if not os.path.isdir("finance_picture"):
    os.mkdir("finance_picture")


for i in picture_pdf_list:
    pdf_path = f"{FINANCE_PATH}/{i}.pdf"
    extracted_text = get_text_from_images_in_pdf(pdf_path)

    with open(f"finance_picture/{i}.txt", 'w') as file:
        file.write("\n".join(extracted_text))
    
    
