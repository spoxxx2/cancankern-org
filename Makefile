publish:
	@echo "--- DEPLOYING SGO v1.3 ---"
	git add .
	git commit -m "site update: $(shell date)" || true
	git push origin main
	@echo "--- CANCAN KERN SITE LIVE ---"
