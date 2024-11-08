import pdfplumber
import json
import os
import numpy as np

def read_text_pdf(pdf_path : str) -> str:
    """
    讀取pdf資料
    並將其轉成字串文本
    """

    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text

def generate_faq_retrieve(faq: dict, id: int) -> str:

    text = ""

    for faq_data in faq[str(id)]:

        question = faq_data["question"]
        answers = faq_data["answers"]
        text += f"{question} {answers}\n"
    return text

def read_target_faq(faq: dict, indexs: list) -> list:

    all_texts = []

    for i in indexs:
        all_texts.append(generate_faq_retrieve(faq, i))
    
    return all_texts

def read_target_insurance_pdf(dir_path: str, indexs: list, already_read: list[str]) -> list:
    """
    讀取指定編號純文字pdf
    並將其合成為一個list
    """

    all_texts = []

    for index in indexs:
        if already_read[index] != "":
            all_texts.append(already_read[index])
            continue
        
            
        filename = f"{dir_path}/{index}"
        text = ""

        if os.path.exists(filename + ".pdf"):
            text = read_text_pdf(filename + ".pdf")
        else:
            text = read_text_pdf(filename + ".txt")

        if already_read[index] == "":
            already_read[index] = text
        all_texts.append(text)
    
    return all_texts


def read_json(json_path : str) -> dict:
    with open(json_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data

