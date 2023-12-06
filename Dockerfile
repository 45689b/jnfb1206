FROM python:3
WORKDIR /demo

COPY main.py .

RUN chmod +x main.py && python3 main.py init cf && chmod +x ./*

EXPOSE 8080

CMD ["python3", "main.py", "run"]

USER 10001
