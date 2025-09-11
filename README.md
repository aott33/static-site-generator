# Static Site Generator

A Python-based static site generator built to create websites from markdown files and templates.

## Project Overview

This static site generator converts markdown content into a fully functional website. The project was developed as part of the [boot.dev backend developer path](https://boot.dev), demonstrating fundamental concepts in web development, file processing, and Python programming.

## Demo Site

The generator was used to build a [J.R. Tolkien Fan Club website](https://github.com/aott33/static-site-generator). You can view the live site and explore the generated output to see the tool in action.

## Features

- Converts markdown files to HTML
- Template-based page generation
- Static asset handling
- Automatic site structure creation
- Clean, semantic HTML output

## Getting Started

### Prerequisites

- Python 3.x
- Basic understanding of markdown syntax

### Installation

1. Clone the repository:
```bash
git clone https://github.com/aott33/static-site-generator.git
cd static-site-generator
```

2. Run the build script:
```bash
./build.sh
```

## Usage

Place your markdown files in the content directory and run the generator to create your static website. The tool will process all markdown files and generate corresponding HTML pages using the provided templates.

## Project Structure

```
static-site-generator/
├── src/           # Source code
├── content/       # Markdown content files
├── static/        # Static assets (CSS, images, etc.)
├── template.html  # HTML template
└── build.sh       # Build script
```

## Learning Objectives

This project was built as part of the boot.dev curriculum and covers:

- File system operations in Python
- Text processing and parsing
- Template rendering
- Web development fundamentals
- Command-line tool development

## Contributing

This is a learning project, but feel free to fork and experiment with your own improvements.

## License

Open source - feel free to use and modify for your own learning purposes.
