from dataclasses import dataclass
from typing import List, Mapping
from mcvt.version_metadata import VersionMetadata


@dataclass
class VersionManifest:
    latest_release_version: str
    latest_snapshot_version: str
    versions: Mapping[str, VersionMetadata]

    @property
    def latest_release(self) -> VersionMetadata:
        return self.versions[self.latest_release_version]

    @property
    def latest_snapshot(self) -> VersionMetadata:
        return self.versions[self.latest_snapshot_version]
