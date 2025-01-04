FROM python

WORKDIR /app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8080

CMD [ "fastapi", "run", "src/main.py", "--workers", "4", "--port", "8080" ]