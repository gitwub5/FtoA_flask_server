import torch
from transformers import PreTrainedTokenizerFast
from transformers import BartForConditionalGeneration
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from Keyword_extractor import keybert

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
    
    return question_list


def get_question(answer, context, max_length=128):
  
    tokenizer = AutoTokenizer.from_pretrained("PrimeQA/mt5-base-tydi-question-generator")
    model = AutoModelForSeq2SeqLM.from_pretrained("PrimeQA/mt5-base-tydi-question-generator")

    input_text = answer +" <<sep>> " + context
    features = tokenizer([input_text], return_tensors='pt')
    output = model.generate(input_ids=features['input_ids'], 
                attention_mask=features['attention_mask'],
                max_length=max_length)
    
    return tokenizer.decode(output[0])
