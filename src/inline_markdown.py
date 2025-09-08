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
    pattern = r"\[(.*?)\]\((.*?)\)"
    
    matches = re.findall(pattern, text)
    
    return matches
