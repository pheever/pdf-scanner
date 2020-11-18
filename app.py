import PyPDF2
pdf_file = open('test.pdf', 'rb')
read_pdf = PyPDF2.PdfFileReader(pdf_file)
for i in range(read_pdf.getNumPages()):
        # contents.join(read_pdf.getPage(i).extractText().encode('utf-8'))
        print(read_pdf.getPage(i).extractText().encode('iso-8859-7').decode('utf-8'))

# print(contents)