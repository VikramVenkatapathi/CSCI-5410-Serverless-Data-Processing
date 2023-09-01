FROM python

WORKDIR /app

COPY . .

COPY assignment-2-390620-60700558380c.json /app/assignment-2-390620-60700558380c.json

ENV GOOGLE_APPLICATION_CREDENTIALS /app/assignment-2-390620-60700558380c.json

RUN pip install --no-cache-dir -r requirements.txt

# COPY registration_handler.py .

EXPOSE 5000

# CMD ["python3", "server.py"]
CMD ["python3", "-m","registration_handler", "run", "--host=0.0.0.0", "--port=5000"]
