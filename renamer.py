import os

from openai import OpenAI
from PIL import Image
from io import BytesIO
import base64


def find_latest_screenshot(directory):
    """Find the most recently added screenshot in the directory."""
    all_files = [
        os.path.join(directory, f) for f in os.listdir(directory) if f.endswith(".png")
    ]
    latest_file = max(all_files, key=os.path.getctime)
    print(f"Found latest file: {latest_file}")
    return latest_file


def analyze_image(image_path):
    """Analyze the image using GPT-4 API and return the description."""

    client = OpenAI()

    with Image.open(image_path) as img:
        IMG_RES = 512
        W, H = img.size
        img = img.resize((IMG_RES, int(IMG_RES * H / W)))
        buffer = BytesIO()
        img.save(buffer, format="PNG")
        img_base64 = base64.b64encode(buffer.getvalue()).decode("utf-8")

    response = client.chat.completions.create(
        model="gpt-4-vision-preview",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "This is a screenshot of something on my screen",
                    },
                    {
                        "type": "image_url",
                        "image_url": f"data:image/png;base64,{img_base64}",
                    },
                    {
                        "type": "text",
                        "text": "Provide me a concise and descriptive file name for this image. Do not add any file extension. Be as descriptive as possible and keep it shorter than 6 words.",
                    },
                ],
            }
        ],
        max_tokens=300,
    )

    return response.choices[0].message.content.strip()


def rename_image(image_path, description):
    """Rename the image file based on the description."""
    directory, filename = os.path.split(image_path)
    new_filename = "_".join(description.split()) + ".png"
    new_path = os.path.join(directory, new_filename)
    os.rename(image_path, new_path)
    return new_path


def main():
    screenshots_dir = "/Users/hudzah/Documents/Screenshots"
    latest_screenshot = find_latest_screenshot(screenshots_dir)
    description = analyze_image(latest_screenshot)
    new_path = rename_image(latest_screenshot, description)
    print(f"Renamed '{latest_screenshot}' to '{new_path}'")


if __name__ == "__main__":
    import sys

    print(sys.executable)

    main()
