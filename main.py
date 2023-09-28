# PyPDF2 is a Python library for working with PDF files. It allows you to perform various operations on
# PDF files, such as reading, writing, merging, splitting, and extracting text and images.

import PyPDF2

# sare pdf's ko ek saat join krne k liye merger use krte hai
merger = PyPDF2.PdfMerger()

pdfiles = ["1.pdf", "2.pdf", "sample.pdf"]
merger = PyPDF2.PdfMerger()
for filename in pdfiles:
    pdfFile = open(filename, 'rb')
    pdfReader = PyPDF2.PdfReader(pdfFile)
    merger.append(pdfReader)
pdfFile.close()
merger.write('merged.pdf')































