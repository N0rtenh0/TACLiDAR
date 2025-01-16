# Script de Processamento MDT

## Trabalho feito por
André Rodrigues a041851
Marta Teixeira a042166

## Visão Geral
Este script processa um Modelo Digital de Elevação (DEM) usando a biblioteca RVT (Raster Visualization Toolkit). Ele calcula a inclinação, a sombra da colina e o fator de visão do céu a partir dos dados LiDAR fornecidos e salva os resultados como arquivos GeoTIFF. O script também inclui funcionalidade para visualizar os resultados.

## Requisitos
Para executar este script, é preciso ter os seguintes pacotes Python instalados:

- `rvt`
- `rasterio`
- `matplotlib`
- `numpy`

Os pacotes necessário podem ser instalados usando o pip: 

- `pip install rvt rasterio matplotlib numpy`
- `conda install rvt`

## Uso
1. **Preparar os Dados**: Certifique-se de ter um arquivo .tif do seu DEM. Atualize a variável `mdt_path` no script para apontar para o seu arquivo .tif.

2. **Execute o Script**: Execute o script usando Python:

   ```bash
   python prog.py
   ```

3. **Saída**: O script criará um diretório chamado `clean/` (se ainda não existir) e salvará os resultados processados como arquivos GeoTIFF:
   - `hillshade.tif`
   - `sky_view_factor.tif`
   - `slope.tif`

4. **Visualização**: O script exibirá os resultados em uma única janela com três subgráficos para sombra da colina, fator de visão do céu e inclinação.

## Funções
- `process_slope_in_tiles(dem, tile_size=50)`: Processa o DEM para calcular a inclinação em blocos.
- `process_hillshade_in_tiles(dem, tile_size=50)`: Processa o DEM para calcular a sombra da colina em blocos.
- `process_dem_in_tiles(dem, tile_size=50)`: Processa o DEM para calcular o fator de visão do céu em blocos.
- `get_optimal_tile_size(dem_shape, max_memory_mb=1024)`: Calcula o tamanho de bloco ideal com base na memória disponível.

## Notas
- Certifique-se de que o DEM de entrada é válido e não está vazio.
- O script inclui tratamento de erros para arquivo não encontrado e valores de resolução inválidos.
  
## Resultados
Sky View
![sky_view_factor](https://github.com/user-attachments/assets/62b27100-5c1e-4ee7-a781-5c8c4fe64c1f)

Slope
![slope](https://github.com/user-attachments/assets/35c0f3a4-09f9-48fc-89a9-4534afd3d389)

Hillshade
![hillshade](https://github.com/user-attachments/assets/f811a59c-9651-45e8-9c05-ff5d3f0a1464)



