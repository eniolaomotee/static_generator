set -e
REPO_NAME="https://github.com/eniolaomotee/static_generator"

# Clean docs dir
rm -rf docs
mkdir docs

python3 src/main.py "/$REPO_NAME/"
