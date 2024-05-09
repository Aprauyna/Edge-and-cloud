FROM gcc

LABEL developer="arunsingh@gmail.com"

WORKDIR /usr/src/cap

COPY . .

RUN gcc "example.c"

CMD [ "./a.out" ]