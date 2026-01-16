# Single Plugin Repository

A single plugin repository contains one plugin at the repository root.

## Structure

```
plugin-name/
├── .claude-plugin/
│   └── plugin.json          # Plugin metadata (required)
├── commands/                 # User-invoked actions (/command-name)
│   └── command-name.md
├── skills/                   # Domain knowledge (auto-matched)
│   └── skill-name/
│       └── SKILL.md
├── agents/                   # Autonomous specialists (Task tool)
│   └── agent-name.md
├── hooks/                    # Event-driven automation
│   ├── hooks.json
│   └── script.sh
└── README.md                 # Plugin documentation
```

## Plugin Metadata (plugin.json)

Required file at `.claude-plugin/plugin.json`:

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

**Step 1: Create directory structure**
```bash
mkdir -p plugin-name/{.claude-plugin,commands,skills,agents,hooks}
```

**Step 2: Create plugin.json**
```bash
cat > plugin-name/.claude-plugin/plugin.json << 'EOF'
{
  "name": "plugin-name",
  "description": "Plugin description",
  "version": "1.0.0"
}
EOF
```

**Step 3: Add components**
Add skills, commands, agents, or hooks as needed based on the plugin's purpose.

**Step 4: Create README.md**
Document the plugin's purpose, components, and usage.

**Step 5: Test locally**
Install the plugin locally to test before publishing:
```bash
/plugin install /path/to/plugin-name
```

## Installation

**Local installation:**
```bash
/plugin install /path/to/plugin-name
```

**GitHub installation:**
```bash
/plugin marketplace add username/repo-name
/plugin install plugin-name@repo-name
```

For private repositories, SSH authentication is required.
