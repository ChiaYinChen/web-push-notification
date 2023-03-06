FROM node:16
WORKDIR /code
ENV TZ=Asia/Taipei
COPY ./package.json .
RUN npm install
COPY . .
ENTRYPOINT ["npm"]