FROM nginx:stable-alpine3.20-perl
WORKDIR /app
COPY . /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]