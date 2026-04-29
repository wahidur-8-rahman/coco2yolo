# coco2yolo v0.1.0

Convert annotations in standard COCO format to YOLO format from the command line.

## Features

- Convert COCO JSON annotations to YOLO labels
- Install directly from GitHub

---

## Installation

Install using pip:

```bash
pip install git+https://github.com/wahidur-8-rahman/coco2yolo.git
```

---

## Usage

Basic usage:

```bash
coco2yolo <coco_json_file> --dir <output directory>
```

Example:

```bash
coco2yolo _annotations_train.coco.json --dir annotations
```

---

## Command Syntax

```bash
coco2yolo <coco_json_file> --dir <output_directory>
```

### Arguments

| Argument | Description |
|---------|-------------|
| `coco_json_file` | Path to COCO annotation JSON file |
| `--dir` | (Mandataory) Output directory for YOLO labels |

---

## Output

Generated YOLO annotation `.txt` files will be saved in the specified output directory.


---


## Requirements

- Python 3.8+
- pip
- Git

---

## Author

Wahidur Rahman

---

## License

MIT
