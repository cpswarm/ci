## Running locally:
# git clone https://git.repository-pert.ismb.it/ftavakolizadeh/ContinuousIntegration.git
# git clone https://git.repository-pert.ismb.it/mrappaport/cpswarm.git frevo/cpswarm
# docker build -t frevo-test .
# docker run -v /path-to-testsuite:/home/testsuite frevo-test

FROM openjdk:8-jre-slim

COPY cpswarm/frevo /home

WORKDIR /home
RUN java -jar createscripts.jar

# testsuite files must be mounted
# TODO: only mount hash files directory (requires script modification)
VOLUME /home/testsuite
WORKDIR testsuite
ENTRYPOINT [ "./testsuite.sh"]