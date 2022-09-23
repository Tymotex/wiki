#!/bin/sh

echo "Syncing..."
git pull --quiet
git add . && git commit --quiet -m "Git Sync: $(date +'%Y-%m-%d %H:%M:%S')" && git push --quiet && echo "Pushed successfully!"
git pull --quiet

# Note: we git pull twice because the first might fail due to unmerged changes.
