from PyPDF2 import PdfReader, PdfWriter

# Path to the PDF file to be rotated
dir_in = ""
file_in = ""
path_in = dir_in + "/" + file_in

# Path and name for the rotated PDF file
dir_out = ""
file_out = file_in.replace('.pdf', '_rotated.pdf')
path_out = dir_out + "/" + file_out

# Pages to be rotated
# If you want to rotate all pages, set the value to None
# If you want to rotate only specific pages, set the value to a list of two integers [start, end]
pages = None

# Rotation angle in degrees
deg = 90

# Open the PDF file
pdf_in = open(path_in, 'rb')
pdf_reader = PdfReader(pdf_in)
pdf_writer = PdfWriter()

# Rotate each page in the PDF file
i=1
for page in pdf_reader.pages:
    if pages is None:
        page.rotate(deg)
        pdf_writer.add_page(page)
    else:
        if i in range(pages[0], pages[1]+1):
            page.rotate(deg)
            pdf_writer.add_page(page)
        else:
            pdf_writer.add_page(page)
    i += 1


# Save the rotated PDF file
pdf_out = open(path_out, 'wb')
pdf_writer.write(pdf_out)

pdf_out.close()
pdf_in.close()