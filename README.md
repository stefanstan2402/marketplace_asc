Nume: Stan Ștefan

Grupă: 333CB

Tema 1 ASC - Marketplace

Explicație pentru soluția aleasă:

Tema implementează problema Multiple Producers - Multiple Consumers, cu precizarea că acești comsumatori pot deveni producători eliminând produsele din cart.

#Producer:

	Producerii sunt theadurile care crează produse noi, care sunt "published" în marketplace. Ei primesc o listă de produse care le aparțin. Dacă marketplace-ul accepta publicarea unui produs, producerul că trebui să aștepte un timp specific. Altfe, vă așteptă un timp dat threadului la creare.

#Consumer:

	Consumerii crează carturi în marketplace, în care adaugă sau scot produse. Când se termină toate aceste operații, se plasează o comandă pe cart și produsele sunt returnate consumatorului.

#Marketplace:

	Marketplace-ul aduce comunicarea și sincronizarea între threadurile aferente producerilor și consumerilor. Stochează o listă de liste de produse, unde fiecare lista internă e asociată că id după id-ul producătorului, și carturile, ținute tot că lista de liste, unde fiecare lista internă e asociată după id cu id-ul cartului. Folosesc lockuri pentru înregistrarea unui producer, crearea unui cart, și adăugarea/ștergerea unui produs din cart.

	Implementarea din marketplace conține și instantierea unui logger, în constructor, după cum se cere în cerință, și de asemenea, fiecare funcție are, în implementarea să, logare la nivel de info pentru intrarea și ieșirea din funcție, respectiv logare la nivel de eroare pentru cazurile funcțiilor ce returnează false (nu a fost găsit productul).

	De asemenea, implementarea din marketplace conține și teste unitare, create în clasă TestMarketplace, unde sunt testate funcționalitățile fiecărei clase din clasa Marketplace.

	Detalierea implementării fiecărei funcții în parte se găsește în comentariile aferente fiecărei funcții.

#Consideri că tema este utilă?

Deși pare o tema simplă, consider că este utilă pentru sedimentarea informațiilor de la APD, și pentru înțelegerea conceptelor de multithreading într-un limbaj mai high-level.

Consideri implementarea naivă, eficientă, se putea mai bine?

Implementarea mea nu este una naivă, dar nu este nici cea mai performanță, dat fiind faptul că testul 10 nu rulează în 60 de secunde decât foarte rar, în rest trebuie mărit timpul pentru că acesta să fie terminat, și da, se putea mai bine (cred că implementarea cu liste de liste și căutarea prin acestea aduce ineficientă, în rest cred că implementarea este una bună. )

	#Întregul enunț al temei este implementat - implementarea propriu zisa + teste unitare + logging + director .git.

Dificultățile date de această tema au fost la început, când nu știam exact de unde să apuc conceptul de mulți producer, mulți consumer, dar am revizuit slide-urile de la laburile de APD de semestrul trecut și am reușit să implementez destul de ok. Ce mi s-a părut interesant a fost la final când am descoperit că folosirea unor structuri de date mai eficiente duce la un timp mai mic de rulare a testelor.

Că și resurse, am utilizat slide-urile de la labul de APD unde am făcut problema producer-consumer, și laburile de ASC de Python, pe care le-am refăcut de la 0.

	#Git

	Link către repo-ul de git: https://github.com/stefanstan2402/marketplace_asc

	Repo-ul este privat, o să îl fac public atunci când se vă termina și deadline ul hard al temei.
