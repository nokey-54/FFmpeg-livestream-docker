# FFmpeg-livestream-docker
Welcome to my dockerized YouTube Livestream app. You can easy host multiple youtube livestreams on your computer in background.



1. Ensure u installed docker and docker compose on your maschine.
2. Open docker-compose.yaml and add your api key to line: 8
3. Open folder stream01/mp3 folder. 
4. Replace all songs inside with the songs you wanna stream. Ensure to follow copyright stuff.
5. You're done. Open YouTube and create a new livestream.
6. run "docker-compose --compatibility up -d --build --force-recreate" without the ""
7. Enjoy stream.



## TODO
- Add solution to host multiple streams with current code
- Extend readme
- Optimization with .env for lower internet upload rates
- Add docker guide for windows and mac
