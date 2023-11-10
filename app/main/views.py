import json
from flask import render_template, jsonify, request
from . import main_bp
from ..ai.Keyword_extractor import keybert
from ..ai.Question_generator import create_question

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
        if(n>3):
            n = 3
        
        QnA = create_question(doc,n)
        
        return jsonify({"QnA": QnA})
