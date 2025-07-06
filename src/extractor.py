import io
import zipfile

class Extractor:
    @staticmethod
    def unzip(zip_bytes):
        """
        Unzip the input bytes content and return a dict of filename -> bytes content.
        """
        try:
            with zipfile.ZipFile(io.BytesIO(zip_bytes)) as zip_ref:
                extracted_files = {}
                for file_name in zip_ref.namelist():
                    trimmed_name = Extractor._trim_filename(file_name)
                    extracted_files[trimmed_name] = zip_ref.read(file_name)
                print(f"Extracted {len(extracted_files)} files from the ZIP archive.")
                return extracted_files
        except zipfile.BadZipFile:
            print("The provided bytes are not a valid ZIP archive.")
            return None
        
    @staticmethod
    def _trim_filename(path: str):
        return path.removeprefix("mql5/")
