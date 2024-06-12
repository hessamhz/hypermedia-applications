FROM python:3.10-alpine

ENV APP_HOME=/usr/src/app

RUN mkdir $APP_HOME

WORKDIR $APP_HOME

ENV PYTHONDONTWRITEBYTECODE 1

ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add libcurl curl-dev python3-dev libc-dev postgresql-dev build-base gcc python3-dev musl-dev libffi-dev \
    py3-pillow freetype-dev libpng-dev openblas-dev g++ \
    jpeg-dev zlib-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev libxslt-dev

RUN pip install --upgrade pip

COPY ../requirements/production.txt $APP_HOME/production.txt
RUN pip install -r production.txt --no-cache-dir

RUN addgroup -S app && adduser -S app -G app


COPY ../build/entrypoint.sh $APP_HOME/entrypoint.sh
RUN chmod +x $APP_HOME/entrypoint.sh

# copy project
COPY ../manage.py $APP_HOME
COPY ../src $APP_HOME/src
COPY ../settings $APP_HOME/settings

# chown all the files to the app user
RUN chmod +x $APP_HOME/manage.py
RUN chown -R app:app $APP_HOME

# change to the app user
USER app

ENTRYPOINT [ "/usr/src/app/entrypoint.sh" ]
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "3", "src.core.wsgi:application"]
