FROM nginx:alpine

RUN rm /etc/nginx/nginx.conf
COPY nginx.conf /etc/nginx/
RUN rm /etc/nginx/conf.d/default.conf

COPY backend.conf /etc/nginx/conf.d/
COPY bot.conf /etc/nginx/conf.d/