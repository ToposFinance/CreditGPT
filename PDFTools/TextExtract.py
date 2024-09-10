
import os
import sys



sys.path.append(os.path.join(os.path.dirname(__file__), '/Users/marcnunes/PycharmProjects/CreditGPT'))


from pypdf import PdfReader


def get_reader(path_to_pdf):
    reader = PdfReader(path_to_pdf)
    return reader

def get_page(reader,page_number):
    try:
        return reader.pages[page_number]
    except Exception as e:
        return e


def get_text(reader):
    all_text = ""
    for k in range(len(reader.pages)):
        page = get_page(reader=reader,page_number=k)
        all_text += page.extract_text()
    return all_text


def split_pdf_by_phrase(path_to_pdf,phrase):
    reader=get_reader(path_to_pdf)
    all_text=get_text(reader)
    splits=all_text.split(phrase)
    return splits


