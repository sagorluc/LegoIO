FROM elasticsearch:7.5.1

# container creator
MAINTAINER orkb

# copy the configuration file into the container
COPY es.yml /usr/share/elasticsearch/config

# expose the default Elasticsearch port
EXPOSE 9200
