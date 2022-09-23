#!/bin/sh

git pull
git add . && git commit -m "Git Sync: $(date +'%Y-%m-%d %H:%M:%S')" && git push
git pull

# Note: we git pull twice because the first might fail due to unmerged changes.
