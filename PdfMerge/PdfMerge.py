import sys
from pdfMerge.Merge import pdfMerger

folderPath = sys.argv[1]
print ("Merging pdf in folder %s" % folderPath)

merger = pdfMerger.pdfMerger(folderPath)
merger.merge()

print("Merged")