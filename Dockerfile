FROM python:3.7
COPY . /app
WORKDIR /app
ENV GOOGLE_APPLICATION_CREDENTIALS API-59a21c3115c7.json
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]