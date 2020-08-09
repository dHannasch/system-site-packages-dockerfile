FROM dahanna/python:3.7-detectron2-tox
COPY ./setup.py ./
RUN python -m virtualenv -vvv --with-traceback --system-site-packages --no-download py38 \
    && python -m pip install detectron2 \
    && py38/bin/python -m pip install . \
    && tox --recreate -vv --sitepackages

# ENTRYPOINT ["py38/bin/python", "-m", "pip", "install", "."]
ENTRYPOINT ["tox", "--recreate", "-vv", "--sitepackages"]

