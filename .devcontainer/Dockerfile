FROM mcr.microsoft.com/devcontainers/base:2.0.3-ubuntu-24.04@sha256:daa08ddb48ad4e4e7367c348e0a6f250762f1f0d8348f1f9acbef5f884ce093d

ARG DEBIAN_FRONTEND=noninteractive
ARG USER=vscode

RUN DEBIAN_FRONTEND=noninteractive \
    && apt-get update \
    && apt-get install -y build-essential --no-install-recommends make \
    ca-certificates \
    git \
    libssl-dev \
    zlib1g-dev \
    libbz2-dev \
    libreadline-dev \
    libsqlite3-dev \
    wget \
    curl \
    llvm \
    libncurses5-dev \
    xz-utils \
    tk-dev \
    libxml2-dev \
    libxmlsec1-dev \
    libffi-dev \
    liblzma-dev

# Python and poetry installation
USER $USER
ARG HOME="/home/$USER/"

# renovate: datasource=github-releases depName=python packageName=containerbase/python-prebuild
ARG PYTHON_VERSION=3.13.5

# renovate: datasource=github-releases depName=python-poetry/poetry
ARG POETRY_VERSION=1.8.5

ENV PYENV_ROOT="${HOME}.pyenv/"
ENV PATH="${PYENV_ROOT}shims:${PYENV_ROOT}/bin:${HOME}/.local/bin:$PATH"

RUN curl https://pyenv.run | bash \
    && echo "installed pyenv" \
    && pyenv install ${PYTHON_VERSION} \
    && echo "installed python ${PYTHON_VERSION}" \
    && pyenv global ${PYTHON_VERSION} \
    && echo "set global python version ${PYTHON_VERSION}" \
    && curl -sSL https://install.python-poetry.org | python3 - \
    && poetry config virtualenvs.in-project true

# Advent of Code
#COPY --link --chown=${USER}:${USER} AOC_TOKE[N] ${HOME}.config/aocd/token
