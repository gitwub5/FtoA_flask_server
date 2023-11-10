from flask import render_template, jsonify, request
from . import main_bp
from ..test.test_ai_module import analyze_sentiment, preprocess_text
from ..ai.Keyword_extractor import keybert
from ..ai.Question_generator import kobart

@main_bp.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@main_bp.route('/extract_keywords', methods=['POST'])
def extract_keywords():
    if request.method == 'POST':
        data = request.get_json()
        doc = data.get('text', '')
        doc = '"""' + doc + '"""'
        n = data.get('n', '')
        
        keywords = keybert(doc,n)
        
        return jsonify({"keywords": keywords})
    

@main_bp.route('/generate_questions', methods=['POST'])
def generate_questions():
    if request.method == 'POST':
        data = request.get_json()
        doc = data.get('text', '')
        n = data.get('n', '')
        
        questions = kobart(doc,n)
        
        return jsonify(questions)



#테스트용
@main_bp.route('/analyze_sentiment', methods=['GET'])
def analyze_sentiment_route():
    sample_text = "I love this product! It's amazing."

    sentiment = analyze_sentiment(sample_text)
    return render_template('result.html', result=f"The sentiment is {sentiment}")

#전처리하고 모듈 돌리는 예시 코드
@main_bp.route('/process_and_analyze', methods=['POST'])
def process_and_analyze_route():
    data = request.get_json()
    text_to_process = data.get('text')

    if not text_to_process:
        return jsonify({'error': 'Text not provided'}), 400

    # 전처리
    preprocessed_text = preprocess_text(text_to_process)

    # AI 모델 호출
    sentiment = analyze_sentiment(preprocessed_text)

    return render_template('result.html', result=f"The sentiment is {sentiment}")