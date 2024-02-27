import pandas as pd
from pathlib import Path

abs_path_to_dir = Path(input('Path to files (absolute): '))

new_path = Path(f'{abs_path_to_dir.name}/')
new_path.mkdir(exist_ok=True)

files = [file for file in abs_path_to_dir.glob('*.*') if file.is_file()]
new_files = [pd.read_excel(file).to_csv(new_path / f'{file.name}.csv', index=False, header=True) for file in files]
