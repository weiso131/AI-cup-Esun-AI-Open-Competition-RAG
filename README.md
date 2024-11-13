# AI CUP 2024 玉山人工智慧公開挑戰賽－RAG與LLM在金融問答的應用 各種怪怪想法?

## 使用imbedded模型
- bge-m3

# 各個題目的解決方法

## FAQ
### 當前作法
- 直接把同個類別FAQ的文字組在一起當一個token
- ACC: 96%


## Insurance
### 當前作法
- 以條文來切分token，過長的法條再用```RecursiveCharacterTextSplitter_400_300```細切
- acc: 94%，WA: 2, 4, 50
- 第4題有兩個答案
- 第50題沒有答案
- 精神上acc: 98%

## finance
### 當前作法
- 先用tesseract盡可能將圖片中的文字題取出來(效果不好)，然後再由人工校正(其實最後都丟到一個圖片轉文字的網站)
- 以```RecursiveCharacterTextSplitter_500_300```切token
- 用reranker: acc: 82%
- 用前幾個關鍵字做rerank: acc: 84%


# 結果
![image](https://github.com/user-attachments/assets/825d8338-2f54-46eb-9568-e4b2aa6aea3a)

- 參賽隊伍數: 487
- 繳交隊伍數: 222
