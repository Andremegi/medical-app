run_api:
	uvicorn images.api:app --reload

docker_build_local:
	@docker build --tag $(GAR_IMAGE):dev .

docker_run_local:
	@docker run -it -e PORT=8000 -p 8000:8000 $(GAR_IMAGE):dev

docker_build_cloud:
	@docker build \
		--platform linux/amd64 \
		-t $(GCP_REGION)-docker.pkg.dev/$(GCP_PROJECT)/$(ARTIFACTSREPO)/$(GAR_IMAGE):prod .

docker_push_cloud:
	@docker push $(GCP_REGION)-docker.pkg.dev/$(GCP_PROJECT)/$(ARTIFACTSREPO)/$(GAR_IMAGE):prod

docker_deploy_cloud:
	gcloud run deploy --image $(GCP_REGION)-docker.pkg.dev/$(GCP_PROJECT)/$(ARTIFACTSREPO)/$(GAR_IMAGE):prod \
		--timeout=300 \
		--memory $(GAR_MEMORY) \
		--region $(GCP_REGION) \
		--env-vars-file .env.yaml

streamlit:
	-@streamlit run frontend/streamlit_app.py

################### DATA SOURCES ACTIONS ################

reset_gcs_files:
	-gsutil rm -r gs://${BUCKET_NAME}
	-gsutil mb -p ${GCP_PROJECT} -l ${GCP_REGION} gs://${BUCKET_NAME}

upload_gcs_image_model:
	python -c "from images.logic.model import save_model_gcs; save_model_gcs('/Users/artem/Downloads/model_3.keras')"

upload_gcs_chat_bot_model:
	python -c "from chat_bot.model import upload_model_tokenizer_to_gcs; upload_model_tokenizer_to_gcs('/Users/artem/Downloads')"
