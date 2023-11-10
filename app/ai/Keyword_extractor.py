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
  keyword_list = noun_extractor(keyword_list)

  return keyword_list


