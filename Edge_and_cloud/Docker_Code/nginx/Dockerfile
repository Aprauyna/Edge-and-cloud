FROM nginx:1.25.3-alpine
WORKDIR /usr/share/nginx/html
COPY index.html /usr/share/nginx/html
EXPOSE 8080
CMD [ "nginx", "-g", "daemon off;" ]


# sudo docker build -t nginx .
# sudo docker run -d  --name ngnixcontainer -p  8080:80  nginx
#localhost:8080

