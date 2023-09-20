import sys
import PyPDF2

inputs = sys.argv[1:]
pdfMerge = PyPDF2.PdfFileMerger()

for pdf_files in inputs:
    pdfMerge.append(pdf_files)

pdfMerge.write("New_Merged_file.pdf")
