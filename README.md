![FFmpeg-livestream-docker](https://images.unsplash.com/photo-1594394489098-74ac04c0fc2e?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=4170&q=80)

# FFmpeg Livestream Docker

## Description
This repository contains a versatile Python tool for setting up a 24/7 YouTube Livestream using mp3 files and a static image. The project utilizes FFmpeg, a widely-used multimedia framework for handling audio and video streams, Python for efficient execution and runtime optimization, and Docker for streamlined and secure deployment.

### status: operational 🟢

## Features
- Dockerized for effortless setup and deployment
- Automated management of YouTube livestreams
- Scalable to accommodate multiple streams (Guide coming soon)

## Requirements
1. Docker and Docker Compose installed on your machine
2. A YouTube API key

## Setup
1. Ensure Docker and Docker Compose are installed on your machine
2. Clone this repository to your local machine or server: `git@github.com:nokey-54/FFmpeg-livestream-docker.git`
3. Edit `docker-compose.yaml` and insert your YouTube API key on line 8
4. Navigate to the `stream01/mp3` folder
5. Replace all existing songs with the ones you wish to stream, adhering to copyright regulations
6. Create a new livestream on YouTube
7. Execute `docker-compose --compatibility up -d --build --force-recreate` in your terminal/command prompt
8. Enjoy your livestream!

## Releases
You can find the latest stable releases, along with a brief summary of changes, on the [Releases](https://github.com/nokey-54/FFmpeg-livestream-docker/releases) page.

## TODO

### General
- Extend support to additional streaming platforms (e.g., Twitch, Facebook)
- Implement Health Check Endpoint for Docker Compose

### Guides
- Provide an extended single stream guide
- Offer a Docker guide for Windows and Mac users
- Develop a multiple stream guide
- Enhance README with more comprehensive instructions and examples

## Contributing
We welcome contributions! Feel free to submit a Pull Request or open an issue to discuss potential features or enhancements.

## License
This project is licensed under the [MIT License](LICENSE.md).
