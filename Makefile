.PHONY: help install-marketplace uninstall-marketplace add-claudehub remove-claudehub add-rpi remove-rpi add-ralph remove-ralph add-github remove-github add-all remove-all

# Get the absolute path to this directory
ROOT_DIR := $(shell pwd)

help:
	@echo "Claude Hub Marketplace Management"
	@echo ""
	@echo "Usage:"
	@echo "  make install-marketplace    Install the marketplace"
	@echo "  make uninstall-marketplace  Uninstall the marketplace"
	@echo ""
	@echo "  make add-claudehub          Install claudehub coordinator plugin"
	@echo "  make remove-claudehub       Uninstall the claudehub plugin"
	@echo "  make add-rpi                Install rpi (research-plan-implement) plugin"
	@echo "  make remove-rpi             Uninstall the rpi plugin"
	@echo "  make add-ralph              Install ralph (autonomous execution) plugin"
	@echo "  make remove-ralph           Uninstall the ralph plugin"
	@echo "  make add-github             Install github plugin"
	@echo "  make remove-github          Uninstall the github plugin"
	@echo ""
	@echo "  make add-all                Install all 4 plugins"
	@echo "  make remove-all             Uninstall all 4 plugins"

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

add-rpi: install-marketplace remove-rpi
	@echo "Installing rpi plugin..."
	@claude plugin install rpi@claudehub
	@echo "✓ rpi plugin installed"

remove-rpi:
	@if claude plugin list 2>/dev/null | grep -q "rpi@claudehub"; then \
		echo "Uninstalling rpi plugin..."; \
		claude plugin uninstall rpi@claudehub; \
		echo "✓ rpi plugin uninstalled"; \
	else \
		echo "rpi plugin not installed"; \
	fi

add-ralph: install-marketplace remove-ralph
	@echo "Installing ralph plugin..."
	@claude plugin install ralph@claudehub
	@echo "✓ ralph plugin installed"

remove-ralph:
	@if claude plugin list 2>/dev/null | grep -q "ralph@claudehub"; then \
		echo "Uninstalling ralph plugin..."; \
		claude plugin uninstall ralph@claudehub; \
		echo "✓ ralph plugin uninstalled"; \
	else \
		echo "ralph plugin not installed"; \
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

add-all: install-marketplace remove-all
	@echo "Installing all plugins..."
	@claude plugin install claudehub@claudehub
	@claude plugin install rpi@claudehub
	@claude plugin install ralph@claudehub
	@claude plugin install github@claudehub
	@echo "✓ All plugins installed"

remove-all: remove-claudehub remove-rpi remove-ralph remove-github
	@echo "✓ All plugins removed"
