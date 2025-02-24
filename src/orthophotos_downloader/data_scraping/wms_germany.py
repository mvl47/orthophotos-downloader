from orthophotos_downloader.data_scraping.image_download import (
    ImageDownloader,
    ExtendedWebMapService,
)


class BayernDop40ImageDownloader(ImageDownloader):
    """
    A class for downloading images from the Bayern DOP40 WMS service.
    The WMS specifications are automatically set to the Bayern DOP40 service.

    Attributes:
        grid_spacing: The grid spacing in meters for the image download.
    """

    def __init__(self, grid_spacing: int):
        """
        Initialize the BayernDop40ImageDownloader.

        Args:
            grid_spacing: The grid spacing in meters for the image download.

        Raises:
            ValueError: If the width and height of the image exceed 6000 pixels for the Bayern DOP40 WMS.
        """
        # Define the parameters specific for the DOP40 WMS
        wms = ExtendedWebMapService(
            url="https://geoservices.bayern.de/od/wms/dop/v1/dop40?",
            version="1.1.1",
            resolution=0.4,
            layer_name="by_dop40c",
            crs="EPSG:25832",
            format="image/tiff",
        )

        if int(grid_spacing / wms.resolution) > 6000:
            raise ValueError(
                "The width and height of the image cannot exceed 6000 pixels for the Bayern DOP40 WMS"
            )

        super().__init__(wms=wms, grid_spacing=grid_spacing)


class BayernDop20ImageDownloader(ImageDownloader):
    """
    A class for downloading images from the Bayern DOP20 WMS service.
    The WMS specifications are automatically set to the Bayern DOP20 service.

    Attributes:
        grid_spacing: The grid spacing in meters for the image download.
    """

    def __init__(self, grid_spacing: int):
        """
        Initialize the BayernDop20ImageDownloader.

        Args:
            grid_spacing: The grid spacing in meters for the image download.

        Raises:
            ValueError: If the width and height of the image exceed 6000 pixels for the Bayern DOP20 WMS.
        """
        # Define the parameters specific for the DOP20 WMS
        wms = ExtendedWebMapService(
            url="https://geoservices.bayern.de/od/wms/dop/v1/dop20?",
            version="1.1.1",
            resolution=0.2,
            layer_name="by_dop20c",
            crs="EPSG:25832",
            format="image/tiff",
        )

        if int(grid_spacing / wms.resolution) > 6000:
            raise ValueError(
                "The width and height of the image cannot exceed 6000 pixels for the Bayern DOP20 WMS"
            )

        super().__init__(wms=wms, grid_spacing=grid_spacing)


class BWDop20ImageDownloader(ImageDownloader):
    """
    A class for downloading images from the BW DOP20 WMS service.
    The WMS specifications are automatically set to the BW DOP20 service.

    Attributes:
        grid_spacing: The grid spacing in meters for the image download.
    """

    def __init__(self, grid_spacing: int):
        """
        Initialize the BayernDop20ImageDownloader.

        Args:
            grid_spacing: The grid spacing in meters for the image download.

        Raises:
            ValueError: If the width and height of the image exceed 6000 pixels for the Bayern DOP20 WMS.
        """
        # Define the parameters specific for the DOP20 WMS
        wms = ExtendedWebMapService(
            url="https://owsproxy.lgl-bw.de/owsproxy/ows/WMS_LGL-BW_ATKIS_DOP_20_C?",
            version="1.1.1",
            resolution=0.2,
            layer_name="IMAGES_DOP_20_RGB",
            crs="EPSG:25832",
            format="image/jpeg",
        )

        if int(grid_spacing / wms.resolution) > 6000:
            raise ValueError(
                "The width and height of the image cannot exceed 6000 pixels for the Bayern DOP20 WMS"
            )

        super().__init__(wms=wms, grid_spacing=grid_spacing)


class BkgDop20ImageDownloader(ImageDownloader):
    """
    A class for downloading images from the BKG DOP20 WMS service.
    The WMS specifications are automatically set to the BKG DOP20 service.
    Can Only be used with an UUID access that you can buy from thew BKG.

    Attributes:
        grid_spacing: The grid spacing in meters for the image download.
    """

    def __init__(self, grid_spacing: int, uuid: str):
        """
        Initialize the BkgDop20ImageDownloader.

        Args:
            grid_spacing: The grid spacing in meters for the image download.
            uuid: The UUID is used for authentication.

        Raises:
            ValueError: If the width and height of the image exceed 6000 pixels for the BKG DOP20 WMS.
        """
        # Define the parameters specific for the DOP20 WMS
        wms = ExtendedWebMapService(
            url=f"https://sg.geodatenzentrum.de/wms_dop__{uuid}?",
            version="1.1.1",
            resolution=0.2,
            layer_name="rgb",
            crs="EPSG:25832",
            format="image/tiff",
        )

        if int(grid_spacing / wms.resolution) > 6000:
            raise ValueError(
                "The width and height of the image cannot exceed 6000 pixels for the BKG DOP20 WMS"
            )

        super().__init__(wms=wms, grid_spacing=grid_spacing)

    def to_dict(self) -> dict:
        """Return a serializable dictionary representation of the BkgDop20ImageDownloader object."""
        r = super().to_dict()
        # replace the uuid with a placeholder to avoid exposing the secret
        r["wms"]["url"] = self.wms.wms.url.split("__")[0] + "__<secret_uuid>?"
        return r
