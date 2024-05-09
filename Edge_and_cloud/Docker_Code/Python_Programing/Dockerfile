FROM python:3

WORKDIR /usr/src/pythonapp

COPY require.txt /usr/src/pythonapp/

RUN pip install --no-cache-dir -r require.txt

COPY . .

CMD [ "python", "pandas_demo.py" ]