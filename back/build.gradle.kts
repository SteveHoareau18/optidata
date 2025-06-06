plugins {
    java
    id("org.springframework.boot") version "3.4.1"
    id("io.spring.dependency-management") version "1.1.7"
}

group = "fr.optidata"
version = "0.0.1-SNAPSHOT"

java {
    toolchain {
        languageVersion = JavaLanguageVersion.of(23)
    }
}

configurations {
    compileOnly {
        extendsFrom(configurations.annotationProcessor.get())
    }
}

repositories {
    mavenCentral()
}

dependencies {
    implementation("org.hibernate.validator:hibernate-validator:8.0.0.Final")
    implementation("org.springdoc:springdoc-openapi-starter-webmvc-ui:2.0.4")
    implementation("org.springframework.boot:spring-boot-starter-data-jpa")
    implementation("org.springframework.boot:spring-boot-devtools")
    implementation("org.springframework.boot:spring-boot-starter-security")
    implementation("org.springframework.boot:spring-boot-starter-web")
    implementation("org.springdoc:springdoc-openapi-starter-webmvc-ui:2.8.4")
    implementation("jakarta.validation:jakarta.validation-api:3.1.1")
    implementation("io.jsonwebtoken:jjwt-api:0.12.6")
    compileOnly("org.projectlombok:lombok")
    runtimeOnly("io.jsonwebtoken:jjwt-impl:0.12.6")
// https://mvnrepository.com/artifact/org.mariadb.jdbc/mariadb-java-client
    implementation("org.mariadb.jdbc:mariadb-java-client:3.5.2")
    // https://mvnrepository.com/artifact/org.mariadb.jdbc/mariadb-java-client
    runtimeOnly("org.mariadb.jdbc:mariadb-java-client:3.5.2")
    runtimeOnly("io.jsonwebtoken:jjwt-jackson:0.12.6")
    annotationProcessor("org.projectlombok:lombok")
    testImplementation("org.springframework.boot:spring-boot-starter-test")
    testImplementation("org.springframework.security:spring-security-test")
    testRuntimeOnly("org.junit.platform:junit-platform-launcher")
}

tasks.withType<Test> {
}