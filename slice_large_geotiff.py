from itertools import product

import rasterio
from rasterio import windows


def get_tiles(ds, width=1024, height=1024):
    """
    Generate window positions for tiling a raster.
    """
    ncols, nrows = ds.meta['width'], ds.meta['height']
    offsets = product(range(0, ncols, width), range(0, nrows, height))
    big_window = windows.Window(col_off=0, row_off=0, width=ncols, height=nrows)
    for col_off, row_off in offsets:
        window = windows.Window(col_off=col_off, row_off=row_off, width=width, height=height).intersection(big_window)
        transform = windows.transform(window, ds.transform)
        yield window, transform


def slice_geotiff(input_filename, output_filename_base, tile_size=1024):
    """
    Slice a GeoTIFF into smaller tiles.

    Args:
    - input_filename (str): Path to the input GeoTIFF file.
    - output_filename_base (str): Base path for output files.
    - tile_size (int): The size of the square tile.
    """
    with rasterio.open(input_filename) as dataset:
        tile_num = 1
        for window, transform in get_tiles(dataset, width=tile_size, height=tile_size):
            print(f"Saving tile {tile_num}...")
            output_filename = f"{output_filename_base}_{tile_num}.tiff"
            tile_num += 1
            with rasterio.open(
                    output_filename, 'w', driver='GTiff',
                    height=window.height, width=window.width,
                    count=dataset.count, dtype=dataset.dtypes[0],
                    crs=dataset.crs, transform=transform,
            ) as tile:
                tile.write(dataset.read(window=window))


# Example usage
slice_geotiff('test-data/livoberezhnyi-raion.tiff', 'test-data/output_tile')
