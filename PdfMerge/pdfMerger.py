import sys
import os
from PyPDF2 import PdfFileMerger

class pdfMerger():
    
    def __init__(self, mergePath):
        self.mergePath = mergePath

    def merge(self):
            final_file_name = os.path.join(self.mergePath, "merged_all.pdf")
            if os.path.exists(final_file_name):
                os.remove(final_file_name)
            pdfs = [os.path.join(self.mergePath, f) for f in os.listdir(self.mergePath) if os.path.isfile(os.path.join(self.mergePath, f))]
            merger = PdfFileMerger()
            for pdf in pdfs:
                merger.append(pdf)
            merger.write(final_file_name)
            merger.close()
