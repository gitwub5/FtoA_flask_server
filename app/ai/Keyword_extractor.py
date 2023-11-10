from keybert import KeyBERT
from kiwipiepy import Kiwi
from transformers import AutoModelForMaskedLM



#명사만 추출
def noun_extractor(list):
  result_list = []

  for text in list:
    results = []
    kiwi = Kiwi()
    result = kiwi.analyze(text)

    for token, pos, _, _ in result[0][0]:
        if len(text) != 1 and (pos.startswith('N') or pos.startswith('SL') or pos.startswith('SN')):
            results.append(token)

    text =  ''.join(results)
    result_list.append(text)
  return result_list


#키워드 추출 모델 (문서랑 키워드 개수 파라미터로 입력)
def keybert(doc,n):
  model = AutoModelForMaskedLM.from_pretrained("bert-base-multilingual-cased")
  kw_model = KeyBERT(model)

  #키워드 생성
  keyword = kw_model.extract_keywords(doc, keyphrase_ngram_range=(1,1), top_n=n, 
                                      use_mmr = True,  diversity = 0.55, stop_words='english',
                                      nr_candidates=10, use_maxsum= True)
  
  #키워드만 리스트로 만들기
  keyword_list = [keyword[i][0] for i in range(len(keyword))]
  #명사 추출
  print(keyword_list)
  keyword_list = noun_extractor(keyword_list)

  return keyword_list



#Example text
doc1 = """ 임진왜란은 1592년(선조 25)부터 1598년까지 2차에 걸쳐서 우리나라에 침입한 일본과의 싸움이다. 

엄청난 시련을 겪으면서도 끈질긴 저항으로 이겨내고 각성과 자기성찰을 바탕으로 민족의 운명을 새로 개척해나간 계기가 된 전쟁이다.
"""
doc2 = """A database is an organized collection of structured information, or data, typically stored electronically in a computer system. A database is usually controlled by a database management system (DBMS). Together, the data and the DBMS, along with the applications that are associated with them, are referred to as a database system, often shortened to just database.

Data within the most common types of databases in operation today is typically modeled in rows and columns in a series of tables to make processing and data querying efficient. The data can then be easily accessed, managed, modified, updated, controlled, and organized. Most databases use structured query language (SQL) for writing and querying data."""
doc3 = """data 전송/유입이 proxy를 통해서 이루어지므로 virus wall로써 적용할 수 있고 반대로 data 전송할 때 packet을 다 볼 수 있으므로 감시도 가능하다."""

doc4 = """운영체제 (Operating System)란? 운영 체제(OS)는 쉽게 이야기해서 하드웨어를 관리하는 프로그램입니다. 운영체제는 컴퓨터를 각종 하드웨어 자원과 소프트웨어 자원을 효율적으로 운영관리함으로써 사용자가 시스템을 이용하는데 편리함을 제공하는 소프트웨어입니다"""
#Test
#list = keybert(doc4,5)
#print(list)