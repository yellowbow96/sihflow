from argopy import DataFetcher

argo = DataFetcher()

# Fetch float 6902746, cycle 1
ds = argo.profile(6902746, 1).to_xarray()
print(ds)
