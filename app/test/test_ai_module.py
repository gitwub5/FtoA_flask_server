from textblob import TextBlob

def preprocess_text(text):
    # 여기에 텍스트 전처리 로직 추가
    # 예: 소문자 변환, 특수 문자 제거 등

    preprocessed_text = text.lower()  # 간단한 예시

    return preprocessed_text

def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment_score = blob.sentiment.polarity

    if sentiment_score > 0:
        sentiment = "positive"
    elif sentiment_score < 0:
        sentiment = "negative"
    else:
        sentiment = "neutral"

    return sentiment