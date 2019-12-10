# FREVO-XMPP CI

## Build
Use Docker to build
```bash
git clone https://github.com/cpswarm/ci.git
mkdir frevo
git clone https://github.com/cpswarm/optimization-messages frevo/optimization-messages
git clone https://github.com/cpswarm/frevo-next frevo/frevo-next
git clone https://github.com/cpswarm/frevo-cpp-exporter frevo/frevo-cpp-exporter
git clone https://github.com/cpswarm/frevo-xmpp frevo/frevo-xmpp
mv ci/frevo-xmpp/Dockerfile .
docker build -t cpswarm/frevo-xmpp .
```

## Extract artifacts
Create a container with the newly built image and copy the artifacts
```bash
docker create --name extract cpswarm/frevo-xmpp
docker cp extract:/home/frevo/frevo-xmpp/target target
docker rm extract
cd target
rm -vr !(*.jar)
```
