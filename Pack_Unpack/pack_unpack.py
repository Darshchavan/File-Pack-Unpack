import os

class Packer:
    def pack(self, folder_name, pack_file):
        if not os.path.exists(folder_name):
            raise FileNotFoundError(f"Folder '{folder_name}' does not exist.")
        
        # Get the parent directory of the folder
        parent_dir = os.path.dirname(folder_name)
        
        # Join the parent directory with the desired packed file name
        pack_file_path = os.path.join(parent_dir, pack_file)

        with open(pack_file_path, 'wb') as fout:
            all_files = os.listdir(folder_name)
            files_packed = []

            for file_name in all_files:
                file_path = os.path.join(folder_name, file_name)
                if os.path.isfile(file_path) and file_name.endswith('.txt'):
                    file_size = os.path.getsize(file_path)

                    # Prepare the header
                    header = f"{file_name} {file_size}".ljust(100)  # File name and size padded to 100 bytes
                    fout.write(header.encode('utf-8'))  # Write header to packed file

                    # Write the file's content
                    with open(file_path, 'rb') as file:
                        while (chunk := file.read(1024)):  # Read in chunks of 1024 bytes
                            fout.write(chunk)

                    files_packed.append(file_name)

        return f"{len(files_packed)} file(s) packed into '{pack_file_path}'."

class Unpacker:
    def unpack(self, pack_file):
        if not os.path.exists(pack_file):
            raise FileNotFoundError(f"Packed file '{pack_file}' does not exist.")

        # Get the parent directory of the packed file
        parent_dir = os.path.dirname(pack_file)
        
        # Create a folder for unpacked files
        unpack_folder = os.path.join(parent_dir, 'unpacked_files')
        if not os.path.exists(unpack_folder):
            os.makedirs(unpack_folder)

        with open(pack_file, 'rb') as fin:
            count = 0
            header = bytearray(100)  # Header size is fixed to 100 bytes

            while fin.readinto(header) > 0:
                str_header = header.decode('utf-8').strip()
                arr = str_header.split()

                if len(arr) < 2:
                    continue  # Skip malformed headers

                file_name = arr[0]
                file_size = int(arr[1])

                # Create the new file in the 'unpacked_files' folder
                unpacked_file_path = os.path.join(unpack_folder, file_name)
                with open(unpacked_file_path, 'wb') as fout:
                    data = fin.read(file_size)
                    fout.write(data)

                count += 1
                print(f"File '{file_name}' unpacked successfully into '{unpacked_file_path}'.")

        return f"{count} file(s) unpacked successfully into '{unpack_folder}'."
