FROM python:slim


COPY ./ /home
WORKDIR /home
RUN pip install -r requirements.txt

CMD ["python", "app.py"]
