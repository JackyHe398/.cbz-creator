# 📚 .cbz Creator – Convert Comic Folders into CBZ Archives

This script automates the process of converting image-based comic folders into **CBZ (Comic Book ZIP)** format, ensuring proper sorting and handling of special pages like "Notice Pages."

## ✨ Features
- 📂 **Batch Process:** Converts all comic folders in the root directory into `.cbz` files.
- 🔢 **Proper Page Sorting:** Ensures pages are ordered numerically, even if filenames are mixed.
- 📌 **Handles Notice Pages:** If there is only one non-numeric image (e.g., "Notice.png"), it gets renamed to be the **last page**.
- ⏭️ **Skips Existing CBZs:** Avoids redundant work by skipping folders where a CBZ already exists.
- 🛠️ **Error Handling:** Warns about issues like missing images or unexpected files.

## 🛠️ Installation
1. **Install Python 3** (if not already installed).
2. Clone the repository:
   ```sh
   git clone https://github.com/JackyHe398/CBZ-Creator.git
   cd CBZ-Creator
3. Run the script:
    ```
    python3 cbz_creator.py
    ```

## 📂 How It Works
1. The script scans all folders in the current directory.
2. It sorts image files numerically (01.png, 02.png, ...).
3. If a non-numeric image (e.g., Notice.png) is detected:
    * If only one exists, it's renamed to be the last page.
    * If multiple exist, they are placed at the end without renaming.
4. Creates a .cbz archive with the ordered images.
5. Skips already processed folders (if a .cbz file exists).

## 📜 Example Structure
Before running the script:
```
📂 Comics/
 ├── 📂 Comic1/
 │    ├── 01.png
 │    ├── 02.png
 │    ├── Notice.png
 ├── 📂 Comic2/
 │    ├── 01.png
 │    ├── 02.png
 │    ├── Extra-Info.png
 │    ├── Notice.png
```
After running the script:
```
📂 Comics/
 ├── Comic1.cbz  ✅ (Notice.png renamed to 03.png)
 ├── Comic2.cbz  ✅ (Extra-Info.png & Notice.png added at the end)
```
**\*note that the original file will not be removed**

## 🛠️ Configuration
You can modify the base_directory variable in cbz_creator.py to specify a different root folder.

```
base_directory = "./"  # Change this to your target folder
```


## 📜 License
Main.py v1.0 and this README.md is licensed under WTFPL. Since the code including this .md is purely generated from chatGPT, I reserve no right under v1.0. License of further version is not guaranteed. 

## 🚀 Contribute
Pull requests are welcome! If you find a bug or want to add a feature, feel free to contribute. 

## 🖥️ Author
👤 ChatGPT
📧 Contact: contact openAI if you want

-- JackyHe398 modified 2025-02-10
