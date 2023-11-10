import torch
from transformers import PreTrainedTokenizerFast
from transformers import BartForConditionalGeneration
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from ..ai.Keyword_extractor import keybert

def kobart(doc,n):
    tokenizer = PreTrainedTokenizerFast.from_pretrained('Sehong/kobart-QuestionGeneration')
    model = BartForConditionalGeneration.from_pretrained('Sehong/kobart-QuestionGeneration')
    
    raw_input_ids = tokenizer.encode(doc)
    input_ids = [tokenizer.bos_token_id] + raw_input_ids + [tokenizer.eos_token_id]

    summary_ids = model.generate(torch.tensor([input_ids]))

    question_list = []
    question = tokenizer.decode(summary_ids.squeeze().tolist(), skip_special_tokens=True)
    question_list.append(question)

    return question_list

def create_question(doc,n):
    keyword_list = keybert(doc, n)
    question_list = []

    for word in keyword_list:
        answer = word
        question = get_question(answer, doc)
        cleaned_question = question.replace('<pad>', '').replace('</s>', '').strip()
        question_list.append(cleaned_question)
    
    QnA = (question_list, keyword_list)
    return QnA


def get_question(answer, context, max_length=128):
  
    tokenizer = AutoTokenizer.from_pretrained("PrimeQA/mt5-base-tydi-question-generator")
    model = AutoModelForSeq2SeqLM.from_pretrained("PrimeQA/mt5-base-tydi-question-generator")

    input_text = answer +" <<sep>> " + context
    features = tokenizer([input_text], return_tensors='pt')
    output = model.generate(input_ids=features['input_ids'], 
                attention_mask=features['attention_mask'],
                max_length=max_length)
    
    return tokenizer.decode(output[0])

context = "운영체제(Operating System, OS)는 컴퓨터 시스템의 핵심 소프트웨어로, 컴퓨터의 하드웨어와 다양한 응용 프로그램 간의 효율적이고 원활한 상호 작용을 조정하고 관리하는 시스템 소프트웨어입니다. 이 소프트웨어는 컴퓨터의 자원을 효율적으로 활용하며, 사용자 및 응용 프로그램이 하드웨어와 원활하게 상호 작용할 수 있도록 지원합니다. 또한 파일 시스템을 통해 데이터를 저장하고 관리하며, 프로세스 관리, 메모리 관리, 입출력 관리 등 다양한 기능을 제공하여 컴퓨터 시스템의 핵심 기능을 담당합니다."
#questions = create_question(context,2)
#print(questions)