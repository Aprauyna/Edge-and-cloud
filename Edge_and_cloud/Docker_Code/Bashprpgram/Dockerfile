FROM ubuntu:22.04 as bashpro
LABEL developer="shivam162@gmail.com"
WORKDIR /myapp
COPY HelloWorld.sh /myapp/
RUN chmod "700" "/myapp/HelloWorld.sh"
ENTRYPOINT [ "/myapp/HelloWorld.sh" ]