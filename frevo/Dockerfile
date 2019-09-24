FROM openjdk:8-jdk-slim

RUN apt update && \
    apt install -y ant

RUN addgroup --gid 1000 frevo && \
    adduser --uid 1000 --ingroup frevo --system frevo

COPY repo/frevo /home/frevo
RUN chown -R frevo:frevo /home/frevo
RUN rm /home/frevo/testsuite/hashes/*
WORKDIR /home/frevo

USER frevo
RUN ant build
RUN java -jar createscripts.jar

# mount to export hash files
VOLUME /home/frevo/testsuite/hashes

WORKDIR testsuite

# Remove piping of errors
RUN sed -i 's/>\/dev\/null 2>&1//g' testsuite.sh
# Temporarily remove remote minisim test
RUN rm testcases/MiniSim_NNGA_FMeshed_AR.zse
ENTRYPOINT ["./testsuite.sh"]
