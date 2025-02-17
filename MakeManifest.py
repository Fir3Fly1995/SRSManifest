import os
from datetime import datetime

def generate_manifest(manifest_path):
    # Get the current date and time for the manifest header
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Write the manifest file with only the timestamp
    with open(manifest_path, "w") as manifest_file:
        manifest_file.write(current_time)
    
    print(f"Manifest file generated at {manifest_path}")
    print(f"Manifest content:\n{current_time}")

# Path to save the manifest file
manifest_file_path = "C:/Users/Alex Edwards/Documents/GitHub/Manifest/SRSManifest/manifest.txt"

# Ensure the output directory exists
os.makedirs(os.path.dirname(manifest_file_path), exist_ok=True)

# Generate the manifest file
generate_manifest(manifest_file_path)