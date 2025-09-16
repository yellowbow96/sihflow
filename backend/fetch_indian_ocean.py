# file: fetch_indian_ocean.py
from argopy import DataFetcher

# Define region: [lon_min, lon_max, lat_min, lat_max, start_date, end_date]
region = [60, 100, -20, 20, "2023-01", "2023-12"]

# Fetch profiles from ERDDAP (faster than GDAC)
argo = DataFetcher(src="erddap").region(region)

# Convert to xarray dataset
ds = argo.to_xarray()

print(ds)
ds.to_netcdf("indian_ocean_2023.nc")   # save locally for reuse
