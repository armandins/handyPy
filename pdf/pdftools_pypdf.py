# pip install pypdf
# https://pypdf.readthedocs.io/en
# .
# Arman Dindar Safa
# 10 / 30 / 2023
# .
from pypdf import PdfReader
# ------------------------------------------------
# Read the pdf file using script below
read = PdfReader('file.pdf') #file.pdf inside same dir.

# ------------------------------------------------
# Print the number of pages:
print('Printing Number of Pages...')
print(len(reader.pages))
# ------------------------------------------------

# ------------------------------------------------
# Extract the text inside a specific page in terminal
page = reader.pages[0] # Page #1
print(page.extract_text())
# ------------------------------------------------

# ------------------------------------------------
# Extract the text inside numerous pages in terminal
for i in range(len(reader.pages)):
	page = reader.pages[i]
	print(page.extract_text())
# ------------------------------------------------

# ------------------------------------------------
# Extract Images
for i in page.images:
	with open(i.name, 'wb') as f:
		f.write(i.data)
# ------------------------------------------------

# ------------------------------------------------
# Pdf size reduction using duplicate removal alg.
reader = PdfReader("big-old-file.pdf")
writer = PdfWriter()

for page in reader.pages:
    writer.add_page(page)

writer.add_metadata(reader.metadata)

with open("smaller-new-file.pdf", "wb") as fp:
    writer.write(fp)
# ------------------------------------------------

# ------------------------------------------------
# Lossless compression
reader = PdfReader("example.pdf")
writer = PdfWriter()

for page in reader.pages:
    writer.add_page(page)

for page in writer.pages:
    # This has to be done on the writer, not the reader!
    page.compress_content_streams()  # This is CPU intensive!

with open("out.pdf", "wb") as f:
    writer.write(f)
# ------------------------------------------------


# ------------------------------------------------
# Merging multiple pdfs
# 3 pdf files in this case called file#.pdf
merger = PdfWriter()

for pdf in ["file1.pdf", "file2.pdf", "file3.pdf"]:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()
# ------------------------------------------------