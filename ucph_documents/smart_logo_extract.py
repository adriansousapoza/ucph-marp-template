#!/usr/bin/env python3
"""
Smart Logo Extractor
Groups nearby elements together to extract complete logo units (logo + text together).
"""

import os
import sys
from pathlib import Path
import numpy as np
from PIL import Image

def find_logo_groups(image_path, horizontal_gap=100, vertical_gap=50, padding=20):
    """Find groups of elements that should be kept together as complete logos"""
    print(f"\n📸 Analyzing image: {image_path}")
    
    img = Image.open(image_path)
    
    # Convert to RGBA if needed
    if img.mode != 'RGBA':
        img = img.convert('RGBA')
    
    print(f"   - Image size: {img.width}x{img.height}")
    
    # Get alpha channel (transparency)
    alpha = np.array(img.split()[-1])
    
    # Create binary mask (non-transparent pixels)
    mask = alpha > 10
    
    print(f"   - Non-transparent pixels: {np.sum(mask)}")
    
    # Label connected components (individual elements)
    from scipy import ndimage
    labeled, num_features = ndimage.label(mask)
    
    print(f"   - Found {num_features} individual elements")
    
    # Get bounding box for each element
    elements = []
    for i in range(1, num_features + 1):
        region = labeled == i
        pixels = np.argwhere(region)
        
        if len(pixels) == 0:
            continue
        
        y_min, x_min = pixels.min(axis=0)
        y_max, x_max = pixels.max(axis=0)
        
        width = x_max - x_min
        height = y_max - y_min
        
        # Filter out tiny artifacts
        if width < 10 or height < 10:
            continue
        
        elements.append({
            'box': (x_min, y_min, x_max, y_max),
            'width': width,
            'height': height,
            'center_x': (x_min + x_max) / 2,
            'center_y': (y_min + y_max) / 2
        })
    
    print(f"   - Valid elements after filtering: {len(elements)}")
    
    # Group elements that are close together
    print(f"\n🔗 Grouping nearby elements (h_gap={horizontal_gap}px, v_gap={vertical_gap}px)...")
    
    groups = []
    used = [False] * len(elements)
    
    for i, elem1 in enumerate(elements):
        if used[i]:
            continue
        
        # Start a new group
        group = [i]
        used[i] = True
        changed = True
        
        # Keep adding nearby elements to this group
        while changed:
            changed = False
            group_box = get_group_bbox([elements[idx] for idx in group])
            
            for j, elem2 in enumerate(elements):
                if used[j]:
                    continue
                
                # Check if this element is close enough to join the group
                if is_nearby(group_box, elem2, horizontal_gap, vertical_gap):
                    group.append(j)
                    used[j] = True
                    changed = True
        
        groups.append(group)
    
    print(f"   - Grouped into {len(groups)} complete logo units")
    
    # Create final bounding boxes with padding
    logo_boxes = []
    for group in groups:
        group_elements = [elements[idx] for idx in group]
        bbox = get_group_bbox(group_elements)
        
        # Add padding
        x_min = max(0, bbox[0] - padding)
        y_min = max(0, bbox[1] - padding)
        x_max = min(img.width, bbox[2] + padding)
        y_max = min(img.height, bbox[3] + padding)
        
        width = x_max - x_min
        height = y_max - y_min
        
        logo_boxes.append({
            'box': (x_min, y_min, x_max, y_max),
            'width': width,
            'height': height,
            'elements': len(group)
        })
    
    # Sort by position (top to bottom, left to right)
    logo_boxes.sort(key=lambda b: (b['box'][1], b['box'][0]))
    
    return img, logo_boxes


def get_group_bbox(elements):
    """Get bounding box that encompasses all elements in a group"""
    x_min = min(e['box'][0] for e in elements)
    y_min = min(e['box'][1] for e in elements)
    x_max = max(e['box'][2] for e in elements)
    y_max = max(e['box'][3] for e in elements)
    return (x_min, y_min, x_max, y_max)


