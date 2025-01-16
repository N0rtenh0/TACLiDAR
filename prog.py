import os
import rvt.default
import rvt.vis
import rvt.blend
import rasterio
from rasterio.plot import show
import matplotlib.pyplot as plt
import numpy as np
import time

# **Configuração do Ambiente Python com RVT:**


# **Carregar o MDT LiDAR:**
mdt_path = 'Tester/teste1.tif'  # Replace with path to your .tif file
output_dir = "clean/"  # Diretório para salvar os resultados
os.makedirs(output_dir, exist_ok=True)

# Verifique se o arquivo existe
if not os.path.exists(mdt_path):
    raise FileNotFoundError(f"O arquivo MDT {mdt_path} não foi encontrado.")

# Ler o MDT usando Rasterio
with rasterio.open(mdt_path) as src:
    mdt = src.read(1)  # Leia a primeira banda
    profile = src.profile  # Salve as propriedades do arquivo
    transform = src.transform

# Obter a resolução do MDT
resolution_x = transform[0]  # Resolução no eixo X
resolution_y = -transform[4]  # Resolução no eixo Y (geralmente negativa, então inverte o sinal)

# Verificações iniciais
if mdt.size == 0:
    raise ValueError("Empty DEM provided")

if resolution_x <= 0 or resolution_y <= 0:
    raise ValueError(f"Invalid resolution values: x={resolution_x}, y={resolution_y}")

