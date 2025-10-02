#!/usr/bin/env python3
"""
PSD Logo Extractor
Extracts individual layers/logos from Photoshop PSD files.
"""

import os
import sys
from pathlib import Path

def extract_psd_layers(psd_path, output_dir):
    """Extract all layers from a PSD file"""
    try:
        from psd_tools import PSDImage
    except ImportError:
        print("psd-tools not installed. Installing now...")
        os.system("pip install psd-tools")
        from psd_tools import PSDImage
    
    print(f"\n📄 Opening PSD file: {psd_path}")
    
    try:
        psd = PSDImage.open(psd_path)
    except Exception as e:
        print(f"❌ Error opening PSD file: {e}")
        return []
    
    print(f"   - Image size: {psd.width}x{psd.height}")
    print(f"   - Layers found: {len(list(psd.descendants()))}")
    
    extracted_files = []
    psd_name = Path(psd_path).stem
    
    # Extract composite image first
    print(f"\n📦 Extracting composite image...")
    try:
        composite = psd.composite()
        output_filename = f"{psd_name}_composite.png"
        output_path = os.path.join(output_dir, output_filename)
        composite.save(output_path)
        extracted_files.append(output_path)
        print(f"   ✓ Saved: {output_filename}")
    except Exception as e:
        print(f"   ✗ Error extracting composite: {e}")
    
    # Extract individual layers
    print(f"\n📦 Extracting individual layers...")
    layer_count = 0
    
    for layer in psd.descendants():
        # Skip group layers and invisible layers
        if layer.is_group():
            continue
        
        layer_count += 1
        layer_name = layer.name if layer.name else f"layer_{layer_count}"
        # Clean layer name for filename
        clean_name = "".join(c if c.isalnum() or c in (' ', '-', '_') else '_' for c in layer_name)
        clean_name = clean_name.strip().replace(' ', '_')
        
        try:
            # Try to extract the layer as an image
            layer_image = layer.composite()
            
            if layer_image:
                output_filename = f"{psd_name}_{layer_count:02d}_{clean_name}.png"
                output_path = os.path.join(output_dir, output_filename)
                
                layer_image.save(output_path)
                extracted_files.append(output_path)
                
                size = os.path.getsize(output_path) / 1024
                print(f"   ✓ Layer {layer_count}: {clean_name} ({layer_image.width}x{layer_image.height}) - {size:.1f} KB")
        except Exception as e:
            print(f"   ✗ Layer {layer_count} ({clean_name}): {e}")
    
    return extracted_files


def show_psd_structure(psd_path):
    """Display the layer structure of a PSD file"""
    try:
        from psd_tools import PSDImage
    except ImportError:
        print("psd-tools not installed. Install with: pip install psd-tools")
        return
    
    print(f"\n📄 PSD File Structure: {psd_path}")
    print("="*60)
    
    try:
        psd = PSDImage.open(psd_path)
        print(f"Size: {psd.width}x{psd.height}")
        print(f"\nLayer hierarchy:")
        
        def print_layer(layer, indent=0):
            prefix = "  " * indent
            if layer.is_group():
                print(f"{prefix}📁 {layer.name} (group)")
                for child in layer:
                    print_layer(child, indent + 1)
            else:
                visible = "👁️" if layer.visible else "🚫"
                print(f"{prefix}{visible} {layer.name} - {layer.kind}")
        
        for layer in psd:
            print_layer(layer)
            
    except Exception as e:
        print(f"❌ Error reading PSD: {e}")


def main():
    if len(sys.argv) < 2:
        print("Usage: python extract_psd_logos.py <psd_file> [output_directory]")
        print("       python extract_psd_logos.py <psd_file> --info  (show structure only)")
        print("\nExample:")
        print("  python extract_psd_logos.py document.psd")
        print("  python extract_psd_logos.py document.psd ./extracted_logos")
        print("  python extract_psd_logos.py document.psd --info")
        sys.exit(1)
    
    psd_path = sys.argv[1]
    
    if not os.path.exists(psd_path):
        print(f"Error: File '{psd_path}' not found!")
        sys.exit(1)
    
    # Check for --info flag
    if "--info" in sys.argv:
        show_psd_structure(psd_path)
        return
    
    # Set output directory
    if len(sys.argv) > 2 and not sys.argv[2].startswith("--"):
        output_dir = sys.argv[2]
    else:
        psd_name = Path(psd_path).stem
        output_dir = f"{psd_name}_layers"
    
    # Create output directory
    os.makedirs(output_dir, exist_ok=True)
    print(f"Output directory: {output_dir}")
    
    # Extract layers
    extracted = extract_psd_layers(psd_path, output_dir)
    
    # Summary
    print("\n" + "="*60)
    print(f"✅ Extraction complete!")
    print(f"Total files extracted: {len(extracted)}")
    print(f"Output directory: {output_dir}")
    print("="*60)
    
    if extracted:
        total_size = sum(os.path.getsize(f) for f in extracted) / 1024
        print(f"\nTotal size: {total_size:.1f} KB")


if __name__ == "__main__":
    main()
