import json
from flask import render_template, jsonify, request
from . import main_bp

@main_bp.route('/', methods=['GET'])
def home():
    return render_template('home.html')

@main_bp.route('/extract_keywords', methods=['POST'])
def extract_keywords():
    if request.method == 'POST':
        data = request.get_json()
        doc = data.get('text', '')
        
        keywords = [
            "운영체제",
            "시스템",
            "operating",
            "소프트웨어",
            "효율"
        ]
        
        return jsonify({"keywords": keywords})
    

@main_bp.route('/generate_questions', methods=['POST'])
def generate_questions():
    if request.method == 'POST':
        data = request.get_json()
        doc = data.get('text', '')
        
        
        QnA =  (
                [
                    "컴퓨터의 핵심 소프트웨어는 무엇인가요?",
                    "운영체제란 무엇인가?",
                    "운영체제에서 사용자의 데이터를 저장하는 기능은 무엇인가?"
                ],
                [
                    "운영체제",
                    "소프트웨어",
                    "데이터"
                ]
        )
        
        return jsonify({"QnA": QnA})

