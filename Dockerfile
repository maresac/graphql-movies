FROM python:3.8-alpine as builder

WORKDIR /tmp
COPY ./ /tmp
RUN apk add --no-cache git\
 && python setup.py bdist_wheel

FROM python:3.8-alpine

COPY --from=builder /tmp/dist/graphqlmovies-*.whl /tmp
RUN pip install --no-cache-dir /tmp/graphqlmovies-*.whl gunicorn
EXPOSE 5000/tcp
ENTRYPOINT ["gunicorn", "--bind", "0.0.0.0:5000", "graphqlmovies.app:app"]
