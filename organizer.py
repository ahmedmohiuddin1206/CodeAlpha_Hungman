from pathlib import Path
import shutil

BASE_DIR = Path(__file__).parent
SOURCE_DIR = BASE_DIR / "images_to_sort"
DEST_DIR = BASE_DIR / "organized_images"

IMAGE_EXTENSIONS = {".jpg", ".jpeg", ".heic"}

def organize_images():
    SOURCE_DIR.mkdir(exist_ok=True)
    DEST_DIR.mkdir(exist_ok=True)

    print("Looking inside:", SOURCE_DIR.resolve())
    print("Files found:", list(SOURCE_DIR.iterdir()))

    moved_count = 0

    for file_path in SOURCE_DIR.iterdir():
        if file_path.is_file():
            print("Checking:", file_path.name)

            if file_path.suffix.lower() in IMAGE_EXTENSIONS:
                destination = DEST_DIR / file_path.name

                counter = 1
                while destination.exists():
                    destination = DEST_DIR / (
                        f"{file_path.stem}_{counter}{file_path.suffix}"
                    )
                    counter += 1

                shutil.move(str(file_path), str(destination))
                print("Moved:", file_path.name)
                moved_count += 1

    print(f"Done! Moved {moved_count} image(s).")

if __name__ == "__main__":
    organize_images()
