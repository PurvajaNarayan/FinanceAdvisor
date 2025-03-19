import sys
from pathlib import Path

# Add project root to Python path
PROJECT_ROOT = Path(__file__).parent.parent
sys.path.append(str(PROJECT_ROOT))

from datetime import datetime
from src.alpaca_news import download_historical_news

download_historical_news(
    from_date=datetime(2024, 1, 1),
    to_date=datetime(2024, 1, 5),
)