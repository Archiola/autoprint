import fitz  # PyMuPDF (Fitz) library
import pytesseract

pdf_file_path = 'king.pdf'
output_pdf_path = 'output_cropped_page.pdf'  # Path to the cropped page

# Open the PDF file with PyMuPDF (Fitz)
pdf_document = fitz.open(pdf_file_path)

# Assuming you are working with the first page
page = pdf_document[0]

# Use Tesseract to extract text from the page
page_image = page.get_pixmap()
extracted_text = pytesseract.image_to_string(page_image)

# Split the extracted text into lines
lines = extracted_text.split('\n')

# Initialize variables for baseline detection
baseline_detected = False
baseline_top = None
baseline_bottom = None

# Define criteria for baseline detection
# In this example, we look for the first line with enough characters (adjust as needed)
min_characters_in_line = 10

# Iterate through the lines to detect the baseline
for line_num, line in enumerate(lines):
    if len(line) >= min_characters_in_line:
        # We found a line with enough characters, consider it as the baseline
        baseline_top = page_image.irect.y0 + page_image.irect.h * (line_num / len(lines))
        baseline_bottom = baseline_top + page_image.irect.h * (1 / len(lines))
        baseline_detected = True
        break

# If the baseline was detected, crop the PDF page
if baseline_detected:
    # Crop the PDF page
    page.set_cropbox(fitz.Rect(0, baseline_top, page.width, baseline_bottom))

    # Save the cropped page as a new PDF
    pdf_document.save(output_pdf_path)
else:
    print("Baseline not detected.")

# Close the PDF document
pdf_document.close()
