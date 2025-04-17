def fetch_law_list_and_detail(query, unit):
    return [{
        "법령명한글": "예시 법령",
        "원문링크": "http://www.law.go.kr/법령/예시법령",
        "조문": [f"제1조 {query} 포함 예시 조문입니다."]
    }]