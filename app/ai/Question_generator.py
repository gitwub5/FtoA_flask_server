import torch
from transformers import PreTrainedTokenizerFast, BartForConditionalGeneration, AutoTokenizer, AutoModelForSeq2SeqLM
from ..ai.Keyword_extractor import keybert

# 전역 범위에서 한 번만 로드
tokenizer_kobart = PreTrainedTokenizerFast.from_pretrained('Sehong/kobart-QuestionGeneration')
model_kobart = BartForConditionalGeneration.from_pretrained('Sehong/kobart-QuestionGeneration')

tokenizer_mt5 = AutoTokenizer.from_pretrained("PrimeQA/mt5-base-tydi-question-generator")
model_mt5 = AutoModelForSeq2SeqLM.from_pretrained("PrimeQA/mt5-base-tydi-question-generator")

# KoBART를 사용하여 문서에서 질문 생성
def kobart(doc):
    raw_input_ids = tokenizer_kobart.encode(doc)
    input_ids = [tokenizer_kobart.bos_token_id] + raw_input_ids + [tokenizer_kobart.eos_token_id]

    summary_ids = model_kobart.generate(torch.tensor([input_ids]))
    question = tokenizer_kobart.decode(summary_ids.squeeze().tolist(), skip_special_tokens=True)

    return [question]

# mT5를 사용하여 주어진 답변과 문맥에서 질문 생성
def get_question(answer, context, max_length=128):
    input_text = answer + " <<sep>> " + context
    features = tokenizer_mt5([input_text], return_tensors='pt')
    output = model_mt5.generate(input_ids=features['input_ids'], 
                                attention_mask=features['attention_mask'],
                                max_length=max_length)
    
    return tokenizer_mt5.decode(output[0])

# 주어진 문서에서 키워드를 추출하고 해당 키워드에 대한 질문 생성
def create_question(doc, n):
    # 여기서 keybert 함수는 키워드를 추출하는 함수로 가정합니다. 그 구현이 여기에 포함되어 있지 않습니다.
    keyword_list = keybert(doc, n)
    question_list = []

    for word in keyword_list:
        question = get_question(word, doc).replace('<pad>', '').replace('</s>', '').strip()
        question_list.append(question)
    
    QnA = (question_list, keyword_list)
    return QnA

