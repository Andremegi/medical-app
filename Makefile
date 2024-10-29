run_api:
	uvicorn tabular_data.apifile:app --reload

docker_build_local:
	@docker build --tag $(GAR_IMAGE):dev .

docker_run_local:
	@docker run -it -e PORT=8000 -p 8000:8000 $(GAR_IMAGE):dev

docker_build_cloud:
	@docker build \
		--platform linux/amd64 \
		-t $(GCP_REGION)-docker.pkg.dev/$(GCP_PROJECT)/medicalapp/$(GAR_IMAGE):prod .

docker_push_cloud:
	@docker push $(GCP_REGION)-docker.pkg.dev/$(GCP_PROJECT)/medicalapp/$(GAR_IMAGE):prod

docker_deploy_cloud:
	gcloud run deploy --image $(GCP_REGION)-docker.pkg.dev/$(GCP_PROJECT)/medicalapp/$(GAR_IMAGE):prod \
		--memory $(GAR_MEMORY) \
		--region $(GCP_REGION) \
		--env-vars-file .env.yaml
