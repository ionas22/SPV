import tkinter as tk
from tkinter import ttk, messagebox
import random
#instaleaza pachetul tkinter dacă esti in linux cu comanda: sudo apt update && sudo apt install -y python3-tk
# Baza de date cu intrebarile si raspunsurile extrase din fisier
QUESTIONS_DB = [
    # ==================== CURSUL 1 ====================
    {
        "curs": "Cursul 1",
        "tip": "Quiz",
        "q": "1. Adevărat sau fals: trebuie să achiziționați Unity Pro pentru a crea jocuri.",
        "correct": "Fals",
        "options": ["Adevărat", "Fals"]
    },
    {
        "curs": "Cursul 1",
        "tip": "Quiz",
        "q": "2. Care vizualizare ne permite să manipulăm vizual obiectele dintr-o scenă?",
        "correct": "Scene",
        "options": ["Scene", "Hierarchy", "Inspector", "Game"]
    },
    {
        "curs": "Cursul 1",
        "tip": "Quiz",
        "q": "3. Adevărat sau fals: ar trebui să mutați întotdeauna fișierele dvs. active în Unity și să nu utilizați exploratorul de fișiere al sistemului de operare.",
        "correct": "Adevărat",
        "options": ["Adevărat", "Fals"]
    },
    {
        "curs": "Cursul 1",
        "tip": "Quiz",
        "q": "4. Adevărat sau fals: Când creați un proiect nou, ar trebui să includeți fiecare activ pe care îl credeți minunat.",
        "correct": "Fals",
        "options": ["Adevărat", "Fals"]
    },
    {
        "curs": "Cursul 1",
        "tip": "Quiz",
        "q": "5. Ce mod introduceți în vizualizarea Scenă atunci când țineți apăsat butonul din dreapta al mouse-ului?",
        "correct": "Flythrough, pentru deplasare liberă prin scena 3D.",
        "options": [
            "Orbit, pentru rotire în jurul pivotului din scena 3D.",
            "Focus, pentru încadrarea selecției din scena 3D.",
            "Pan, pentru deplasare în planul camerei din scena 3D.",
            "Flythrough, pentru deplasare liberă prin scena 3D."
        ]
    },
    {
        "curs": "Cursul 1",
        "tip": "Q&A",
        "q": "Q&A: Sunt activele (assets) și obiectele de joc (GameObjects) la fel?",
        "correct": "Un asset este o resursă a proiectului. Un GameObject este o entitate care poate folosi resurse în scenă.",
        "options": [
            "Un asset este un obiect inactiv din Hierarchy. Același obiect devine GameObject când este activat.",
            "Un asset este o instanță din scenă. Un GameObject este fișierul din Project din care provine instanța.",
            "Un asset este o componentă atașată în Inspector. Un GameObject este fișierul în care se salvează componenta.",
            "Un asset este o resursă a proiectului. Un GameObject este o entitate care poate folosi resurse în scenă."
        ]
    },
    {
        "curs": "Cursul 1",
        "tip": "Q&A",
        "q": "Q&A: Există o mulțime de controale și opțiuni diferite. Va trebui să le memorez imediat pe toate?",
        "correct": "Începi cu setările implicite și înveți controalele pe măsură ce le folosești.",
        "options": [
            "Reconfigurezi toate comenzile la început, ca să le poți folosi la fel în fiecare proiect.",
            "Începi cu setările implicite și înveți controalele pe măsură ce le folosești.",
            "Memorezi întâi scurtăturile, fiindcă aceleași acțiuni sunt indisponibile în meniuri.",
            "Înveți întâi toate opțiunile Inspectorului, fiindcă setările implicite sunt doar pentru previzualizare."
        ]
    },

    # ==================== CURSUL 2 ====================
    {
        "curs": "Cursul 2",
        "tip": "Quiz",
        "q": "1. Ce înseamnă D în 2D și 3D?",
        "correct": "Dimensiune",
        "options": ["Diagonală", "Dimensiune", "Direcție", "Distanță"]
    },
    {
        "curs": "Cursul 2",
        "tip": "Quiz",
        "q": "2. Câte transformări există?",
        "correct": "Trei",
        "options": ["Trei", "Șase", "Patru", "Două"]
    },
    {
        "curs": "Cursul 2",
        "tip": "Quiz",
        "q": "3. Adevărat sau Fals: Unity nu are obiecte încorporate și trebuie să le creați.",
        "correct": "Fals. Unity include primitive precum cubul, sfera și capsula.",
        "options": [
            "Adevărat. Primitivele trebuie importate dintr-un pachet extern.",
            "Adevărat. Meniul GameObject creează doar obiecte fără geometrie.",
            "Fals. Cubul este singura primitivă disponibilă direct în editor.",
            "Fals. Unity include primitive precum cubul, sfera și capsula."
        ]
    },
    {
        "curs": "Cursul 2",
        "tip": "Quiz",
        "q": "4. Dacă doriți ca un obiect să fie „așezat pe partea sa” 5 unități la dreapta poziției sale actuale, ați roti obiectul și apoi îl translatați sau translatați obiectul și apoi îl rotiți?",
        "correct": "Îl deplasezi 5 unități pe dreapta locală inițială, apoi îl rotești pe o parte.",
        "options": [
            "Îl rotești în jurul axei verticale, apoi îl deplasezi 5 unități pe dreapta locală nouă.",
            "Îl rotești pe o parte, apoi îl deplasezi 5 unități pe dreapta locală nouă.",
            "Îl deplasezi 5 unități pe dreapta locală inițială, apoi îl rotești în jurul axei verticale.",
            "Îl deplasezi 5 unități pe dreapta locală inițială, apoi îl rotești pe o parte."
        ]
    },
    {
        "curs": "Cursul 2",
        "tip": "Q&A",
        "q": "Q&A: Este important să învățați atât conceptele 2D, cât și cele 3D?",
        "correct": "Da, un joc 3D poate folosi concepte 2D pentru interfață și 3D pentru lumea de joc.",
        "options": [
            "Da, conceptele 2D sunt necesare pentru ca un joc 3D să poată folosi o cameră în perspectivă.",
            "Nu, interfața unui joc 3D trebuie să folosească aceeași geometrie 3D ca lumea de joc.",
            "Da, un joc 3D poate folosi concepte 2D pentru interfață și 3D pentru lumea de joc.",
            "Nu, conceptele 2D se aplică doar dacă întreaga scenă este randată în mod ortografic."
        ]
    },
    {
        "curs": "Cursul 2",
        "tip": "Q&A",
        "q": "Q&A: Ar trebui să învăț să folosesc toate obiectele de joc încorporate imediat?",
        "correct": "Înveți întâi obiectele utile în scena ta și le studiezi pe celelalte când ai nevoie de ele.",
        "options": [
            "Înveți întâi obiectele utile în scena ta și le studiezi pe celelalte când ai nevoie de ele.",
            "Înveți toate obiectele încorporate înainte de a construi prima scenă funcțională.",
            "Înveți întâi fiecare tip de obiect în 3D, apoi poți folosi obiectele dintr-un proiect 2D.",
            "Înveți întâi variantele de coliziune ale tuturor obiectelor, apoi poți exersa transformările."
        ]
    },
    {
        "curs": "Cursul 2",
        "tip": "Q&A",
        "q": "Q&A: Care este cel mai bun mod de a vă familiariza cu transformările?",
        "correct": "Modifici separat poziția, rotația și scara și compari efectele pe axele locale și globale.",
        "options": [
            "Exersezi doar scalarea uniformă, apoi folosești aceleași reguli pentru deplasare și rotire.",
            "Exersezi doar în modul Global, unde axele obiectului se rotesc odată cu acesta.",
            "Modifici separat poziția, rotația și scara și compari efectele pe axele locale și globale.",
            "Modifici doar poziția și deduci din aceleași valori cum se schimbă rotația și scara."
        ]
    },

    # ==================== CURSUL 3 ====================
    {
        "curs": "Cursul 3",
        "tip": "Quiz",
        "q": "1. Adevărat sau fals: Din cauza naturii lor simple, pătratele alcătuiesc ochiuri (meshes) în modele.",
        "correct": "Fals. Fețele unui mesh obișnuit sunt randate ca triunghiuri.",
        "options": [
            "Adevărat. Fețele pătrate sunt păstrate de motor ca unități de randare.",
            "Adevărat. Fețele pătrate sunt obligatorii pentru toate modelele texturate.",
            "Fals. Fețele unui mesh obișnuit sunt randate ca poligoane pentagonale.",
            "Fals. Fețele unui mesh obișnuit sunt randate ca triunghiuri."
        ]
    },
    {
        "curs": "Cursul 3",
        "tip": "Quiz",
        "q": "2. Ce formate de fișier acceptă Unity pentru modelele 3D?",
        "correct": ".fbx, .dae, .3ds, .dxf, .obj (în versiunea din curs)",
        "options": [
            ".fbx, .ply, .3ds, .dxf, .obj (în versiunea din curs)",
            ".fbx, .dae, .3ds, .dxf, .obj (în versiunea din curs)",
            ".fbx, .dae, .3ds, .off, .obj (în versiunea din curs)",
            ".fbx, .dae, .stl, .dxf, .obj (în versiunea din curs)"
        ]
    },
    {
        "curs": "Cursul 3",
        "tip": "Quiz",
        "q": "3. Adevărat sau Fals: Numai modelele plătite pot fi descărcate din Unity Assets Store.",
        "correct": "Fals. Magazinul oferă atât modele gratuite, cât și modele contra cost.",
        "options": [
            "Fals. Magazinul oferă atât modele gratuite, cât și modele contra cost.",
            "Adevărat. Secțiunea gratuită include doar unelte, fără modele 3D.",
            "Fals. Modelele plătite devin gratuite dacă folosești Unity Personal.",
            "Adevărat. Modelele listate ca gratuite sunt doar previzualizări."
        ]
    },
    {
        "curs": "Cursul 3",
        "tip": "Quiz",
        "q": "4. Explicați relația dintre texturi, shadere și materiale.",
        "correct": "Materialul alege shaderul și îi transmite valori și texturi. Shaderul stabilește cum se calculează aspectul suprafeței.",
        "options": [
            "Materialul stabilește singur calculele de iluminare. Shaderul oferă doar imaginea care este aplicată pe suprafață.",
            "Shaderul alege materialul și extrage din el geometria. Textura stabilește cum răspunde suprafața la lumină.",
            "Materialul alege shaderul și îi transmite valori și texturi. Shaderul stabilește cum se calculează aspectul suprafeței.",
            "Textura alege shaderul și îi transmite valorile materialului. Shaderul stabilește cum se importă fișierul imaginii."
        ]
    },
    {
        "curs": "Cursul 3",
        "tip": "Q&A",
        "q": "Q&A: Voi mai putea face jocuri dacă nu sunt artist?",
        "correct": "Da, poți folosi resurse grafice create de alții, respectând licențele acestora.",
        "options": [
            "Da, dar poți folosi resursele create de alții doar ca referință pentru grafica proprie.",
            "Da, poți folosi resurse grafice create de alții, respectând licențele acestora.",
            "Da, dacă înlocuiești resursele gratuite cu resurse proprii înainte de publicare.",
            "Da, dacă importi grafica din Unity Asset Store, singura sursă acceptată pentru resurse externe."
        ]
    },
    {
        "curs": "Cursul 3",
        "tip": "Q&A",
        "q": "Q&A: Va trebui să știu să folosesc toate shaderele încorporate?",
        "correct": "Înveți întâi shaderele de bază și le aprofundezi pe cele cerute de efectele proiectului.",
        "options": [
            "Înveți întâi shaderele de bază și le aprofundezi pe cele cerute de efectele proiectului.",
            "Înveți toate shaderele compatibile înainte de a aplica primul material.",
            "Înveți doar shaderul implicit, care acoperă toate tipurile de suprafețe și efecte.",
            "Înveți câte un shader pentru fiecare format de imagine pe care îl imporți."
        ]
    },
    {
        "curs": "Cursul 3",
        "tip": "Q&A",
        "q": "Q&A: Dacă există active de artă plătite în Unity Asset Store, asta înseamnă că pot vinde propriile mele active?",
        "correct": "Da, poți publica resurse proprii ca publisher dacă pachetul respectă cerințele magazinului.",
        "options": [
            "Da, după ce cumperi o resursă grafică din aceeași categorie cu pachetul pe care îl publici.",
            "Da, poți publica resurse proprii ca publisher dacă pachetul respectă cerințele magazinului.",
            "Da, dar numai ca parte dintr-un șablon de joc complet, fără pachete grafice separate.",
            "Da, dacă ai un abonament Pro activ pe toată durata listării pachetului."
        ]
    },

    # ==================== CURSUL 4 ====================
    {
        "curs": "Cursul 4",
        "tip": "Quiz",
        "q": "1. Adevărat sau fals: Puteți face peșteri din teren Unity.",
        "correct": "Fals. Prin sculptarea hărții de înălțime din curs obții o singură cotă pentru fiecare punct de pe teren.",
        "options": [
            "Adevărat. Prin sculptarea hărții de înălțime poți îndoi suprafața până când aceasta se suprapune.",
            "Fals. Prin sculptarea hărții de înălțime poți modifica textura, însă cotele terenului rămân fixe.",
            "Fals. Prin sculptarea hărții de înălțime din curs obții o singură cotă pentru fiecare punct de pe teren.",
            "Adevărat. Prin sculptarea hărții de înălțime poți crea un plafon și o podea deasupra aceluiași punct."
        ]
    },
    {
        "curs": "Cursul 4",
        "tip": "Quiz",
        "q": "2. Cum se numește o imagine în tonuri de gri care conține informații despre altitudinea terenului?",
        "correct": "Hartă de înălțime (Heightmap)",
        "options": [
            "Hartă de opacitate (Opacity Map)",
            "Hartă de normale (Normal Map)",
            "Hartă de rugozitate (Roughness Map)",
            "Hartă de înălțime (Heightmap)"
        ]
    },
    {
        "curs": "Cursul 4",
        "tip": "Quiz",
        "q": "3. Adevărat sau fals: Sculptura terenului în Unity este foarte mult ca pictura.",
        "correct": "Adevărat",
        "options": ["Adevărat", "Fals"]
    },
    {
        "curs": "Cursul 4",
        "tip": "Quiz",
        "q": "4. Cum accesați texturile de teren disponibile ale Unity?",
        "correct": "În versiunea din curs, imporți Terrain Assets din Assets > Import Package.",
        "options": [
            "În versiunea din curs, imporți Terrain Assets din Assets > Import Package.",
            "În versiunea din curs, descarci texturile din Window > Lighting > Environment.",
            "În versiunea din curs, alegi texturile standard din Assets > Create > Terrain.",
            "În versiunea din curs, generezi texturile standard din Terrain > Paint Details."
        ]
    },
    {
        "curs": "Cursul 4",
        "tip": "Q&A",
        "q": "Q&A: Jocul meu trebuie să aibă teren?",
        "correct": "Poți construi scena din modele și folosi Terrain când ai nevoie de relief.",
        "options": [
            "Poți construi scena din modele și folosi Terrain când ai nevoie de relief.",
            "Adaugi Terrain în orice scenă cu perspectivă, pentru a stabili planul orizontului.",
            "Adaugi Terrain chiar și sub podelele modelate, pentru ca acestea să permită coliziuni.",
            "Poți omite Terrain în 2D, dar în 3D el stabilește originea scenei."
        ]
    },
    {
        "curs": "Cursul 4",
        "tip": "Q&A",
        "q": "Q&A: Terenul meu nu arată prea bine. E normal?",
        "correct": "Da. Rezultatul se îmbunătățește exersând cu pensulele și testând nivelul în joc.",
        "options": [
            "Nu. Forma este finalizată automat când treci din Scene în Game.",
            "Nu. Dacă forma este neregulată, trebuie să o refaci într-un editor 3D înainte de testare.",
            "Da. Rezultatul se corectează prin creșterea rezoluției, fără să mai ajustezi forma.",
            "Da. Rezultatul se îmbunătățește exersând cu pensulele și testând nivelul în joc."
        ]
    },

    # ==================== CURSUL 5 ====================
    {
        "curs": "Cursul 5",
        "tip": "Quiz",
        "q": "1. Ce setare controlează cât de mult copacii se leagănă în vânt?",
        "correct": "În configurația din curs, Bending controlează iarba, iar copacii folosiți acolo rămân statici.",
        "options": [
            "În configurația din curs, Bending controlează copacii, iar iarba rămâne statică.",
            "În configurația din curs, Wind Speed controlează amplitudinea copacilor, iar Bending controlează viteza lor.",
            "În configurația din curs, Bending controlează iarba, iar copacii folosiți acolo rămân statici.",
            "În configurația din curs, Wind Speed controlează amplitudinea copacilor, iar Bending controlează culoarea ierbii."
        ]
    },
    {
        "curs": "Cursul 5",
        "tip": "Quiz",
        "q": "2. Care este numele efectului ambiental care poate simula ceața sau decolorarea culorilor la distanță?",
        "correct": "Ceață (Fog)",
        "options": [
            "Ceață (Fog)",
            "Expunere (Exposure)",
            "Ocluzie ambientală (Ambient Occlusion)",
            "Iluminare ambientală (Ambient Lighting)"
        ]
    },
    {
        "curs": "Cursul 5",
        "tip": "Quiz",
        "q": "3. Acest obiect este un cub care se potrivește în jurul lumii dumneavoastră și este texturat pentru a arăta ca un cer.",
        "correct": "Skybox",
        "options": [
            "Proiecție panoramică pe un plan",
            "Skybox",
            "Volum de ceață (Fog Volume)",
            "Volum de reflexie (Reflection Probe)"
        ]
    },
    {
        "curs": "Cursul 5",
        "tip": "Quiz",
        "q": "4. Ce controler de caractere ai adăuga la scena ta: Prima persoană sau a treia persoană?",
        "correct": "Pentru exercițiul din curs, controler la prima persoană, cu vedere din poziția personajului.",
        "options": [
            "Pentru exercițiul din curs, controler cu vedere de sus, cu camera orientată către sol.",
            "Pentru exercițiul din curs, controler la persoana a treia, cu vedere din spatele personajului.",
            "Pentru exercițiul din curs, controler la prima persoană, cu vedere din poziția personajului.",
            "Pentru exercițiul din curs, controler lateral, cu deplasare într-un singur plan."
        ]
    },
    {
        "curs": "Cursul 5",
        "tip": "Q&A",
        "q": "Q&A: Copacii și iarba au un impact semnificativ asupra performanței?",
        "correct": "Impactul depinde de cantitatea de vegetație randată și de puterea dispozitivului.",
        "options": [
            "Impactul depinde de cantitatea de vegetație randată și de puterea dispozitivului.",
            "Impactul crește cu distanța de vizualizare, la același cost pentru orice complexitate a modelelor.",
            "Impactul crește cu numărul de modele distincte, iar copiile unui model au cost zero.",
            "Impactul crește cu suprafața terenului, la același cost pentru orice densitate de vegetație."
        ]
    },
    {
        "curs": "Cursul 5",
        "tip": "Q&A",
        "q": "Q&A: Pot să-mi fac propriile skybox-uri?",
        "correct": "Da, poți aplica texturi proprii unui material care folosește un shader de skybox.",
        "options": [
            "Da, dacă rescrii texturile unui skybox inclus, deoarece materialele de skybox au texturi fixe.",
            "Da, dacă generezi texturile în timpul rulării, fiindcă skybox-ul respinge imaginile importate.",
            "Da, dacă pornești de la un skybox oficial, obligatoriu pentru orice material de skybox nou.",
            "Da, poți aplica texturi proprii unui material care folosește un shader de skybox."
        ]
    },
    {
        "curs": "Cursul 5",
        "tip": "Q&A",
        "q": "Q&A: Există o mulțime de proprietăți pentru controlerul de caractere. Va trebui să le cunosc pe toate?",
        "correct": "Începi cu valorile implicite și ajustezi proprietățile relevante când comportamentul o cere.",
        "options": [
            "Ajustezi toate proprietățile împreună, fiindcă ele trebuie să păstreze aceleași proporții.",
            "Configurezi toate proprietățile înainte de test, fiindcă valorile implicite sunt doar pentru afișare.",
            "Înveți doar înălțimea și raza capsulei, fiindcă restul setărilor nu influențează deplasarea.",
            "Începi cu valorile implicite și ajustezi proprietățile relevante când comportamentul o cere."
        ]
    },

    # ==================== CURSUL 6 ====================
    {
        "curs": "Cursul 6",
        "tip": "Quiz",
        "q": "1. Dacă doriți să iluminați o întreagă scenă cu o singură lumină, ce tip ar trebui să utilizați?",
        "correct": "Lumină direcțională (Directional Light)",
        "options": [
            "Lumină direcțională (Directional Light)",
            "Lumină punctuală (Point Light)",
            "Lumină de arie (Area Light)",
            "Lumină conică (Spot Light)"
        ]
    },
    {
        "curs": "Cursul 6",
        "tip": "Quiz",
        "q": "2. Câte camere pot fi adăugate la o scenă?",
        "correct": "Oricâte, fără o limită fixă de camere pe scenă.",
        "options": [
            "O singură cameră în scenă, cu mai multe moduri de proiecție.",
            "O singură cameră activă pentru fiecare strat al scenei.",
            "Oricâte, fără o limită fixă de camere pe scenă.",
            "Câte o cameră pentru fiecare afișaj configurat."
        ]
    },
    {
        "curs": "Cursul 6",
        "tip": "Quiz",
        "q": "3. Câte straturi (layers) definite de utilizator puteți avea?",
        "correct": "24 (în versiunea din curs)",
        "options": [
            "24 (în versiunea din curs)",
            "8 (în versiunea din curs)",
            "32 (în versiunea din curs)",
            "16 (în versiunea din curs)"
        ]
    },
    {
        "curs": "Cursul 6",
        "tip": "Quiz",
        "q": "4. Ce proprietate determină ce straturi sunt ignorate de lumini și camere?",
        "correct": "Culling Mask",
        "options": ["Layer Overrides", "Culling Mask", "Occlusion Culling", "Rendering Layer Mask"]
    },
    {
        "curs": "Cursul 6",
        "tip": "Q&A",
        "q": "Q&A: Am observat că am sărit peste lightmapping (lumină). E important să înveți?",
        "correct": "Este util pentru iluminarea precalculată, iar studiul lui poate aștepta până când proiectul are nevoie de ea.",
        "options": [
            "Este necesar înainte de a folosi materiale, fiindcă lightmap-ul stabilește culorile tuturor texturilor.",
            "Este util pentru iluminarea precalculată, iar studiul lui poate aștepta până când proiectul are nevoie de ea.",
            "Este util mai ales pentru luminile care se mișcă, fiindcă le recalculează umbrele la fiecare cadru.",
            "Este necesar înainte de prima scenă 3D, fiindcă nicio lumină nu poate fi afișată fără lightmap."
        ]
    },
    {
        "curs": "Cursul 6",
        "tip": "Q&A",
        "q": "Q&A: Cum știu dacă vreau o cameră de perspectivă sau ortografică?",
        "correct": "Folosești de obicei perspectiva pentru profunzime în 3D și proiecția ortografică pentru un aspect 2D.",
        "options": [
            "Alegi proiecția în funcție de numărul de camere, fiindcă perspectiva se poate folosi pe o singură cameră.",
            "Folosești de obicei perspectiva pentru a păstra dimensiunile la distanță și proiecția ortografică pentru profunzime.",
            "Alegi proiecția în funcție de formatul texturilor, fiindcă imaginile 2D cer o cameră ortografică.",
            "Folosești de obicei perspectiva pentru profunzime în 3D și proiecția ortografică pentru un aspect 2D."
        ]
    },

    # ==================== CURSUL 7 (Partea 1) ====================
    {
        "curs": "Cursul 7",
        "tip": "Quiz",
        "q": "1. Cu care trei limbaje vă permite Unity să programați (conform cursului)?",
        "correct": "C#, JavaScript (UnityScript), Boo",
        "options": [
            "C#, JavaScript (UnityScript), Python",
            "C#, Java, Boo",
            "C++, JavaScript (UnityScript), Boo",
            "C#, JavaScript (UnityScript), Boo"
        ]
    },
    {
        "curs": "Cursul 7",
        "tip": "Quiz",
        "q": "2. Adevărat sau Fals: Codul din metoda Start se execută la începutul fiecărui cadru.",
        "correct": "Fals. Start se apelează o dată înainte de primul Update al componentei.",
        "options": [
            "Adevărat. Start se apelează în fiecare cadru de fizică, înainte de FixedUpdate.",
            "Fals. Start se apelează de fiecare dată când componenta este reactivată.",
            "Adevărat. Start se apelează înainte de fiecare Update al componentei.",
            "Fals. Start se apelează o dată înainte de primul Update al componentei."
        ]
    },
    {
        "curs": "Cursul 7",
        "tip": "Quiz",
        "q": "3. Ce tip de variabilă este tipul implicit de număr în virgulă mobilă din Unity?",
        "correct": "float (System.Single)",
        "options": [
            "int (System.Int32)",
            "double (System.Double)",
            "decimal (System.Decimal)",
            "float (System.Single)"
        ]
    },
    {
        "curs": "Cursul 7",
        "tip": "Quiz",
        "q": "4. Care operator returnează restul împărțirii întregi?",
        "correct": "Operatorul %",
        "options": ["Operatorul /", "Operatorul &", "Operatorul %", "Operatorul *"]
    },
    {
        "curs": "Cursul 7",
        "tip": "Quiz",
        "q": "5. Ce este o declarație condiționată?",
        "correct": "O structură care alege ce bloc de cod se execută în funcție de rezultatul unui test.",
        "options": [
            "O structură care permite unei metode să transmită o valoare către apelant.",
            "O structură care grupează instrucțiuni într-un bloc ce poate fi apelat după nume.",
            "O structură care alege ce bloc de cod se execută în funcție de rezultatul unui test.",
            "O structură care repetă un bloc de cod pentru un număr prestabilit de iterații."
        ]
    },
    {
        "curs": "Cursul 7",
        "tip": "Quiz",
        "q": "6. Care tip de buclă este cel mai potrivit pentru numărare?",
        "correct": "for",
        "options": ["for", "foreach", "do ... while", "while"]
    },
    {
        "curs": "Cursul 7",
        "tip": "Q&A",
        "q": "Q&A: Cât de multă programare este necesară pentru a face un joc?",
        "correct": "Volumul de programare depinde în principal de complexitatea comportamentelor jocului.",
        "options": [
            "Volumul de programare este stabilit la crearea proiectului, prin alegerea șablonului.",
            "Volumul de programare depinde în principal de complexitatea comportamentelor jocului.",
            "Volumul de programare este aproximativ același pentru orice joc care are tot atâtea scene.",
            "Volumul de programare depinde în principal de numărul de modele pe care le imporți."
        ]
    },
    {
        "curs": "Cursul 7",
        "tip": "Q&A",
        "q": "Q&A: Asta e tot ce ține de scripting (scenariu)?",
        "correct": "Capitolul prezintă structurile de bază, pe care le poți combina pentru a construi comportamente mai complexe.",
        "options": [
            "Capitolul prezintă toate metodele motorului, care pot fi aplicate direct în orice proiect.",
            "Capitolul prezintă comenzi valabile doar pentru exemplul său, care trebuie înlocuite în alte proiecte.",
            "Capitolul prezintă structurile de bază, pe care le poți combina pentru a construi comportamente mai complexe.",
            "Capitolul prezintă întreaga sintaxă, iar mecanicile noi cer doar schimbarea valorilor din Inspector."
        ]
    },

    # ==================== CURSUL 7 (Partea 2 / Cursul 8) ====================
    {
        "curs": "Cursul 8 (Cap. 7.2)",
        "tip": "Quiz",
        "q": "1. Adevărat sau Fals: Metodele pot fi, de asemenea, menționate ca funcții.",
        "correct": "Adevărat",
        "options": ["Adevărat", "Fals"]
    },
    {
        "curs": "Cursul 8 (Cap. 7.2)",
        "tip": "Quiz",
        "q": "2. Adevărat sau Fals: Nu fiecare metodă are un tip de returnare.",
        "correct": "Fals. O metodă declară un tip de returnare, inclusiv void când nu întoarce o valoare.",
        "options": [
            "Fals. O metodă fără rezultat declară tipul null în locul unui tip concret.",
            "Fals. O metodă declară un tip de returnare, inclusiv void când nu întoarce o valoare.",
            "Adevărat. O metodă poate omite tipul de returnare dacă are o instrucțiune return.",
            "Adevărat. O metodă fără parametri poate omite tipul de returnare din declarație."
        ]
    },
    {
        "curs": "Cursul 8 (Cap. 7.2)",
        "tip": "Quiz",
        "q": "3. De ce este un lucru rău să mapați interacțiunile jucătorului la butoane specifice?",
        "correct": "Legarea directă de o tastă îngreunează remaparea. O acțiune poate primi altă tastă fără să schimbi logica jocului.",
        "options": [
            "Legarea directă de o tastă activează repetarea. O acțiune trimite întotdeauna un singur eveniment per apăsare.",
            "Legarea directă de o tastă îngreunează remaparea. O acțiune poate primi altă tastă fără să schimbi logica jocului.",
            "Legarea directă de o tastă schimbă frecvența citirii. O acțiune se citește la o rată fixă, indiferent de cadru.",
            "Legarea directă de o tastă schimbă durata apăsării. O acțiune transformă automat orice apăsare într-una scurtă."
        ]
    },
    {
        "curs": "Cursul 8 (Cap. 7.2)",
        "tip": "Quiz",
        "q": "4. Cubul a fost translatat de-a lungul axei X pozitive și rotit de-a lungul axei Z, deplasându-se într-un cerc mare. De ce?",
        "correct": "Deplasarea urmărește axa X locală, care își schimbă direcția după fiecare rotație pe Z.",
        "options": [
            "Deplasarea urmărește axa X globală, iar rotația cubului mută automat poziția în jurul originii scenei.",
            "Deplasarea urmărește axa X locală, care își schimbă direcția după fiecare rotație pe Z.",
            "Deplasarea urmărește axa X globală, care își schimbă direcția când cubul se rotește pe Z.",
            "Deplasarea urmărește axa X locală, care rămâne fixă deoarece rotația este pe altă axă."
        ]
    },
    {
        "curs": "Cursul 8 (Cap. 7.2)",
        "tip": "Q&A",
        "q": "Q&A: Câte metode ar trebui să scriu?",
        "correct": "Scrii atâtea metode câte sunt necesare pentru a separa responsabilitățile în operații clare.",
        "options": [
            "Scrii câte o metodă pentru fiecare eveniment Unity, chiar dacă evenimentul nu este folosit.",
            "Scrii câte o metodă pentru fiecare tip de rezultat, grupând toate operațiile cu același tip.",
            "Scrii atâtea metode câte sunt necesare pentru a separa responsabilitățile în operații clare.",
            "Scrii câte o metodă pentru fiecare variabilă, chiar dacă variabilele țin de aceeași operație."
        ]
    },
    {
        "curs": "Cursul 8 (Cap. 7.2)",
        "tip": "Q&A",
        "q": "Q&A: De ce nu aflăm mai multe despre gamepad-uri în acest capitol?",
        "correct": "Modelele de gamepad, sistemele de operare și disponibilitatea dispozitivelor fac exercițiul greu de reprodus.",
        "options": [
            "Axa fiecărui gamepad trebuie asociată unui obiect din scenă înainte de a fi citită dintr-un script.",
            "Maparea unui gamepad blochează intrările de la tastatură, ceea ce ar schimba exercițiile capitolului.",
            "Modelele de gamepad, sistemele de operare și disponibilitatea dispozitivelor fac exercițiul greu de reprodus.",
            "Semnalul de la gamepad poate fi citit doar după export, ceea ce împiedică testarea din editor."
        ]
    },
    {
        "curs": "Cursul 8 (Cap. 7.2)",
        "tip": "Q&A",
        "q": "Q&A: Fiecare componentă poate fi editată prin script?",
        "correct": "Poți modifica proprietățile pe care componenta le expune pentru scriere prin API-ul său.",
        "options": [
            "Poți modifica doar componentele personalizate, fiindcă cele încorporate sunt accesibile doar pentru citire.",
            "Poți modifica proprietățile pe care componenta le expune pentru scriere prin API-ul său.",
            "Poți modifica doar câmpurile serializate, fiindcă proprietățile neserializate sunt inaccesibile la rulare.",
            "Poți modifica orice proprietate vizibilă în Inspector, fiindcă afișarea ei garantează accesul din script."
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