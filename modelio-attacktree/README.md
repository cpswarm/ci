# Modelio - Attack Tree Designer - CI

## Test


docker build -t attacktreetest .

docker run -d -v ./attack-tree:/attack-tree  -v ${JMDAC_ARCIVES_PATH}:/module_jmdac_archives attacktreetest

