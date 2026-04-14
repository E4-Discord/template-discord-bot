FROM python:3.14-slim

LABEL maintainer="eu4ng97@gmail.com"
LABEL version="0.1.0"
LABEL description="Run app.py"

# uv 설치
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

# 작업 디렉토리 설정
WORKDIR /usr/src/app

# 파이썬 의존성 패키지 설치
COPY .python-version pyproject.toml uv.lock ./
ENV UV_COMPILE_BYTECODE=1
RUN uv sync --frozen

# 파이썬 프로젝트 소스 코드 복사
COPY app.py ./
COPY Cogs/ Cogs/

# 환경 변수 설정
ENV PATH="/usr/src/app/.venv/bin:$PATH"
ENV PYTHON_FILE_NAME="app"

# 파이썬 실행
ENTRYPOINT ["sh", "-c"]
CMD ["python -u $PYTHON_FILE_NAME.py"]