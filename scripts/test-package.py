#!/usr/bin/env python3
"""
Test script to validate the package structure and imports before deployment.
"""

import sys
import importlib.util
from pathlib import Path


def test_package_structure():
    """Test that the package has the expected structure."""
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
    
    print("✅ Package structure looks good")
    return True


def test_imports():
    """Test that the main modules can be imported."""
    print("\n🔍 Testing imports...")
    
    # Add src to path for testing
    src_path = Path("src").absolute()
    sys.path.insert(0, str(src_path))
    
    try:
        # Test basic package import
        import orthophotos_downloader
        print("✅ orthophotos_downloader imported successfully")
        
        # Test submodule imports (skip if dependencies not available)
        try:
            from orthophotos_downloader.data_scraping import auto_downloader
            print("✅ auto_downloader imported successfully")
            
            from orthophotos_downloader.data_scraping import image_download
            print("✅ image_download imported successfully")
            
            from orthophotos_downloader.data_scraping import wms_germany
            print("✅ wms_germany imported successfully")
            
            from orthophotos_downloader.utils import logging
            print("✅ logging utils imported successfully")
            
        except ImportError as e:
            if any(dep in str(e) for dep in ['rasterio', 'geopandas', 'matplotlib', 'OWSLib']):
                print(f"⚠️  Dependency not available: {e}")
                print("   This is expected in CI/test environments without full dependencies")
            else:
                print(f"❌ Import error: {e}")
                return False
        
        return True
        
    except ImportError as e:
        print(f"❌ Import error: {e}")
        return False
    
    finally:
        # Remove src from path
        if str(src_path) in sys.path:
            sys.path.remove(str(src_path))


def test_metadata():
    """Test that package metadata is properly configured."""
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
            print(f"✅ {field}: {project[field]}")
        
        # Check dependencies
        dependencies = project.get("dependencies", [])
        print(f"✅ Dependencies: {len(dependencies)} packages")
        
        return True
        
    except Exception as e:
        print(f"❌ Error reading pyproject.toml: {e}")
        return False


def main():
    """Run all tests."""
    print("🧪 Running pre-deployment tests for orthophotos-downloader\n")
    
    tests = [
        test_package_structure,
        test_imports, 
        test_metadata
    ]
    
    results = []
    for test in tests:
        results.append(test())
    
    print(f"\n📊 Test Results: {sum(results)}/{len(results)} passed")
    
    if all(results):
        print("🎉 All tests passed! Package is ready for deployment.")
        return 0
    else:
        print("❌ Some tests failed. Please fix the issues before deployment.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
