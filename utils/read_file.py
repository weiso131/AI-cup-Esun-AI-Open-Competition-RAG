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

def read_target_insurance_pdf(dir_path : str, indexs : list) -> list:
    """
    讀取指定編號純文字pdf
    並將其合成為一個list
    """

    all_pdf = os.listdir(dir_path)
    all_texts = []
    order_list = []
    for i in range(len(all_pdf)):
        if not int(all_pdf[i][:-4]) in indexs:
            continue
        
        pdf_name = all_pdf[i]
        text = read_text_pdf(f"{dir_path}/{pdf_name}")
        all_texts.append(text)
        order_list.append(int(pdf_name[:-4]))
    
    return all_texts, np.array(order_list)


def read_json(json_path : str) -> dict:
    with open(json_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data

