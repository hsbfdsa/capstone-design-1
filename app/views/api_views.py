from flask import Blueprint, request, jsonify

from assistant.chat import Chatbot


chatbot = Chatbot()

bp = Blueprint('api', __name__, url_prefix='/api')


@bp.route('/kakao', methods=['POST'])
def get_assistant_response():
    try:
        body = request.get_json()
        user_input = body['userRequest']['utterance']
        print("사용자 입력: ", user_input)
        
        # 
        chat_response = chatbot.ask(user_input)
        print("어시스턴트 응답: ", chat_response)
        
        data = {
            "version": "2.0",
            "template": {
                "outputs": [
                    {
                        "simpleText": {
                            "text": chat_response
                        }
                    }
                ]
            }
        }
        return jsonify(data), 200
    except Exception as e:
        print(f"Error parsing JSON: {e}")
        return "Bad Request", 400

