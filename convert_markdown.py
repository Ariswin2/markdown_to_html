# main.py

import markdown
import os

def convert_markdown_to_html(md_file_path):
    # Check if the file exists
    if not os.path.exists(md_file_path):
        print("File not found!")
        return

    # Read the markdown file
    with open(md_file_path, 'r', encoding='utf-8') as f:
        text = f.read()

    # Convert markdown to HTML
    html = markdown.markdown(text)

    # Save to HTML file
    output_file = md_file_path.replace('.md', '.html')
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"Successfully converted! HTML file saved as: {output_file}")

if __name__ == "__main__":
    md_path = input("Enter the path to your Markdown (.md) file: ")
    convert_markdown_to_html(md_path)
