# SingleFile-dockerized
SingleFile docker implementation providing access via either a dockerized-CLI or a WEB service.

Prototype work:
https://github.com/gildas-lormeau/SingleFile

## Usage

### Option #1: Run it directly from your docker host:

```bash
docker pull screenbreak/singlefile-dockerized
docker run -it screenbreak/singlefile-dockerized http://www.example.com/
```
You will get the HTML output of SingleFile in your console stdout.

### Option #2: Deploy it as a webserver in a docker-compose.yml:

```yaml
version: '3'
services:
  singlefile:
    container_name: singlefile
    image: screenbreak/singlefile-dockerized
    entrypoint: python3
    command: webserver.py
    expose:
      - 80
```

Then any HTTP POST on port 80 with url parameter will respond with the HTML output of SingleFile in the payload:

```bash
curl -d 'url=http://www.example.com/' singlefile:80
```

### Output example:

```html
<!DOCTYPE html> <html><!--
 Page saved with SingleFile 
 url: http://www.example.com/ 
 saved date: Sun Sep 13 2020 18:21:28 GMT+0000 (Coordinated Universal Time)
--><meta charset=utf-8>
<title>Example Domain</title>
<meta name=viewport content="width=device-width, initial-scale=1">
<style>body{background-color:#f0f0f2;margin:0;padding:0;font-family:-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI","Open Sans","Helvetica Neue",Helvetica,Arial,sans-serif}div{width:600px;margin:5em auto;padding:2em;background-color:#fdfdff;border-radius:0.5em;box-shadow:2px 3px 7px 2px rgba(0,0,0,0.02)}a:link,a:visited{color:#38488f;text-decoration:none}@media (max-width:700px){div{margin:0 auto;width:auto}}</style>
<link rel=canonical href=http://www.example.com/></head>
<body>
<div>
 <h1>Example Domain</h1>
 <p>This domain is for use in illustrative examples in documents. You may use this
 domain in literature without prior coordination or asking for permission.</p>
 <p><a href=https://www.iana.org/domains/example>More information...</a></p>
</div>
```
