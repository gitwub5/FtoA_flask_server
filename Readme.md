# FtoA⁺ 
Khuthon 2023 우수상 수상작
+ 서비스명: F to A⁺
+ 의미: F만 받던 나도 이 서비스로 매일 복습하면 A⁺ 맞을 수 있다!
+ 한줄 소개: 망각곡선 활용 문제 추천 및 문제 생성 AI 서비스
+ 취지: 쉽고 재밌게 퀴즈를 통해 장기기억으로 암기하자! 암기를 싫어하는 당신을 위한 최고의 도구!
+ 문제유형1: 빈칸 추론, 문제유형2: 키워드 기반 단답형 퀴즈 문제

<p align="center">
<img width="941" alt="image" src="https://github.com/gitwub5/FtoA/assets/132264450/7be810ce-8ec5-4009-8e90-590d01d2ea59">

<img width="893" alt="image" src="https://github.com/gitwub5/FtoA/assets/132264450/8e12d05b-1c3f-4192-b994-88e00897bf80">
</p>

## Architecture
FRONTEND: React

BACKEND: Node.js 

AI: Flask

<img width="721" alt="스크린샷 2023-11-11 오전 4 23 02" src="https://github.com/gitwub5/FtoA/assets/132264450/697e60ce-738a-48f8-8f9d-63ba4d539399">

## Main features
1. AI 모델을 활용한 빈칸 추론, 단답형 문제 생성

   * 빈칸 추론 : [keybert](https://github.com/MaartenGr/KeyBERT)로 키워드 추출→ 키워드를 빈칸으로 뚫음 
        * 키워드 개수(n) 지정 가능 
   * 단답형 : keybert로 추출한 키워드를 답으로 설정 -> [mt5-base-tydi-question-generator](https://huggingface.co/PrimeQA/mt5-base-tydi-question-generator )
        * 만들 질문 개수(n) 지정 가능, 정답 확인 가능 

2. 시간에 따른 복습 중요도를 색상, 퍼센트로 시각화
   
   * 망각 곡선에 따라 많이 망각된 내용은 빨리 복습할 수 있도록 망각 곡선 페이지에서 빨간색으로 가장 앞쪽에 배치
   * 망각 곡선에 기반하여 마지막으로 내용을 본 시각 기준에서 현재 시각의  망각 퍼센트를 계산하여 명시적으로 표시

  3. 사용자가 오늘 풀어야하는 문제 카톡으로 알림 기능(구현중) 

