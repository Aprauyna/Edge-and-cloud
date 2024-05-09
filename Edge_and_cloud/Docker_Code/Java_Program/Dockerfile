FROM openjdk
# FROM eclipse/ubuntu_jdk8

WORKDIR /usr/src/javaapp

COPY . /usr/src/javaapp

RUN javac "Book.java"

CMD [ "java", "Book" ]