FROM python:3.11.9-alpine3.19
MAINTAINER Ivan Sliepov, slepow1985@gmail.com

#ENV http_proxy=http://proxy.lancope.ciscolabs.com:3128
#ENV https_proxy=http://proxy.lancope.ciscolabs.com:3128
#
COPY . /app
#
WORKDIR /app
#
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 8000
ENTRYPOINT ["uvicorn", "--host", "0.0.0.0", "main:app"]