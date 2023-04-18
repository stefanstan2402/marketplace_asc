Nume: Stan Stefan
Grupă: 333CB

Tema 1 ASC - Marketplace

Explicație pentru soluția aleasă:

Tema implementeaza problema  Multiple Producers - Multiple Consumers, cu precizarea ca acesti comsumatori pot deveni producatori eliminand produsele din cart.

#Producer:
	
	Producerii sunt theadurile care creaza produse noi, care sunt "published" in marketplace. Ei primesc o lista de produse care le apartin. Daca marketplace-ul accepta publicarea unui produs, producerul ca trebui sa astepte un timp specific. Altfe, va astepta un timp dat threadului la creare.


#Consumer: 
	
	Consumerii creaza carturi in marketplace, in care adauga sau scot produse. Cand se termina toate aceste operatii, se plaseaza o comanda pe cart si produsele sunt returnate consumatorului.


#Marketplace:
	
	Marketplace-ul aduce comunicarea si sincronizarea intre threadurile aferente producerilor si consumerilor. Stocheaza o lista de liste de produse, unde fiecare lista interna e asociata ca id dupa id-ul producatorului, si carturile, tinute tot ca lista de liste, unde fiecare lista interna e asociata dupa id cu id-ul cartului. Folosesc lockuri pentru inregistrarea unui producer, crearea unui cart, si adaugarea/stergerea unui produs din cart.
	Implementarea din marketplace contine si instantierea unui logger, in constructor, dupa cum se cere in cerinta, si de asemenea, fiecare functie are, in implementarea sa, logare la nivel de info pentru intrarea si iesirea din functie, respectiv logare la nivel de eroare pentru cazurile functiilor ce returneaza false (nu a fost gasit productul).
	De asemenea, implementarea din marketplace contine si teste unitare, create in clasa TestMarketplace, unde sunt testate functionalitatile fiecarei clase din clasa Marketplace.
	Detalierea implementarii fiecarei functii in parte se gaseste in comentariile aferente fiecarei functii.
	
#Consideri că tema este utilă?
	
	Desi pare o tema simpla, consider ca este utila pentru sedimentarea informatiilor de la APD, si pentru intelegerea conceptelor de multithreading intr-un limbaj mai high-level. 

Consideri implementarea naivă, eficientă, se putea mai bine?
	
	Implementarea mea nu este una naiva, dar nu este nici cea mai performanta, dat fiind faptul ca testul 10 nu ruleaza in 60 de secunde decat foarte rar, in rest trebuie marit timpul pentru ca acesta sa fie terminat, si da, se putea mai bine(cred ca implementarea cu liste de liste si cautarea prin acestea aduce ineficienta, in rest cred ca implementarea este una buna.)


#Intregul enunt al temei este implementat -> implementarea propriu zisa + teste unitare + logging + director .git. 

Dificultatile date de aceasta tema au fost la inceput, cand nu stiam exact de unde sa apuc conceptul de multi producer, multi consumer, dar am revizuit slide-urile de la laburile de APD de semestrul trecut si am reusit sa implementez destul de ok. Ce mi s-a parut interesant a fost la final cand am descoperit ca folosirea unor structuri de date mai eficiente duce la un timp mai mic de rulare a testelor.

Ca si resurse, am utilizat slide-urile de la labul de APD unde am facut problema producer-consumer, si laburile de ASC de Python, pe care le-am refacut de la 0.

#Git

	Link către repo-ul de git: https://github.com/stefanstan2402/marketplace_asc

	Repo-ul este privat, o sa il fac public atunci cand se va termina si deadline ul hard al temei. 

