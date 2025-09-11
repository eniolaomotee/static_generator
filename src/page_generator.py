import os
from pathlib import Path
from markdown_to_blocks import markdown_to_html


def generate_pages_recursive(dir_path_content,template_path, dest_dir_path, basepath):
    os.makedirs(dest_dir_path,exist_ok=True)
    for entry in os.listdir(dir_path_content):
        src_path = os.path.join(dir_path_content,entry)
        dest_path = os.path.join(dest_dir_path,entry)
        
        if os.path.isfile(src_path) and src_path.endswith(".md"):
            dest_file = str(Path(dest_path).with_suffix(".html"))
            generate_page(src_path,template_path,dest_file,basepath)
            
        elif os.path.isdir(src_path):
            # Folder exists before recursion
            print(f"📁 Entering directory: {src_path}")
            os.makedirs(dest_path,exist_ok=True)
            generate_pages_recursive(src_path,template_path,dest_path,basepath)
            

def generate_page(from_path:str,template_path:str, dest_path:str,basepath):
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
    
    output_html = output_html.replace('href="/', 'href="' + basepath)
    output_html = output_html.replace('src="/', 'src="' + basepath)
    
    dest_dir = os.path.dirname(dest_path)
    if dest_dir:
        os.makedirs(dest_dir,exist_ok=True)
        
    with open(dest_path,"w") as f:
        f.write(output_html)
        
    print(f"Written {dest_path}")
    


def extract_title(md):
    lines = md.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2:]
    raise ValueError("no title found")