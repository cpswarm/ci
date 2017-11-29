FROM openjdk:8-jre-alpine

RUN adduser -u 1000 -S frevo
USER frevo

COPY repo/frevo /home/frevo
WORKDIR /home/frevo
RUN java -jar createscripts.jar

# mount to export hash files
VOLUME /home/frevo/testsuite/hashes

WORKDIR testsuite
ENTRYPOINT ["sh", "testsuite.sh"]

## Running locally:
# git clone https://git.repository-pert.ismb.it/ftavakolizadeh/ContinuousIntegration.git
# git clone https://git.repository-pert.ismb.it/mrappaport/cpswarm.git repo
# docker build -t frevo-test .
# docker run -v $(pwd)/hashes:/home/frevo/testsuite/hashes --rm frevo-test -renew
# docker run -v $(pwd)/hashes:/home/frevo/testsuite/hashes --rm frevo-test