#!/usr/bin/env python3
"""
Simple structure test that doesn't require dependencies.
"""

import sys
from pathlib import Path


def test_basic_structure():
    """Test basic package structure without importing dependencies."""
    print("🧪 Running basic package structure test\n")
    
    print("🔍 Testing package structure...")
    
    # Check if src/orthophotos_downloader exists
    src_path = Path("src/orthophotos_downloader")
    if not src_path.exists():
        print("❌ src/orthophotos_downloader directory not found")
        return False
    
    # Check for __init__.py
    if not (src_path / "__init__.py").exists():
        print("❌ src/orthophotos_downloader/__init__.py not found")
        return False
    
    # Check for required modules
    required_modules = [
        "data_scraping/__init__.py",
        "data_scraping/auto_downloader.py", 
        "data_scraping/image_download.py",
        "data_scraping/wms_germany.py",
        "utils/__init__.py",
        "utils/logging.py"
    ]
    
    for module in required_modules:
        if not (src_path / module).exists():
            print(f"❌ {module} not found")
            return False
        print(f"✅ {module} found")
    
    print("\n🔍 Testing metadata...")
    
    try:
        import tomllib
        with open("pyproject.toml", "rb") as f:
            config = tomllib.load(f)
        
        project = config.get("project", {})
        
        # Check required fields
        required_fields = ["name", "version", "description", "authors"]
        for field in required_fields:
            if field not in project:
                print(f"❌ Missing required field in pyproject.toml: {field}")
                return False
            print(f"✅ {field}: OK")
        
        # Check dependencies
        dependencies = project.get("dependencies", [])
        print(f"✅ Dependencies: {len(dependencies)} packages")
        
        print(f"\n✅ All tests passed! Package structure is ready.")
        return True
        
    except Exception as e:
        print(f"❌ Error reading pyproject.toml: {e}")
        return False


if __name__ == "__main__":
    success = test_basic_structure()
    sys.exit(0 if success else 1)
