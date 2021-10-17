from pathlib import Path

import requests as requests


def create_empty_file(file_path: str) -> None:
    # create folders if needed
    path = Path(file_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    extension = path.suffix
    #download the correct file from the internet
    try:
        download_file(f"https://github.com/VerifyTests/EmptyFiles/raw/main/index/empty{extension}", file_path)
    except:
        open(file_path, "w").close()


def download_file(url: str, file_path: str) -> str:
    # NOTE the stream=True parameter below
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(file_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                # If you have chunk encoded response uncomment if
                # and set chunk_size parameter to None.
                #if chunk:
                f.write(chunk)
    return file_path