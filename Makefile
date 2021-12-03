PROJECT_NAME ?= dbproject
VERSION = $(shell python3 setup.py --version | tr '+' '-')
PROJECT_NAMESPACE ?= aaab
REGISTRY_IMAGE ?= $(PROJECT_NAMESPACE)/$(PROJECT_NAME)

all:
	@echo "make devenv		- Create & setup development virtual environment"
	@echo "make postgres	- Start postgres container"
	@echo "make clean		- Remove files created by distutils"
	@echo "make sdist		- Make source distribution"
	@echo "make docker		- Build a docker image"
	@exit 0

clean:
	rm -fr *.egg-info dist

devenv: clean
	rm -rf env
	# создаем новое окружение
	python3.8 -m venv env
	# обновляем pip
	env/bin/pip install -U pip
	# устанавливаем основные + dev зависимости из extras_require (см. setup.py)
	env/bin/pip install -Ue '.[dev]'

postgres:
	docker stop analyzer-postgres || true
	docker run --rm --detach --name=dbproject-postgres \
		--env POSTGRES_USER=user \
		--env POSTGRES_PASSWORD=password \
		--env POSTGRES_DB=dbproject \
		--publish 5432:5432 postgres

sdist: clean
	# официальный способ дистрибуции python-модулей
	python3 setup.py sdist

docker: sdist
	docker build --target=api -t $(PROJECT_NAME):$(VERSION) .
