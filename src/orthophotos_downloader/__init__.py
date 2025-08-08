# Version information
__version__ = "0.1.0rc3"

# Lazy imports to avoid heavy dependencies during package introspection
def _lazy_import():
    """Lazy import of main components to avoid dependency issues during build/CI."""
    try:
        from .utils.logging import setup_logging
        from .data_scraping.auto_downloader import AutoOrthophotoDownloader, auto_download_orthophotos
        
        setup_logging()
        return AutoOrthophotoDownloader, auto_download_orthophotos
    except ImportError:
        # This allows the package to be importable even without heavy dependencies
        # useful for CI/CD and package introspection
        return None, None

# Make main components available at package level when dependencies are available
try:
    AutoOrthophotoDownloader, auto_download_orthophotos = _lazy_import()
    if AutoOrthophotoDownloader is not None:
        __all__ = ['AutoOrthophotoDownloader', 'auto_download_orthophotos', '__version__']
    else:
        __all__ = ['__version__']
except ImportError:
    AutoOrthophotoDownloader = None
    auto_download_orthophotos = None
    __all__ = ['__version__']
