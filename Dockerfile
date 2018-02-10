FROM python:2.7

ADD . /app
WORKDIR /app

# Install dependencies
RUN  apt-get update \
  && apt-get install -y wget unzip

# Download catalog dataset
RUN wget -qO- https://s3.us-east-2.amazonaws.com/case-study.dafiti.gfg.science/catalog-data.csv.gz \
  | unzip > data/catalog-data.csv

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]

CMD ["app/app.py"]
