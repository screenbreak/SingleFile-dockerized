import subprocess
from flask import Flask, request, Response

server = Flask(__name__)

SINGLEFILE_EXECUTABLE = '/node_modules/single-file/cli/single-file'
BROWSER_PATH = '/opt/google/chrome/google-chrome'
BROWSER_ARGS = '["--no-sandbox"]'


@server.route('/', methods=['POST'])
def singlefile():
    url = request.form.get('url')
    if url:
        p = subprocess.Popen([
            SINGLEFILE_EXECUTABLE,
            '--browser-executable-path=' + BROWSER_PATH,
            "--browser-args='%s'" % BROWSER_ARGS,
            request.form['url'],
            '--dump-content',
            ],
            stdout=subprocess.PIPE)
    else:
        return Response('Error: url parameter not found.',
                        status=500)
    singlefile_html = p.stdout.read()
    return Response(
        singlefile_html,
        mimetype="text/html",
    )


if __name__ == '__main__':
    server.run(host='0.0.0.0', port=80)
