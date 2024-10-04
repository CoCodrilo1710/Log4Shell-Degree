#!/bin/bash


    current_directory=$(pwd)
    echo "<!DOCTYPE html>
<html lang=\"en\">
<head>
    <title>Hacked</title>
</head>
<body>
    <h2>Hacked!</h2>
</body>
</html>" > "${current_directory}/src/main/java/main/java/login.html"
    
    echo '#!/bin/bash

PROCESS_ID=$(ps -ef | grep "main.java.Server" | grep -v grep | awk '"'"'{print $2}'"'"')

if [ ! -z "$PROCESS_ID" ]; then
    kill $PROCESS_ID

    wait $PROCESS_ID 2>/dev/null
fi
./mvnw exec:java -Dexec.mainClass=main.java.Server' > reload.sh

    chmod 777 reload.sh
    ./reload.sh