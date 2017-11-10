FROM openjdk:8-jre-slim

# git clone https://git.repository-pert.ismb.it/ftavakolizadeh/ContinuousIntegration.git
# git clone https://git.repository-pert.ismb.it/mrappaport/cpswarm.git frevo/cpswarm

COPY cpswarm/frevo /home

WORKDIR /home
RUN java -jar createscripts.jar

# testsuite files must be mounted
# TODO: only mount hash files directory (requires script modification)
VOLUME /home/testsuite
WORKDIR testsuite
ENTRYPOINT [ "./testsuite.sh"]