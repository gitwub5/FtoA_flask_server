from keybert import KeyBERT
from kiwipiepy import Kiwi
from transformers import BertModel


def noun_extractor(list):
  result_list = []
  for text in list:
    results = []
    kiwi = Kiwi()
    result = kiwi.analyze(text)
    for token, pos, _, _ in result[0][0]:
        if len(token) != 1 and pos.startswith('N') or pos.startswith('SL'):
            results.append(token)
    text =  ' '.join(results)
    result_list.append(text)
  return result_list


#키워드 추출 모델 (문서랑 키워드 개수 파라미터로 입력)
def keybert(doc,n):
  model = BertModel.from_pretrained('skt/kobert-base-v1')
  #모델 객체로 불러오기
  kw_model = KeyBERT(model)

  #키워드 추출(top_n으로 키워드 개수 조절, 5가 디폴트)
  keyword = kw_model.extract_keywords(doc, keyphrase_ngram_range=(1,1), stop_words=None, top_n=n)
  #키워드만 리스트로 만들기
  keyword_list = [keyword[i][0] for i in range(len(keyword))]

  return keyword_list

#Example text
doc1 = """ 임진왜란은 1592년(선조 25)부터 1598년까지 2차에 걸쳐서 우리나라에 침입한 일본과의 싸움이다. 

엄청난 시련을 겪으면서도 끈질긴 저항으로 이겨내고 각성과 자기성찰을 바탕으로 민족의 운명을 새로 개척해나간 계기가 된 전쟁이다.
"""
doc2 = """A database is an organized collection of structured information, or data, typically stored electronically in a computer system. A database is usually controlled by a database management system (DBMS). Together, the data and the DBMS, along with the applications that are associated with them, are referred to as a database system, often shortened to just database.

Data within the most common types of databases in operation today is typically modeled in rows and columns in a series of tables to make processing and data querying efficient. The data can then be easily accessed, managed, modified, updated, controlled, and organized. Most databases use structured query language (SQL) for writing and querying data."""
#Test
"""
list = keybert(doc1, 2)
print(list)
kw_model = KeyBERT()
#키워드 추출할 문서 파라미터로 입력
keywords = kw_model.extract_keywords(doc)
print(keywordtext = kw_model.extract_keywords(doc2, highlight=True,top_n=5))
"""

list = keybert(doc1,5)
print(noun_extractor(list))
#print(list)