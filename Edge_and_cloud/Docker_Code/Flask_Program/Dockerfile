FROM python:3

WORKDIR /usr/src/pythonapp

COPY require1.txt /usr/src/pythonapp/

RUN pip install --no-cache-dir -r require1.txt

COPY . .

EXPOSE 5000

CMD [ "python", "flask_prog.py" ]