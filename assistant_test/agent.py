from langchain.chat_models import ChatOpenAI
from langchain.callbacks import StreamingStdOutCallbackHandler
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.memory import ConversationSummaryBufferMemory
from langchain.chains import LLMChain


# ------------------------------------------------------------
# BasicGPT
# ------------------------------------------------------------
llm_basic = ChatOpenAI(
    temperature=0.1,
    callbacks=[StreamingStdOutCallbackHandler()],
)

prompt_basic = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{message}"),    
])

memory_basic = ConversationSummaryBufferMemory(
    llm=llm_basic,
    max_token_limit=150,
    memory_key="chat_history",
    return_messages=True,
)

chain_basic = LLMChain(
    llm=llm_basic,
    prompt=prompt_basic,
    memory=memory_basic,
    verbose=True,    
)

# ------------------------------------------------------------
# Classifier
# ------------------------------------------------------------
from langchain.prompts.few_shot import FewShotChatMessagePromptTemplate
from langchain.output_parsers.enum import EnumOutputParser
from enum import Enum

# Define LLM
llm_clf = ChatOpenAI(
    temperature=0.1,
    callbacks=[StreamingStdOutCallbackHandler()],
)

# Define prompt
examples = [
    {"message": "선생님 한 달 쉬게 해드릴까요?", "sentiment": "malicious"},
    {"message": "아이폰 쓰지 마라. 애들이 보고 사달라고 조른다.", "sentiment": "malicious"},
    {"message": "학교에서 뭘 가르쳤길래 우리 애가 야동을 보냐.", "sentiment": "malicious"},
    {"message": "선생님 우리 아이 좀 깨워주세요 초인종 눌러서요.", "sentiment": "malicious"},
    {"message": "잠시만요, 선생님 우리 아이 혼내셨어요?", "sentiment": "malicious"},
    {"message": "애가 준비물을 안챙겨갔으면 저한테 연락을 주셨어야죠.", "sentiment": "malicious"},
    {"message": "내 아이 장염이에요. 죽 끓여 먹이세요.", "sentiment": "malicious"},
    {"message": "우리 아이 장염 걸렸으니 죽 끓여 먹여라.", "sentiment": "malicious"},
    {"message": "교사 말투가 마음에 안 든다. 아이들 앞에서 교사가 공개 사과해라.", "sentiment": "malicious"},
    {"message": "교사 자격이 없다. 우리 아이 왜 메디폼 안 붙였냐.", "sentiment": "malicious"},
    {"message": "받아쓰기 어려워 우리 아이 자존감 떨어진다.", "sentiment": "malicious"},
    {"message": "선생님이 아침마다 초인종 눌러서 깨워주시죠.", "sentiment": "malicious"},
    {"message": "우리 아이 마음 다치니 받아쓰기 틀린 것 빗금 치지 말아달라.", "sentiment": "malicious"},
    {"message": "선생님 신문에 나고 싶어요? 뭐 저런 게 선생이야.", "sentiment": "malicious"},
    {"message": "월급 받고 하는 게 뭐냐.", "sentiment": "malicious"},
    {"message": "숙제 내주니 네가 가정폭력범이야 씨XX아.", "sentiment": "malicious"},
    {"message": "학기 초인데 왜 이렇게 오래 쉬냐.", "sentiment": "malicious"},
    {"message": "아프다고 연락 안 받냐. 내 방식대로 처리하겠다.", "sentiment": "malicious"},
    {"message": "방과 후 돌봄에 네가 왜 책임이 없어? 내 세금으로 세금 먹는 벌레야.", "sentiment": "malicious"},
    {"message": "우리 아이가 왜 그랬는지 한 번쯤 생각해 보셨어요?", "sentiment": "malicious"},
    {"message": "학교에서는 선생님이 엄마잖아요.", "sentiment": "malicious"},
    {"message": "과일 깎아 간식 제공해라.", "sentiment": "malicious"},
    {"message": "내 아이가 다쳤으니 담임 교사 네 책임.", "sentiment": "malicious"},
    {"message": "학교에서는 선생님이 엄마잖아요.", "sentiment": "malicious"},
    {"message": "담임교사가 집에 와서 보충 지도해달라.", "sentiment": "malicious"},
    {"message": "우리 아이가 일기를 썼는데 왜 칭찬 도장을 안 찍어주냐?", "sentiment": "malicious"},
    {"message": "네가 내 딸 밖에서 재웠냐? 우리 아이가 그 이후로 잠을 못 잔다.", "sentiment": "malicious"},
    {"message": "운동회 언제에요?", "sentiment": "non-malicious"},
    {"message": "우리 아이가 가정통신문을 잃어버렸는데 하나 더 받을 수 있을까요?", "sentiment": "non-malicious"},
    {"message": "선생님 저희 아이가 조금 늦을 것 같아요.", "sentiment": "non-malicious"},
]
    
