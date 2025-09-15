from argopy import DataFetcher
import matplotlib.pyplot as plt

# Example float in Indian Ocean
float_id = 6902746
argo = DataFetcher()

# Fetch dataset for that float
ds = argo.float(float_id).to_xarray()

# Check what variables exist
print("Variables in dataset:", list(ds.data_vars))

# Pick latest profile (last N_PROF index)
latest = ds.isel(N_PROF=-1)

# Extract arrays
pres = latest["PRES"].values.flatten()
temp = latest["TEMP"].values.flatten()
psal = latest["PSAL"].values.flatten()

# --- Plot Temperature & Salinity vs Depth ---
fig, axs = plt.subplots(1, 2, figsize=(10, 7))

# Temperature
axs[0].plot(temp, pres, color="royalblue", marker="o")
axs[0].invert_yaxis()
axs[0].set_xlabel("Temperature (°C)")
axs[0].set_ylabel("Pressure (dbar)")
axs[0].set_title(f"Float {float_id} - Temp Profile")

# Salinity
axs[1].plot(psal, pres, color="darkorange", marker="o")
axs[1].invert_yaxis()
axs[1].set_xlabel("Salinity (PSU)")
axs[1].set_title(f"Float {float_id} - Salinity Profile")

plt.suptitle("Latest Argo Profile", fontsize=14)
plt.tight_layout()
plt.show()
