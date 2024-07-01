import hashlib

def hash_check(type, asset, filename, down_folder, subfolder=None, hash=None, k=None, b=None):
    """Function to check the hash of a file.

    Args:
        type (str): The type of asset ('hdris' or 'other').
        asset (str): The name of the asset.
        filename (str): The name of the file.
        down_folder (str): The path to the folder where the file is located if it's an HDRI file.
        subfolder (str, optional): The path to the folder where the file is located if it's not an HDRI file. Defaults to None.
        hash (str, optional): The expected hash of the file. Defaults to None.
        k (int, optional): An additional identifier for the asset if needed. Defaults to None.
        b (bool, optional): A flag to indicate whether an additional subfolder is present or not. Defaults to None.

    Returns:
        bool: True if the hash of the file matches the expected hash, False otherwise.
    """
    # Determine the path to the file based on its type
    if type == "hdris":
        file_path = down_folder + filename
    else:
        sub_path = f"{asset}_{k}" if k is not None else asset
        file_path = f"{subfolder}/{sub_path}/textures/{filename}"
        if b:
            file_path = f"{subfolder}/{sub_path}/{filename}"

    # Calculate the hash of the file
    with open(file_path, "rb") as f:
        md5_hash = hashlib.md5()
        while chunk := f.read(8192):
            md5_hash.update(chunk)

    # Compare the calculated hash with the expected hash (if provided)
    if hash is not None and hash != md5_hash.hexdigest():
        return False
    return True
