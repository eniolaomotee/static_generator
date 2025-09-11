import os
from utils_markdown import extract_title
from markdown_to_blocks import markdown_to_html

def generate_page(from_path:str,template_path:str, dest_path:str):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    
    # read from path file
    with open(from_path,"r") as f:
        markdown = f.read()
        
    # read from template path file
    with open(template_path, "r") as f:
        template = f.read()
        
    root_node = markdown_to_html(markdown)
    content_html = root_node.to_html()
    
    
    title = extract_title(markdown)
    
    output_html = template.replace("{{ Title }}", title).replace("{{ Content }}", content_html)
    
    dest_dir = os.path.dirname(dest_path)
    if dest_dir:
        os.makedirs(dest_dir,exist_ok=True)
        
    with open(dest_path,"w") as f:
        f.write(output_html)
        
    print(f"Written {dest_path}")