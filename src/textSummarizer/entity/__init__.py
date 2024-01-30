from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_url: str
    local_data_file: Path
    unzip_dir: Path
    
@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    status_file: str
    all_required_files: list