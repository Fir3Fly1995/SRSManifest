import os
from datetime import datetime

def generate_manifest(directory, manifest_path):
    manifest_lines = []
    
    # Get the current date and time for the manifest header
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    manifest_lines.append(current_time)
    
    # List of files to include in the manifest
    files_to_include = [
        "launcher.exe",
        "launcher.py",
        "launcher.spec",
        "updater.py",
        "Verifier.py",
        "SRSLogo.ico"
    ]
    
    # Walk through the directory and list specified files with their last modified times
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file in files_to_include:
                file_path = os.path.join(root, file)
                relative_path = os.path.relpath(file_path, directory)
                last_modified_time = datetime.fromtimestamp(os.path.getmtime(file_path)).strftime("%Y-%m-%d %H:%M:%S")
                manifest_lines.append(f"{relative_path} {last_modified_time}")
                print(f"File: {relative_path}, Last Modified: {last_modified_time}")
    
    # Write the manifest file
    with open(manifest_path, "w") as manifest_file:
        manifest_file.write("\n".join(manifest_lines))
    
    print(f"Manifest file generated at {manifest_path}")
    print(f"Manifest content:\n{'\n'.join(manifest_lines)}")

# Directory to scan for updated files
directory_to_scan = "C:/Users/Alex Edwards/Documents/GitHub/RSI_Verifications/SRSBot"

# Path to save the manifest file
manifest_file_path = "C:/Users/Alex Edwards/Documents/GitHub/Manifest/SRSManifest/manifest.txt"

# Ensure the output directory exists
os.makedirs(os.path.dirname(manifest_file_path), exist_ok=True)

# Generate the manifest file
generate_manifest(directory_to_scan, manifest_file_path)