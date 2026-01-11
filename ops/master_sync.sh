#!/bin/bash

# Configuration
EXPORT_PATH="$HOME/.local/lib/python3.9/site-packages"
export PYTHONPATH=$PYTHONPATH:$EXPORT_PATH

echo "🚀 INITIALIZING CANCANKERN ADAPTIVE SYNC..."

# 1. Trigger Vision Inference
echo "🔍 Running YOLOv12 + ViT Panoptic Segmentation..."
python3 vision_core.py

# 2. Sync to Digital Twin
echo "📡 Hardwiring metadata to Supabase Cloud..."
python3 adaptive_logger.py

echo "✅ SYNC COMPLETE. Visit https://cancankern.org/public_log to view telemetry."
