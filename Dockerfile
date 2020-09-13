FROM buildkite/puppeteer

RUN apt-get update \
     && apt-get install -y git

RUN npm install 'gildas-lormeau/SingleFile#master'

WORKDIR /opt/app

RUN apt-get update && apt-get install --no-install-recommends -y \
      python3 python3-pip python3-setuptools

COPY requirements.txt .
COPY webserver.py .

RUN pip3 install \
    --no-cache-dir \
    --no-warn-script-location \
    --user \
    -r requirements.txt

RUN rm requirements.txt
