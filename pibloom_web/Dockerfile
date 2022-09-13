################################################################################
# build stage: install npm and build web app
# FROM node:lts-alpine as build-stage
FROM arm64v8/node:lts-alpine as build-stage

WORKDIR /app
COPY package*.json ./

# install dependencies
RUN npm install
COPY . .

# build vue web app
RUN npm run build


################################################################################
# production stage: copy web app and serve it
# FROM node:lts-alpine as production-stage
FROM arm64v8/node:lts-alpine as production-stage
WORKDIR /app

# copy modules, server, and web app files
COPY --from=build-stage /app ./
EXPOSE 8080
CMD node server/server.js