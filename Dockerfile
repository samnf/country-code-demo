FROM python:3.9

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY country_code_rest.py .

EXPOSE 8000

CMD [ "uvicorn", "country_code_rest:app" ]