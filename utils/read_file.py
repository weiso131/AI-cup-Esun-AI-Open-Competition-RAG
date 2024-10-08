import pdfplumber
import json
import os

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

def read_target_insurance_pdf(dir_path : str, indexs : list) -> list:
    """
    讀取指定編號純文字pdf
    並將其合成為一個list

    TODO：
    怎麼切分token比較好
    """

    all_pdf = os.listdir(dir_path)
    all_texts = []

    for i in range(len(all_pdf)):
        if not (i + 1) in indexs:
            continue
        pdf_name = all_pdf[i]
        text = read_text_pdf(f"{dir_path}/{pdf_name}")
        all_texts.append(text)
    
    return all_texts


def read_json(json_path : str) -> dict:
    with open(json_path, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data



