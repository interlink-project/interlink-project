# This script need optimisation


.PHONY: danger warning success

# Colores
RED := \033[0;31m
YELLOW := \033[0;33m
GREEN := \033[0;32m
PURPLE := \033[0;35m
NC := \033[0m

define check_variables_template
	$(eval SECRETS_FILE := $1)
	$(eval MANDATORYVARIABLES := $2)
	$(eval ENVIRONMENT := $3)
	make info message="---------------------------------------------------------"
	make info message="| Checking mandatory variables for $(ENVIRONMENT) |"
	make info message="---------------------------------------------------------"
	@if [ -f $(SECRETS_FILE) ]; then \
		for variable in $(MANDATORYVARIABLES); do \
			if grep -q "^$$variable=" $(SECRETS_FILE); then \
				make success message="The variable $$variable is defined"; \
			else \
				make warning message="The variable $$variable is not defined. Please define it."; \
				read -p "Enter the value for $$variable: " value; \
				echo "$$variable=$$value" >> $(SECRETS_FILE); \
				make success message="The variable $$variable has been defined"; \
			fi; \
		done; \
	else \
		make warning message="The file $(SECRETS_FILE) does not exist"; \
		touch $(SECRETS_FILE); \
		make warning message="The file $(SECRETS_FILE) has been created. Please define the variables"; \
		for variable in $(MANDATORYVARIABLES); do \
			make danger message="The variable $$variable is not defined. Please define it."; \
			read -p "Enter the value for $$variable: " value; \
			echo "$$variable=$$value" >> $(SECRETS_FILE); \
			make success message="The variable $$variable has been defined"; \
		done; \
	fi
endef

check_variables_coproduction:
	$(call check_variables_template,../backend-coproduction/.secrets,AUTH0_CLIENT_ID AUTH0_JWK_URL,BACKEND-COPRODUCTION)

check_variables_auth:
	$(call check_variables_template,../backend-auth/.secrets,CLIENT_SECRET AUTH0_CLIENT_ID AUTH0_CLIENT_SECRET AUTH0_DOMAIN,BACKEND-AUTH)

check_variables_catalogue:
	$(call check_variables_template,../backend-catalogue/.secrets,AUTH0_CLIENT_ID AUTH0_JWK_URL,BACKEND-CATALOGUE)

check_variables_googledrive:
	$(call check_variables_template,../interlinker-googledrive/.secrets,GOOGLE_PROJECT_ID GOOGLE_PRIVATE_KEY_ID GOOGLE_PRIVATE_KEY GOOGLE_CLIENT_EMAIL GOOGLE_CLIENT_ID,BACKEND-INTERLINKER-GOOGLEDRIVE)

clean:
	@read -p "Are you sure you want to delete all secrets files? [y/N]: " confirm && \
		[[ $$confirm == [yY] || $$confirm == [yY][eE][sS] ]] || exit 1
	make danger message="---------------"
	make danger message="| Cleaning up |"
	make danger message="---------------"
	@rm -f ../backend-coproduction/.secrets
	@rm -f ../backend-auth/.secrets
	@rm -f ../backend-catalogue/.secrets
	@rm -f ../interlinker-googledrive/.secrets
	make success message="The secrets files have been deleted"


danger:
	@echo -e "$(RED)[-]$(NC) $(message)"

warning:
	@echo -e "$(YELLOW)[ ]$(NC) $(message)"

success:
	@echo -e "$(GREEN)[+]$(NC) $(message)"

info:
	@echo -e "$(PURPLE)[*]$(NC) $(message)"
