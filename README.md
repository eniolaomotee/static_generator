Static Site Generator
======================

A simple **Markdown to HTML static site generator** built in Python.\
It converts `.md` files into `.html` pages using a template, copies static assets, and organizes everything into a `public/` directory that can be served as a website.

* * * * *

🚀 Features
-----------

-   Converts Markdown (`.md`) files to HTML.

-   Supports **headings, paragraphs, lists, quotes, code blocks, images, and links**.

-   Preserves directory structure: nested folders in `content/` map to nested folders in `public/`.

-   Uses a `template.html` with `{{ Title }}` and `{{ Content }}` placeholders.

-   Copies static files (images, CSS, etc.) from `static/` into `public/`.

-   Built-in development server (`python3 -m http.server`).

* * * * *

📂 Project Structure
--------------------

`.
├── content/             # Markdown files (site content)
│   ├── index.md
│   ├── contact.md
│   └── blog/
│       ├── tom/index.md
│       ├── glorfindel/index.md
│       └── majesty/index.md
│
├── static/              # Static assets (CSS, images, etc.)
│   ├── index.css
│   └── images/
│       ├── rivendell.png
│       └── tolkien.png
│
├── public/              # Generated site (ignored in Git)
│   └── ... (generated HTML + static files)
│
├── src/                 # Python source files
│   ├── main.py
│   ├── page_generator.py
│   ├── htmlnode.py
│   └── utils_markdown.py
│
├── template.html        # Base template
├── main.sh              # Build + serve script
└── README.md`

* * * * *

⚡ Usage
-------

1.  **Install requirements** (Python 3.9+):

    `git clone <repo>
    cd static_generator`

2.  **Generate the site**:

    `./main.sh`

    This will:

    -   Delete the old `public/` directory.

    -   Copy files from `static/` → `public/`.

    -   Convert all Markdown in `content/` → HTML in `public/`.

    -   Start a server at **<http://localhost:8888>**.

3.  **Open your site**:\
    Go to <http://localhost:8888> in your browser.