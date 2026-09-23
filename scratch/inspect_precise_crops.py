import os
from PIL import Image

files = sorted(os.listdir('c:/nimit/scratch/precise_crops'))

# Check crops for specific problem indices
problem_indices = [7, 15, 17, 22, 35, 59, 62, 86]
for idx in problem_indices:
    fn = f"card_{idx:02d}_"
    match = [f for f in files if f.startswith(fn)][0]
    img = Image.open(f'c:/nimit/scratch/precise_crops/{match}')
    print(f"Index {idx:02d} ({match}): size={img.size}")
