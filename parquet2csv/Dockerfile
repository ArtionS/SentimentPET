
FROM jupyter/all-spark-notebook

USER root 
RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip" && unzip awscliv2.zip && ./aws/install &&\
    apt-get update && apt-get install -y -qq less groff

COPY ./scripts /usr/local/bin

USER jovyan
WORKDIR /app