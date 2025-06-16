# ===============================
# 第一階段：下載並解壓 Chrome & Chromedriver
# ===============================
FROM debian:bullseye-slim AS chrome-builder

RUN apt-get update && apt-get install -y wget unzip && \
    wget -O chrome-linux64.zip https://storage.googleapis.com/chrome-for-testing-public/136.0.7103.49/linux64/chrome-linux64.zip && \
    wget -O chromedriver-linux64.zip https://storage.googleapis.com/chrome-for-testing-public/136.0.7103.49/linux64/chromedriver-linux64.zip && \
    unzip chrome-linux64.zip && \
    unzip chromedriver-linux64.zip

# ===============================
# 第二階段：正式 image
# ===============================
FROM apache/airflow:2.10.5-python3.12

USER root

# 安裝基本工具與瀏覽器相關依賴
RUN apt-get update && apt-get install -y \
        bash git zsh vim curl make procps gcc python3-dev gnupg ca-certificates \
        fonts-liberation libnss3 libxss1 libatk-bridge2.0-0 libgtk-3-0 libgbm1 libasound2 \
        libx11-xcb1 libxcomposite1 libxcursor1 libxdamage1 libxrandr2 libdrm2 libxfixes3 \
        libxi6 libgl1 && \
    rm -rf /var/lib/apt/lists/*

# 從 builder 階段複製 chrome 與 chromedriver
COPY --from=chrome-builder /chrome-linux64 /opt/chrome
COPY --from=chrome-builder /chromedriver-linux64/chromedriver /usr/local/bin/chromedriver

# 建立 google-chrome 的符號連結
RUN [ -L /usr/local/bin/google-chrome ] ||  ln -s /opt/chrome/chrome /usr/local/bin/google-chrome && \
    chmod +x /usr/local/bin/google-chrome /usr/local/bin/chromedriver

# 安裝 oh-my-zsh (不影響主流程)
RUN echo "Y" | sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" || true

# 安裝 poetry
RUN curl -sSL https://install.python-poetry.org | python3 - && \
    ln -s /root/.local/bin/poetry /usr/local/bin/poetry


# 複製爬蟲專案的檔案
COPY ./crawler-service/src /opt/airflow/src
COPY ./crawler-service/data /opt/airflow/data
COPY ./crawler-service/tasks /opt/airflow/tasks
COPY ./crawler-service/utils /opt/airflow/utils
COPY ./crawler-service/pyproject.toml ./crawler-service/poetry.lock /opt/airflow/

# 設定工作目錄並安裝專案依賴
WORKDIR /opt/airflow
RUN poetry config virtualenvs.create false && poetry install --no-root

# 切換回 airflow 使用者
USER airflow

# 回到 airflow 預設工作目錄
WORKDIR /opt/airflow


