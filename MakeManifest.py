import os
import hmac
import hashlib
import tkinter as tk
from tkinter import messagebox, ttk
from datetime import datetime
import logging

# Configure logging
log_file_path = os.path.expandvars(r"%LocalAppData%\SRSBot\Logs\MakeManifest_log.txt")
os.makedirs(os.path.dirname(log_file_path), exist_ok=True)
logging.basicConfig(filename=log_file_path, level=logging.DEBUG, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Function to log messages
def log(message):
    logging.debug(message)
    with open(log_file_path, "a") as log_file:
        log_file.write(message + "\n")
    print(message)

# Function to retrieve a field (for demonstration purposes, it just shows a message)
def retrieve_field(entry):
    messagebox.showinfo("Retrieve Field", f"Retrieve field: {entry.get()}")

# Function to save a field (for demonstration purposes, it just shows a message)
def save_field(entry):
    messagebox.showinfo("Save Field", f"Save field: {entry.get()}")

# Function to delete a field
def delete_field(field_frame):
    field_frame.destroy()

# Function to increment the value in an entry field
def increment(entry):
    try:
        value = int(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(value + 1))
    except ValueError:
        entry.insert(0, "1")

# Function to decrement the value in an entry field
def decrement(entry):
    try:
        value = int(entry.get())
        if value > 0:
            entry.delete(0, tk.END)
            entry.insert(0, str(value - 1))
    except ValueError:
        entry.insert(0, "0")

# Function to read the manifest file and populate the fields
def read_manifest():
    manifest_path = os.path.expandvars(r"C:\Users\Alex Edwards\Documents\GitHub\Manifest\SRSManifest\manifest.txt")
    logo_path = os.path.expandvars(r"C:\Users\Alex Edwards\Documents\GitHub\RSI_Verifications\SRSBot\BotStuff\SRSLogo.ico")

    # Check if the SRSLogo.ico file exists
    if not os.path.exists(logo_path):
        messagebox.showerror("Error", f"SRSLogo.ico file not found at {logo_path}")
        return

    # Read the SRSLogo.ico file as the key for HMAC
    with open(logo_path, "rb") as logo_file:
        key = logo_file.read()

    if not os.path.exists(manifest_path):
        messagebox.showerror("Error", f"Manifest file not found at {manifest_path}")
        return

    with open(manifest_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    # Clear existing fields
    for tab in [botstuff_frame, updater_frame, other_frame]:
        for widget in tab.winfo_children():
            widget.destroy()

    # Populate fields with manifest content
    for line in lines[2:]:  # Skip the first two lines (date and time, and the blank line)
        line = line.strip()
        if line:
            parts = line.split()
            if len(parts) >= 3:
                item_type = parts[0]
                file_folder_name = " ".join(parts[1:-2])
                version_number = parts[-2]
                stored_hmac_revision = parts[-1]

                # Verify HMAC for the revision number
                for i in range(1000):  # Assuming revision numbers are between 0 and 999
                    revision_number = str(i / 10)
                    hmac_object = hmac.new(key, revision_number.encode('utf-8'), hashlib.sha256)
                    calculated_hmac_revision = hmac_object.hexdigest()
                    if hmac.compare_digest(stored_hmac_revision, calculated_hmac_revision):
                        break
                else:
                    messagebox.showerror("Error", f"Failed to verify HMAC for {file_folder_name}")
                    continue

                print(f"Processing: {file_folder_name}, Version: {version_number}, Revision: {revision_number}")

                if item_type == "RootDir":
                    parent_frame = botstuff_frame
                elif item_type == "ItemB":
                    parent_frame = botstuff_frame
                elif item_type == "ItemU":
                    parent_frame = updater_frame
                elif item_type == "Folder":
                    parent_frame = other_frame
                else:
                    continue

                field_frame = tk.Frame(parent_frame)
                field_frame.pack(fill="x", pady=5)

                label_item_type = tk.Label(field_frame, text=item_type, width=10)
                label_item_type.pack(side="left", padx=5)

                entry_name = tk.Entry(field_frame, width=30)
                entry_name.insert(0, file_folder_name)
                entry_name.pack(side="left", padx=5)

                entry_version = tk.Entry(field_frame, width=10)
                entry_version.insert(0, version_number)
                entry_version.pack(side="left", padx=5)

                increment_version_button = tk.Button(field_frame, text="+", command=lambda e=entry_version: increment(e))
                increment_version_button.pack(side="left", padx=5)

                decrement_version_button = tk.Button(field_frame, text="-", command=lambda e=entry_version: decrement(e))
                decrement_version_button.pack(side="left", padx=5)

                entry_revision = tk.Entry(field_frame, width=10)
                entry_revision.insert(0, revision_number)
                entry_revision.pack(side="left", padx=5)

                increment_revision_button = tk.Button(field_frame, text="+", command=lambda e=entry_revision: increment(e))
                increment_revision_button.pack(side="left", padx=5)

                decrement_revision_button = tk.Button(field_frame, text="-", command=lambda e=entry_revision: decrement(e))
                decrement_revision_button.pack(side="left", padx=5)

# Function to read a plain text manifest file and populate the fields
def read_plain_manifest():
    manifest_path = os.path.expandvars(r"C:\Users\Alex Edwards\Documents\GitHub\Manifest\SRSManifest\Manifest.txt")

    if not os.path.exists(manifest_path):
        messagebox.showerror("Error", f"Plain text manifest file not found at {manifest_path}")
        return

    with open(manifest_path, "r", encoding="utf-8") as file:
        lines = file.readlines()

    # Clear existing fields
    for tab in [botstuff_frame, updater_frame, other_frame]:
        for widget in tab.winfo_children():
            widget.destroy()

    # Populate fields with manifest content
    for line in lines[2:]:  # Skip the first two lines (date and time, and the blank line)
        line = line.strip()
        if line:
            parts = line.split()
            if len(parts) >= 3:
                item_type = parts[0]
                file_folder_name = " ".join(parts[1:-2])
                version_number = parts[-2]
                revision_number = parts[-1]

                print(f"Processing: {file_folder_name}, Version: {version_number}, Revision: {revision_number}")

                if item_type == "RootDir":
                    parent_frame = botstuff_frame
                elif item_type == "ItemB":
                    parent_frame = botstuff_frame
                elif item_type == "ItemU":
                    parent_frame = updater_frame
                elif item_type == "Folder":
                    parent_frame = other_frame
                else:
                    continue

                field_frame = tk.Frame(parent_frame)
                field_frame.pack(fill="x", pady=5)

                label_item_type = tk.Label(field_frame, text=item_type, width=10)
                label_item_type.pack(side="left", padx=5)

                entry_name = tk.Entry(field_frame, width=30)
                entry_name.insert(0, file_folder_name)
                entry_name.pack(side="left", padx=5)

                entry_version = tk.Entry(field_frame, width=10)
                entry_version.insert(0, version_number)
                entry_version.pack(side="left", padx=5)

                increment_version_button = tk.Button(field_frame, text="+", command=lambda e=entry_version: increment(e))
                increment_version_button.pack(side="left", padx=5)

                decrement_version_button = tk.Button(field_frame, text="-", command=lambda e=entry_version: decrement(e))
                decrement_version_button.pack(side="left", padx=5)

                entry_revision = tk.Entry(field_frame, width=10)
                entry_revision.insert(0, revision_number)
                entry_revision.pack(side="left", padx=5)

                increment_revision_button = tk.Button(field_frame, text="+", command=lambda e=entry_revision: increment(e))
                increment_revision_button.pack(side="left", padx=5)

                decrement_revision_button = tk.Button(field_frame, text="-", command=lambda e=entry_revision: decrement(e))
                decrement_revision_button.pack(side="left", padx=5)

# Function to write the manifest file
def write_all():
    manifest_path = os.path.expandvars(r"C:\Users\Alex Edwards\Documents\GitHub\Manifest\SRSManifest\manifest.txt")
    logo_path = os.path.expandvars(r"C:\Users\Alex Edwards\Documents\GitHub\RSI_Verifications\SRSBot\BotStuff\SRSLogo.ico")

    # Read the SRSLogo.ico file as the key for HMAC
    with open(logo_path, "rb") as logo_file:
        key = logo_file.read()

    manifest_content = f"<{datetime.now().strftime('%Y-%m-%d_%H:%M:%S')}>\n\n"
    for tab in [botstuff_frame, updater_frame, other_frame]:
        for widget in tab.winfo_children():
            if isinstance(widget, tk.Frame):
                entries = [w for w in widget.winfo_children() if isinstance(w, tk.Entry)]
                if len(entries) >= 3:
                    entry_name = entries[0]
                    entry_version = entries[1]
                    entry_revision = entries[2]

                    file_folder_name = entry_name.get()
                    version_number = entry_version.get()
                    revision_number = entry_revision.get()

                    # Determine the item type based on the parent frame
                    if tab == botstuff_frame:
                        if file_folder_name == "SRSBot":
                            item_type = "RootDir"
                        else:
                            item_type = "ItemB"
                    elif tab == updater_frame:
                        item_type = "ItemU"
                    else:
                        item_type = "Folder"

                    # Generate HMAC for the revision number
                    hmac_object = hmac.new(key, revision_number.encode('utf-8'), hashlib.sha256)
                    hmac_revision = hmac_object.hexdigest()

                    manifest_content += f"{item_type} {file_folder_name} {version_number} {hmac_revision}\n"

    with open(manifest_path, "w", encoding="utf-8") as file:
        file.write(manifest_content)

    messagebox.showinfo("Success", "Manifest file written successfully!")

# Create the main window
root = tk.Tk()
root.title("Make Manifest")
root.geometry("560x400")

# Create a notebook (tabbed interface)
notebook = ttk.Notebook(root)
notebook.pack(fill="both", expand=True)

# Create frames for each tab
botstuff_frame = tk.Frame(notebook)
updater_frame = tk.Frame(notebook)
other_frame = tk.Frame(notebook)

# Add tabs to the notebook
notebook.add(botstuff_frame, text="BotStuff")
notebook.add(updater_frame, text="Updater")
notebook.add(other_frame, text="Other")

# Create a frame to hold the buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

# Create a button to read the manifest file
read_button = tk.Button(button_frame, text="Read Manifest", command=read_manifest)
read_button.pack(side="left", padx=5)

# Create a button to read the plain text manifest file
read_plain_button = tk.Button(button_frame, text="Read Plain Manifest", command=read_plain_manifest)
read_plain_button.pack(side="left", padx=5)

# Create a button to write the manifest file
write_button = tk.Button(button_frame, text="Write All", command=write_all)
write_button.pack(side="left", padx=5)

# Run the main event loop
root.mainloop()