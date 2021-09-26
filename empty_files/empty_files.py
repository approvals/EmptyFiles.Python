from pathlib import Path
def create_empty_file(file_path: str) -> None:
    # create folders if needed
    Path(file_path).parent.mkdir(parents=True, exist_ok=True)
    # create empty file using the name
    open(file_path, "w").close()