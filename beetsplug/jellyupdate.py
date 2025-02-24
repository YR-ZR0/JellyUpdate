import requests
import urllib3
from beets.plugins import BeetsPlugin
from beets.ui import Subcommand
from beets import config


class JellyUpdate(BeetsPlugin):
    def __init__(self):
        super(JellyUpdate, self).__init__()
        config["apikey"].redact = True
        self.register_listener("database_change", self.await_db_change)

    def await_db_change(self, lib):
        self.register_listener("cli_exit", self.update_jellyfin)

    def commands(self):
        return [update_command]

    def build_headers(self):
        headers = {}
        authorization = 'MediaBrowser Client="beets", Device="JellyUpdate", DeviceId="f47ac10b-58cc-4372-a567-0e02b2c3d479", Version="0.0.1"'
        headers["Authorization"] = (
            f'{authorization}, Token="{self.config["apikey"].get()}"'
        )
        return headers

    def update_jellyfin(self, lib, opts, args):
        if not self.config["secure"].get():
            urllib3.disable_warnings(category=urllib3.exceptions.InsecureRequestWarning)

        headers = self.build_headers()

        res = requests.post(
            f"{self.config['url'].get()}/Library/Refresh",
            headers=headers,
            verify=self.config["secure"].get(),
            timeout=5,
        )
        match res.status_code:
            case 204:
                self._log.info("Jellyfin library scan started!")
            case 401:
                self._log.fatal("Invalid API key")
            case 403:
                self._log.fatal("API key does not have permission to update library")
            case _:
                self._log.fatal("Failed to update Jellyfin library")


update_command = Subcommand("jupdate", help="Manually Update your Jellyfin library")
update_command.func = JellyUpdate().update_jellyfin
