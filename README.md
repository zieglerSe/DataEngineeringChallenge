# DataEngineeringChallenge

In diesem Repository werden die Grundlagen geschaffen um mittels Python und Kafka Events zu erzeugen und diese zu aggregieren. Simuliert sind Edits verschiedener Wikis, welche in zufälligen Zeitabständen (zwischen 0 und 1 Sekunde) in zwei Topics emittiert werden. 
Die Unterteilung in zwei Topics basiert auf der Fragestellung nach den Edits pro Minute der jeweils (simulierten) deutschen und globalen Wikipedia.

Die Ergebnisse dieser Aggregation werden in einer `.txt` Datei gespeichert, und an jeweils ein zusätzliches dafür vorgesehenes Topic gesendet. 

Um die Anwendung zu verwenden, sind die folgenden Schritte zum Setup nötig: 

Technische Voraussetzungen:

- Python (hier 3.11.5 verwendet)
    - Kafka & Pandas
    - zum Installieren: ``` pip install -r requirements.txt ```

- Docker (samt Docker compose)

Step by Step Anleitung: 

- Laden des Docker Containers mit Kafka und Zookeeper:
    - Im Directory des Docker Containers ausführen: 
        ``` docker-compose -f docker-compose.yml up -d ```
    - Überprüfen, ob Container ausgeführt werden: 
        ``` docker-compose ps ```

- Kommunikation mit Kafka: 
    - Terminal im Directory des Docker Containers öffnen 

    - Starten der Konsole: 
        ``` docker exec -it kafka /bin/bash ```

    - Um eine Übersicht der Topics zu erhalten: 
        ``` kafka-topics.sh --zookeeper zookeeper:2181 -list ```

    - Zurücksetzen der Topics: 
        ``` python
            kafka-topics.sh --delete --zookeeper zookeeper:2181 --topic editsAll
            kafka-topics.sh --delete --zookeeper zookeeper:2181 --topic editsGerm
            kafka-topics.sh --delete --zookeeper zookeeper:2181 --topic avg
            kafka-topics.sh --delete --zookeeper zookeeper:2181 --topic avgGerm
        ```

- Ausführen der Python Scripts: 
    - Es werden 3 Konsolen benötigt
    - Starten der Consumer (`python consumerAllEdits.py` & `python consumerGermanEdits.py`)
    - Starten des Producers (`python DataProducer.py`)

- In den Dateien `outputAll.txt` und `outputGermany.txt` können sowohl die Timestamps, als auch die durchschnittliche Anzahl der Messages pro Minute eingesehen werden. Eine beispielhafte Weiterverarbeitung der Messages (aus dem Topic) ist in `ExampleJson.py` gezeigt. 
