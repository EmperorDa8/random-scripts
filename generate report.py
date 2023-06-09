#!/usr/bin/env python3
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet


def getdata():
    with open("Downloads\\CIT292.txt", "r")as fil:
        textdata=fil.read()
    print("loading....")
    return textdata


def generate_report(save_name,title):
    info=getdata()
    styles=getSampleStyleSheet()
    save_path='Documents/cv_danu.pdf'
    report=SimpleDocTemplate(save_path)
    report_title=Paragraph(title, styles["h1"])
    report_info =Paragraph(info, styles["BodyText"])
    empty_line=Spacer(1,19)
    report.build([report_title, empty_line, report_info, empty_line])
    print('generate_report sucessfully')
    return report

generate_report("CV-report","Dan-res",)


# improve version below


#!/usr/bin/env python3

import logging
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

logger = logging.getLogger(__name__)

def get_data(file_path):
    with open(file_path, "r") as file:
        text_data = file.read()
    logger.info("Loaded data from file %s", file_path)
    return text_data

def generate_report(file_path, title):
    info = get_data(file_path)
    styles = getSampleStyleSheet()
    save_path = 'Documents/cv_danu.pdf'
    report = SimpleDocTemplate(save_path)
    report_title = Paragraph(title, styles["h1"])
    report_info = Paragraph(info, styles["BodyText"])
    empty_line = Spacer(1, 19)
    report.build([report_title, empty_line, report_info, empty_line])
    logger.info('Successfully generated report %s', save_path)
    return report

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    file_path = "Downloads/CIT292.txt"
    report_title = "Dan's CV"
    generate_report(file_path, report_title)
