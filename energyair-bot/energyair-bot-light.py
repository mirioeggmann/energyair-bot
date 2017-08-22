import sys
from lxml import html
import requests
import os

rounds = 0
phoneNumber = os.environ["PHONE_NUMBER"]
print("using " + str(phoneNumber) + " as phone number")
questions = {
    'Wann fand das erste Energy Air statt?' : 1,
    'Wann ist die offizielle Türöffnung beim Energy Air?' : 1,
    'Von wem wird das Energy Air durchgeführt?' : 1,
    'Wer hatte den letzten Auftritt am Energy Air 2016?' : 1,
    'Welche Plätze gibt es am Energy Air?' : 3,
    'Wie heissen zwei andere grosse Events von Energy?' : 1,
    'Wie hiess die Energy Air Hymne 2015?' : 1,
    'Welcher Künstler stand NOCH NIE auf der Energy Air Bühne?' : 1,
    'Ab wann darf man, ohne eine erwachsene Begleitperson, am Energy Air teilnehmen?' : 3,
    'Welcher dieser Acts Stand schon auf der Stade de Suisse Bühne?' : 2,
    'Von welchem ehemaligen Energy Air Act ist der Song «Bilder im Kopf»?' : 1,
    'Welcher DJ stand noch nie auf der Energy Air Bühne?' : 2,
    'Wann fand das Energy Air letztes Jahr statt?' : 1,
    'Welcher Energy Air Act aus den letzten Jahren stand nur mit seinem Gitarristen auf der Bühne?' : 1,
    'Welches Stadion ist das grösste der Schweiz?' : 1,
    'Wie oft pro Jahr findet das Energy Air statt?' : 3,
    'Was bedeutet Air auf Deutsch?' : 2,
    'Wann wurde das Stade de Suisse offiziell fertig gestellt?' : 1,
    'Welcher Pop-Sänger stand in diesem Jahr schon auf der Bühne des Stade de Suisse?' : 1,
    'Welche deutsche Sängerin stand letztes Jahr auf der Energy Air Bühne?' : 1,
    'Mit welchem Künstler stand Schlangenfrau Nina Burri auf der Bühne?' : 1,
    'In welchem Jahr stand OneRepublic auf der Bühne des Energy Air?' : 1,
    'Welcher Act performte in einem Karton-Hippie-Bus?' : 3,
    'Wie heissen die beiden anderen grossen Events von Energy?' : 1,
    'Wann findet das diesjährige Energy Air statt?' : 2,
    'Was ist das Energy Air als einziger Energy Event?' : 1,
    'Wie lautet der offizielle Energy Air Hashtag?' : 3,
    'Wo findet das Energy Air statt?' : 3,
    'Wann ist offiziell Türöffnung beim Energy Air?' : 1,
    'Wie viele Sitzplätze hat das Stade de Suisse bei Sport Veranstaltungen?' : 1,
    'Wo kann man Energy Air Tickets kaufen?' : 3,
    'Zum wievielten Mal findet das Energy Air statt?' : 2,
    'Von welchem ehemaligen Energy Air Act ist der Song «Bilder im Kopf»?' : 1,
    'Welcher Act stand NOCH NIE auf der Energy Air Bühne?' : 3,
    'Wie hiess das Stade de Suisse früher?' : 1,
    'Wie viel kostet ein Energy Air Ticket?' : 1,
    'Welcher Act stand NOCH NIE auf der Energy Air Bühne?' : 1,
    'Welche Farben dominieren das Energy Air Logo?' : 3,
    'Welcher Act stand schon einmal auf der Energy Air Bühne?' : 1,
    'Wer war der letzte Act am Energy Air 2016?' : 3,
    'In welchen Schweizer Stadt hat Energy KEIN Radiostudio?' : 3,
    'Wann fand das erste Energy Air statt?' : 1,
    'Von welchem vergangenen Energy Air Act ist der Song «Angelina»?' : 1,
    'Wie viele Zuschauer passen ins Stade de Suisse?' : 1,
    'Wie hiess der Energy Air Song im Jahr 2014?' : 3,
    'Wie viele Tage dauert das Energy Air?' : 3,
    'Von wem wird das Energy Air durchgeführt?' : 1,
    'Wie viel kostet die Energy Air App?' : 2,
    'Wie viele Tickets werden für das Energy Air verlost?' : 1,
    'Wie gross ist die Spielfläche des Stade de Suisse?' : 2,
    'Wie hiess im Jahr 2015 die Energy Air Hymne?' : 1,
    'Das Energy Air ist ...?' : 1,
    'Wie viele Male standen Dabu Fantastic bereits auf der Energy Air Bühne?' : 1,
    'Welcher Fussballverein ist im Stade de Suisse Zuhause?' : 1,
    'Ab wann darf man am Energy Air teilnehmen?' : 1,
    'Was ist die obere Altersbeschränkung des Energy Air?' : 2,
    'In welchem Monat findet das Energy Air jeweils statt?' : 2,
    'Was für Plätze gibt es am Energy Air?' : 3,
    'In welcher Schweizer Stadt hat Energy KEIN Radiostudio?' : 3
}

def get_answer(question):
    answer = questions.get(question, 0)
    if answer == 0:
        return 1
    return answer

def next_question(antwort):
    data = {'question': antwort}
    q2 = session.post('https://game.energy.ch/', data)
    tree = html.fromstring(q2.content)
    frage = tree.xpath('//form[@class="question"]/h1/text()')[0]
    return frage

try:
    while True:
        try:
            rounds += 1
            session = requests.session()
            data = {'mobile': phoneNumber}
            q1 = session.post('https://game.energy.ch/', data)
            tree = html.fromstring(q1.content)

            frage = tree.xpath('//form[@class="question"]/h1/text()')[0]
            print("answering questions...")
            for i in range(9):
                antwort = get_answer(frage)
                frage = next_question(antwort)
            antwort = get_answer(frage)

            data = {'question': antwort}
            q2 = session.post('https://game.energy.ch/', data)
            print("all questions answered!")

            tree = html.fromstring(q2.content)
            verloren = tree.xpath('//div[@id="content"]/h2/text()')
            if verloren[0] == "Glückwunsch!":
                data = {'site': 'win'}
                q2 = session.post('https://game.energy.ch/', data)
                q2 = session.get('https://game.energy.ch/?ticket=10')
                tree = html.fromstring(q2.content)
                verloren = tree.xpath('//div[@id="wingame"]/h1/text()')
                if len(verloren) == 1:
                    if verloren[0] != "Das war das falsche Logo, knapp daneben! Versuche es erneut!":
                        f = open('win.txt', 'wb')
                        f.write(q2.content)
                        f.close()
                        print("won!")
                    else:
                        print("code 4")
                        print("restart...")
                else:
                    print("code 3")
                    print("restart...")
            else:
                print("code 2")
                print("restart...")

        except Exception:
            print("code 1")
            print("restart...")
            pass
finally:
    print("\n\n------see ya------")
    print("Rounds: " + str(rounds))
    print("------------------")
    sys.exit(0)
