A simple server for converting documents using Flask, Pandoc, and AWS.

Installation:

`git clone https://github.com/razzius/flask_pandoc.git`

`virtualenv venv` or `mkvirtualenv pandoc` (with virtualenvwrapper)

`pip install -r requirements.txt`

Configuration: Add these to your venv/bin/activate

`export AWS_ACCESS_KEY_ID='xxxxxxxxxxxxxxxxxxxx'`

`export AWS_SECRET_ACCESS_KEY='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'`

Running the server:

`python flask_pandoc.py`
` * Running on http://127.0.0.1:5000/`

Other:

`util.py` can be run to create a bucket for use with S3.