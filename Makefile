.PHONY: help install install-marketplace install-plugins uninstall uninstall-plugins uninstall-marketplace reinstall

# Get the absolute path to this directory
ROOT_DIR := $(shell pwd)

help:
	@echo "Claude Hub Plugin Management"
	@echo ""
	@echo "Usage:"
	@echo "  make install              Install marketplace and all plugins"
	@echo "  make install-marketplace  Install just the marketplace"
	@echo "  make install-plugins      Install all plugins (requires marketplace)"
	@echo "  make uninstall            Uninstall all plugins and marketplace"
	@echo "  make uninstall-plugins    Uninstall just the plugins"
	@echo "  make uninstall-marketplace Uninstall just the marketplace"
	@echo "  make reinstall            Reinstall everything (uninstall then install)"

install: install-marketplace install-plugins
	@echo "✓ Installation complete"

install-marketplace:
	@if claude plugin marketplace list 2>/dev/null | grep -q "claude-hub"; then \
		echo "Marketplace already installed"; \
	else \
		echo "Installing marketplace from: $(ROOT_DIR)"; \
		claude plugin marketplace add $(ROOT_DIR); \
		echo "✓ Marketplace installed"; \
	fi

install-plugins:
	@if claude plugin list 2>/dev/null | grep -q "github"; then \
		echo "Plugin 'github' already installed"; \
	else \
		echo "Installing plugins..."; \
		claude plugin install github@claude-hub; \
		echo "✓ Plugins installed"; \
	fi

uninstall: uninstall-plugins uninstall-marketplace
	@echo "✓ Uninstall complete"

uninstall-plugins:
	@if claude plugin list 2>/dev/null | grep -q "github"; then \
		echo "Uninstalling plugins..."; \
		claude plugin uninstall github; \
		echo "✓ Plugins uninstalled"; \
	else \
		echo "Plugin 'github' not installed, skipping"; \
	fi

uninstall-marketplace:
	@if claude plugin marketplace list 2>/dev/null | grep -q "claude-hub"; then \
		echo "Uninstalling marketplace..."; \
		claude plugin marketplace remove claude-hub; \
		echo "✓ Marketplace uninstalled"; \
	else \
		echo "Marketplace not installed, skipping"; \
	fi

reinstall: uninstall install
	@echo "✓ Reinstall complete"
