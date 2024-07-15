import os
import json
import requests


# 테스트할 API 엔드포인트
url = 'http://127.0.0.1:5000/api/kakao'

# 테스트할 민원 유형 선택
comp_type = input("민원 유형을 선택하세요: ")

# 테스트용 JSON 데이터 로드
if comp_type == "악성":
    json_path = os.path.join(os.path.dirname(__file__), 'negative_body.json')
elif comp_type == "단순":
    json_path = os.path.join(os.path.dirname(__file__), 'neutral_body.json')
elif comp_type == "정상":
    json_path = os.path.join(os.path.dirname(__file__), 'positive_body.json')
else:
    json_path = os.path.join(os.path.dirname(__file__), 'hello_body.json')
    
test_json = json.load(open(json_path, 'r', encoding='utf-8'))

# POST 요청을 보냄
response_post = requests.post(url, json=test_json)
print(f"POST Response Status Code: {response_post.status_code}")

decoded_content = json.loads(response_post.text)
print(f"POST Response Content (Decoded): {json.dumps(decoded_content, ensure_ascii=False)}")
