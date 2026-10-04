Python Taschenrechner – CI/CD Pipeline

Dieses Projekt implementiert einen einfachen Taschenrechner in Python mit zugehörigen Unit-Tests. Zusätzlich wurde eine vollständige CI/CD-Pipeline mit GitHub Actions erstellt, die den Code prüft, ein Build-Artefakt erzeugt, ein geschütztes Deployment durchführt und automatisch ein Release erstellt.

Projektbeschreibung

Die Anwendung besteht aus einer kleinen Python-Funktionalität zur Berechnung einfacher Operationen. Die Pipeline stellt sicher, dass jede Änderung getestet, gebaut und automatisiert veröffentlicht wird. Das Projekt dient als Beispiel für eine vollständige CI/CD-Umsetzung mit GitHub Actions.

Pipeline im Überblick

Die Pipeline besteht aus zwei zentralen Jobs, die über needs miteinander verbunden sind.

Der test-Job führt folgende Schritte aus:

1.	Repository auschecken
2.	Python einrichten
3.	Cache für Dependencies verwenden
4.	Dependencies installieren
5.	Tests ausführen
6.	Ein Build erzeugen, der ein ZIP-Paket erstellt
7.	Das Build-Artefakt hochladen

Der deploy-Job führt folgende Schritte aus:

1.	Läuft nur nach erfolgreichem test-Job
2.	Läuft ausschließlich auf dem Branch main
3.	Nutzt ein geschütztes Environment mit Reviewer-Freigabe
4.	Prüft ein Secret, ohne dessen Wert auszugeben
5.	Erstellt ein automatisches Release und hängt das ZIP-Artefakt an

Trigger

Die Pipeline startet automatisch bei zwei Ereignissen:

1.	push auf beliebige Branches
2.	pull_request

Der deploy-Job wird ausschließlich ausgeführt, wenn der Branch main betroffen ist und der test-Job erfolgreich abgeschlossen wurde.

Secrets und Environment

Das Projekt verwendet ein Secret mit dem Namen DEPLOY_TOKEN. Der Wert wird nicht ausgegeben, sondern lediglich indirekt geprüft.
Für das Deployment wird ein GitHub Environment mit dem Namen production verwendet. Dieses Environment besitzt eine Schutzregel, die eine manuelle Freigabe durch einen Reviewer erfordert. Zusätzlich ist festgelegt, dass Deployments nur vom Branch main erlaubt sind.

Deployment

Beim Deployment wird das zuvor erzeugte Build-Artefakt heruntergeladen und ein Release erstellt. Das Release enthält das ZIP-Paket der Anwendung. Die erfolgreiche Durchführung des Deployments lässt sich auf der Releases-Seite des GitHub-Repositories überprüfen. Dort erscheint nach jedem erfolgreichen Lauf ein neues Release mit einer fortlaufenden Versionsnummer und dem angehängten Artefakt.

Lokal ausführen

Die Anwendung kann lokal wie folgt ausgeführt und getestet werden:

Virtuelle Umgebung erstellen: python -m venv .venv
Virtuelle Umgebung aktivieren: Linux und macOS: source .venv/bin/activate
Windows: .venv\Scripts\activate

Dependencies installieren: python -m pip install -r requirements.txt

Tests ausführen: python -m pytest -v

Build lokal erzeugen: mkdir -p build python -m zipfile -c build/app.zip src/

Screenshots
Für die Challenge wurden folgende Screenshots erstellt:

•	Übersicht der GitHub Actions
•	test-Job mit sichtbarem Artefakt
•	deploy-Job mit Freigabeanforderung
•	Release-Seite mit ZIP-Artefakt
•	Environment-Einstellungen mit Schutzregel

Reflexion

Im Verlauf des Projekts wurde eine vollständige CI/CD-Pipeline aufgebaut, die alle wesentlichen Elemente moderner Softwarebereitstellung umfasst. 
Dazu gehören automatisierte Tests, Build-Prozesse, Artefaktverwaltung, der Einsatz von Secrets, geschützte Environments und automatisierte Releases. Besonders wertvoll war das Verständnis der Job-Abhängigkeiten, der Schutzmechanismen von GitHub Environments und der sicheren Handhabung von Secrets.
