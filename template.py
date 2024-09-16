import os
from pathlib import Path

list_of_files =[
    f"LICENSE",
    f"README.md",
    f"requirements.txt",
    f"setup.py",


    f"src/components/__init__.py",
    f"src/components/data_ingestion.py",
    f"src/components/data_transformation.py",
    f"src/components/model_trainer.py",

    
    f"src/__init__.py",
    f"src/exception.py",
    f"src/logger.py",
    f"src/main.py",
    f"src/utils.py",

    f"pipeline/__init__.py",
    f"pipeline/predict_pipeline.py",
    f"pipeline/train_pipeline.py",


]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir !="":
        os.makedirs(filedir, exist_ok=True)
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
    else:
        print(f"file is already present at: {filepath}")