# SmartShot

## Introduction
SmartShot automates the task of organizing and renaming screenshots in a specified folder on macOS. It uses the built-in Automater app to auto-detect when new screenshots are taken and runs a script to rename them.

## Setup Instructions

### API Key Configuration
1. **Set OpenAI API Key as an Environment Variable:**
   - Open your Terminal.
   - Edit your `.zshrc` file by typing `nano ~/.zshrc`.
   - Add the following line at the end of the file:
  
     ```sh
     export OPENAI_API_KEY='your-api-key'
     ```

### Python Script
1. **Place the Python Script:**
   - Save the provided Python script (e.g., `renamer.py`) to a directory, such as `/Users/[YourUsername]/[some_folder]/screenshot-renamer/`.
2. **Modify DIRS inside renamer.py**
   - Modify the DIRS for your screenshot folder:
  
     ```python3
      DIRS = [
        "/Users/username/path_to_screenshots",
        "/Users/username/some_folder/screenshot-renamer/processed.log"]
     ```   

### Automator Configuration
1. **Create a Folder Action:**
   - Open Automator and select "Folder Action."
   - Choose the folder where screenshots are saved (e.g., `~/Desktop` or `~/Documents/Screenshots`).

2. **Configure the Folder Action:**
   - Add the "Run Shell Script" action.
   - Input the following command:
     ```sh
     chmod +x /Users/[YourUsername]/[some_folder]/screenshot-renamer/renamer.py
     source ~/.zshrc
     /usr/local/bin/python3 /Users/[YourUsername]/[some_folder]/screenshot-renamer/renamer.py
     ```
   - Adjust the path to the Python executable and the script as necessary.

3. **Save and Activate:**
   - Save the Automator action with a meaningful name, like "SmartShot Action."

### Testing the Setup
- Take a screenshot and ensure it's saved to the folder monitored by Automator. The script should automatically analyze and rename the screenshot.

## Troubleshooting
- **API Key Access:** If the script cannot access the API key, verify the `.zshrc` file's configuration and the environment variable export.
- **GPT4 Rate Limit** With GPT4V preview, you only 100 requests per day.
- **Automator Configuration:** Confirm the correct paths in Automator and ensure the Python script has the necessary execution permissions.