def is_nearby(bbox, element, h_gap, v_gap):
    """Check if an element is close enough to a bounding box to be grouped together"""
    box1_x_min, box1_y_min, box1_x_max, box1_y_max = bbox
    box2_x_min, box2_y_min, box2_x_max, box2_y_max = element['box']
    
    # Check horizontal distance
    if box2_x_min > box1_x_max:
        h_dist = box2_x_min - box1_x_max
    elif box1_x_min > box2_x_max:
        h_dist = box1_x_min - box2_x_max
    else:
        h_dist = 0  # Overlapping
    
    # Check vertical distance
    if box2_y_min > box1_y_max:
        v_dist = box2_y_min - box1_y_max
    elif box1_y_min > box2_y_max:
        v_dist = box1_y_min - box2_y_max
    else:
        v_dist = 0  # Overlapping
    
    # Elements are nearby if they're close enough in both dimensions
    return h_dist <= h_gap and v_dist <= v_gap


def extract_complete_logos(image_path, output_dir, horizontal_gap=100, vertical_gap=50, padding=20):
    """Extract complete logo units (logo + text together)"""
    
    img, logo_boxes = find_logo_groups(image_path, horizontal_gap, vertical_gap, padding)
    
    if not logo_boxes:
        print("   ⚠️  No logos detected")
        return []
    
    extracted_files = []
    base_name = Path(image_path).stem
    
    print(f"\n✂️  Extracting {len(logo_boxes)} complete logo units...")
    
    for idx, logo_info in enumerate(logo_boxes, 1):
        box = logo_info['box']
        width = logo_info['width']
        height = logo_info['height']
        elements = logo_info['elements']
        
        # Crop the region
        cropped = img.crop(box)
        
        # Save
        output_filename = f"{base_name}_logo{idx:02d}.png"
        output_path = os.path.join(output_dir, output_filename)
        
        cropped.save(output_path)
        extracted_files.append(output_path)
        
        size_kb = os.path.getsize(output_path) / 1024
        print(f"   ✓ Logo {idx}: {output_filename} ({width}x{height}px, {elements} elements) - {size_kb:.1f} KB")
    
    return extracted_files


def main():
    if len(sys.argv) < 2:
        print("Usage: python smart_logo_extract.py <image_file> [output_directory] [--h-gap=100] [--v-gap=50] [--padding=20]")
        print("\nParameters:")
        print("  --h-gap    : Max horizontal gap to group elements (default: 100px)")
        print("  --v-gap    : Max vertical gap to group elements (default: 50px)")
        print("  --padding  : Padding around each logo (default: 20px)")
        print("\nExamples:")
        print("  python smart_logo_extract.py logo_composite.png")
        print("  python smart_logo_extract.py logo_composite.png ./logos --h-gap=150")
        print("  python smart_logo_extract.py logo_composite.png --h-gap=200 --v-gap=100")
        sys.exit(1)
    
    image_path = sys.argv[1]
    
    if not os.path.exists(image_path):
        print(f"Error: File '{image_path}' not found!")
        sys.exit(1)
    
    # Parse arguments
    output_dir = None
    h_gap = 100
    v_gap = 50
    padding = 20
    
    for arg in sys.argv[2:]:
        if arg.startswith("--h-gap="):
            h_gap = int(arg.split("=")[1])
        elif arg.startswith("--v-gap="):
            v_gap = int(arg.split("=")[1])
        elif arg.startswith("--padding="):
            padding = int(arg.split("=")[1])
        elif not output_dir:
            output_dir = arg
    
    # Set output directory
    if not output_dir:
        base_name = Path(image_path).stem
        output_dir = f"{base_name}_complete_logos"
    
    # Create output directory
    os.makedirs(output_dir, exist_ok=True)
    print(f"Output directory: {output_dir}")
    print(f"Settings: h_gap={h_gap}px, v_gap={v_gap}px, padding={padding}px")
    
    # Extract logos
    extracted = extract_complete_logos(image_path, output_dir, h_gap, v_gap, padding)
    
    # Summary
    print("\n" + "="*60)
    print(f"✅ Extraction complete!")
    print(f"Total complete logos extracted: {len(extracted)}")
    print(f"Output directory: {output_dir}")
    print("="*60)
    
    if extracted:
        total_size = sum(os.path.getsize(f) for f in extracted) / 1024
        print(f"\nTotal size: {total_size:.1f} KB")
        print("\nExtracted files:")
        for f in extracted:
            print(f"  • {os.path.basename(f)}")
    else:
        print("\n💡 Tip: Try adjusting --h-gap and --v-gap values")
        print("   - Increase h-gap to group elements further apart horizontally")
        print("   - Increase v-gap to group elements further apart vertically")


if __name__ == "__main__":
    main()
