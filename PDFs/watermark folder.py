from PyPDF2 import PdfFileWriter, PdfFileReader
import os


def get_listing():
    path = r'C:\Users\paihnativ\OneDrive\work\Standards & Test Methods\AS 1289'
    for entry in os.listdir(path):
        if os.path.isfile(os.path.join(path, entry)):
            return entry
            print(entry)


def create_watermark(input_pdf, output, watermark):
    watermark_obj = PdfFileReader(watermark)
    watermark_page = watermark_obj.getPage(0)

    pdf_reader = PdfFileReader(input_pdf)
    pdf_writer = PdfFileWriter()

    # Watermark all the pages
    for page in range(pdf_reader.getNumPages()):
        page = pdf_reader.getPage(page)
        page.mergePage(watermark_page)
        pdf_writer.addPage(page)

    with open(output, 'wb') as out:
        pdf_writer.write(out)


if __name__ == '__main__':
    entry = ''
    get_listing()
    create_watermark(
        input_pdf=entry,
        output=entry+'watermark.pdf',
        watermark='watermark.pdf')
