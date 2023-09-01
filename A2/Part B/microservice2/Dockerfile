FROM python

WORKDIR /app

COPY . .

COPY assignment-2-390620-60700558380c.json /app/assignment-2-390620-60700558380c.json

ENV GOOGLE_APPLICATION_CREDENTIALS /app/assignment-2-390620-60700558380c.json

RUN pip install --no-cache-dir -r requirements.txt
# RUN pip install --upgrade google-cloud-firestore
# RUN python -m pip install google-cloud-firestore
# RUN pip uninstall google-cloud-firestore
# RUN pip install google-cloud-firestore

# COPY registration_handler.py .

EXPOSE 5001

# CMD ["python3", "server.py"]
CMD ["python3", "-m","login_handler", "run", "--host=0.0.0.0", "--port=5001"]
