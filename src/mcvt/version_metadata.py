from dataclasses import dataclass
from datetime import datetime


@dataclass
class VersionMetadata:
    version_id: str
    release: bool
    url: str
    time: datetime
    release_time: datetime
    fingerprint: str
    compliance_level: int

    @property
    def snapshot(self):
        return not self.release
