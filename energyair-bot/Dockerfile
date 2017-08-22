FROM python:3.6
USER root

RUN python3 -m pip install lxml
RUN python3 -m pip install requests
RUN git clone https://github.com/mirioeggmann/energyair-bot.git /work/energyair-bot
RUN echo 'alias start="python3 /work/energyair-bot/energyair-bot/energyair-bot-light.py"' >> ~/.bashrc
