'''
    result_code : 성공 여부 (성공 : success, 에러 : error)
    query : 분석을 위한 텍스트 값
    type : 분석 종류
    score: 결과에 대한 스코어 0.0~1.0(1.0에 가까울수록 신뢰도 높음)
    label: 감성 종류 : [부정, 중립, 긍정] , 감정 종류 : [기쁨, 신뢰, 공포, 기대, 놀라움, 슬픔, 혐오, 분노]
    error_code: 에러 코드 (에러시 표시)
    error_msg: 에러 사유 (에러시 표시)
'''

result1 = {
    "request_id": "0",
    "return_type": "omAnalysis",
    "result": 0,
    "reason": "",
    "return_object": {
        "query": "코로나 무증상 증상 넘 무서워요.",
        "type": "감성분석",
        "score": 0.9489038586616516,
        "label": "부정"
    },
    "result_code": "success"
}

result2 = {
    "request_id": "0",
    "return_type": "omAnalysis",
    "result": 0,
    "reason": "",
    "return_object": {
        "query": "코로나 무증상 증상 넘 무서워요.",
        "type": "감정분석",
        "Result": [
            [
            0.8162028789520264,
            "공포"
            ]
        ]
    },
    "result_code": "success"
} 