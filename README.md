Dit project bevat 2 folders in de root. Eentje is een python api en de ander een symfony website. De python api kan je opstarten door naar die folder te gaan en daar docker compose up te runnen via docker. Als je een python omgeving hebt kun je hem ook gewoon starten. De symfony app is niet gedockerized vanwege performance problemen.
De home page van het project is een site waar je functies in kan gooien die geplot worden. De api accepteerd niet alleen x maar ook bijvoorbeeld t als variabele. De symfony app communiceerd met de python api om de plots te genereren. 
