# Multi-Plugin Repository

A multi-plugin repository contains multiple plugins in separate directories, managed by a marketplace configuration.

## Structure

```
repo-name/
├── .claude-plugin/
│   └── marketplace.json     # Marketplace config (required)
├── plugin-one/
│   ├── .claude-plugin/
│   │   └── plugin.json      # Plugin metadata (required)
│   ├── commands/
│   ├── skills/
│   └── README.md
├── plugin-two/
│   ├── .claude-plugin/
│   │   └── plugin.json      # Plugin metadata (required)
│   ├── skills/
│   ├── agents/
│   └── README.md
└── README.md                 # Repository documentation
```

## Marketplace Configuration (marketplace.json)

Required file at `.claude-plugin/marketplace.json` at the repository root:

```json
{
  "name": "repository-name",
  "owner": {
    "name": "Owner Name"
  },
  "metadata": {
    "description": "Repository description"
  },
  "plugins": [
    {
      "name": "plugin-one",
      "source": "./plugin-one",
      "description": "First plugin description"
    },
    {
      "name": "plugin-two",
      "source": "./plugin-two",
      "description": "Second plugin description"
    }
  ]
}
```

**Fields:**
- `name`: Repository identifier
- `owner.name`: Owner display name
- `metadata.description`: Repository description
- `plugins`: Array of plugin configurations
  - `name`: Plugin name (must match plugin.json)
  - `source`: Relative path to plugin directory
  - `description`: Plugin description

## Plugin Metadata (plugin.json)

Each plugin in the repository needs its own `.claude-plugin/plugin.json`:

```json
{
  "name": "plugin-name",
  "description": "Brief description of what this plugin does",
  "version": "1.0.0"
}
```

**Fields:**
- `name`: Plugin identifier (lowercase, hyphens)
- `description`: One-line summary shown in plugin list
- `version`: Semantic version (MAJOR.MINOR.PATCH)

## Setup Steps

**Step 1: Create marketplace.json**
```bash
mkdir -p .claude-plugin
cat > .claude-plugin/marketplace.json << 'EOF'
{
  "name": "my-plugins",
  "owner": {
    "name": "Your Name"
  },
  "metadata": {
    "description": "Collection of Claude Code plugins"
  },
  "plugins": []
}
EOF
```

**Step 2: Create plugin directories**
For each plugin:
```bash
mkdir -p plugin-name/{.claude-plugin,commands,skills,agents,hooks}
cat > plugin-name/.claude-plugin/plugin.json << 'EOF'
{
  "name": "plugin-name",
  "description": "Plugin description",
  "version": "1.0.0"
}
EOF
```

**Step 3: Add plugin to marketplace.json**
Add an entry to the `plugins` array:
```json
{
  "name": "plugin-name",
  "source": "./plugin-name",
  "description": "Plugin description"
}
```

**Step 4: Add components**
Add skills, commands, agents, or hooks to each plugin as needed.

**Step 5: Create README files**
Document both the repository and individual plugins.

**Step 6: Test locally**
Install plugins locally to test before publishing:
```bash
/plugin marketplace add /path/to/repo
/plugin install plugin-name@repo-name
```

## Installation

**Local installation:**
```bash
/plugin marketplace add /path/to/repo
/plugin install plugin-name@repo-name
```

**GitHub installation:**
```bash
/plugin marketplace add username/repo-name
/plugin install plugin-name@repo-name
```

For private repositories, SSH authentication is required.

## Common Patterns

**Team-based:**
Group plugins by team: `team-backend`, `team-platform`, `team-ml`

**Domain-based:**
Group plugins by domain: `terraform`, `kubernetes`, `analytics`
