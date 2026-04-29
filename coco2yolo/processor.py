import json
import os
import shutil
from tqdm import tqdm


def convert(cwd, file, dir):

    folder = cwd/ dir #folder -> output folder, dir -> dir name
    folder.mkdir(exist_ok=True)
    
    JSON_PATH = cwd / file
    DEST_PATH=folder
    
    # Load COCO data
    with open(JSON_PATH, 'r') as f:
        coco_data = json.load(f)

  
    images = {img['id']: img for img in coco_data['images']}

    print("Converting annotations...")
    for ann in tqdm(coco_data['annotations']):
        # Skip if segmentation is missing or empty
        if not ann.get('segmentation'):
            continue

        img_info = images[ann['image_id']]
        w, h = img_info['width'], img_info['height']
        img_name = img_info['file_name']
        

        # Create the label text file
        label_filename = os.path.splitext(img_name)[0] + '.txt'
        # label_path = os.path.join(DATASET_ROOT, 'labels/train', label_filename)
        label_path = os.path.join(DEST_PATH, label_filename)


        # Normalize segmentation points [x1, y1, x2, y2...]
        # COCO uses absolute pixels; YOLO uses normalized 0-1 values
        category_id = ann['category_id']
        for poly in ann['segmentation']:
            
            normalized_poly = []
            for i, coord in enumerate(poly):
                if i % 2 == 0:
                    normalized_poly.append(str(round(coord / w, 6))) # x
                else:
                    normalized_poly.append(str(round(coord / h, 6))) # y

            # Format: <class_id> <x1> <y1> <x2> <y2> ...
            line = f"{category_id} {' '.join(normalized_poly)}\n"

            with open(label_path, 'a') as f:
                f.write(line)