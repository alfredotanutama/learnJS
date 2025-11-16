import os
import shutil

def organize_manga(directory, title, volume_chapters):
    """
    Organize manga chapters into volume folders.
    
    Parameters:
    - directory (str): Path to the main folder containing chapter folders.
    - title (str): Title prefix for new volume folders.
    - volume_chapters (dict): Dictionary mapping volume number to chapter ranges.
                              Example: {1: "1-3", 2: "4-6"}
    """

    for vol, chap_range in volume_chapters.items():
        # Parse chapter range
        start, end = map(int, chap_range.split('-'))
        vol_name = f"{title}, Vol. {vol}"
        vol_path = os.path.join(directory, vol_name)

        # Create volume folder
        os.makedirs(vol_path, exist_ok=True)

        # Move chapters into volume folder
        for chap_num in range(start, end + 1):
            chap_folder = os.path.join(directory, f"Chapter {chap_num}")
            if os.path.exists(chap_folder):
                shutil.move(chap_folder, vol_path)
                print(f"Moved {chap_folder} -> {vol_path}")
            else:
                print(f"⚠️ Chapter {chap_num} not found in {directory}")


if __name__ == "__main__":
    # Example usage:
    directory = r"C:\Users\Alfredo\Documents\Mangas\Fullmetal Alchemist"
    title = "Fullmetal Alchemist"
    volume_chapters = {
    7: "26-29",
    8: "30-33",
    9: "34-37",
    10: "38-41",
    11: "42-45",
    12: "46-49",
    13: "50-53",
    14: "54-57",
    15: "58-61",
    16: "62-65"
        # Add more volumes as needed
    }

    organize_manga(directory, title, volume_chapters)