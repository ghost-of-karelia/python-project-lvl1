install:
	poetry install

build: 
	poetry build

brain-games:
	poetry run brain-games

brain-even:
	poetry run brain-even

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user dist/*.whl

lint:
	poetry run flake8 brain_games