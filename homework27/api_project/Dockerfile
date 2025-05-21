FROM python:3.8
COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt
COPY * /usr/src/app/
CMD ["pytest", "usr/src/app/test_apidoc.py"]