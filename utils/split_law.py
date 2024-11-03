import re
from langchain.text_splitter import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=400,  # 每段的目標長度
    chunk_overlap=300  # 分段間的重疊字符數
)

LAW_PATTERN = r"(【.+】)*\n第\s*[零一二三四五六七八九十百千壹貳參肆伍陸柒捌玖拾佰仟]+\s*條(\s|【)"


def split_law_to_token(document: str) -> list:
    """
    將條文依據第幾條作切分
    然後再將過長的條文分段
    
    """
    matches = re.finditer(LAW_PATTERN, document)
    indexs = [0]
    for m in matches:
        indexs.append(m.start())
    indexs.append(len(indexs))

    all_chunk = []
    for i in range(len(indexs) - 1):
        text = document[indexs[i] : indexs[i + 1]]
        if text == "":
            continue
        chunks = text_splitter.split_text(text)
        all_chunk.extend(chunks)

    return all_chunk
