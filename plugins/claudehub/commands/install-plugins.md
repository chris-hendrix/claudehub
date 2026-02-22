---
description: Install claudehub ecosystem plugins from marketplace
allowed-tools: Bash
---

## Process

1. **Install each plugin from the claudehub marketplace**

   Run these commands sequentially, reporting the result of each:

   ```bash
   claude plugin install rpi@claudehub
   ```

   ```bash
   claude plugin install ralph@claudehub
   ```

   ```bash
   claude plugin install github@claudehub
   ```

2. **Report results**
   - List which plugins were installed successfully
   - If any failed, show the error and suggest running `claude plugin marketplace list` to verify the marketplace is registered

## Notes

- The claudehub marketplace must be registered first. If plugins fail to install, the user may need to run `claude plugin marketplace add <path-to-claudehub-repo>`.
- Plugins that are already installed will be updated to the latest version.
