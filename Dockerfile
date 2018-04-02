FROM python:2.7

# add folder contents to container
WORKDIR /app
ADD . /app

# install source code
RUN chmod +x setup.py
RUN python setup.py install