# **Funções de Processamento:**
def process_slope_in_tiles(dem, tile_size=50):
    """
    Processa o MDT em blocos menores para calcular a declividade,
    mostrando progresso e tempo estimado
    """
    rows, cols = dem.shape
    result = np.zeros_like(dem, dtype=np.float32)
    total_tiles = ((rows + tile_size - 1) // tile_size) * ((cols + tile_size - 1) // tile_size)
    current_tile = 0
    start_time = time.time()
    
    print("\nProcessing Slope:")
    for i in range(0, rows, tile_size):
        for j in range(0, cols, tile_size):
            current_tile += 1
            elapsed_time = max(time.time() - start_time, 0.001)  # Prevent division by zero
            tiles_per_second = current_tile / elapsed_time
            remaining_tiles = total_tiles - current_tile
            estimated_remaining_time = remaining_tiles / tiles_per_second
            
            print(f"\rProgress: {current_tile}/{total_tiles} tiles ({(current_tile/total_tiles)*100:.1f}%) - Est. remaining time: {estimated_remaining_time:.1f}s", end="")
            
            # Define tile bounds
            row_end = min(i + tile_size, rows)
            col_end = min(j + tile_size, cols)
            
            # Process tile
            tile = dem[i:row_end, j:col_end]
            tile_result = rvt.vis.slope_aspect(
                dem=tile,
                resolution_x=resolution_x,
                resolution_y=resolution_y,
                output_units="degree"
            )["slope"]
            
            # Store result
            result[i:row_end, j:col_end] = tile_result
    
    print("\nSlope processing complete!")
    return result

def process_hillshade_in_tiles(dem, tile_size=50):
    """
    Processa o MDT em blocos menores para calcular o sombreamento,
    mostrando progresso e tempo estimado
    """
    try:
        rows, cols = dem.shape
        result = np.zeros_like(dem, dtype=np.float32)
        total_tiles = ((rows + tile_size - 1) // tile_size) * ((cols + tile_size - 1) // tile_size)
        current_tile = 0
        start_time = time.time()
        
        print("\nProcessing Hillshade:")
        for i in range(0, rows, tile_size):
            for j in range(0, cols, tile_size):
                current_tile += 1
                elapsed_time = max(time.time() - start_time, 0.001)  # Prevent division by zero
                tiles_per_second = current_tile / elapsed_time
                remaining_tiles = total_tiles - current_tile
                estimated_remaining_time = remaining_tiles / tiles_per_second
                
                print(f"\rProgress: {current_tile}/{total_tiles} tiles ({(current_tile/total_tiles)*100:.1f}%) - Est. remaining time: {estimated_remaining_time:.1f}s", end="")
                
                # Define tile bounds
                row_end = min(i + tile_size, rows)
                col_end = min(j + tile_size, cols)
                
                # Process tile
                tile = dem[i:row_end, j:col_end]
                tile_result = rvt.vis.hillshade(
                    dem=tile,
                    resolution_x=resolution_x,
                    resolution_y=resolution_y,
                    sun_elevation=45,
                    sun_azimuth=315
                )
                
                # Store result
                result[i:row_end, j:col_end] = tile_result
        
        print("\nHillshade processing complete!")
        return result
    except Exception as e:
        print(f"\nError processing hillshade: {str(e)}")
        raise

def process_dem_in_tiles(dem, tile_size=50):
    """
    Processa o MDT em blocos menores para calcular o Sky View Factor,
    mostrando progresso e tempo estimado
    """
    rows, cols = dem.shape
    result = np.zeros_like(dem, dtype=np.float32)
    total_tiles = ((rows + tile_size - 1) // tile_size) * ((cols + tile_size - 1) // tile_size)
    current_tile = 0
    start_time = time.time()
    
    print("\nProcessing Sky View Factor:")
    for i in range(0, rows, tile_size):
        for j in range(0, cols, tile_size):
            current_tile += 1
            elapsed_time = max(time.time() - start_time, 0.001)  # Prevent division by zero
            tiles_per_second = current_tile / elapsed_time
            remaining_tiles = total_tiles - current_tile
            estimated_remaining_time = remaining_tiles / tiles_per_second
            
            print(f"\rProgress: {current_tile}/{total_tiles} tiles ({(current_tile/total_tiles)*100:.1f}%) - Est. remaining time: {estimated_remaining_time:.1f}s", end="")
            
            # Define tile bounds
            row_end = min(i + tile_size, rows)
            col_end = min(j + tile_size, cols)
            
            # Process tile
            tile = dem[i:row_end, j:col_end]
            tile_result = rvt.vis.sky_view_factor(
                dem=tile,
                resolution=resolution_x,
            )
            
            # Extract just the SVF values from the dictionary
            svf_values = tile_result["svf"]
            
            # Store result
            result[i:row_end, j:col_end] = svf_values
    
    print("\nSky View Factor processing complete!")
    return result

# **Processamento do MDT:**
slope = process_slope_in_tiles(mdt, tile_size=50)
hillshade = process_hillshade_in_tiles(mdt, tile_size=50)
sky_view_factor = process_dem_in_tiles(mdt, tile_size=50)

# **Salvar Resultados como GeoTIFF:**
output_files = {
    "hillshade": os.path.join(output_dir, "hillshade.tif"),
    "sky_view_factor": os.path.join(output_dir, "sky_view_factor.tif"),
    "slope": os.path.join(output_dir, "slope.tif"),
}

for key, output_path in output_files.items():
    with rasterio.open(
        output_path,
        "w",
        driver="GTiff",
        height=mdt.shape[0],
        width=mdt.shape[1],
        count=1,
        dtype=mdt.dtype,
        crs=profile["crs"],
        transform=profile["transform"]
    ) as dst:
        dst.write(locals()[key], 1)

# **Visualização dos Resultados:**
fig, axes = plt.subplots(1, 3, figsize=(18, 6))

# Hillshade
axes[0].imshow(hillshade, cmap="gray", aspect="auto")
axes[0].set_title("Hillshade")
axes[0].axis("off")

# Sky-view Factor
axes[1].imshow(sky_view_factor, cmap="gray", aspect="auto")
axes[1].set_title("Sky-view Factor")
axes[1].axis("off")

# Slope
axes[2].imshow(slope, cmap="terrain", aspect="auto")
axes[2].set_title("Slope")
axes[2].axis("off")

plt.tight_layout()
plt.show()

print(f"Resultados processados e salvos em: {output_dir}")

# **Função para Calcular Tamanho Ideal do Bloco:**
def get_optimal_tile_size(dem_shape, max_memory_mb=1024):
    """
    Calcula o tamanho ideal dos blocos baseado na memória disponível
    para evitar problemas de memória durante o processamento
    """
    pixel_size_bytes = 4  # tamanho de um float32
    total_pixels = dem_shape[0] * dem_shape[1]
    max_pixels_per_tile = (max_memory_mb * 1024 * 1024) // pixel_size_bytes
    suggested_tile_size = int(np.sqrt(max_pixels_per_tile))
    return min(suggested_tile_size, 500)  # Limita o tamanho máximo a 500

# **Uso da Função para Definir Tamanho do Bloco:**
tile_size = get_optimal_tile_size(mdt.shape)