example_prompt = ChatPromptTemplate.from_messages([
    ("human", "{message}"),
    ("ai", "{sentiment}")
])

fewshot_prompt = FewShotChatMessagePromptTemplate(
    example_prompt=example_prompt,
    examples=examples,
)

full_prompt_clf = ChatPromptTemplate.from_messages([
    ("system", """You are a classifier for complaint messages sent by parents to a school.
The messages are written mainly in Korean. Classify each message as "malicious" or "non-malicious".

## Definition
A message is MALICIOUS if its main tone is abusive toward the recipient (teacher or school staff). Malicious complaints typically contain:
1. Profanity, swear words, or vulgar slang, including masked or abbreviated forms such as "ㅅㅂ", "ㅈㄹ", "씨발", "개새끼", "병신".
2. Insults or personal attacks on the person, not on the issue (e.g. calling someone incompetent or useless, "교사 자격도 없다").
3. Disrespectful or contemptuous speech: banmal (반말) used as an insult, mocking, sarcasm meant to demean, or repeated shouting (excessive "!!!", "??").
4. Threats or intimidation (e.g. "가만 안 두겠다", "각오해").

A message is NON-MALICIOUS if it is a genuine complaint, question, request, or report, even when the parent is upset, firm, or critical, as long as the language stays free of the features above. Strong dissatisfaction alone is NOT malicious. Politely worded complaints, requests for explanation, and concerns about a child's safety or grades are non-malicious.

## How to decide
- Look first at HOW it is said (profanity, insults, contemptuous tone), then at WHAT is said.
- Many profane or insulting expressions is a strong signal for malicious.
- A single mild expression in an otherwise polite complaint should not change the label to malicious.
- If you are still uncertain after applying these rules, answer "malicious".

## Output
Answer with exactly one word: malicious or non-malicious. Do not add any explanation.

## Examples
Message: "선생님, 어제 아이가 숙제 때문에 혼났다고 하는데 어떤 상황이었는지 알려주실 수 있을까요?"
Answer: non-malicious

Message: "급식 문제가 계속되는데 왜 개선이 안 됩니까. 이번 주 안에 답변 부탁드립니다."
Answer: non-malicious

Message: "야 이 ㅅㅂ 선생이 애를 어떻게 가르치길래 이 모양이야 ㅈㄹ 하지 마"
Answer: malicious

Message: "교사 자격도 없는 게 월급만 받아먹냐. 가만 안 두겠다."
Answer: malicious
"""
),
    fewshot_prompt,
    ("human", "{message}"),
])

# Define output parser
class Sentiment(Enum):
    MALICIOUS = "malicious"
    NON_MALICIOUS = "non-malicious"
    
parser_clf = EnumOutputParser(enum=Sentiment)

# Define chain
chain_clf = LLMChain(
    llm=llm_clf,
    prompt=full_prompt_clf,
    output_parser=parser_clf,
    verbose=True,        
)

