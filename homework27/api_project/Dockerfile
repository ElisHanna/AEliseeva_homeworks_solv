FROM python:3.8
COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r /usr/src/app/requirements.txt
COPY env.py /usr/src/app/
COPY test_data.py /usr/src/app/
COPY api_actions.py /usr/src/app/
COPY pytest.ini /usr/src/app/
COPY __init__.py /usr/src/app/
COPY test_apidoc.py /usr/src/app/
CMD ["pytest", "-v", "homework27/", "--alluredir=allure-results"]