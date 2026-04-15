# 🤖 Template Discord Bot

파이썬(Python) 기반 디스코드 봇 개발 및 자동 배포를 위한 템플릿 저장소입니다. 

코드를 푸시하면 도커(Docker) 이미지 빌드부터 Portainer 스택 업데이트까지의 배포 과정이 GitHub Actions를 통해 자동으로 실행됩니다.

도커 이미지 태그는 `master` 브랜치에 푸시되는 경우 `latest`로, `develop` 브랜치에 푸시되는 경우 `dev`로 자동 할당됩니다.

## 🛠️ 사전 준비

### 1. Discord 봇 생성

> 안정적인 서비스를 위해 운영(Production) 환경과 개발(Development) 환경을 분리하여 **총 2개의 Discord 봇** 생성을 권장합니다. 

#### 봇 생성 및 설정 방법

1. [Discord 개발자 포털](https://discord.com/developers/applications)에 접속하여 **New Application** 버튼을 클릭해 봇 애플리케이션을 생성합니다.
2. 좌측 메뉴 **봇** 항목을 클릭한 뒤, **토큰 초기화**를 클릭하여 발급된 봇 토큰을 복사해 둡니다. (이후 단계에서 사용)
3. 동일한 페이지 하단의 **Privileged Gateway Intents** 섹션에서 **Message Content Intent**를 활성화합니다.

### 2. Portainer 환경 구축

> Discord 봇을 호스팅하고 관리하기 위한 서버에 Portainer가 사전에 구축되어 있어야 합니다. Portainer 설치 방법 및 역방향 프록시, SSL 인증서 설정 등 인프라 구성에 대한 상세한 가이드는 본 문서의 범위를 벗어나므로 생략합니다.

---

## 🚀 CI/CD 및 배포 환경 설정

### 1. 템플릿 적용

이 저장소 메인의 **Use this template** 버튼을 눌러 본인의 계정에 새로운 저장소를 생성합니다.

### 2. 프로젝트 정보 수정

새롭게 생성한 저장소에서 아래 파일들의 식별자 및 정보를 본인 프로젝트에 맞게 수정합니다.

- `docker-compose.yml`, `docker-compose-dev.yml`
    - `services`
    - `image`
    - `container_name`
    - `secrets`
- `Dockerfile`
    - `maintainer`
    - `description`
- `pyproject.toml`
    - `name` 
    - `description`
- `.github/workflows/deploy.yaml`
    - `PACKAGE_NAME`

### 3. Portainer Secrets 추가

Portainer 대시보드의 **Secrets** 메뉴로 이동하여 복사해둔 토큰을 추가합니다.

- `discord_bot_template_token`: 운영 전용 Discord 봇 토큰
- `discord_bot_template_dev_token`: 개발 전용 Discord 봇 토큰

### 4. Portainer 스택 최초 수동 배포

자동 업데이트 파이프라인이 동작하기 위해서는 먼저 빈 스택을 생성해 두어야 합니다. Portainer의 **Stacks** 메뉴에서 아래 파일의 내용을 붙여넣어 최초 배포를 진행합니다.

- `docker-compose.yml` 파일 내용으로 운영 스택 배포
- `docker-compose-dev.yml` 파일 내용으로 개발 스택 배포

> **참고**: 배포 완료 후 각각의 스택 관리 페이지 URL에서 `ENDPOINT_ID`와 `STACK_ID` 2가지를 찾아서 메모해 둡니다.
> *(예시 URL: `.../#!/ENDPOINT_ID/docker/stacks/...id=STACK_ID...`)*

### 5. Portainer 액세스 토큰 발급

GitHub Actions에서 Portainer API를 호출할 수 있도록 액세스 토큰을 발급받습니다.

- Portainer 우측 상단 프로필 클릭 > **My Account** > **Access tokens** 
- **Add access token**을 클릭하여 새로운 토큰 발급 후 값 복사

### 6. GitHub Secrets 설정

본인의 GitHub 저장소 **Settings > Secrets and variables > Actions** 메뉴로 이동하여 다음 시크릿(Repository secrets)들을 추가합니다.

- `PORTAINER_URL`: 본인의 Portainer 주소 (예: `portainer.example.com` - `https://` 제외)
- `PORTAINER_TOKEN`: 이전 단계에서 발급받은 Portainer 액세스 토큰
- `ENDPOINT_ID`: 메모해둔 Portainer Endpoint ID
- `STACK_ID_LATEST`: 운영 스택의 ID
- `STACK_ID_DEV`: 개발 스택의 ID

---

## 💻 로컬 개발 가이드

실제 코드를 작성하고 테스트하기 위한 로컬 환경 구성 방법입니다.

### 1. 저장소 클론

```bash
git clone https://github.com/e4-discord/template-discord-bot.git
```

### 2. 패키지 의존성 설치

파이썬 패키지 매니저인 `uv`가 시스템에 설치되어 있어야 합니다.

```bash
uv sync
```

### 3. 로컬 환경 변수 설정

로컬 개발 환경에서는 Docker Secrets를 바로 사용할 수 없으므로 루트 폴더에 `.env` 파일을 생성하여 환경 변수로 대신 사용합니다.

```env
discord_bot_token='MTQ5Mz...'
VERSION='local'
```

### 4. 기능 추가 및 개발

명령어 등의 실제 동작 로직은 `src/Cogs/` 폴더 내에 작성합니다. 기존에 작성된 템플릿 파일을 참고하여 새로운 기능을 자유롭게 추가하세요.

### 5. 봇 로컬 실행

```bash
uv run python app.py
```