import sys
import pdfMerger

def main():
    folderPath = sys.argv[1]
    print ("Merging pdf in folder %s" % folderPath)
    merger = pdfMerger.pdfMerger(folderPath)
    merger.merge()
    print("Merged")

if __name__ == '__main__':
    main()
   