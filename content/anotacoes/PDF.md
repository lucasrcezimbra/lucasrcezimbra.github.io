---
title: "PDF"
date: 2023-08-15
lastmod: 2023-10-13
---
## How to merge images into PDF
Using [Python]({{< ref "Python" >}})
```python
from pathlib import Path

from PIL import Image
from PyPDF2 import PdfMerger


path = Path('/home/lucas/Downloads/Photos-001/')

Image.open(path / 'casa1.jpg').save(path / 'casa1.pdf')
Image.open(path / 'casa2.jpg').save(path / 'casa2.pdf')

merger = PdfMerger()
merger.append(path / 'casa1.pdf')
merger.append(path / 'casa2.pdf')
merger.write(path / 'casa.pdf')
merger.close()
```

