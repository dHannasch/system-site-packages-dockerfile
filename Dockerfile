FROM dahanna/python:3.8-detectron2

COPY ./setup.py ./
COPY ./tox.ini ./
COPY ./test_blah.py ./

RUN python -m pip install tox
    && python -m virtualenv -vvv --with-traceback --system-site-packages --no-download py38 \
    && python -m pip install detectron2 \
    # Without virtualenv involved, pip install detectron2 yields
    # Requirement already satisfied: detectron2 in /opt/conda/lib/python3.7/site-packages
    && py38/bin/python -m pip install . \
    && tox --recreate -vv --sitepackages

# ENTRYPOINT ["py38/bin/python", "-m", "pip", "install", "."]
ENTRYPOINT ["tox", "--recreate", "-vv", "--sitepackages"]

