import PyPDF2
import numpy as np
#it ceates two pdf
#one has the pages in the array
#other has the pages not it the array
def sepreate_pages_in_array(n,pdfFileObj):
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    pdfWriter1 = PyPDF2.PdfFileWriter()
    pdfWriter2 = PyPDF2.PdfFileWriter()
    n=np.asarray(n)
    n=n-1
    for pageNum in range(pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)

        if (len(np.where(n==pageNum)[0])==0):
            pdfWriter1.addPage(pageObj)
        else:
            pdfWriter2.addPage(pageObj)

    pdfOutputFile1 = open('notinarray.pdf', 'wb')
    pdfWriter1.write(pdfOutputFile1)

    pdfOutputFile2 = open('inarray.pdf', 'wb')
    pdfWriter2.write(pdfOutputFile2)

    pdfOutputFile1.close()
    pdfOutputFile2.close()

def merge_pdf(pdf1,pdf2):
    pdfReader1 = PyPDF2.PdfFileReader(pdf1)
    pdfReader2 = PyPDF2.PdfFileReader(pdf2)
    pdfWriter = PyPDF2.PdfFileWriter()
    for pageNum in range(pdfReader1.numPages):
        pageObj = pdfReader1.getPage(pageNum)
        pdfWriter.addPage(pageObj)
    for pageNum in range(pdfReader2.numPages):
        pageObj = pdfReader2.getPage(pageNum)
        pdfWriter.addPage(pageObj)
    pdfOutputFile = open('merged.pdf', 'wb')
    pdfWriter.write(pdfOutputFile)
    pdfOutputFile.close()


#uncomment the merge part to implement that

#split pdf based on the array 
#pdf = open('check.pdf', 'rb')#pdf to process
#n=[2,3,5]
#sepreate_pages_in_array(n,pdf)

#merge pdf
pdf1 = open('check1.pdf', 'rb')#pdf to process
pdf2 = open('check2.pdf', 'rb')#pdf to process
merge_pdf(pdf1,pdf2)
pdf1.close()
pdf2.close()
