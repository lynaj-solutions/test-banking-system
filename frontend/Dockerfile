# Stage 1 - build frontend app
FROM node:10-alpine as build-deps

# Set Oracle Java as the default Java
RUN apk update && \
    apk add openjdk8 && \
    apk add --no-cache firefox-esr && \
    apk add apache-ant;

# Setup JAVA_HOME -- useful for docker commandline
ENV JAVA_HOME /usr/lib/jvm/java-8-openjdk-amd64/
RUN export JAVA_HOME

WORKDIR /app/

COPY frontend/package.json frontend/package-lock.json /app/
RUN npm install

COPY frontend /app/
COPY .env /app/.env

CMD ["npm", "run", "nightwatch"]
CMD ["npm", "run", "test"]
