package main.java;

import org.apache.logging.log4j.LogManager;
import org.apache.logging.log4j.Logger;
import spark.Spark;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;

public class Server {

    static Logger log = LogManager.getLogger(Server.class.getName());

    public static void main(String[] args) {

        log.info("Server started!");

        Spark.port(8080);
        Spark.get("/", (req, res) -> {
            try {
                String htmlFilePath = "/home/bogdan/Desktop/server-try2/Server-vulnerabil/src/main/java/main/java/login.html";
                return new String(Files.readAllBytes(Paths.get(htmlFilePath)));
            } catch (IOException e) {
                log.error("Eroare la citire", e);
                res.status(500);
                return "Eroare la incarcarea resursei";
            }
        });


        Spark.post("/login", (req, res) -> {
            String username = req.queryParams("username");
            String password = req.queryParams("password");

            log.info("User " + username + " tried to login");


            if ("admin".equals(username) && "admin".equals(password)) {
                return "Welcome, " + username + "!";
            } else {
                return "Invalid credentials. Please try again.";
            }
        });
    }
}
