import os
import re
import glob

def get_md_files():
    """Get all markdown files in the specified range and sort them."""
    # Find all markdown files in the current directory
    all_md_files = glob.glob("*.md")
    
    # Filter for files that match the pattern N-java-*.md where N is a number
    pattern = re.compile(r"(\d+)-java-.*\.md")
    numbered_files = []
    
    for file in all_md_files:
        match = pattern.match(file)
        if match:
            file_num = int(match.group(1))
            # Filter files between 10 and 42 inclusive
            if 10 <= file_num <= 42:
                numbered_files.append((file_num, file))
    
    # Sort files by their number
    numbered_files.sort()
    return [file for _, file in numbered_files]

def add_next_buttons():
    """Add next buttons to each markdown file."""
    md_files = get_md_files()
    print(f"Found {len(md_files)} markdown files to process")
    
    for i, current_file in enumerate(md_files):
        # Skip the last file as it doesn't have a next file
        if i == len(md_files) - 1:
            print(f"Skipping {current_file} as it's the last file")
            continue
        
        next_file = md_files[i + 1]
        print(f"Processing {current_file} -> {next_file}")
        
        # Read the current file content
        with open(current_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if the next button already exists
        next_button = f'<a href="{next_file}" class="next">Next</a>'
        if next_button in content:
            print(f"Next button already exists in {current_file}")
            continue
        
        # Add the next button at the end of the file
        content += f"\n\n{next_button}\n"
        
        # Write back the content
        with open(current_file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"Added next button to {current_file}")

if __name__ == "__main__":
    # Change to the directory containing the markdown files if needed
    # os.chdir("/path/to/markdown/files")
    
    add_next_buttons()
    print("Done adding next buttons!")

