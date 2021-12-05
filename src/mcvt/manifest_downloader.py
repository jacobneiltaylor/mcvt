from typing import Text, Optional
from requests import Session
from mcvt.constants import (
    LAUNCHER_METADATA_ENDPOINT,
    VERSION_MANIFEST_PATH,
)


class ManifestDownloader:
    def __init__(
        self,
        endpoint: Text = LAUNCHER_METADATA_ENDPOINT,
        client: Optional[Session] = None
    ):
        if not client:
            client = Session()
        self.client = client
        self.endpoint = endpoint


    def get_raw_version_manifest(self):
        response = self.client.get(f"{self.endpoint}{VERSION_MANIFEST_PATH}")
        return response.json()

    def 