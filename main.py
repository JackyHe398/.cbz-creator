# v1.0 created by chatGPT 4o with prompt by JackyHe398

import os
import zipfile

def create_cbz_from_folders(root_dir):
    for folder in sorted(os.listdir(root_dir)):
        folder_path = os.path.join(root_dir, folder)
        cbz_filename = f"{folder}.cbz"
        cbz_filepath = os.path.join(root_dir, cbz_filename)

        # ✅ Ignore non-directories
        if not os.path.isdir(folder_path):
            continue  # Skip any files (including existing CBZs)

        # ✅ Check if CBZ already exists
        if os.path.exists(cbz_filepath):
            print(f"⏭️  Skipping '{folder}' (CBZ already exists)")
            continue

        try:
            # ✅ Get only valid image files
            images = [f for f in os.listdir(folder_path) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp'))]

            if not images:
                print(f"⚠️ Warning: No valid images found in '{folder}', skipping...")
                continue

            # ✅ Separate numeric and non-numeric files
            numeric_images = []
            non_numeric_images = []

            for img in images:
                if img.split('.')[0].isdigit():
                    numeric_images.append(img)
                else:
                    non_numeric_images.append(img)

            # ✅ Sort numeric images properly
            numeric_images.sort(key=lambda x: int(x.split('.')[0]))

            # ✅ Handle notice pages (Non-numeric images)
            if len(non_numeric_images) <= 1:  # If one or fewer non-numeric images
                if non_numeric_images:
                    last_page_number = int(numeric_images[-1].split('.')[0]) if numeric_images else 0
                    new_notice_name = f"{last_page_number + 1}.png"
                    os.rename(os.path.join(folder_path, non_numeric_images[0]),
                              os.path.join(folder_path, new_notice_name))
                    numeric_images.append(new_notice_name)  # Add to list in proper order
                    print(f"📌 Moved notice page '{non_numeric_images[0]}' to '{new_notice_name}'")
            else:  # If multiple non-numeric images exist, just add them in alphabetical order
                non_numeric_images.sort()
                numeric_images.extend(non_numeric_images)

            # ✅ Create CBZ archive
            with zipfile.ZipFile(cbz_filepath, 'w', zipfile.ZIP_DEFLATED) as cbz:
                for image in numeric_images:
                    image_path = os.path.join(folder_path, image)
                    cbz.write(image_path, arcname=image)

            print(f"✅ Created: {cbz_filename}")

        except Exception as e:
            print(f"❌ Error processing folder: {folder_path}")
            print(f"   ➤ {e}")

if __name__ == "__main__":
    base_directory = "./"  # Change this if needed
    create_cbz_from_folders(base_directory)
