import tkinter as tk
from tkinter import ttk, messagebox
import random
#instaleaza pachetul tkinter dacă esti in linux cu comanda:     sudo apt update && sudo apt install -y python3-tk
# Baza de date cu intrebarile si raspunsurile extrase din fisier
QUESTIONS_DB = [
    # ==================== CURSUL 1 ====================
    {
        "curs": "Cursul 1",
        "tip": "Quiz",
        "q": "1. Adevărat sau fals: trebuie să achiziționați Unity Pro pentru a crea jocuri.",
        "correct": "False (Fals)",
        "options": ["True (Adevărat)", "False (Fals)"]
    },
    {
        "curs": "Cursul 1",
        "tip": "Quiz",
        "q": "2. Care vizualizare ne permite să manipulăm vizual obiectele dintr-o scenă?",
        "correct": "The Scene view",
        "options": ["The Scene view", "The Game view", "The Inspector view", "The Hierarchy view"]
    },
    {
        "curs": "Cursul 1",
        "tip": "Quiz",
        "q": "3. Adevărat sau fals: ar trebui să mutați întotdeauna fișierele dvs. active în Unity și să nu utilizați exploratorul de fișiere al sistemului de operare.",
        "correct": "True (Adevărat)",
        "options": ["True (Adevărat)", "False (Fals)"]
    },
    {
        "curs": "Cursul 1",
        "tip": "Quiz",
        "q": "4. Adevărat sau fals: Când creați un proiect nou, ar trebui să includeți fiecare activ pe care îl credeți minunat.",
        "correct": "False (Fals)",
        "options": ["True (Adevărat)", "False (Fals)"]
    },
    {
        "curs": "Cursul 1",
        "tip": "Quiz",
        "q": "5. Ce mod introduceți în vizualizarea Scenă atunci când țineți apăsat butonul din dreapta al mouse-ului?",
        "correct": "Flythrough mode",
        "options": ["Flythrough mode", "Orbit mode", "Pan mode", "Play mode"]
    },
    {
        "curs": "Cursul 1",
        "tip": "Q&A",
        "q": "Q&A: Sunt activele (assets) și obiectele de joc (GameObjects) la fel?",
        "correct": "Nu chiar. Activele au un fișier sau grup de fișiere pe hard disk, în timp ce un obiect de joc nu are. Un activ poate conține sau nu un obiect de joc.",
        "options": [
            "Nu chiar. Activele au un fișier sau grup de fișiere pe hard disk, în timp ce un obiect de joc nu are. Un activ poate conține sau nu un obiect de joc.",
            "Da, sunt complet identice și termenii pot fi folosiți interschimbabil.",
            "Nu. Obiectele de joc sunt salvate direct pe hard disk ca fișiere separate, iar activele există doar în memoria RAM.",
            "Da, dar numai în proiectele 3D."
        ]
    },
    {
        "curs": "Cursul 1",
        "tip": "Q&A",
        "q": "Q&A: Există o mulțime de controale și opțiuni diferite. Va trebui să le memorez imediat pe toate?",
        "correct": "Deloc. Cele mai multe controale și opțiuni vor fi deja setate la o stare implicită care acoperă majoritatea situațiilor.",
        "options": [
            "Deloc. Cele mai multe controale și opțiuni vor fi deja setate la o stare implicită care acoperă majoritatea situațiilor.",
            "Da, Unity nu funcționează dacă nu configurați manual fiecare control înainte de rulare.",
            "Doar controalele avansate de iluminare și fizică trebuie memorate din prima zi.",
            "Da, deoarece Unity nu are valori implicite pentru componente."
        ]
    },

    # ==================== CURSUL 2 ====================
    {
        "curs": "Cursul 2",
        "tip": "Quiz",
        "q": "1. Ce înseamnă D în 2D și 3D?",
        "correct": "Dimensiune.",
        "options": ["Dimensiune.", "Direcție.", "Distanță.", "Dinamică."]
    },
    {
        "curs": "Cursul 2",
        "tip": "Quiz",
        "q": "2. Câte transformări există?",
        "correct": "Trei.",
        "options": ["Trei.", "Două.", "Patru.", "Șase."]
    },
    {
        "curs": "Cursul 2",
        "tip": "Quiz",
        "q": "3. Adevărat sau Fals: Unity nu are obiecte încorporate și trebuie să le creați.",
        "correct": "Fals. Unity vă oferă multe obiecte încorporate.",
        "options": [
            "Fals. Unity vă oferă multe obiecte încorporate.",
            "Adevărat. Trebuie să modelați fiecare obiect într-un program extern.",
            "Adevărat, cu excepția camerei principale.",
            "Fals. Unity are doar un singur obiect încorporat (Cubul)."
        ]
    },
    {
        "curs": "Cursul 2",
        "tip": "Quiz",
        "q": "4. Dacă doriți ca un obiect să fie „așezat pe partea sa” 5 unități la dreapta poziției sale actuale, ați roti obiectul și apoi îl translatați sau translatați obiectul și apoi îl rotiți?",
        "correct": "Translație și apoi rotație.",
        "options": [
            "Translație și apoi rotație.",
            "Rotație și apoi translație.",
            "Scalare și apoi rotație.",
            "Ordinea operațiilor este irelevantă."
        ]
    },
    {
        "curs": "Cursul 2",
        "tip": "Q&A",
        "q": "Q&A: Este important să învățați atât conceptele 2D, cât și cele 3D?",
        "correct": "Da. Chiar și jocurile care sunt în întregime 3D utilizează încă unele dintre conceptele 2D la nivel tehnic.",
        "options": [
            "Da. Chiar și jocurile care sunt în întregime 3D utilizează încă unele dintre conceptele 2D la nivel tehnic.",
            "Nu. Jocurile 3D nu folosesc niciodată coordonate sau elemente 2D.",
            "Doar dacă realizați jocuri exclusiv pentru mobil.",
            "Nu, conceptele 2D sunt învechite și eliminate din Unity."
        ]
    },
    {
        "curs": "Cursul 2",
        "tip": "Q&A",
        "q": "Q&A: Ar trebui să învăț să folosesc toate obiectele de joc încorporate imediat?",
        "correct": "Nu neapărat. Există multe obiecte de joc și poate fi copleșitor să încercați să le învățați imediat.",
        "options": [
            "Nu neapărat. Există multe obiecte de joc și poate fi copleșitor să încercați să le învățați imediat.",
            "Da, este obligatoriu să le folosiți pe toate în fiecare scenă.",
            "Da, deoarece sunt doar două obiecte de joc încorporate.",
            "Nu, obiectele încorporate nu trebuie folosite niciodată."
        ]
    },
    {
        "curs": "Cursul 2",
        "tip": "Q&A",
        "q": "Q&A: Care este cel mai bun mod de a vă familiariza cu transformările?",
        "correct": "Practică. Continuă să lucrezi cu ele; în cele din urmă, vor deveni destul de naturale.",
        "options": [
            "Practică. Continuă să lucrezi cu ele; în cele din urmă, vor deveni destul de naturale.",
            "Memorarea tabelelor matematice de rotație fără a deschide editorul.",
            "Evitarea folosirii mouse-ului în Scene View.",
            "Scrierea de shadere personalizate pentru fiecare obiect."
        ]
    },

    # ==================== CURSUL 3 ====================
    {
        "curs": "Cursul 3",
        "tip": "Quiz",
        "q": "1. Adevărat sau fals: Din cauza naturii lor simple, pătratele alcătuiesc ochiuri (meshes) în modele.",
        "correct": "Fals, ochiurile de plasă sunt alcătuite din triunghiuri.",
        "options": [
            "Fals, ochiurile de plasă sunt alcătuite din triunghiuri.",
            "Adevărat, pătratele sunt baza tuturor modelelor 3D.",
            "Fals, ochiurile de plasă sunt alcătuite din cercuri.",
            "Adevărat, dar numai pentru personaje."
        ]
    },
    {
        "curs": "Cursul 3",
        "tip": "Quiz",
        "q": "2. Ce formate de fișier acceptă Unity pentru modelele 3D?",
        "correct": "fișierele .fbx, .dae, .3ds, .dxf și .obj.",
        "options": [
            "fișierele .fbx, .dae, .3ds, .dxf și .obj.",
            "doar fișierele .png, .jpg și .bmp.",
            "fișierele .mp3, .wav și .ogg.",
            "doar fișierele .exe și .dll."
        ]
    },
    {
        "curs": "Cursul 3",
        "tip": "Quiz",
        "q": "3. Adevărat sau Fals: Numai modelele plătite pot fi descărcate din Unity Assets Store.",
        "correct": "Fals. Există mai multe modele gratuite.",
        "options": [
            "Fals. Există mai multe modele gratuite.",
            "Adevărat. Toate activele din magazin sunt contra cost.",
            "Adevărat, modelele gratuite sunt disponibile doar în Unity Pro.",
            "Fals. În Unity Asset Store nu există modele 3D, ci doar sunete."
        ]
    },
    {
        "curs": "Cursul 3",
        "tip": "Quiz",
        "q": "4. Explicați relația dintre texturi, shadere și materiale.",
        "correct": "Materialele conțin texturi și shadere. Shaders dictează proprietățile care pot fi setate de material și modul în care materialul devine prestat (randat).",
        "options": [
            "Materialele conțin texturi și shadere. Shaders dictează proprietățile care pot fi setate de material și modul în care materialul devine prestat (randat).",
            "Texturile conțin materiale și shadere, iar materialele sunt simple imagini 2D.",
            "Shaderele sunt fișiere audio, iar materialele controlează doar coliziunile fizice.",
            "Nu există nicio relație între ele; se aplică independent direct pe cameră."
        ]
    },
    {
        "curs": "Cursul 3",
        "tip": "Q&A",
        "q": "Q&A: Voi mai putea face jocuri dacă nu sunt artist?",
        "correct": "Absolut. Folosind resurse online gratuite și Unity Asset Store, puteți găsi diverse opere de artă pentru a le pune în jocurile dvs.",
        "options": [
            "Absolut. Folosind resurse online gratuite și Unity Asset Store, puteți găsi diverse opere de artă pentru a le pune în jocurile dvs.",
            "Nu, Unity blochează compilarea jocului dacă nu desenați singur modelele.",
            "Doar jocuri text fără nicio interfață grafică.",
            "Nu, deoarece Unity Asset Store este accesibil doar artiștilor certificați."
        ]
    },
    {
        "curs": "Cursul 3",
        "tip": "Q&A",
        "q": "Q&A: Va trebui să știu să folosesc toate shaderele încorporate?",
        "correct": "Nu neapărat. Multe shaders sunt foarte situaționale. Începeți cu cele de bază și învățați mai multe dacă proiectul o cere.",
        "options": [
            "Nu neapărat. Multe shaders sunt foarte situaționale. Începeți cu cele de bază și învățați mai multe dacă proiectul o cere.",
            "Da, fiecare material trebuie să folosească toate shaderele simultan.",
            "Nu, deoarece Unity nu are shadere încorporate.",
            "Da, altfel modelele 3D nu pot fi importate în proiect."
        ]
    },
    {
        "curs": "Cursul 3",
        "tip": "Q&A",
        "q": "Q&A: Dacă există active de artă plătite în Unity Asset Store, asta înseamnă că pot vinde propriile mele active?",
        "correct": "Ba da. Dacă puteți crea active de înaltă calitate (nu doar de artă), le puteți vinde cu siguranță în magazin.",
        "options": [
            "Ba da. Dacă puteți crea active de înaltă calitate (nu doar de artă), le puteți vinde cu siguranță în magazin.",
            "Nu, doar compania Unity are voie să vândă active în Asset Store.",
            "Da, dar numai fișiere audio, nu și modele sau scripturi.",
            "Nu, toate activele încărcate de utilizatori devin automat gratuite."
        ]
    },

    # ==================== CURSUL 4 ====================
    {
        "curs": "Cursul 4",
        "tip": "Quiz",
        "q": "1. Adevărat sau fals: Puteți face peșteri din teren Unity.",
        "correct": "Fals, terenul Unității nu se poate suprapune.",
        "options": [
            "Fals, terenul Unității nu se poate suprapune.",
            "Adevărat, folosind peria de săpare orizontală.",
            "Adevărat, terenul Unity permite goluri subterane native.",
            "Fals, deoarece terenul Unity nu poate fi modificat pe înălțime."
        ]
    },
    {
        "curs": "Cursul 4",
        "tip": "Quiz",
        "q": "2. Cum se numește o imagine în tonuri de gri care conține informații despre altitudinea terenului?",
        "correct": "O hartă a înălțimii (Heightmap).",
        "options": [
            "O hartă a înălțimii (Heightmap).",
            "Un Skybox.",
            "Un Culling Mask.",
            "Un RigidBody."
        ]
    },
    {
        "curs": "Cursul 4",
        "tip": "Quiz",
        "q": "3. Adevărat sau fals: Sculptura terenului în Unity este foarte mult ca pictura.",
        "correct": "Adevărat.",
        "options": ["Adevărat.", "Fals."]
    },
    {
        "curs": "Cursul 4",
        "tip": "Quiz",
        "q": "4. Cum accesați texturile de teren disponibile ale Unity?",
        "correct": "Importați activele terenului mergând la Active > Import Pachet > Active teren.",
        "options": [
            "Importați activele terenului mergând la Active > Import Pachet > Active teren.",
            "Mergând la File > Build Settings > Terrain.",
            "Din fereastra Game > Add Texture.",
            "Apăsând tasta F12 în timpul rulării jocului."
        ]
    },
    {
        "curs": "Cursul 4",
        "tip": "Q&A",
        "q": "Q&A: Jocul meu trebuie să aibă teren?",
        "correct": "Deloc. Multe jocuri au loc în întregime în interiorul camerelor modelate sau în spații abstracte.",
        "options": [
            "Deloc. Multe jocuri au loc în întregime în interiorul camerelor modelate sau în spații abstracte.",
            "Da, o scenă Unity nu poate rula fără un obiect Terrain.",
            "Da, altfel personajele nu pot fi adăugate în Hierarchy.",
            "Doar jocurile 2D au nevoie obligatoriu de un obiect Terrain 3D."
        ]
    },
    {
        "curs": "Cursul 4",
        "tip": "Q&A",
        "q": "Q&A: Terenul meu nu arată prea bine. E normal?",
        "correct": "Da, este nevoie de timp și practică pentru a construi competență cu instrumentele de sculptură și testarea nivelului.",
        "options": [
            "Da, este nevoie de timp și practică pentru a construi competență cu instrumentele de sculptură și testarea nivelului.",
            "Nu, înseamnă că placa video este defectă.",
            "Nu, terenul ar trebui să se genereze fotorealist singur fără intervenție.",
            "Da, deoarece Unity nu suportă aplicarea texturilor pe teren."
        ]
    },

    # ==================== CURSUL 5 ====================
    {
        "curs": "Cursul 5",
        "tip": "Quiz",
        "q": "1. Ce setare controlează cât de mult copacii se leagănă în vânt?",
        "correct": "Aceasta este o întrebare truc. Copacii nu se balansează în vânt, iarba o face. Setarea care îl controlează este Bending (under Wind Settings).",
        "options": [
            "Aceasta este o întrebare truc. Copacii nu se balansează în vânt, iarba o face. Setarea care îl controlează este Bending (under Wind Settings).",
            "Setarea Tree Sway Speed din fereastra Lighting.",
            "Proprietatea Culling Mask a camerei.",
            "Setarea Gravity din Physics Manager."
        ]
    },
    {
        "curs": "Cursul 5",
        "tip": "Quiz",
        "q": "2. Care este numele efectului ambiental care poate simula ceața sau decolorarea culorilor la distanță?",
        "correct": "Ceață. Fog",
        "options": ["Ceață. Fog", "Skybox", "Heightmap", "Flythrough"]
    },
    {
        "curs": "Cursul 5",
        "tip": "Quiz",
        "q": "3. Acest obiect este un cub care se potrivește în jurul lumii dumneavoastră și este texturat pentru a arăta ca un cer.",
        "correct": "Un skybox.",
        "options": ["Un skybox.", "Un terrain.", "O lumină direcțională.", "Un shader."]
    },
    {
        "curs": "Cursul 5",
        "tip": "Quiz",
        "q": "4. Ce controler de caractere ai adăuga la scena ta: Prima persoană sau a treia persoană?",
        "correct": "Prima persoană.",
        "options": [
            "Prima persoană.",
            "A treia persoană.",
            "Niciunul, controlerele nu funcționează pe teren.",
            "Controlerul 2D ortografic."
        ]
    },
    {
        "curs": "Cursul 5",
        "tip": "Q&A",
        "q": "Q&A: Copacii și iarba au un impact semnificativ asupra performanței?",
        "correct": "Depinde cât de mult aveți pe scenă deodată și de puterea computerului. Folosiți-le acolo unde au impact pozitiv asupra scenei.",
        "options": [
            "Depinde cât de mult aveți pe scenă deodată și de puterea computerului. Folosiți-le acolo unde au impact pozitiv asupra scenei.",
            "Nu, poți pune milioane de copaci fără niciun impact asupra performanței.",
            "Da, un singur copac blochează complet orice calculator.",
            "Iarba crește viteza de rulare a jocului cu 50%."
        ]
    },
    {
        "curs": "Cursul 5",
        "tip": "Q&A",
        "q": "Q&A: Pot să-mi fac propriile skybox-uri?",
        "correct": "Ba da, poți. Este util mai ales dacă construiești o lume personalizată cu detalii specifice.",
        "options": [
            "Ba da, poți. Este util mai ales dacă construiești o lume personalizată cu detalii specifice.",
            "Nu, skybox-urile sunt codate fix în motorul Unity și nu pot fi schimbate.",
            "Doar dacă rescrii codul sursă al sistemului de operare.",
            "Nu, Unity acceptă doar fundal negru."
        ]
    },
    {
        "curs": "Cursul 5",
        "tip": "Q&A",
        "q": "Q&A: Există o mulțime de proprietăți pentru controlerul de caractere. Va trebui să le cunosc pe toate?",
        "correct": "Nu chiar. Controlerele de caractere sunt ușor de utilizat așa cum sunt; modificările nu sunt necesare pentru majoritatea utilizărilor.",
        "options": [
            "Nu chiar. Controlerele de caractere sunt ușor de utilizat așa cum sunt; modificările nu sunt necesare pentru majoritatea utilizărilor.",
            "Da, trebuie modificate toate la fiecare cadru din cod.",
            "Da, altfel controlerul se șterge automat din scenă.",
            "Nu, deoarece controlerul de caractere nu are nicio proprietate."
        ]
    },

    # ==================== CURSUL 6 ====================
    {
        "curs": "Cursul 6",
        "tip": "Quiz",
        "q": "1. Dacă doriți să iluminați o întreagă scenă cu o singură lumină, ce tip ar trebui să utilizați?",
        "correct": "O lumină direcțională este singura lumină care este aplicată uniform pe o scenă întreagă.",
        "options": [
            "O lumină direcțională este singura lumină care este aplicată uniform pe o scenă întreagă.",
            "O lumină de tip Spot (reflector).",
            "O lumină punctuală (Point Light) cu rază 1.",
            "Nu este posibilă iluminarea unei scene cu o singură lumină."
        ]
    },
    {
        "curs": "Cursul 6",
        "tip": "Quiz",
        "q": "2. Câte camere pot fi adăugate la o scenă?",
        "correct": "Puteți avea cât mai multe doriți.",
        "options": [
            "Puteți avea cât mai multe doriți.",
            "Doar o singură cameră.",
            "Maximum două camere (una 2D și una 3D).",
            "Maximum 4 camere."
        ]
    },
    {
        "curs": "Cursul 6",
        "tip": "Quiz",
        "q": "3. Câte straturi (layers) definite de utilizator puteți avea?",
        "correct": "24.",
        "options": ["24.", "8.", "16.", "100."]
    },
    {
        "curs": "Cursul 6",
        "tip": "Quiz",
        "q": "4. Ce proprietate determină ce straturi sunt ignorate de lumini și camere?",
        "correct": "Proprietatea Culling Mask.",
        "options": [
            "Proprietatea Culling Mask.",
            "Proprietatea Field of View.",
            "Proprietatea Transform Position.",
            "Proprietatea Wind Bending."
        ]
    },
    {
        "curs": "Cursul 6",
        "tip": "Q&A",
        "q": "Q&A: Am observat că am sărit peste lightmapping (lumină). E important să înveți?",
        "correct": "Lightmapping este o tehnică utilă pentru optimizarea performanței unei scene, dar este un subiect mai avansat pentru proiecte viitoare.",
        "options": [
            "Lightmapping este o tehnică utilă pentru optimizarea performanței unei scene, dar este un subiect mai avansat pentru proiecte viitoare.",
            "Nu, lightmapping-ul nu are nicio legătură cu iluminarea sau performanța.",
            "Este obligatoriu chiar și pentru un proiect gol, altfel Unity nu pornește.",
            "Lightmapping-ul este folosit doar pentru reglarea volumului audio."
        ]
    },
    {
        "curs": "Cursul 6",
        "tip": "Q&A",
        "q": "Q&A: Cum știu dacă vreau o cameră de perspectivă sau ortografică?",
        "correct": "Regula generală este că doriți perspectivă pentru jocuri și efecte 3D și ortografică pentru jocuri și efecte 2D.",
        "options": [
            "Regula generală este că doriți perspectivă pentru jocuri și efecte 3D și ortografică pentru jocuri și efecte 2D.",
            "Ortografică pentru jocuri 3D FPS și perspectivă doar pentru meniuri 2D.",
            "Nu există nicio diferență vizuală între ele.",
            "Camera ortografică redă doar sunetul, nu și imaginea."
        ]
    },

    # ==================== CURSUL 7 (Partea 1) ====================
    {
        "curs": "Cursul 7",
        "tip": "Quiz",
        "q": "1. Cu care trei limbaje vă permite Unity să programați (conform cursului)?",
        "correct": "C#, JavaScript și Boo.",
        "options": [
            "C#, JavaScript și Boo.",
            "C++, Python și Java.",
            "PHP, Ruby și Swift.",
            "HTML, CSS și SQL."
        ]
    },
    {
        "curs": "Cursul 7",
        "tip": "Quiz",
        "q": "2. Adevărat sau Fals: Codul din metoda Start se execută la începutul fiecărui cadru.",
        "correct": "Fals. Metoda Start se execută la începutul scenei. Metoda Actualizare (Update) execută fiecare cadru.",
        "options": [
            "Fals. Metoda Start se execută la începutul scenei. Metoda Actualizare (Update) execută fiecare cadru.",
            "Adevărat. Metoda Start se apelează de 60 de ori pe secundă.",
            "Fals. Metoda Start se execută doar când jucătorul închide aplicația.",
            "Adevărat, iar metoda Update se execută doar o singură dată la pornire."
        ]
    },
    {
        "curs": "Cursul 7",
        "tip": "Quiz",
        "q": "3. Ce tip de variabilă este tipul implicit de număr în virgulă mobilă din Unity?",
        "correct": "Float",
        "options": ["Float", "Int", "Bool", "String"]
    },
    {
        "curs": "Cursul 7",
        "tip": "Quiz",
        "q": "4. Care operator returnează restul împărțirii întregi?",
        "correct": "Modulul",
        "options": ["Modulul", "Adunarea", "Înmulțirea", "Asignarea"]
    },
    {
        "curs": "Cursul 7",
        "tip": "Quiz",
        "q": "5. Ce este o declarație condiționată?",
        "correct": "O structură de cod care permite computerului să aleagă o cale de cod bazată pe o decizie simplă.",
        "options": [
            "O structură de cod care permite computerului să aleagă o cale de cod bazată pe o decizie simplă.",
            "O variabilă care stochează exclusiv numere întregi.",
            "Un fișier model 3D importat în scenă.",
            "O buclă care blochează execuția jocului."
        ]
    },
    {
        "curs": "Cursul 7",
        "tip": "Quiz",
        "q": "6. Care tip de buclă este cel mai potrivit pentru numărare?",
        "correct": "For",
        "options": ["For", "If", "Switch", "Float"]
    },
    {
        "curs": "Cursul 7",
        "tip": "Q&A",
        "q": "Q&A: Cât de multă programare este necesară pentru a face un joc?",
        "correct": "Cele mai multe jocuri folosesc programare pentru comportamente complexe; cu cât comportamentele sunt mai complexe, cu atât programarea e mai complexă.",
        "options": [
            "Cele mai multe jocuri folosesc programare pentru comportamente complexe; cu cât comportamentele sunt mai complexe, cu atât programarea e mai complexă.",
            "Deloc, niciun joc comercial nu folosește programare.",
            "Programarea este folosită doar pentru desenarea texturilor în Paint.",
            "Comportamentele complexe necesită mai puțină programare decât cele simple."
        ]
    },
    {
        "curs": "Cursul 7",
        "tip": "Q&A",
        "q": "Q&A: Asta e tot ce ține de scripting (scenariu)?",
        "correct": "Da și nu. Sunt prezentate blocurile fundamentale de programare care nu se schimbă niciodată, ci doar se aplică în moduri noi și unice.",
        "options": [
            "Da și nu. Sunt prezentate blocurile fundamentale de programare care nu se schimbă niciodată, ci doar se aplică în moduri noi și unice.",
            "Da, nu mai există niciun alt concept în programare în afară de variabila float.",
            "Nu, blocurile fundamentale se schimbă complet în fiecare săptămână.",
            "Scriptingul nu poate fi folosit în Unity."
        ]
    },

    # ==================== CURSUL 7 (Partea 2 / Cursul 8) ====================
    {
        "curs": "Cursul 8 (Cap. 7.2)",
        "tip": "Quiz",
        "q": "1. Adevărat sau Fals: Metodele pot fi, de asemenea, menționate ca funcții.",
        "correct": "Adevărat.",
        "options": ["Adevărat.", "Fals."]
    },
    {
        "curs": "Cursul 8 (Cap. 7.2)",
        "tip": "Quiz",
        "q": "2. Adevărat sau Fals: Nu fiecare metodă are un tip de returnare.",
        "correct": "Fals. Fiecare metodă returnează un tip. Dacă metoda nu returnează nimic, tipul este nul (void).",
        "options": [
            "Fals. Fiecare metodă returnează un tip. Dacă metoda nu returnează nimic, tipul este nul (void).",
            "Adevărat. Doar metoda Start are tip de returnare.",
            "Adevărat. Metodele nu pot returna niciodată valori.",
            "Fals. Toate metodele returnează obligatoriu un float."
        ]
    },
    {
        "curs": "Cursul 8 (Cap. 7.2)",
        "tip": "Quiz",
        "q": "3. De ce este un lucru rău să mapați interacțiunile jucătorului la butoane specifice?",
        "correct": "Jucătorii vor avea un timp mult mai greu la remapping pentru preferințele lor. Prin maparea la axe generice, butoanele se pot modifica ușor.",
        "options": [
            "Jucătorii vor avea un timp mult mai greu la remapping pentru preferințele lor. Prin maparea la axe generice, butoanele se pot modifica ușor.",
            "Deoarece butoanele specifice șterg scena curentă la apăsare.",
            "Deoarece tastatura nu este suportată în Unity pe PC.",
            "Deoarece maparea la butoane specifice dezactivează iluminarea scenei."
        ]
    },
    {
        "curs": "Cursul 8 (Cap. 7.2)",
        "tip": "Quiz",
        "q": "4. Cubul a fost translatat de-a lungul axei X pozitive și rotit de-a lungul axei Z, deplasându-se într-un cerc mare. De ce?",
        "correct": "Transformările au loc pe sistemul local de coordonate. Cubul s-a mutat pe axa X pozitivă, dar direcția axei față de cameră a continuat să se schimbe.",
        "options": [
            "Transformările au loc pe sistemul local de coordonate. Cubul s-a mutat pe axa X pozitivă, dar direcția axei față de cameră a continuat să se schimbe.",
            "Deoarece cuburile în Unity se pot mișca doar în cerc, niciodată în linie dreaptă.",
            "Deoarece camera se rotea în jurul cubului, iar cubul era complet static.",
            "Deoarece axa X pozitivă este întotdeauna o linie curbă în geometria 3D."
        ]
    },
    {
        "curs": "Cursul 8 (Cap. 7.2)",
        "tip": "Q&A",
        "q": "Q&A: Câte metode ar trebui să scriu?",
        "correct": "O metodă ar trebui să fie o funcție unică, concisă. Atâta timp cât fiecare proces are propria metodă specifică, aveți suficient.",
        "options": [
            "O metodă ar trebui să fie o funcție unică, concisă. Atâta timp cât fiecare proces are propria metodă specifică, aveți suficient.",
            "Tot codul jocului trebuie scris într-o singură metodă uriașă.",
            "Nu aveți voie să scrieți mai mult de două metode pe proiect.",
            "Câte o metodă pentru fiecare literă din alfabet."
        ]
    },
    {
        "curs": "Cursul 8 (Cap. 7.2)",
        "tip": "Q&A",
        "q": "Q&A: De ce nu aflăm mai multe despre gamepad-uri în acest capitol?",
        "correct": "Toate gamepad-urile diferă și sistemele de operare le tratează diferit, deci nu ar permite o experiență constantă cititorului (plus nu toată lumea are gamepad).",
        "options": [
            "Toate gamepad-urile diferă și sistemele de operare le tratează diferit, deci nu ar permite o experiență constantă cititorului (plus nu toată lumea are gamepad).",
            "Deoarece Unity nu suportă niciun fel de gamepad sau controller.",
            "Deoarece gamepad-urile pot fi folosite doar pentru editarea modelelor 3D.",
            "Deoarece gamepad-urile funcționează doar cu camera ortografică."
        ]
    },
    {
        "curs": "Cursul 8 (Cap. 7.2)",
        "tip": "Q&A",
        "q": "Q&A: Fiecare componentă poate fi editată prin script?",
        "correct": "Da, cel puțin toate cele încorporate.",
        "options": [
            "Da, cel puțin toate cele încorporate.",
            "Nu, scripturile nu au acces la nicio componentă din Unity.",
            "Doar componenta Transform poate fi accesată, restul sunt blocate.",
            "Nu, componentele pot fi modificate exclusiv manual cu jocul oprit."
        ]
    }
]


