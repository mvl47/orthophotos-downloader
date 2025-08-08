# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Multi-state orthophoto download functionality
- AutoOrthophotoDownloader class for automatic state detection
- Cross-border support for areas spanning multiple German federal states
- Comprehensive API documentation and examples
- Enhanced visualization pipeline for multi-state downloads

### Changed
- Improved project structure and documentation
- Enhanced file organization for multi-state outputs

### Fixed
- Various bug fixes and improvements

## [0.1.0] - 2025-01-XX

### Added
- Initial release of orthophotos-downloader
- Support for German WMS services
- Basic orthophoto download functionality
- Core WMS integration for German federal states
- RGB, CIR, and RGBI image type support
- Basic visualization tools

### Dependencies
- geopandas==0.14.4
- imageio==2.34.0
- matplotlib==3.8.4
- OWSLib==0.30.0
- rasterio==1.3.10
- requests==2.31.0

[Unreleased]: https://github.com/ffe-munich/orthophotos-downloader/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/ffe-munich/orthophotos-downloader/releases/tag/v0.1.0
