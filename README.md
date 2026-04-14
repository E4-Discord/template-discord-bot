# 🤖 Template Discord Bot

디스코드 봇 전용 템플릿 저장소

## 🛠️ 사전 준비

- **Discord 개발자 포털** > **봇** > **Message Content Intent** 활성화
- 본인의 환경에 맞게 `docker-compose.yml` 및 `.github/workflows/deploy.yaml` 파일 수정

## 🚀 배포 방법

1. **Docker secrets**에 `discord_bot_template_token` 추가
2. **docker-compose.yml** 파일로 **Stack** 배포

## 💻 개발 방법

1. 저장소 클론:
    ```bash
    git clone https://github.com/e4-discord/template-discord-bot.git
    ```

2. 의존성 설치: `uv`가 설치되어 있어야 합니다.

    ```bash
    uv sync
    ```

3. 환경 변수 설정: 최상단에 `.env` 파일을 생성하고 토큰을 추가합니다.

    ```env
    discord_bot_token = 'MTQ5Mz...'
    ```

4. 기능 추가: `Cogs/` 폴더 내의 파일을 참고하여 새로운 기능을 추가하세요.

5. 봇 실행:

    ```bash
    uv run python app.py
    ```