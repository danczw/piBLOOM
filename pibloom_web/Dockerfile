# build stage: install npm and build web app
FROM node:lts-alpine as build-stage
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

# production stage: copy web app and serve it
FROM node:lts-alpine as production-stage
WORKDIR /app
COPY --from=build-stage /app ./
EXPOSE 8080
CMD node server/server.js