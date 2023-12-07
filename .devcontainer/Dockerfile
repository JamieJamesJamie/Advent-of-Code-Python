FROM mcr.microsoft.com/devcontainers/base:1.0.17-ubuntu-22.04

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

# renovate: datasource=github-releases lookupName=containerbase/python-prebuild
ARG PYTHON_VERSION=3.11.6

# renovate: datasource=github-releases lookupName=python-poetry/poetry
ARG POETRY_VERSION=1.7.0

ENV PYENV_ROOT="${HOME}.pyenv/"
ENV PATH="${PYENV_ROOT}shims:${PYENV_ROOT}/bin:${HOME}/.local/bin:$PATH"

RUN curl https://pyenv.run | bash \
    && echo "installed pyenv" \
    && pyenv install ${PYTHON_VERSION} \
    && echo 'eval "$(pyenv init -)"' >> ~/.bashrc \
    && echo 'eval "$(pyenv init -)"' >> ~/.profile \
    && echo "installed python ${PYTHON_VERSION}" \
    && pyenv global ${PYTHON_VERSION} \
    && echo "set global python version ${PYTHON_VERSION}" \
    && curl -sSL https://install.python-poetry.org | python3 - \
    && poetry config virtualenvs.in-project true

# Advent of Code
COPY --link --chown=${USER}:${USER} AOC_TOKE[N] ${HOME}.config/aocd/token
