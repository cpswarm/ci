FROM openjdk:8-jdk-slim

RUN apt update && \
    apt install -y ant

RUN adduser --uid 1000 --system frevo

COPY repo/frevo /home/frevo
RUN chown -R frevo /home/frevo
WORKDIR /home/frevo

USER frevo
RUN ant build
RUN java -jar createscripts.jar

# mount to export hash files
VOLUME /home/frevo/testsuite/hashes

WORKDIR testsuite
ENTRYPOINT ["./testsuite.sh"]

## Running locally:
# git clone https://git.repository-pert.ismb.it/ftavakolizadeh/ContinuousIntegration.git
# git clone https://git.repository-pert.ismb.it/mrappaport/cpswarm.git repo
# docker build -t frevo-test .
# docker run -v $(pwd)/hashes:/home/frevo/testsuite/hashes --rm frevo-test -renew
# docker run -v $(pwd)/hashes:/home/frevo/testsuite/hashes --rm frevo-test