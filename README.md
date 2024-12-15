# File-Pack-Unpack

# Packer Unpacker

**Packer Unpacker** is a Python Flask-based web application that allows users to **pack multiple text files** from a folder into a single binary file and **unpack files** from the binary back to their original format.  

---

## Features

- **Pack Files**: Combines all `.txt` files from a folder into a single packed binary file.
- **Unpack Files**: Extracts the packed files back into their original format in a separate folder.
- **Web Interface**: User-friendly web UI for easy interaction.
- **Validation**: Ensures input files and folders exist before proceeding.
- **Error Handling**: Displays descriptive error messages to guide users.

---

## Technologies Used

- **Flask**: For the backend and web framework.
- **HTML/CSS**: For the frontend.
- **Python**: For file operations and business logic.

---

## Project Structure
. ├── app.py # Main application file with Flask routes. ├── pack_unpack.py # Logic for packing and unpacking files. ├── templates # HTML templates for the web app. │ ├── base.html # Base layout template. │ ├── pack.html # UI for packing files. │ ├── unpack.html # UI for unpacking files. ├── static │ └── style.css # Styling for the web app.


---

## How It Works

### Packing
1. The user provides:
   - **Folder path** containing `.txt` files.
   - **Packed file name** where all files will be stored.
2. The application creates a binary file, storing:
   - Metadata (file name and size).
   - Contents of each `.txt` file.

### Unpacking
1. The user provides the path to the **packed file**.
2. The application extracts files:
   - Reads metadata to identify file details.
   - Reconstructs the original `.txt` files in a new folder named `unpacked_files`.

---

## Setup and Usage

### Prerequisites

- Python 3.x installed.
- Flask module installed (`pip install flask`).


