FROM dahanna/python-alpine-package:tox-alpine
RUN python -m pip install detectron2 -f https://dl.fbaipublicfiles.com/detectron2/wheels/cu101/torch1.5/index.html \
    && python -m virtualenv -vvv --with-traceback --system-site-packages --no-download py38 \
    && py38/bin/python -m pip install . \
    && tox --recreate -vv --sitepackages

# ENTRYPOINT ["py38/bin/python", "-m", "pip", "install", "."]
ENTRYPOINT ["tox", "--recreate", "-vv", "--sitepackages"]

