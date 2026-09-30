import pandas as pd

TARGET = "class"
REQUIRED = {TARGET, "duration", "credit_amount", "age", "checking_status"}

def load_data():
    return pd.read_csv("data/raw/dataset.csv")

def test_dataset_is_not_empty():
    assert not load_data().empty, "El dataset no debe estar vacío"

def test_required_columns_exist():
    assert REQUIRED <= set(load_data().columns), "Faltan columnas clave requeridas en el dataset"

def test_target_has_no_missing_and_two_classes():
    y = load_data()[TARGET]
    assert y.notna().all(), "El target contiene valores nulos"
    assert y.nunique() >= 2, "El target debe tener al menos dos clases de clasificación"