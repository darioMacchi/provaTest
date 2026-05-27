FROM python

WORKDIR /app

COPY main.py .
COPY README.md .

# oppure CMD
ENTRYPOINT ["python3", "main.py"]
