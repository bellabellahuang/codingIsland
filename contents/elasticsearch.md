### ElasticSearch Local Setup

#### [Installation](https://www.elastic.co/downloads/elasticsearch)

#### Configuration

* Configure CORS in elasticsearch.yml

        http.cors.enabled: true
        http.cors.allow-origin: '*'

* Load data into elasticsearch using docker

        docker run --rm -v ~/.aws/:/root/.aws --network=host bbtv/elastic-loader:latest YYYYMMDD http://host.docker.internal:9200/

