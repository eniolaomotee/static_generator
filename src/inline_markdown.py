from text_node import TextNodeType, TextNode
import re

def split_nodes_delimiter(old_nodes, delimiter,text_type):
    new_node = []
    for old_node in old_nodes:
        if old_node.text_type != TextNodeType.TEXT:
            new_node.append(old_node)
            continue
        
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("Please check closing delimiter")
        
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextNodeType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_node.extend(split_nodes)
    return new_node



def extract_markdown_images(text):
    pattern = r"!\[(.*?)\]\((.*?)\)"
    
    matches = re.findall(pattern, text)
    return matches

def extract_markdown_links(text):
    pattern = r"(?<!!)\[(.*?)\]\((.*?)\)"
    
    matches = re.findall(pattern, text)
    
    return matches

def split_nodes_images(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextNodeType.TEXT:
            new_nodes.append(old_node)
            continue
        
        images = extract_markdown_images(old_node.text)
        if not images:
            new_nodes.append(old_node)
            continue
        
        text = old_node.text
        for alt, url in images:
            # Split around the first occurence of the exact image markdown
            before,after = text.split(f"![{alt}]({url})", 1)
            
            if before:
                new_nodes.append(TextNode(before,TextNodeType.TEXT))
                
            new_nodes.append(TextNode(alt, TextNodeType.IMAGE, url))
            
            text = after
            
        if text:
            new_nodes.append(TextNode(text, TextNodeType.TEXT))
    return new_nodes

def split_nodes_links(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextNodeType.TEXT:
            new_nodes.append(old_node)
            continue
        
        links = extract_markdown_links(old_node.text)
        if not links:
            new_nodes.append(old_node)
            continue
        
        text = old_node.text
       
        for alt,url in links:
            before, after = text.split(f"[{alt}]({url})", 1)

            
            if before:
                new_nodes.append(TextNode(before, TextNodeType.TEXT))
                
            new_nodes.append(TextNode(alt, TextNodeType.LINK, url))
            
            text = after
        
        if text:
            new_nodes.append(TextNode(text, TextNodeType.TEXT)) 
    return new_nodes
        


def text_to_textnodes(text:str) -> list[TextNode]:
    # Start with one big text node
    nodes = [TextNode(text,TextNodeType.TEXT)]
    
    # Split out bold (**..**)
    nodes = split_nodes_delimiter(nodes, "**", TextNodeType.BOLD)
    
    # Split out italic(_.._)
    nodes = split_nodes_delimiter(nodes, "_", TextNodeType.ITALIC)
    
    # Split out code
    nodes = split_nodes_delimiter(nodes, "`", TextNodeType.CODE)
    
    # Split out images
    nodes = split_nodes_images(nodes)
    
    # Split out links
    nodes = split_nodes_links(nodes)
    
    return nodes

def markdown_to_blocks(markdown):
    rawblock = markdown.split("\n\n")
    output = []
    for block in rawblock:
        if not block.strip():
            continue
        
        cleaned_lines = [line.strip() for line in block.splitlines() if line.strip()]
        if cleaned_lines:
            output.append("\n".join(cleaned_lines))
    return output
