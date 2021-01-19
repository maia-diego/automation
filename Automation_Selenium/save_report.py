from time import strftime
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.platypus import PageBreak
from app_selenium import Test

file_path = r'C:\IBM\Treinamentos\Automation_Selenium\outputs\reports'
image_path = r'C:\IBM\Treinamentos\Automation_Selenium\outputs\screeshots'
PAGE_WIDTH, PAGE_HEIGHT = A4


def draw_ruler(pdf):
    pdf.drawString(100, 810, 'x100')
    pdf.drawString(200, 810, 'x200')
    pdf.drawString(300, 810, 'x300')
    pdf.drawString(400, 810, 'x400')
    pdf.drawString(500, 810, 'x500')

    pdf.drawString(10, 100, 'y100')
    pdf.drawString(10, 200, 'y200')
    pdf.drawString(10, 300, 'y300')
    pdf.drawString(10, 400, 'y400')
    pdf.drawString(10, 500, 'y500')
    pdf.drawString(10, 600, 'y600')
    pdf.drawString(10, 700, 'y700')
    pdf.drawString(10, 800, 'y800')


def create_pdf(pdf_name, document_title):
    pdf = canvas.Canvas(pdf_name, pagesize=A4)
    pdf.setTitle(document_title)
    return pdf


def write_title(title, pdf):
    pdf.setFont('Helvetica-Bold', 20)
    pdf.drawCentredString(PAGE_WIDTH/2.0, PAGE_HEIGHT-100, title)


def write_subtitle(subtitle, pdf):
    pdf.setFont('Helvetica-Bold', 14)
    pdf.drawCentredString(PAGE_WIDTH/2.0, PAGE_HEIGHT-120, subtitle)


def project_report(tests):
    document_title = f'{strftime("%m/%d/%y")} Consult CEP Test Report'
    title = 'Automated Test of Consult CEP Web Service'
    subtitle = f'{strftime("%m/%d/%y")} - Diego de Freitas Maia'
    pdf_name = file_path + '\\' + strftime("%Y-%m-%d") + '_' + 'cep' + '_report.pdf'

    report_pdf = create_pdf(pdf_name, document_title)

    for test in tests:
        write_title(title, report_pdf)
        write_subtitle(subtitle, report_pdf)

        report_pdf.setFont('Helvetica-Bold', 12)
        line = f'Test {test.id_test} Results'
        report_pdf.drawString(80, 650, line)

        report_pdf.setFont('Helvetica', 12)
        line = f'Input: {test.input_string} Status: {test.general_result[test.input_string]}'
        report_pdf.drawString(80, 635, line)

        y = 635
        i = 1
        for result in test.results.keys():
            for_height = y - i*15
            line = f'{result}: {test.results[result]}'
            report_pdf.drawString(80, for_height, line)
            i += 1

        report_pdf.drawImage(test.input_screenshot, ((PAGE_WIDTH / 2.0) - 150), 330, 250, 188)
        report_pdf.drawImage(test.result_screenshot, ((PAGE_WIDTH / 2.0) - 150), 50, 250, 188)

        page_num = report_pdf.getPageNumber()
        report_pdf.drawString(520, 50, str(page_num))
        report_pdf.showPage()

    report_pdf.save()