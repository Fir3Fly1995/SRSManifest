import os
from datetime import datetime

# Function to create a blank manifest file
def create_blank_manifest():
    manifest_path = os.path.expandvars(r"C:\Users\Alex Edwards\Documents\GitHub\Manifest\SRSManifest\manifest.txt")
    
    # Get the current date and time
    current_datetime = datetime.now().strftime("%Y-%m-%d_%H:%M:%S")

    # Define the entries
    entries = [
        "RootDir SRSBot  1 1.1",
        "ItemB launcher.py       1 1.1",
        "ItemB Launcher.spec     1 1.1",
        "ItemB launcher.exe      1 1.1",
        "ItemB notes.txt         1 1.1",
        "ItemB SRSLogo.ico       1 1.1",
        "ItemB SRSBotV.py        1 1.1",
        "ItemB SRSBotV.spec      1 1.1",
        "ItemB SRSBotV.exe       1 1.1",
        "ItemU Standalone_Updater.py 1 1.1",
        "ItemU standalone_updater.spec 1 1.1",
        "ItemU Standalone_Updater.exe 1 1.1"
        ]

    
    # Create the manifest content
    manifest_content = f"<{current_datetime}>\n\n"
    for entry in entries:
        manifest_content += f"{entry}\n"
    
    # Write the manifest content to the file
    with open(manifest_path, "w", encoding="utf-8") as file:
        file.write(manifest_content)
    
    print(f"Manifest file created at {manifest_path}")

# Run the function to create the blank manifest
create_blank_manifest()