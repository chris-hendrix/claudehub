.PHONY: help install install-marketplace install-plugins uninstall reinstall

# Get the absolute path to this directory
ROOT_DIR := $(shell pwd)

help:
	@echo "Claude Hub Plugin Management"
	@echo ""
	@echo "Usage:"
	@echo "  make install              Install marketplace and all plugins"
	@echo "  make install-marketplace  Install just the marketplace"
	@echo "  make install-plugins      Install all plugins (requires marketplace)"
	@echo "  make uninstall            Uninstall marketplace (uninstalls all plugins)"
	@echo "  make reinstall            Reinstall everything (uninstall then install)"

install: install-marketplace install-plugins
	@echo "✓ Installation complete"

install-marketplace:
	@if claude plugin marketplace list 2>/dev/null | grep -q "claudehub"; then \
		echo "Marketplace already installed"; \
	else \
		echo "Installing marketplace from: $(ROOT_DIR)"; \
		claude plugin marketplace add $(ROOT_DIR); \
		echo "✓ Marketplace installed"; \
	fi

install-plugins:
	@echo "Installing plugins..."
	@if claude plugin list 2>/dev/null | grep -q "github@claudehub"; then \
		echo "Plugin 'github' already installed"; \
	else \
		claude plugin install github@claudehub; \
		echo "✓ Plugin 'github' installed"; \
	fi
	@if claude plugin list 2>/dev/null | grep -q "claudehub@claudehub"; then \
		echo "Plugin 'claudehub' already installed"; \
	else \
		claude plugin install claudehub@claudehub; \
		echo "✓ Plugin 'claudehub' installed"; \
	fi
	@echo "✓ All plugins installed"

uninstall:
	@echo "Uninstalling plugins..."
	@if claude plugin list 2>/dev/null | grep -q "github@claudehub"; then \
		claude plugin uninstall github@claudehub; \
		echo "✓ Plugin 'github' uninstalled"; \
	else \
		echo "Plugin 'github' not installed"; \
	fi
	@if claude plugin list 2>/dev/null | grep -q "claudehub@claudehub"; then \
		claude plugin uninstall claudehub@claudehub; \
		echo "✓ Plugin 'claudehub' uninstalled"; \
	else \
		echo "Plugin 'claudehub' not installed"; \
	fi
	@if claude plugin marketplace list 2>/dev/null | grep -q "claudehub"; then \
		echo "Uninstalling marketplace..."; \
		claude plugin marketplace remove claudehub; \
		echo "✓ Marketplace uninstalled"; \
	else \
		echo "Marketplace not installed, skipping"; \
	fi
	@echo "✓ Uninstall complete"

reinstall: uninstall install
	@echo "✓ Reinstall complete"
