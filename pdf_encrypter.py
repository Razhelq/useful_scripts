# pdf_encrypter - encrypt given file with provided password


import PyPDF2, os, sys


file = sys.argv[1]
pw = sys.argv[2]

if file and pw:
    pdf_file_obj = open(os.path.join(os.getcwd() + '\\' + file), 'rb')
    pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj)
    pdf_writer = PyPDF2.PdfFileWriter()
    for page_num in range(1, pdf_reader.numPages):
        page_obj = pdf_reader.getPage(page_num)
        pdf_writer.addPage(page_obj)
    pdf_output = open('{}_encrypted.pdf'.format(file[:len(file) - 4]), 'wb')
    pdf_writer.encrypt(pw)
    pdf_writer.write(pdf_output)
    pdf_output.close()