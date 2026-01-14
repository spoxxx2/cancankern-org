#!/data/data/com.termux/files/usr/bin/bash

echo "🔄 Syncing with origin..."
git pull --rebase

echo "📦 Staging changes..."
git add -A

echo "📝 Commit message:"
read msg

git commit -m "$msg"

echo "🚀 Pushing to origin..."
git push

