FROM willfarrell/crontab

# Install python/pip
ENV PYTHONUNBUFFERED=1
ENV PIP_ROOT_USER_ACTION=ignore

RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip

ADD --chown=root:root --chmod=755 entrypoint.sh .
RUN chmod +x entrypoint.sh
ENTRYPOINT ["sh", "/entrypoint.sh"]
# CMD ["./entrypoint.sh"]
