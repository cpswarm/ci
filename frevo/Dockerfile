FROM openjdk:8-jre-slim

# git clone https://git.repository-pert.ismb.it/mrappaport/cpswarm.git
# git clone https://git.repository-pert.ismb.it/ftavakolizadeh/ContinuousIntegration.git cpswarm

COPY cpswarm/frevo /home
COPY testsuite /home/testsuite

WORKDIR /home
RUN java -jar createscripts.jar

WORKDIR testsuite
ENTRYPOINT [ "./testsuite.sh" ]