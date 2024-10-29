run_api:
	uvicorn tabular_data.apifile:app --reload

docker_build_local:
	@docker build --tag $(DOCKER_IMAGE):dev .

docker_run_local:
	@docker run -it -e PORT=8000 -p 8000:8000 $(DOCKER_IMAGE):dev
