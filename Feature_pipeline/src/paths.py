from pathlib import Path
import os

#The history news document will be saved in real_time_data folder.
PARENT_DIR = Path(__file__).parent.resolve().parent
DATA_DIR = PARENT_DIR / 'history_data'

if not Path(DATA_DIR).exists():
    os.mkdir(DATA_DIR)