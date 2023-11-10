#테스트용 views
import json
from flask import render_template, jsonify, request
from ..main import main_bp

@main_bp.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@main_bp.route('/extract_keywords', methods=['POST'])
def extract_keywords():
    if request.method == 'POST':
        data = request.get_json()
        doc = data.get('text', '')
        
        keywords = ['운영체제', '윈도우', '슈퍼컴퓨터', '프로그램', '전화']
        
        return jsonify({"keywords": keywords})
    

@main_bp.route('/generate_questions', methods=['POST'])
def generate_questions():
    if request.method == 'POST':
        data = request.get_json()
        doc = data.get('text', '')
        
        
        QnA =  (
                ['컴퓨터에서 사용되는 컴퓨터는 무엇인가?', '운영체제는 무엇인가?', '운영체제는 무엇인가?'], 
                ['운영체제', '프로그램', '전화']
        )
        
        return jsonify({"QnA": QnA})

