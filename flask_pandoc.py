from subprocess import Popen, PIPE
from os import environ
from datetime import datetime

from flask import Flask, request, abort, jsonify
from boto import connect_s3, s3

app = Flask(__name__)

AWS_ACCESS_KEY_ID = environ['AWS_ACCESS_KEY_ID']
AWS_SECRET_KEY = environ['AWS_SECRET_KEY']

@app.route('/', methods=['POST'])
def convert():
	html = request.values.get('html')
	if not html:
		abort(400)
	docs = create_documents(html)
	upload_documents(docs)
	info = {"docs": docs}
	return jsonify(info)


def create_documents(html):
	iso_time = datetime.now().isoformat()
	formats = ['pdf', 'docx']
	# 2013-11-12T19:59:09.768845.pdf, for example.
	docs = ["{}.{}".format(iso_time, format) for format in formats]
	for doc in docs:
		create_file(html, doc)
	return docs

def create_file(html, name):
	p = Popen(['pandoc', '-f', 'html', '-o', name], stdin=PIPE)
	p.communicate(html)

def upload_documents(docs):
	conn = connect_s3(AWS_ACCESS_KEY_ID, AWS_SECRET_KEY)
	bucket = conn.get_bucket('emerald_test_bucket')
	for doc in docs:
		key = s3.key.Key(bucket)
		key.name = doc
		key.set_contents_from_filename(doc)


if __name__ == '__main__':
	app.run(debug=True)
