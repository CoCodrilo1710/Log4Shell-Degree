#!/bin/bash

PROCESS_ID=$(ps -ef | grep "main.java.Server" | grep -v grep | awk '{print $2}')

if [ ! -z "$PROCESS_ID" ]; then
    kill $PROCESS_ID

    wait $PROCESS_ID 2>/dev/null
fi
./mvnw exec:java -Dexec.mainClass=main.java.Server
