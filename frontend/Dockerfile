FROM node:17-alpine3.14
WORKDIR /code
ENV TZ=Asia/Taipei
COPY . .
RUN npm install
ENTRYPOINT ["npm"]