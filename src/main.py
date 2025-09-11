import sys
from copy_static import copy_static_to_public
from page_generator import generate_pages_recursive
default_basepath = "/"


def main():
    basepath = default_basepath
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
        
    if not basepath.endswith("/"):
        basepath += "/"
    
    print(f"Using basepath: {basepath}")
    
    copy_static_to_public()
    generate_pages_recursive("content","template.html","docs",basepath)
    
if __name__ == "__main__":
    main()