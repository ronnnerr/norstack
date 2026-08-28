#!/usr/bin/env bash
# Idempotent norstack install. Symlinks skills into the agents you already use.
# Safe to re-run. Removes nothing it did not create.
set -euo pipefail

ROOT="$(cd "$(dirname "$0")" && pwd)"
DATA="${NORSTACK_HOME:-$HOME/.norstack}"
BACKUPS="$DATA/backups/skills"
STAMP="$(date +%Y%m%d-%H%M%S)"

echo "norstack install from $ROOT"

chmod +x "$ROOT/install.sh"
mkdir -p "$DATA"/{sessions,handoffs,logs}

# Hosts to wire. A host is installed only if its config directory already exists.
HOSTS=()
[ -d "$HOME/.claude" ] && HOSTS+=("$HOME/.claude")
[ -d "$HOME/.grok" ] && HOSTS+=("$HOME/.grok")

if [ ${#HOSTS[@]} -eq 0 ]; then
  echo "No agent config directory found (~/.claude or ~/.grok)."
  echo "Create one, or symlink skills/ wherever your agent reads skills from."
  exit 1
fi

link_skill() {
  local name="$1" host="$2"
  local src="$ROOT/skills/$name"
  local dst="$host/skills/$name"
  [ -d "$src" ] || return 0
  mkdir -p "$host/skills"
  # A real directory at the target would make `ln -sfn` nest the link inside it.
  if [ -e "$dst" ] && [ ! -L "$dst" ]; then
    mkdir -p "$BACKUPS"
    mv "$dst" "$BACKUPS/$name.pre-norstack.$STAMP"
    echo "  backed up existing $name to $BACKUPS/$name.pre-norstack.$STAMP"
  fi
  ln -sfn "$src" "$dst"
}

count=0
for src in "$ROOT"/skills/*/; do
  name="$(basename "$src")"
  for host in "${HOSTS[@]}"; do link_skill "$name" "$host"; done
  count=$((count + 1))
done

for host in "${HOSTS[@]}"; do echo "linked $count skills into $host/skills"; done

# Your projects live in profile.md, which is gitignored. Seed it once.
if [ ! -f "$ROOT/skills/profile/profile.md" ]; then
  cp "$ROOT/skills/profile/profile.example.md" "$ROOT/skills/profile/profile.md"
  echo "created skills/profile/profile.md from the template. Fill it in."
fi

echo
echo "done."
echo "next: edit skills/profile/profile.md, then ask your agent to load 'norstack'."
