# AI 민원 상담 시스템

민원 접수와 조회 기능에 AI 챗봇을 결합한 웹 서비스입니다.

사용자는 웹에서 민원을 등록하고 조회할 수 있으며, AI 챗봇을 통해 민원과 관련된 질문에 대한 답변을 받을 수 있습니다. Flask 기반의 웹 애플리케이션으로 구현했으며, OpenAI API와 Kakao 챗봇을 연동하여 자연어 기반 상담 기능을 제공합니다.

<br>

## 프로젝트 소개

기존 민원 시스템은 단순 조회 및 접수 기능에 집중되어 있어 사용자가 원하는 정보를 찾기 위해 여러 단계를 거쳐야 하는 불편함이 있습니다.

이 프로젝트는 AI 챗봇을 도입하여 민원과 관련된 질문에 자연어로 답변하고, 민원 관리 기능까지 함께 제공하는 것을 목표로 개발했습니다.

---

## 주요 기능

### 회원 관리

- 회원가입
- 로그인 / 로그아웃
- 사용자 인증

### 민원 관리

- 민원 등록
- 민원 목록 조회
- 민원 상세 조회
- 댓글 작성
- 검색 기능
- 상태별 필터링

### AI 챗봇

- OpenAI API 기반 자연어 응답
- Kakao 챗봇 연동
- 민원 관련 질의응답

---

## 기술 스택

### Backend

- Python
- Flask
- SQLAlchemy
- SQLite

### Frontend

- HTML
- CSS
- Bootstrap
- Jinja2

### AI

- OpenAI API
- GPT-3.5 Turbo

---

## 프로젝트 구조

```
capstone-design-1
│
├── app
│   ├── models.py
│   ├── forms.py
│   ├── filter.py
│   ├── templates
│   ├── static
│   └── views
│
├── assistant
│   ├── chat.py
│   └── classifier.py
│
├── assistant_test
│
├── config.py
├── requirements.txt
└── README.md
```

---

## 시스템 구조

```text
                사용자
                   │
        ┌──────────┴──────────┐
        │                     │
        ▼                     ▼
   웹 브라우저          Kakao 챗봇
        │                     │
        └──────────┬──────────┘
                   ▼
             Flask Server
                   │
      ┌────────────┴────────────┐
      │                         │
      ▼                         ▼
 SQLite Database         OpenAI API
      │                         │
      └────────────┬────────────┘
                   ▼
                응답 반환
```

---

## 실행 방법

### 저장소 클론

```bash
git clone https://github.com/hsbfdsa/capstone-design-1.git
```

### 가상환경 생성

```bash
python -m venv venv
```

### 패키지 설치

```bash
pip install -r requirements.txt
```

### 서버 실행

```bash
flask run
```

기본적으로 `localhost:5000`에서 실행됩니다.

---

## 주요 구현 내용

### MVC 구조

프로젝트는 Flask Blueprint를 활용하여 기능별로 모듈을 분리했습니다.

- 인증
- 민원
- 댓글
- API

각 기능을 독립적으로 관리할 수 있도록 구성하여 유지보수성을 높였습니다.

---

### 데이터베이스

SQLAlchemy ORM을 사용하여

- 사용자
- 민원
- 댓글

데이터를 관리합니다.

---

### AI 챗봇

OpenAI GPT 모델을 이용하여 사용자의 질문에 자연어 형태로 답변하도록 구현했습니다.

또한 Kakao 챗봇과 연동하여 메신저에서도 동일한 기능을 사용할 수 있도록 구성했습니다.

---

## 프로젝트를 통해 배운 점

- Flask 기반 웹 서비스 개발
- SQLAlchemy ORM 활용
- Blueprint를 이용한 프로젝트 구조 설계
- REST API 구현
- OpenAI API 연동
- 사용자 인증 및 세션 관리
- AI 기능을 웹 서비스에 통합하는 방법

---

## 개선 사항

- OpenAI API Key 환경변수 관리
- 관리자 페이지 추가
- 민원 카테고리 분류 자동화
- AI 답변 품질 개선
- Docker 기반 배포
- AWS를 이용한 서비스 운영

---

## 개발 환경

| 항목 | 내용 |
|------|------|
| Language | Python |
| Framework | Flask |
| Database | SQLite |
| ORM | SQLAlchemy |
| AI | OpenAI GPT |
| Frontend | HTML, CSS, Bootstrap |

---

## Contributors

- 홍승범
