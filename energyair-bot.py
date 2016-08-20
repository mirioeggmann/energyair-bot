# coding=utf-8

# Script: energyair-bot.py v0.3 by luvirx
## How to call, run: ./race.sh

# Imports
from selenium import webdriver

# Questions and answers
questions = {
    'Wo findet das grösste Jazz-Festival Europas statt?' : 2,
    'Woher stammt Kungs?' : 1,
    'Mit welchem Hit gelang Kungs der europaweite Durchbruch?' : 1,
    'Welche Sängerin singt im Remix «Dont Be So Shy» von Filatov & Karas?' : 3,
    'Die wievielte Ausgabe des Energy Air findet 2016 statt?' : 2,
    'Wie heisst Dua Lipas neuster Hit?' : 2,
    'Was gehört für viele bei einem Festival auf den Kopf?' : 3,
    'Wie war der Slogan des legendären Woodstock Festival?' : 1,
    'Als was arbeitete Dua Lipa vor ihrer Musikkarriere?' : 2,
    'Woher stammen Dua Lipas Eltern?' : 3,
    'Welcher Energy Air Act trat schon mal am Tomorrowland auf?' : 3,
    'Welches Festival findet in der gleichen Stadt statt wie Energy Air?' : 2,
    'Wie heisst Manillios aktuelles Album?' : 1,
    'Wie heisst der neue Song von Kungs?' : 2,
    'Wie heisst der Frontsänger von OneRepublic?' : 3,
    'In welcher Stadt findet das Energy Air 2016 statt?' : 1,
    'Woher stammt das DJ-Duo Filatov & Karas?' : 2,
    'Was ist ein Line-Up?' : 2,
    'In welchem Kanton findet das Gampel Openair statt?' : 3,
    'Wie lautet der Slogan des Energy Air?' : 3,
    'Welche Acts kommen ans Energy Air?' : 1,
    'Wo findet das Energy Air dieses Jahr statt?' : 1,
    'Welche Energy Radiostation existiert nicht?' : 3,
    'In welchem Jahr wurde Kungs geboren?' : 2,
    'Wie lautet der offizielle Hashtag für das Energy Air 2016?' : 1,
    'Woher kommt das «Holi Festival of Colours» ursprünglich?' : 2,
    'Welches Sujet taucht rund ums Energy Air immer wieder auf?' : 1,
    'Wer stand letztes Jahr bei Energy Air als erstes auf der Bühne?' : 3,
    'Wie heisst der offizielle Energy Air Song 2015?' : 3,
    'Wie viel Technikmaterial wurde letztes Jahr für die Show benötigt?' : 3,
    'Wo ist Rapper Manillio aufgewachsen?' : 3,
    'Wie lautet Manillios bürgerlicher Name?' : 1,
    'Aus wie vielen Musikern besteht OneRepublic?' : 2,
    'In welchem Bundesstaat feiern Musikbegeisterte das Coachella Festival?' : 2,
    'Wie viele Konzertliebhaber feiern das Energy Air jedes Jahr?' : 3,
    'Welcher dieser Acts war am letzten Energy Air nicht dabei?' : 3
}

# Start Firefox and open the game site
driver = webdriver.Firefox()
driver.get('https://game.energy.ch')

# Start the ggame
driver.find_element_by_link_text('Los gehts!').click()

# Answer all questions with the help of the answer list
for i in range(10):
    question = driver.find_element_by_tag_name('h1').text
    answer = questions[question.encode('utf-8', 'ignore')]
    driver.find_elements_by_tag_name('label')[answer-1].click()
    driver.find_element_by_id('submitQuestion').click()

# Klick on 1 of the 12 logos
driver.find_element_by_tag_name('button').click()
driver.find_elements_by_tag_name('a')[6].click()

# Close the window if you didn't win
if(driver.find_element_by_tag_name('h1').text == "Das war das falsche Logo, knapp daneben! Versuche es erneut!"):
    driver.quit()