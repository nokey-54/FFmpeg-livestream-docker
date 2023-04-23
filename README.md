# FFmpeg-livestream-docker
Docker Application to 24/7 livestream mp3 files from subfolder and static image. Using Docker + Docker Compose + FFmpeg + python 


1. Ensure u installed docker and docker compose on your maschine.
2. Open docker-compose.yaml and add your api key to line: 8
3. Open folder stream01/mp3 folder. 
4. Replace all songs inside with the songs you wanna stream. Ensure to follow copyright stuff.
5. You're done. Open YouTube and create a new livestream.
6. run "docker-compose --compatibility up -d --build --force-recreate" without the ""
7. Enjoy stream.