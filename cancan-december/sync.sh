#!/bin/bash
echo "🚀 Hardwiring Identity & SSH..."
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_rsa_cancan
git config user.email "spoxxx2@gmail.com"
git config user.name "spoxxx2"

echo "📦 Committing Jan 10 Master Strategy (Fog + Gallery)..."
git add .
git commit -m "CANCAN Jan 10: Founder Message & Weathering Fog Update"

echo "📡 Pushing with Low-Memory Calibration..."
# This command bypasses the memory-heavy compression causing the crash
git -c core.packedGitLimit=128m -c core.packedGitWindowSize=128m push origin main --force

echo "✅ Deployment Triggered for https://cancan-backend1.onrender.com"
