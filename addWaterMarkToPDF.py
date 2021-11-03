from pdfrw import PdfReader, PdfWriter, PageMerge

def Wwatermarker(path, watermark, output):
    base_pdf = PdfReader(path)
    watermarker_pdf = PdfReader(watermark)
    mark = watermarker_pdf.pages[0]


    #loop through the pages
    for page in range(len(base_pdf.pages)):
        merger = PageMerge(base_pdf.pages[page])
        merger.add(mark).render()

    writer = PdfWriter()
    writer.write(output, base_pdf)
if __name__ == '__main__':
    watermarker('re')