class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Unity - Pregătire Cursuri (1 - 8)")
        self.root.geometry("820x580")
        self.root.minsize(700, 500)

        # Variabile de stare
        self.filtered_questions = []
        self.wrong_questions = []
        self.current_index = 0
        self.score = 0
        self.answered = False
        self.selected_option = tk.StringVar(value="")
        self.shuffle_var = tk.BooleanVar(value=True)

        self._build_ui()
        self.start_quiz()

    def _build_ui(self):
        # --- Bara de filtre sus ---
        top_frame = tk.Frame(self.root, padx=12, pady=10, bg="#f0f0f0", relief="groove", bd=1)
        top_frame.pack(fill="x")

        tk.Label(top_frame, text="Curs:", bg="#f0f0f0", font=("Arial", 10, "bold")).pack(side="left")
        self.course_cb = ttk.Combobox(
            top_frame,
            values=[
                "Toate cursurile",
                "Cursul 1",
                "Cursul 2",
                "Cursul 3",
                "Cursul 4",
                "Cursul 5",
                "Cursul 6",
                "Cursul 7",
                "Cursul 8 (Cap. 7.2)"
            ],
            state="readonly",
            width=18
        )
        self.course_cb.current(0)
        self.course_cb.pack(side="left", padx=(4, 12))
        self.course_cb.bind("<<ComboboxSelected>>", lambda e: self.start_quiz())

        tk.Label(top_frame, text="Tip:", bg="#f0f0f0", font=("Arial", 10, "bold")).pack(side="left")
        self.type_cb = ttk.Combobox(
            top_frame,
            values=["Doar Quiz/Test (35)", "Doar Q&A (20)", "Toate (55)"],
            state="readonly",
            width=18
        )
        self.type_cb.current(0)
        self.type_cb.pack(side="left", padx=(4, 12))
        self.type_cb.bind("<<ComboboxSelected>>", lambda e: self.start_quiz())

        tk.Checkbutton(
            top_frame,
            text="Amestecă",
            variable=self.shuffle_var,
            bg="#f0f0f0",
            command=self.start_quiz
        ).pack(side="left", padx=4)

        tk.Button(
            top_frame,
            text="Restart",
            command=self.start_quiz,
            bg="#e1e1e1",
            padx=8
        ).pack(side="left", padx=6)

        self.score_label = tk.Label(
            top_frame,
            text="Scor: 0 / 0",
            bg="#f0f0f0",
            font=("Arial", 11, "bold"),
            fg="#1a5fb4"
        )
        self.score_label.pack(side="right", padx=6)

        # --- Zona principala pentru intrebare ---
        main_frame = tk.Frame(self.root, padx=20, pady=15)
        main_frame.pack(fill="both", expand=True)

        self.meta_label = tk.Label(
            main_frame,
            text="",
            font=("Arial", 10, "italic"),
            fg="#555555",
            anchor="w"
        )
        self.meta_label.pack(fill="x", pady=(0, 6))

        self.question_label = tk.Label(
            main_frame,
            text="",
            font=("Arial", 13, "bold"),
            wraplength=760,
            justify="left",
            anchor="w"
        )
        self.question_label.pack(fill="x", pady=(0, 15))

        # Container pentru variantele de raspuns
        self.options_frame = tk.Frame(main_frame)
        self.options_frame.pack(fill="both", expand=True)

        self.radio_buttons = []
        for i in range(4):
            rb = tk.Radiobutton(
                self.options_frame,
                text="",
                variable=self.selected_option,
                value="",
                font=("Arial", 11),
                wraplength=720,
                justify="left",
                anchor="w",
                padx=10,
                pady=8,
                indicatoron=1
            )
            rb.pack(fill="x", pady=4, anchor="w")
            self.radio_buttons.append(rb)

        # --- Feedback Label ---
        self.feedback_label = tk.Label(
            main_frame,
            text="",
            font=("Arial", 11, "bold"),
            wraplength=760,
            justify="left",
            anchor="w",
            pady=8
        )
        self.feedback_label.pack(fill="x", pady=(5, 5))

        # --- Bara de jos cu butoane ---
        bottom_frame = tk.Frame(self.root, padx=20, pady=12, bg="#f8f8f8")
        bottom_frame.pack(fill="x", side="bottom")

        self.action_btn = tk.Button(
            bottom_frame,
            text="Verifică răspunsul (Enter)",
            font=("Arial", 11, "bold"),
            bg="#2ec27e",
            fg="white",
            padx=16,
            pady=6,
            command=self.handle_action
        )
        self.action_btn.pack(side="right")

        self.retry_wrong_btn = tk.Button(
            bottom_frame,
            text="Reia doar întrebările greșite",
            font=("Arial", 10, "bold"),
            bg="#e66100",
            fg="white",
            padx=12,
            pady=6,
            command=self.start_wrong_only
        )
        # Ascuns initial, apare cand exista greseli la final
        self.root.bind("<Return>", lambda event: self.handle_action())

    def start_quiz(self, custom_list=None):
        if custom_list is not None:
            self.filtered_questions = list(custom_list)
        else:
            course_filter = self.course_cb.get()
            type_filter = self.type_cb.get()

            self.filtered_questions = []
            for item in QUESTIONS_DB:
                if course_filter != "Toate cursurile" and item["curs"] != course_filter:
                    continue
                if type_filter.startswith("Doar Quiz") and item["tip"] != "Quiz":
                    continue
                if type_filter.startswith("Doar Q&A") and item["tip"] != "Q&A":
                    continue
                self.filtered_questions.append(item)

        if self.shuffle_var.get():
            random.shuffle(self.filtered_questions)

        self.current_index = 0
        self.score = 0
        self.wrong_questions = []
        self.retry_wrong_btn.pack_forget()
        self.action_btn.config(state="normal")
        self.load_question()

    def start_wrong_only(self):
        if not self.wrong_questions:
            return
        self.start_quiz(custom_list=self.wrong_questions)

    def load_question(self):
        total = len(self.filtered_questions)
        self.score_label.config(text=f"Scor: {self.score} / {total}")

        if self.current_index >= total:
            self.show_summary()
            return

        self.answered = False
        self.selected_option.set("")
        self.feedback_label.config(text="", fg="black")
        self.action_btn.config(text="Verifică răspunsul (Enter)", bg="#1a5fb4")

        q_data = self.filtered_questions[self.current_index]
        self.meta_label.config(
            text=f"[{q_data['curs']} • {q_data['tip']}]  Întrebarea {self.current_index + 1} din {total}"
        )
        self.question_label.config(text=q_data["q"])

        options = list(q_data["options"])
        if len(options) > 2:
            random.shuffle(options)

        for i, rb in enumerate(self.radio_buttons):
            if i < len(options):
                rb.config(
                    text=options[i],
                    value=options[i],
                    fg="black",
                    bg=self.root.cget("bg"),
                    state="normal"
                )
                rb.pack(fill="x", pady=4, anchor="w")
            else:
                rb.pack_forget()

    def handle_action(self):
        if self.current_index >= len(self.filtered_questions):
            return

        if not self.answered:
            choice = self.selected_option.get()
            if not choice:
                messagebox.showwarning("Atenție", "Selectează o variantă de răspuns înainte de verificare!")
                return

            self.answered = True
            q_data = self.filtered_questions[self.current_index]
            correct_ans = q_data["correct"]

            # Evidentiere raspunsuri
            for rb in self.radio_buttons:
                val = rb.cget("value")
                if val == correct_ans:
                    rb.config(fg="#1b7f46")
                elif val == choice and choice != correct_ans:
                    rb.config(fg="#c01c28")

            if choice == correct_ans:
                self.score += 1
                self.feedback_label.config(
                    text=f"✔ Corect! {correct_ans}",
                    fg="#1b7f46"
                )
            else:
                self.wrong_questions.append(q_data)
                self.feedback_label.config(
                    text=f"✘ Greșit! Răspunsul corect este:\n{correct_ans}",
                    fg="#c01c28"
                )

            self.score_label.config(text=f"Scor: {self.score} / {len(self.filtered_questions)}")
            self.action_btn.config(text="Următoarea întrebare (Enter) ➔", bg="#2ec27e")
        else:
            self.current_index += 1
            self.load_question()

    def show_summary(self):
        total = len(self.filtered_questions)
        procent = (self.score / total * 100) if total > 0 else 0
        self.meta_label.config(text="Rezultat final")
        self.question_label.config(
            text=f"Ai terminat testul!\nScor final: {self.score} din {total} ({procent:.1f}%)"
        )

        for rb in self.radio_buttons:
            rb.pack_forget()

        if self.wrong_questions:
            self.feedback_label.config(
                text=f"Ai greșit {len(self.wrong_questions)} întrebări. Apasă butonul portocaliu de jos pentru a le relua doar pe acestea!",
                fg="#e66100"
            )
            self.retry_wrong_btn.pack(side="left")
        else:
            self.feedback_label.config(
                text="Felicitări! Ai răspuns corect la toate întrebările!",
                fg="#1b7f46"
            )

        self.action_btn.config(state="disabled")


if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()