# energyair-bot
The energyair-bot should only be used for educational purposes. Otherwise it is unfair for the other persons that play the game for real. You can try the bot **but at your own risk!**

## Codes
- **code 1:** Error occured
- **code 2:** Not enough answers right
- **code 3:** Something went wrong
- **code 4:** Wrong logo chosen
- **code 5:** Won!

## Getting started

### Windows
#### With Docker
##### Requirements
- [Git](https://git-scm.com/downloads)
- [Docker for Windows](https://store.docker.com/editions/community/docker-ce-desktop-windows)
- Powershell (already installed on Windows)
##### Setup
1. Start the application "Docker for Windows" and wait until Docker is up and running
2. Open the powershell and enter the following commands:
```bash
git clone https://github.com/mirioeggmann/energyair-bot.git
cd energyair-bot
docker build energyair-bot --no-cache -t energyair-bot
```
##### Usage
- Enter the following commands in the powershell:**(don't forget to replace 0793332211 with your own phone number!)**
```bash
docker run -e PHONE_NUMBER=0793332211 -it energyair-bot bash
```
- Now you are in the docker container... to start the bot, just type the following command and press enter:
```bash
start
```
- To stop the bot press *CTRL+C*
- To exit the docker container type the following command and press enter:
```bash
exit
```

#### Without Docker
Not recommended

## Issues
[GitHub Issues](https://github.com/luvirx/energyair-bot/issues) - Got issues? Please tell me, but first check if someone already created one for your problem.

## License
Licensed under the [MIT license](https://opensource.org/licenses/MIT)
