import unittest
from unittest.mock import patch, MagicMock
from beetsplug.jellyupdate import JellyUpdate


class TestJellyUpdate(unittest.TestCase):
    def setUp(self):
        self.plugin = JellyUpdate()
        self.plugin.config = {
            "apikey": MagicMock(get=MagicMock(return_value="test_api_key")),
            "url": MagicMock(get=MagicMock(return_value="http://test.url")),
            "secure": MagicMock(get=MagicMock(return_value=False)),
        }

    @patch("requests.post")
    def test_update_jellyfin_success(self, mock_post):
        mock_post.return_value.status_code = 204
        with self.assertLogs(self.plugin._log, "INFO") as log:
            self.plugin.update_jellyfin(None, None, None)
            self.assertIn("Jellyfin library scan started!", log.output[0])

    @patch("requests.post")
    def test_update_jellyfin_invalid_api_key(self, mock_post):
        mock_post.return_value.status_code = 401
        with self.assertLogs(self.plugin._log, level="FATAL") as log:
            self.plugin.update_jellyfin(None, None, None)
            self.assertIn("Invalid API key", log.output[0])

    @patch("requests.post")
    def test_update_jellyfin_no_permission(self, mock_post):
        mock_post.return_value.status_code = 403
        with self.assertLogs(self.plugin._log, level="FATAL") as log:
            self.plugin.update_jellyfin(None, None, None)
            self.assertIn(
                "API key does not have permission to update library", log.output[0]
            )

    @patch("requests.post")
    def test_update_jellyfin_failure(self, mock_post):
        mock_post.return_value.status_code = 500
        with self.assertLogs(self.plugin._log, level="FATAL") as log:
            self.plugin.update_jellyfin(None, None, None)
            self.assertIn("Failed to update Jellyfin library", log.output[0])

    def test_config_host(self):
        self.assertEqual(self.plugin.config["url"].get(), "http://test.url")

    def test_config_api_key(self):
        self.assertEqual(self.plugin.config["apikey"].get(), "test_api_key")

    def test_config_secure(self):
        self.assertEqual(self.plugin.config["secure"].get(), False)


if __name__ == "__main__":
    unittest.main()
