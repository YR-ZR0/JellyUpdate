# JellyUpdate Beets Plugin

JellyUpdate is a plugin for [Beets](https://beets.io/) that allows you to manually update your Jellyfin library whenever there is a change in your Beets database.

## Installation

1. Clone the repository:

   ```sh
   git clone git@github.com:YR-ZR0/JellyUpdate.git
   ```

2. Install the plugin:

   ```sh
   cd JellyUpdate
   pip install .
   ```

3. Enable the plugin in your Beets configuration file (`config.yaml`):

   ```yaml
   plugins: jellyupdate

   jellyupdate:
     apikey: YOUR_JELLYFIN_API_KEY
     url: http://your.jellyfin.server
     secure: true
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
- `secure`: Set to `false` if your Jellyfin server uses a Self-signed certificate HTTPS, otherwise `true`.

## License

This project is licensed under the MIT License.
