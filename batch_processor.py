import os
from ultralytics import YOLO

# Load the optimized YOLOv12 weights
model = YOLO('yolov12n.pt') 

def run_batch(folder_path):
    # Gather all images in the folder
    images = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if f.endswith('.jpg')]
    
    if not images:
        print("No images found in batch folder.")
        return

    print(f"--- Processing {len(images)} images via YOLOv12 Batch Inference ---")
    
    # Run batch inference (Stronger memory management)
    results = model(images, stream=True)
    
    for i, result in enumerate(results):
        # Save each result to your Digital Twin log
        output_name = f"audit_result_{i}.json"
        result.save_txt(f"~/audit_logs/{output_name}")
        print(f"Verified: {images[i]} -> {output_name}")

if __name__ == "__main__":
    run_batch('/data/data/com.termux/files/home/test_batch')
