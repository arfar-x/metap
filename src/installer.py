import os

class Installer:
    @staticmethod
    def run(target_path, files_dict):
        """
        Write the extracted files (dict of filename -> bytes) into the target directory.
        """
        if not os.path.exists(target_path):
            try:
                os.makedirs(target_path, exist_ok=True)
                print(f"Created directory: {target_path}")
            except Exception as e:
                print(f"Failed to create directory {target_path}: {e}")
                return False
        
        try:
            for filename, content in files_dict.items():
                dirname = os.path.dirname(filename)
                os.makedirs(f"{target_path}/{dirname}", exist_ok=True)
                file_path = os.path.join(target_path, filename)
                with open(file_path, "wb") as f:
                    f.write(content)
                print(f"Installed file: {file_path}")
            return True
        except Exception as e:
            print(f"Failed to write files: {e}")
            return False