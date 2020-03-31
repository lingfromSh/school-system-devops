FROM alpine:latest

LABEL AUTHOR="Stephen Ling"
LABEL EMAIL="lingfromsh@163.com"

# Environment

ENV PIP_REQUIREMENTS="/root/requirements.txt"
ENV PROJECT_NAME="School-System"
ENV PROJECT_AUTHOR="Stephen Ling"
ENV PROJECT_AUTHOR_EMAIL="lingfromsh@163.com"
ENV PROJECT_WORKDIR="/root/school-system"
ENV GIT_REPO=""

VOLUME [ ${PROJECT_WORKDIR} ]

# EXPOSE PORT
EXPOSE 8000

# Add requirements for python lib
COPY ./python/requirements.txt /root/requirements.txt
# Use Tsinghua mirror instead of original apk source
COPY ./apk/repositories /etc/apk/repositories

RUN apk update && apk upgrade && apk add git python3 python3-dev gcc g++ linux-headers libffi-dev openssl-dev postgresql-dev && \
    pip3 config set global.index-url "https://pypi.tuna.tsinghua.edu.cn/simple" && \
    pip3 install -U pip && pip3 install -r ${PIP_REQUIREMENTS} && \
    git clone https://github.com/lingfromSh/school-system-core.git ${PROJECT_WORKDIR} && \
    echo -e "\033[0;32m Build Successully \033[0m"

WORKDIR ${PROJECT_WORKDIR}

CMD ["/bin/sh"]
