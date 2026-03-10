import os
import re

def sanitize_md(content):
    # Only keep headers: Profile, Quirks, age/role/occupation
    lines = content.split('\n')
    public_lines = []
    
    # Identify headers to keep
    KEEP_HEADERS = ['Profile', 'Quirks', 'Quirk', 'Occupation', 'Age', 'Role']
    # Identify headers to STOP at (SPOILERS)
    STOP_HEADERS = ['Secret', 'Objective', 'Motive', 'Clue', 'Relationships', 'Hidden Evidence', 'What She Knows', 'What He Knows', 'The Truth']
    
    is_visible = True
    
    for line in lines:
        header_match = re.match(r'^##\s+(.*)', line)
        if header_match:
            header_name = header_match.group(1).strip()
            # If we hit a stop header, we stop adding content until the next header
            if any(stop in header_name for stop in STOP_HEADERS):
                is_visible = False
            # Check if it's a keep header to resume
            elif any(keep in header_name for keep in KEEP_HEADERS):
                is_visible = True
        
        # Always allow the main # Title and initial metadata
        header1_match = re.match(r'^#\s+(.*)', line)
        if header1_match:
            is_visible = True
            
        if is_visible:
            public_lines.append(line)
            
    return '\n'.join(public_lines)

def process_dir(src_dir, dest_dir):
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
        
    for filename in os.listdir(src_dir):
        if filename.endswith('.md'):
            with open(os.path.join(src_dir, filename), 'r', encoding='utf-8') as f:
                content = f.read()
            
            sanitized = sanitize_md(content)
            
            with open(os.path.join(dest_dir, filename), 'r+' if os.path.exists(os.path.join(dest_dir, filename)) else 'w', encoding='utf-8') as f:
                f.write(sanitized)

# Paths
base_dir = os.path.dirname(os.path.abspath(__file__))
process_dir(os.path.join(base_dir, 'characters', 'primary'), os.path.join(base_dir, 'docs', 'dossiers'))
process_dir(os.path.join(base_dir, 'characters', 'secondary'), os.path.join(base_dir, 'docs', 'dossiers'))

# Handle host_director.md separately if it exists
host_src = os.path.join(base_dir, 'characters', 'host_director.md')
if os.path.exists(host_src):
    with open(host_src, 'r', encoding='utf-8') as f:
        host_content = sanitize_md(f.read())
    with open(os.path.join(base_dir, 'docs', 'dossiers', 'host_director.md'), 'w', encoding='utf-8') as f:
        f.write(host_content)

print("Public dossiers generated successfully!")
