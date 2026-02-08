.PHONY: help install-marketplace uninstall-marketplace add-claudehub remove-claudehub add-github remove-github

# Get the absolute path to this directory
ROOT_DIR := $(shell pwd)

help:
	@echo "Claude Hub Marketplace Management"
	@echo ""
	@echo "Usage:"
	@echo "  make install-marketplace    Install the marketplace"
	@echo "  make uninstall-marketplace  Uninstall the marketplace"
	@echo "  make add-claudehub          Install marketplace then reinstall claudehub plugin"
	@echo "  make remove-claudehub       Uninstall the claudehub plugin"
	@echo "  make add-github             Install marketplace then reinstall github plugin"
	@echo "  make remove-github          Uninstall the github plugin"

install-marketplace:
	@if claude plugin marketplace list 2>/dev/null | grep -q "claudehub"; then \
		echo "Marketplace already installed"; \
	else \
		echo "Installing marketplace from: $(ROOT_DIR)"; \
		claude plugin marketplace add $(ROOT_DIR); \
		echo "✓ Marketplace installed"; \
	fi

uninstall-marketplace:
	@if claude plugin marketplace list 2>/dev/null | grep -q "claudehub"; then \
		echo "Uninstalling marketplace..."; \
		claude plugin marketplace remove claudehub; \
		echo "✓ Marketplace uninstalled"; \
	else \
		echo "Marketplace not installed"; \
	fi

add-claudehub: install-marketplace remove-claudehub
	@echo "Installing claudehub plugin..."
	@claude plugin install claudehub@claudehub
	@echo "✓ claudehub plugin installed"

remove-claudehub:
	@if claude plugin list 2>/dev/null | grep -q "claudehub@claudehub"; then \
		echo "Uninstalling claudehub plugin..."; \
		claude plugin uninstall claudehub@claudehub; \
		echo "✓ claudehub plugin uninstalled"; \
	else \
		echo "claudehub plugin not installed"; \
	fi

add-github: install-marketplace remove-github
	@echo "Installing github plugin..."
	@claude plugin install github@claudehub
	@echo "✓ github plugin installed"

remove-github:
	@if claude plugin list 2>/dev/null | grep -q "github@claudehub"; then \
		echo "Uninstalling github plugin..."; \
		claude plugin uninstall github@claudehub; \
		echo "✓ github plugin uninstalled"; \
	else \
		echo "github plugin not installed"; \
	fi
