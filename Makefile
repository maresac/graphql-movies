.PHONY: fmt clean detox test docker-build compose-up

fmt:
	black graphqlmovies tests

clean:
	find . -name "*.py[c|o]" -delete

detox: clean
	rm -rf .tox

test: fmt clean
	tox

docker-build:
	docker build -t graphqlmovies .

compose-up:
	docker-compose up -d
