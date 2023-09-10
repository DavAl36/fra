import os

from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase.pdfmetrics import stringWidth
from reportlab.rl_config import defaultPageSize


def txt_to_pdf(path_in, path_out):

    #initialize PDF file
    fontName = 'Times-Roman'
    fontSize = 10
    canvas = Canvas(path_out, pagesize=A4)
    canvas.setFont(fontName, fontSize)

    # open the data file
    file = open(path_in, mode="r", encoding="utf-8")
    
    #starting Y coordinate 
    Y_max = 10*inch
    Y = Y_max
    Y_min = inch
    PAGE_WIDTH  = defaultPageSize[0]
    PAGE_HEIGHT = defaultPageSize[1]

    for line in file.readlines():
        if(len(line) > 1):
            line = line[0:-1]# evita di scrivere ■ nel pdf
            text_width = stringWidth(line,fontName,fontSize)
            #canvas.drawString(1 * inch, Y, line)
            canvas.drawString((PAGE_WIDTH - text_width) / 2.0 , Y, line)
            #write a new page
            if Y <= Y_min:
                Y = Y_max
                canvas.showPage() #New Page
                canvas.setFont("Times-Roman", 10)
            Y = Y - 10  

    # close the file
    canvas.save()
    file.close()
    os.chmod(path_out,0o777)