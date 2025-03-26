FROM eclipse-temurin:23-jdk-alpine

RUN apk add --no-cache gradle bash

WORKDIR /app

COPY . .

CMD rm -rf .gradle/
CMD rm -rf build/

CMD ["sh", "-c", "gradle build && gradle bootRun"]