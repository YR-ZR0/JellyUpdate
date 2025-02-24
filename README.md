# JellyUpdate Beets Plugin

JellyUpdate is a plugin for [Beets](https://beets.io/) that allows you to manually update your Jellyfin library whenever there is a change in your Beets database.

## Installation

1. Clone the repository:

   ```sh
   git clone /path/to/JellyUpdate
   ```

2. Install the plugin:

TODO: Add instructions for installing the plugin

3. Enable the plugin in your Beets configuration file (`config.yaml`):

   ```yaml
   plugins: jellyupdate

   jellyupdate:
     apikey: YOUR_JELLYFIN_API_KEY
     url: http://your.jellyfin.server
     secure: true # Set to false if using HTTPS self-signed certificate
   ```

## Usage

To manually trigger a Jellyfin library update, use the following command:

```sh
beet jupdate
```

JellyUpdate also listens for the events `cli_exit` and `database_change` to automatically update your Jellyfin library whenever there is a change in your Beets database.

## Configuration

- `apikey`: Your Jellyfin API key.
- `url`: The URL of your Jellyfin server.
- `secure`: Set to `true` if your Jellyfin server uses HTTPS, otherwise `false`.

## License

This project is licensed under the MIT License.
