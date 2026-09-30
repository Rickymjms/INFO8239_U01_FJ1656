from pathlib import Path
import pandas as pd

# Nombres canónicos de los 20 predictores + la variable objetivo 'class'
COLUMN_NAMES = [
    "checking_status", "duration", "credit_history", "purpose", "credit_amount",
    "savings_status", "employment", "installment_commitment", "personal_status",
    "other_parties", "residence_since", "property_magnitude", "age",
    "other_payment_plans", "housing", "existing_credits", "job",
    "num_dependents", "own_telephone", "foreign_worker", "class"
]

def download_csv(url: str, destination="data/raw/dataset.csv") -> Path:
    if not url.startswith(("https://", "http://")):
        raise ValueError("La fuente debe ser una URL HTTP(S)")
    path = Path(destination)
    path.parent.mkdir(parents=True, exist_ok=True)
    
    # Lee el archivo en bruto delimitado por espacios y le asigna las columnas
    frame = pd.read_csv(url, sep=r"\s+", header=None, names=COLUMN_NAMES)
    if frame.empty:
        raise ValueError("El dataset descargado está vacío")
    
    frame.to_csv(path, index=False)
    return path