![FFmpeg-livestream-docker](https://images.unsplash.com/photo-1594394489098-74ac04c0fc2e?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=4170&q=80)

# FFmpeg-livestream-docker
Welcome to my dockerized YouTube Livestream app. You can easily host multiple YouTube livestreams on your computer in the background. This project uses FFmpeg, the popular multimedia framework, to handle audio and video streams and Docker for simple deployment.

## Features
- Dockerized for easy setup and deployment
- Support for multiple audio formats
- Automatic handling of livestreams on YouTube
- Scalable for multiple streams

## Requirements
1. Docker and Docker Compose installed on your machine.
2. A YouTube API key.

## Setup
1. Ensure you have installed Docker and Docker Compose on your machine.
2. Clone this repository to your local machine or server `git@github.com:nokey-54/FFmpeg-livestream-docker.git`
3. Open `docker-compose.yaml` and add your YouTube API key to line: 8.
4. Open the `stream01/mp3` folder.
5. Replace all songs inside with the songs you want to stream. Make sure to follow copyright regulations.
6. Set up a new livestream on YouTube.
7. Run `docker-compose --compatibility up -d --build --force-recreate` in your terminal/command prompt.
8. Enjoy your livestream!

## TODO
- Add a solution to host multiple streams with the current code
- Extend README with more detailed instructions and examples
- Optimize with `.env` file for lower internet upload rates
- Add a Docker guide for Windows and Mac users
- Add support for more streaming platforms (e.g., Twitch, Facebook)
- Implement a user-friendly web interface for managing streams

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request or open an issue to discuss new features or improvements.

## License
This project is licensed under the [MIT License](LICENSE.md).
