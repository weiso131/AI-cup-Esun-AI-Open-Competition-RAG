from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def get_ans(embedded_model, question_data: dict, documents: list, k=1):
    document_ebeddings = embedded_model.encode(documents)

    # 使用者查詢
    user_query = question_data["query"]

    # 查詢文本轉換成嵌入向量
    query_embedding = embedded_model.encode([user_query])

    # 計算相似度
    similarities = cosine_similarity(query_embedding, document_ebeddings)
    k_highest = np.argsort(similarities[0])[-k:][::-1]
    return k_highest, similarities[0]

def show_wrong_ans(i: int, predict: int, ans: dict, token_index, \
                   order_list, real_index, similarities, chunk_real_index, tokens, path):
    print(f"qid: {i + 1}, predict: {predict}, ans: {ans["ground_truths"][i]["retrieve"]}")
    chunks_text = f"qid: {i + 1}, ans:{ans["ground_truths"][i]["retrieve"]}\n\n\n"

    for j in range(len(token_index)):
        chunks_text += f"index: {order_list[real_index[j]]}, similarity: {similarities[token_index[j]]}\n\n{tokens[token_index[j]]}\n\n\n"

    chunks_text += f"正確答案{ans["ground_truths"][i]["retrieve"]}的token\n"
    for j in range(len(tokens)):
        
        if order_list[chunk_real_index[j]] == ans["ground_truths"][i]["retrieve"]:
            chunks_text += f"token:{j + 1}, similarity: {similarities[j]}\n\n{tokens[j]}\n\n\n"


    with open(f"{path}/qid_{i + 1}.txt", 'w', encoding='utf-8') as file:
        file.write(chunks_text)

def use_reranker(reranker, top10: list[str], query: str, all_predict):
    pairs = [[query, text] for text in top10]
    scores = reranker.compute_score(pairs)
    order = np.argsort(scores)[::-1]
    return all_predict[order[0]]