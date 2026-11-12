"""Programa curado a mano a partir del mapa oficial de la IMM y fuentes nombradas.

Cada actividad: (inicio, fin, título, descripción, tags, personas, fuentes, nota)
inicio/fin "HH:MM" o None. tags: ninos musica charla presentacion lectura taller.
"""

SOURCES = {
    "imm": {"label": "Mapa oficial IMM", "url": "https://eventos.montevideo.gub.uy/node/1022"},
    "ladiaria": {
        "label": "la diaria",
        "url": "https://ladiaria.com.uy/libros/articulo/2026/11/la-noche-de-las-librerias-2026-llega-con-130-actividades-en-montevideo-y-ganas-de-seguir-creciendo/",
    },
    "elobservador": {
        "label": "El Observador",
        "url": "https://www.elobservador.com.uy/cultura-y-espectaculos/de-lucrecia-martel-y-mauro-libertella-guadalupe-nettel-las-visitas-autores-del-exterior-la-noche-las-librerias-n6063380",
    },
    "busqueda": {
        "label": "Búsqueda",
        "url": "https://www.busqueda.com.uy/tiempo-libre/la-noche-las-librerias-escaramuza-tendra-musica-gastronomia-cine-y-mucha-literatura-n5419256",
    },
    "fadu": {"label": "FADU", "url": "https://www.fadu.edu.uy/noticias/noche-de-las-librerias-en-la-fadu/"},
    "cce": {"label": "CCE", "url": "https://ccemontevideo.aecid.es/w/noche-de-las-librer%C3%ADas-2026"},
    "mec": {
        "label": "Guía MEC 2026",
        "url": "https://www.gub.uy/ministerio-educacion-cultura/sites/ministerio-educacion-cultura/files/documentos/noticias/Programacion-Noche_de_las_librerias-2026.pdf",
    },
    "elobservador-zambra": {
        "label": "El Observador (9/11)",
        "url": "https://www.elobservador.com.uy/cultura-y-espectaculos/alejandro-zambra-viene-montevideo-y-es-el-momento-volver-bonsai-su-primera-novela-n6062874",
    },
    "infouruguay": {"label": "InfoUruguay", "url": "https://infouruguay.com.uy/noticias/3834-que-hacer-este-fin-de-semana-en-montevideo-y-canelones"},
}

NOT_IN_MEC = {
    ("Escaramuza", "Fernando Cabrera y su dulzura distante"),
    ("Escaramuza", "Guadalupe Nettel: la belleza del monstruo"),
    ("Escaramuza", "Coloquio de las quiltras"),
    ("Escaramuza", "Esto también es tarot"),
    ("Escaramuza", "Alejandro Zambra en primera persona"),
}


def A(start, end, title, desc="", tags=(), people=(), src=("imm",), note=None):
    return {
        "start": start,
        "end": end,
        "title": title,
        "desc": desc,
        "tags": list(tags),
        "people": list(people),
        "src": list(src),
        **({"note": note} if note else {}),
    }


PLACES = [
    {
        "name": "Adagio Librería Café", "barrio": "Punta Carretas", "addr": "Gral. Gregorio Suárez 2741",
        "hours": ["18:30", "01:00"],
        "note": "«Cartas pendientes», primera edición: un encuentro sobre la literatura que vive en las cartas. La librería no publicó horarios por actividad.",
        "acts": [
            A(None, None, "Escribí una carta", "Invitación a escribir una carta, a solas o en compañía.", ["taller"]),
            A(None, None, "Concurso literario «Cartas pendientes»", "Concurso que celebra el poder de las palabras escritas en cartas.", []),
            A(None, None, "Micrófono abierto de poesía", "Espacio abierto para leer poesía.", ["lectura"]),
            A(None, None, "Música en vivo", "", ["musica"]),
        ],
    },
    {
        "name": "Afrodita Libros", "barrio": "Cordón", "addr": "Dr. Tristán Narvaja 1528",
        "acts": [A("22:30", None, "Noche de jazz", "Dúo de contrabajo y guitarra en vivo.", ["musica"])],
    },
    {
        "name": "Amazonia", "barrio": "Palermo", "addr": "Maldonado 1775",
        "note": "Corta la calle desde las 19:45 (según la diaria).",
        "acts": [
            A("19:00", None, "Narrativas del miedo", "Terror y suspenso en la literatura uruguaya contemporánea.", ["charla"]),
            A("19:45", None, "Los epílogos", "Música en vivo con versiones de canciones inspiradas en clásicos de la literatura.", ["musica"], ["Los epílogos"], ["imm", "ladiaria"]),
            A("20:30", None, "Ya ni siquiera miraba las puertas", "Claudio Invernizzi conversa con Sofía Romano sobre su último libro.", ["presentacion", "charla"], ["Claudio Invernizzi", "Sofía Romano"], ["imm", "ladiaria"]),
            A("21:15", None, "Supongamos que el mundo es", "Gabriel Calderón presenta su libro y reflexiona sobre el teatro y la vida.", ["presentacion"], ["Gabriel Calderón"], ["imm", "ladiaria"]),
            A("22:00", None, "Algo prestado, en vivo", "Tamara Tenenbaum y Malena Rey graban su podcast en vivo, desde Argentina.", ["charla"], ["Tamara Tenenbaum", "Malena Rey"], ["imm", "ladiaria", "elobservador"]),
            A("23:00", None, "Ninguna Higuera en vivo", "Cierre musical con la banda nominada a los Premios Graffiti 2026.", ["musica"], ["Ninguna Higuera"], ["imm", "ladiaria"]),
        ],
    },
    {
        "name": "América Latina", "barrio": "Cordón", "addr": "Av. 18 de Julio 2089",
        "acts": [
            A("19:00", None, "Cinco claves inútiles para elegir un libro para otro", "El Colectivo Migas de Papel propone un laboratorio sobre los criterios y sensibilidades al elegir una lectura para regalar o recomendar.", ["taller", "charla"], ["Colectivo Migas de Papel"]),
            A("21:00", None, "Hacia un tejido lector", "Joanna Peluffo y Maite González Vallejo, impulsoras de la Red Nacional de Clubes de Lectura, conversan sobre su libro y sobre crear espacios de lectura compartida.", ["presentacion", "charla"], ["Joanna Peluffo", "Maite González Vallejo"]),
        ],
    },
    {
        "name": "Amuleto – Libros de la Arena", "barrio": "Malvín", "addr": "Orinoco 4964",
        "acts": [
            A("19:00", None, "Hacé tu historieta de ciencia ficción", "Taller con Arghyla y Mario Pester para inventar una aventura de una niña ingeniera y un gato hacker en el Uruguay de 2170.", ["taller", "ninos"], ["Arghyla", "Mario Pester"]),
            A("20:00", None, "Belleza química: historias de autocuidado y transformación", "Lucía Vázquez Sica presenta su libro: belleza, ciencia, género y salud.", ["presentacion", "charla"], ["Lucía Vázquez Sica"]),
            A("20:30", None, "Pachequistas. Derecha política y dictadura en Uruguay (1973-1985)", "Marcos Rey presenta su investigación sobre Jorge Pacheco Areco y sus dirigentes durante la dictadura.", ["presentacion"], ["Marcos Rey"]),
            A("21:00", None, "Máxima pureza", "Fernando Butazzoni conversa con la editora Luisina Ríos sobre su libro, junto al Espacio Corto Buscaglia.", ["presentacion", "charla"], ["Fernando Butazzoni", "Luisina Ríos"]),
            A("22:00", None, "Parque hotel", "Carlos Rehermann presenta su novela, ambientada en el carnaval montevideano de los años treinta.", ["presentacion"], ["Carlos Rehermann"]),
            A("23:00", None, "En defensa de la mojarra", "El compositor y productor Fede Graña presenta su libro de textos e ilustraciones vinculados a su último disco.", ["presentacion"], ["Fede Graña"]),
        ],
    },
    {
        "name": "Club Cultural Charco", "barrio": "Palermo", "addr": "Maldonado 1477",
        "note": "Durante la noche: platitos y tapas de Peperoncino en el patio.",
        "acts": [
            A("19:00", "20:00", "Contesto absolutamente cualquier pregunta", "Pablo Casacuberta propone un micrófono abierto para responder preguntas sobre el sentido de la vida, el futuro y la experiencia humana.", ["charla"], ["Pablo Casacuberta"]),
            A("20:30", "21:30", "Sostener la paradoja", "El psicoanalista Santiago Lanza conversa con Eugenia Ladra y Martín Otegui Piñeyrúa sobre la paradoja y la literatura.", ["charla"], ["Santiago Lanza", "Eugenia Ladra", "Martín Otegui Piñeyrúa"]),
            A("22:00", "22:30", "Camila Ferrari solista", "Recital íntimo bajo el ficus de la librería.", ["musica"], ["Camila Ferrari"]),
        ],
    },
    {
        "name": "Librería Cultural Alfabeta", "barrio": "Pocitos", "addr": "Miguel Barreiro 3231",
        "acts": [
            A("20:00", None, "Leyendas en poesía y música", "La historia celta de Angus y el cisne, recitada y acompañada por flauta.", ["lectura", "musica"]),
            A("20:30", None, "Otra que yo, con ellos", "Elisa Lieber presenta su libro junto a Nole Marrone, Gonzalo Cammarota y Salvador Banchero: las versiones de una misma mujer, los mandatos y las contradicciones.", ["presentacion"], ["Elisa Lieber", "Nole Marrone", "Gonzalo Cammarota", "Salvador Banchero"]),
            A("21:15", None, "Música con notas", "Paola Larrama propone un recorrido en el que literatura y música se entrelazan.", ["musica"], ["Paola Larrama"]),
            A("22:00", None, "Las ciudades de Mario", "Mauro Libertella y Gabriel Peveroni conversan sobre Mario Levrero y el libro «Un hombre entre paréntesis».", ["presentacion", "charla"], ["Mauro Libertella", "Gabriel Peveroni", "Mario Levrero"], ["imm", "elobservador"]),
            A("22:45", None, "Escritoras del riesgo: escritura con el cuerpo adentro", "Conversación sobre experiencia, cuerpo, verdad y lenguaje.", ["charla"]),
            A("23:30", None, "Una cartografía de la extrañeza: Ciudad de México, Jujuy, Minas", "Guadalupe Nettel, Salomé Esper y Tamara Silva Bernaschina conversan sobre herencias, transformaciones e identidades. Modera Pía Supervielle.", ["charla"], ["Guadalupe Nettel", "Salomé Esper", "Tamara Silva Bernaschina", "Pía Supervielle"], ["imm", "elobservador"]),
            A("00:30", None, "Cierre musical con Tallo", "Entre la post milonga y la psicodelia.", ["musica"], ["Tallo"]),
        ],
    },
    {
        "name": "DAP Libros", "barrio": "Parque Rodó", "addr": "Jackson 1307 bis",
        "acts": [
            A("18:00", None, "Kermesse con descuentos", "Los descuentos en artículos de la librería se ganan en juegos de kermesse: tiro de aros a la botella, ruleta china, rueda de premios.", [], [], ["mec"]),
            A("18:00", "21:00", "Taller de dibujo y pintura", "Creación de personajes y guiones para cómics y manga.", ["taller"]),
            A("21:00", "22:00", "Taller de cosplay", "Accesorios y vestuario inspirados en personajes: máscaras, cascos y espadas.", ["taller"]),
        ],
    },
    {
        "name": "Diomedes Libros", "barrio": "Cordón", "addr": "Bulevar España 2129",
        "acts": [A("21:00", "22:00", "Música en vivo con Garo Arakelian", "Canciones clásicas del artista y adelantos de su última producción.", ["musica"], ["Garo Arakelian"])],
    },
    {
        "name": "El Yelmo de Mambrino", "barrio": "Palermo", "addr": "Canelones 1716",
        "acts": [
            A("19:30", None, "Patrimoñarte: descubrí Montevideo jugando", "Para niñas, niños y familias: explorar el patrimonio de la ciudad con juegos, imágenes, historias y desafíos, junto a Chinela.", ["ninos", "taller"], ["Chinela"]),
            A("20:30", None, "La Doña Blues Band", "Sexteto de blues y rock en vivo.", ["musica"], ["La Doña Blues Band"]),
            A("22:30", None, "El Peyote Asesino", "Pablo Izmirlian presenta su libro sobre la banda y cuenta el proceso de investigación.", ["presentacion"], ["Pablo Izmirlian", "El Peyote Asesino"]),
        ],
    },
    {
        "name": "Escaramuza", "barrio": "Cordón", "addr": "Dr. Pablo de María 1185",
        "note": "Corta la calle; actividades en la vereda y en el patio. Durante la noche: feria de libros y vinilos (Discomoda y La Mesa de los Discos), DJ set de LBR y gastronomía.",
        "acts": [
            A("20:00", None, "Lucrecia Martel presenta «Un destino común»", "Universos sonoros y dispositivos narrativos para imaginar futuros colectivos. Entrevista Natalia Ortiz Maldonado.", ["presentacion", "charla"], ["Lucrecia Martel", "Natalia Ortiz Maldonado"], ["imm", "busqueda", "elobservador"]),
            A("20:00", None, "Una ciudad fracturada: reimaginar Montevideo", "En el patio. Alquileres, transporte público y vecindad, con Fernando Filgueira, Víctor Borrás Ramos, Anabel Rieiro y Sebastián Aguiar. Modera Paula Scorza.", ["charla"], ["Fernando Filgueira", "Víctor Borrás Ramos", "Anabel Rieiro", "Sebastián Aguiar", "Paula Scorza"], ["imm", "busqueda"]),
            A("21:00", None, "Fernando Cabrera y su dulzura distante", "Concierto con guitarra y voz.", ["musica"], ["Fernando Cabrera"], ["imm", "busqueda", "ladiaria"]),
            A("21:00", None, "Fragmentos sin lugar, metapaisajes", "En el patio. Cruce de voces e imágenes con Lourdes Silva y Leo Giráldez.", ["lectura"], ["Lourdes Silva", "Leo Giráldez"], ["imm", "busqueda"]),
            A("21:30", None, "Cruzar el umbral: reminiscencias y fantasías en el limbo", "En el patio. Salomé Esper, Leticia Jorge y Gonzalo Deniz (Franny Glass) conversan. Modera Laura Amaya.", ["charla"], ["Salomé Esper", "Leticia Jorge", "Gonzalo Deniz", "Laura Amaya"], ["imm", "busqueda", "elobservador"]),
            A("22:00", None, "Guadalupe Nettel: la belleza del monstruo", "Entrevista en tres partes con Noelia Carrancio, Soledad Gago y Tania de Tomas.", ["charla"], ["Guadalupe Nettel", "Noelia Carrancio", "Soledad Gago", "Tania de Tomas"], ["imm", "busqueda", "elobservador"],
              note="La guía del MEC la ubica a las 21:00; el mapa y la prensa del 11/11, a las 22:00."),
            A("22:00", None, "Alejandro Zambra en primera persona", "Jugar, garabatear, escribir. Entrevista al escritor chileno, a cargo de Inés Bortagaray.", ["charla"], ["Alejandro Zambra", "Inés Bortagaray"], ["mec", "elobservador-zambra"],
              note="Figura en la guía del MEC y en El Observador (9/11), pero no en la versión más reciente del mapa ni en la prensa del 11/11. Confirmá el horario."),
            A("22:30", None, "Coloquio de las quiltras", "Lectura performática de la escritora chilena Lina Meruane.", ["lectura"], ["Lina Meruane"], ["imm", "busqueda", "elobservador"]),
            A("23:00", None, "Esto también es tarot", "Elisa Carricajo presenta su libro y propone una tirada colectiva de cartas, con Federica Folco y Mercedes Dellatorre.", ["presentacion"], ["Elisa Carricajo", "Federica Folco", "Mercedes Dellatorre"], ["imm", "elobservador"],
              note="La guía del MEC la ubica a las 22:30."),
            A("23:00", None, "Martín Buscaglia y sus Bochamakers", "Con Martín Ibarburu, Coby Acosta, Juana Buscaglia, Facundo Guiondjian y Tomás Nieves.", ["musica"], ["Martín Buscaglia", "Martín Ibarburu", "Coby Acosta", "Juana Buscaglia", "Facundo Guiondjian", "Tomás Nieves"], ["imm", "busqueda", "ladiaria"]),
            A("23:30", None, "Boni: avant-première musical", "Con Emiliano Aquino, Diego Pollovero, Agustina Canavesi, Álvaro Cardoso y Nicolás Grieco.", ["musica"], ["Boni"]),
            A("00:00", None, "Karibe con K", "Cierre musical.", ["musica"], ["Karibe con K"], ["imm", "busqueda", "ladiaria"]),
        ],
    },
    {
        "name": "Germina", "barrio": "Centro", "addr": "Carlos Roxlo 1370 bis",
        "acts": [
            A("18:30", None, "Soñando y jugando con Magda Dos Santos", "Música para toda la familia, especialmente para los más chicos, con canciones de su disco.", ["ninos", "musica"], ["Magda Dos Santos"]),
            A("19:30", None, "Creá y dibujá con Nico Peruzzo", "Dibujar y conversar con el creador de Pancho el Pit Bull.", ["ninos", "taller"], ["Nico Peruzzo"]),
        ],
    },
    {
        "name": "Guarida, Casa de Libros", "barrio": "Punta Carretas", "addr": "Héctor Miranda 2410",
        "note": "Durante la noche: Rincón del Haiku en la sala exterior y «Mate y escritura» con consignas en el patio.",
        "acts": [
            A("18:00", None, "Poesía ultrajoven", "Taller abierto de poesía y creatividad a cargo de menores de 18 años del taller En Una.", ["taller", "lectura"], [], ["imm", "ladiaria"]),
            A("19:00", "20:00", "Club de clubes, café literario", "Traé un libro para compartir, recomendar o hacer circular. Conversación, café e intercambio.", ["charla"], [], ["imm", "ladiaria"]),
            A("20:00", "21:30", "Cámara, libros, souvenirs literarios y nuevos autores", "Entrevistas abiertas a escritoras y escritores, y una mesa de nuevos autores con fragmentos para descubrir.", ["charla", "lectura"], [], ["imm", "ladiaria"]),
            A("22:00", None, "Micrófono abierto", "Con apertura de Viviane, de Poeta Soporta Poeta.", ["lectura"], ["Viviane", "Poeta Soporta Poeta"], ["imm", "ladiaria"]),
            A("23:00", "23:45", "Serenata literaria con Juan Solá", "Lectura desde el balcón para quienes estén dentro de la librería y en la calle.", ["lectura"], ["Juan Solá"], ["imm", "ladiaria"]),
            A("00:00", None, "Cierre musical con el Coro Guarida", "Concierto en completa oscuridad, en la Caverna.", ["musica"], ["Coro Guarida"], ["imm", "ladiaria"]),
        ],
    },
    {
        "name": "Idea Librería", "barrio": "Cordón", "addr": "Dr. Tristán Narvaja 1578",
        "hours": ["19:00", "01:00"],
        "acts": [
            A(None, None, "Lectura y encuentro con poetas locales", "", ["lectura"]),
            A(None, None, "Bandas y DJ", "Espectáculos musicales, bandas y DJ.", ["musica"]),
        ],
    },
    {
        "name": "Isadora Libros", "barrio": "Punta Carretas", "addr": "José Ellauri 661",
        "acts": [
            A("20:30", None, "Cuentos que se escapan de los libros", "Narración y juegos para niñas y niños, con humor, sonidos y finales inesperados.", ["ninos", "lectura"]),
            A("21:30", None, "Lecturas fracasantes", "Romina Serrano, Daniela Trimarco, Ivonne Calderón y voces invitadas leen fragmentos de literatura fracasante.", ["lectura"], ["Romina Serrano", "Daniela Trimarco", "Ivonne Calderón"]),
        ],
    },
    {
        "name": "La Libélula Libros & Café", "barrio": "Cordón", "addr": "Av. Gral. Rivera 2298",
        "acts": [
            A("17:50", None, "Arcos Unidos", "Música con violas, violonchelos, acordeones y otros instrumentos, con Cecilia, Juan y compañía.", ["musica"]),
            A("18:15", None, "Cuentos con Grace", "Grace Cuentacuentos comparte historias para disfrutar en familia, con música antes y después.", ["ninos", "lectura"], ["Grace Cuentacuentos"]),
            A("19:00", None, "Dulces trillizas, con Sandra Escames", "La autora presenta su libro para niñas y niños desde 7 años y firma ejemplares.", ["ninos", "presentacion"], ["Sandra Escames"]),
            A("21:00", None, "Belleza química, con Lucía Vázquez Sica", "Conversación sobre su libro, con preguntas y firma de ejemplares.", ["presentacion", "charla"], ["Lucía Vázquez Sica"]),
        ],
    },
    {
        "name": "Las Karamazov", "barrio": "Pocitos", "addr": "Av. Gral. Rivera 2670",
        "acts": [
            A("20:00", "21:30", "Introducción a la mística femenina en la Edad Media", "Con Atrio: mujeres que transformaron sus experiencias espirituales en escritos, visiones e imágenes.", ["charla"], ["Atrio"]),
            A("20:00", "23:00", "Intervención artística colectiva con Pulso Negro", "Creación participativa de una pegatina para intervenir la fachada por los 10 años de la librería. Para todas las edades.", ["taller", "ninos"], ["Pulso Negro"]),
            A("22:00", None, "Música en vivo con Emilia Olmedo", "Cantante y guitarrista, integrante de la murga joven Amarga.", ["musica"], ["Emilia Olmedo"]),
        ],
    },
    {
        "name": "Lautréamont Librería", "barrio": "Parque Rodó", "addr": "Maldonado 2045",
        "acts": [A("22:00", "23:00", "Música en vivo con Chino", "", ["musica"], ["Chino"])],
    },
    {
        "name": "Librería Areté", "barrio": "Cordón", "addr": "Dr. Tristán Narvaja 1641",
        "acts": [A("21:00", "00:00", "DJ en vivo", "Música para acompañar la noche.", ["musica"])],
    },
    {
        "name": "Librería El Virrey", "barrio": "Punta Carretas", "addr": "21 de Setiembre 2747",
        "acts": [
            A("19:00", None, "¿Cuántas mujeres caben en una misma mujer?", "Elisa Lieber conversa sobre su libro «Otra que yo»: mandatos, expectativas e identidad.", ["presentacion", "charla"], ["Elisa Lieber"]),
            A("20:15", None, "Charla sobre la adultez y otras imperfecciones", "Camila Suárez presenta «Metamorfosis»: la adultez, el amor y la identidad.", ["presentacion", "charla"], ["Camila Suárez"]),
            A("21:00", None, "A cara de perro", "Presentación del libro de Alfonso Lessa y conversación con el autor.", ["presentacion"], ["Alfonso Lessa"]),
            A("22:30", None, "El tridente: poder narco en Uruguay", "Antonio Ladra presenta su libro sobre el narcotráfico en el país.", ["presentacion"], ["Antonio Ladra"]),
        ],
    },
    {
        "name": "Librería Fundación de Cultura Universitaria", "barrio": "Ciudad Vieja", "addr": "25 de Mayo 553",
        "acts": [A("09:00", "20:00", "60 años de la FCU", "Exposición y presentación por los 60 años de la institución.", [])],
    },
    {
        "name": "Librería Guyunusa", "barrio": "Cordón", "addr": "Dr. Tristán Narvaja 1601",
        "acts": [
            A("21:30", None, "El living del goce", "En la calle: literatura, sexualidad, humor y activismo. Sobre el derecho a desear, decidir y habitar el propio cuerpo sin culpas.", ["charla"], [], ["imm", "ladiaria"]),
            A("22:30", None, "¡El goce suena!: Charlie Cromo", "Primera de tres propuestas de mujeres músicas.", ["musica"], ["Charlie Cromo"], ["imm", "ladiaria"]),
            A("23:00", None, "¡El goce suena!: Espíritu Olímpico", "", ["musica"], ["Espíritu Olímpico"], ["imm", "ladiaria"]),
            A("23:30", None, "¡El goce suena!: Las Toscas", "", ["musica"], ["Las Toscas"], ["imm", "ladiaria"]),
        ],
    },
    {
        "name": "Lannister Comics & Libros", "barrio": "Centro", "addr": "Av. 18 de Julio 892",
        "acts": [A("19:00", "21:00", "Taller de storytelling", "El guionista Diego Vázquez propone crear historias cortas. Podés llevar una historia empezada o empezar de cero. Inscripción por redes sociales o WhatsApp.", ["taller"], ["Diego Vázquez"])],
    },
    {
        "name": "Librería Mundos Invisibles", "barrio": "Cordón", "addr": "Av. Gral. Rivera 2205",
        "acts": [
            A("20:30", "21:30", "Más de un nacimiento en una misma vida", "Lauro Alonso invita a reflexionar sobre la percepción, la existencia y las posibilidades del presente.", ["charla"], ["Lauro Alonso"]),
            A("22:15", "23:15", "Música y palabras para el encuentro", "Canciones de autor, poesía, cánticos y mantras con momentos de meditación, a cargo de Florencia Slyomovich (Ambhar Music).", ["musica", "lectura"], ["Florencia Slyomovich"]),
        ],
    },
    {
        "name": "Libros de la Arena Pocitos", "barrio": "Pocitos", "addr": "Juan Benito Blanco 962",
        "acts": [
            A("19:30", "20:30", "A texto en cuello: micrófono abierto", "Cuentos breves del concurso en redes, poemas y fragmentos de autores que dejaron huella.", ["lectura"], [], ["imm", "ladiaria"]),
            A("21:00", "22:00", "Trabaja para no cerrar", "Conversatorio con Germán Di Pierro sobre su libro «Efectos especiales» y el rol del artista hoy.", ["presentacion", "charla"], ["Germán Di Pierro"], ["imm", "ladiaria"]),
            A("22:30", None, "Alias Tuk", "Un personaje de otro planeta llega con canciones y un mensaje de paz, amor y esperanza.", ["musica", "ninos"], ["Alias Tuk"], ["imm", "ladiaria"]),
        ],
    },
    {
        "name": "Libros del Paso", "barrio": "Centro", "addr": "Av. 18 de Julio 1308",
        "acts": [
            A("22:00", None, "El libro de terror en Uruguay", "Charla sobre la literatura de terror en el país.", ["charla"]),
            A("23:00", None, "Concurso de disfraces: viernes trece, noche de terror", "Participá con tu disfraz; se elige el más original.", []),
        ],
    },
    {
        "name": "Mercadito Eureka", "barrio": "Parque Rodó", "addr": "San Salvador 1981",
        "acts": [
            A("19:00", None, "Susurros insistentes ante la crueldad y Atisbo/Abismo", "Presentación de las obras de Susurro Resistente (Leticia Pérez de Sierra) y Lilián Toledo.", ["presentacion"], ["Leticia Pérez de Sierra", "Lilián Toledo"]),
            A("21:00", None, "Aparta/mientos", "Presentación del libro de Santiago Ferreira.", ["presentacion"], ["Santiago Ferreira"]),
            A("22:00", None, "Tarot de las Videntes", "Presentación de la obra de Lidia Martínez Novoa.", ["presentacion"], ["Lidia Martínez Novoa"]),
        ],
    },
    {
        "name": "Minerva Libros", "barrio": "Cordón", "addr": "Dr. Tristán Narvaja 1679",
        "acts": [
            A("20:00", None, "A cara de perro", "Alfonso Lessa presenta su último libro.", ["presentacion"], ["Alfonso Lessa"]),
            A("20:45", None, "Coro coordinado por Santiago Wirth", "Unos 20 participantes.", ["musica"], ["Santiago Wirth"]),
            A("21:30", None, "Constelación del Navío: poesía completa de Amanda Berenguer", "Presentación a cargo de Luis Bravo y Raquel Diana.", ["presentacion", "lectura"], ["Amanda Berenguer", "Luis Bravo", "Raquel Diana"]),
            A("22:30", None, "¿Quién se llevó mis vacas?", "Manuel Pérez Bravo conversa con Sergio Israel sobre su libro acerca del caso Conexión Ganadera.", ["presentacion", "charla"], ["Manuel Pérez Bravo", "Sergio Israel"]),
            A("23:30", None, "Revista literaria Fuga", "El mapa lo anuncia como lanzamiento, aunque el primer número se presentó en septiembre.", ["presentacion"], ["Revista Fuga"]),
        ],
    },
    {
        "name": "Oruga Libros", "barrio": "Parque Rodó", "addr": "Constituyente 2022",
        "acts": [
            A("18:00", "00:00", "Presentación de «Palabras para jugar»", "Parte de «Poesía, rimas y algo más».", ["ninos", "presentacion"]),
            A("18:00", "00:00", "Taller de rimas y creación de títeres", "Parte de «Poesía, rimas y algo más».", ["ninos", "taller"]),
            A("18:00", "21:00", "Pintacaritas", "Maquillaje artístico para las infancias.", ["ninos"]),
            A("19:00", "00:00", "¡Oh, sí! Una historia invertida", "Espectáculo interactivo de narración oral y teatro, con cuentos y juegos.", ["ninos", "lectura"]),
            A("20:00", "00:00", "Presentación de «Animales bien contados»", "", ["ninos", "presentacion"]),
            A("20:00", "00:00", "Taller: inventar animales estrafalarios", "Para jugar con las letras y enredar palabras.", ["ninos", "taller"]),
        ],
    },
    {
        "name": "Plaza Café", "barrio": "Parque Rodó", "addr": "Jackson 885",
        "acts": [
            A("09:00", "23:00", "El libro te elige", "Libros envueltos, sin que se vea título ni tema: cada lector elige a partir de una breve descripción del personal.", []),
            A("15:00", "23:00", "Micrófono abierto", "Un espacio para compartir lecturas y expresiones artísticas.", ["lectura"]),
        ],
        "note": "El mapa oficial le atribuye también actividades de Pocho Kids; la guía del MEC confirma que son de Pocho Kids.",
    },
    {
        "name": "Pocho Kids", "barrio": "Cordón", "addr": "Juan Paullier 1548",
        "note": "Sucursal infantil y juvenil de Librería Pocho.",
        "acts": [
            A("19:00", None, "Nenúfar", "Antología poética uruguaya publicada en 2026 por Ediciones Venado Real, con textos de 13 autoras y autores.", ["presentacion", "lectura"], ["Ediciones Venado Real"]),
            A("19:40", None, "Sofía Aguerre y Camila Silva", "Dos escritoras uruguayas de literatura juvenil: fantasía, ciencia ficción, misterio y una escritura sensible y poética.", ["presentacion", "charla"], ["Sofía Aguerre", "Camila Silva"]),
            A("20:30", None, "Nuevas voces de la literatura uruguaya", "Franco Bitancort, Martina Ramos y Diana García Techera: de Wattpad y la autopublicación a las editoriales tradicionales.", ["charla"], ["Franco Bitancort", "Martina Ramos", "Diana García Techera"]),
            A("21:30", None, "Celebramos el cómic nacional", "Autores de La Modernidad Editorial (Diego Vázquez, Catalina Rodríguez, Gabriel Ameijenda, Lucas Roselli, Carolina Duarte) y de Maldito Canario (Olimarvile Lumaga, Sebastián Navas).", ["charla"], ["Maldito Canario", "La Modernidad Editorial"]),
        ],
    },
    {
        "name": "Puro Verso", "barrio": "Centro", "addr": "Av. 18 de Julio 1199",
        "acts": [
            A("19:00", "22:00", "El Taller de Naiat", "Actividades artísticas para infancias, jóvenes y familias, en torno al cuento «El vestido más lindo del mundo», de Mónica Dos Santos y Colectivo Nzinga.", ["ninos", "taller"], ["Mónica Dos Santos", "Colectivo Nzinga"]),
            A("20:00", "20:45", "Dolor de rambla, de Pedro Dalton", "Presenta su nuevo poemario (Estuario) en charla con el escritor Mateo Piaggio.", ["presentacion", "charla"], ["Pedro Dalton", "Mateo Piaggio"]),
            A("20:45", "21:30", "Contra el antisemitismo y sus instrumentalizaciones", "Lucía Erlich, Victoria de Mello y Alejandro Joysz (Mentirosa Editora) conversan sobre voces judías, no judías y judeo-palestinas.", ["charla"], ["Lucía Erlich", "Victoria de Mello", "Alejandro Joysz"]),
            A("21:30", None, "Premio de los Libreros de Puro Verso", "Diálogo con el ganador del primer premio a la Mejor Novela Nacional 2026.", ["charla"]),
            A("22:15", None, "Anna Paola Rossi: Sanar desde el alma", "Charla abierta sobre el regreso de su libro (Grijalbo) y los registros akáshicos.", ["charla", "presentacion"], ["Anna Paola Rossi"]),
            A("23:00", None, "Cantate una", "Autores del libro de Acercándonos Ediciones conversan sobre el cancionero murguista e interpretan letras.", ["presentacion", "musica"], ["Acercándonos Ediciones"]),
        ],
    },
    {
        "name": "Ronda Espacio Creativo", "barrio": "Parque Rodó", "addr": "Bulevar España 2141",
        "note": "Descuentos en todos los libros desde las 16:00, aproximadamente (guía del MEC).",
        "acts": [
            A("19:30", None, "Taller de poesía", "Encuentro abierto en el café para descubrir y compartir poesía.", ["taller", "lectura"]),
            A("21:30", None, "Escucha de vinilos", "Selección musical en vinilo para el cierre.", ["musica"]),
        ],
    },
    {
        "name": "Librería Vila", "barrio": "Cordón", "addr": "Dr. Tristán Narvaja 1642",
        "acts": [A("23:00", "01:00", "DJ junto a Librería Areté", "Música para el cierre de la noche.", ["musica"])],
    },
    {
        "name": "Pocitos Libros", "barrio": "Pocitos", "addr": "Av. Brasil 2561",
        "note": "Noche de tango, con baile en la vereda.",
        "acts": [
            A("19:30", None, "Homenaje a Julio Sosa en su centenario", "Conversación sobre el libro «El tango de mi barrio».", ["charla", "presentacion"], ["Julio Sosa"], ["imm", "ladiaria"]),
            A("20:00", None, "Bandoneón y versos", "", ["musica", "lectura"], [], ["imm", "ladiaria"]),
            A("20:30", None, "Julio Sosa, pa' que sepan cómo soy", "Presentación del libro.", ["presentacion"], ["Julio Sosa"], ["imm", "ladiaria"]),
            A("21:00", None, "Tanguitarra", "Presentación con actuación musical en vivo.", ["presentacion", "musica"], [], ["imm", "ladiaria"]),
            A("21:30", None, "Baile de tangos en la vereda", "", ["musica"], [], ["imm", "ladiaria"]),
        ],
    },
    {
        "name": "Feltrinelli", "barrio": "Ciudad Vieja", "addr": "Sarandí 675",
        "note": "Tiene restaurante en la planta alta.",
        "acts": [
            A("19:30", None, "Un hombre entre paréntesis: retrato de Mario Levrero", "El escritor argentino Mauro Libertella conversa con Nicolás Tabárez sobre su libro.", ["presentacion", "charla"], ["Mauro Libertella", "Nicolás Tabárez", "Mario Levrero"], ["imm", "ladiaria", "elobservador"]),
            A("20:20", None, "Soy tu groupie", "Patricia Turnes, Naoko y Kristel Latecki conversan sobre rock y las historias entre artistas y seguidores.", ["charla"], ["Patricia Turnes", "Naoko", "Kristel Latecki"]),
            A("21:10", None, "Ino Guridi: show performático", "Intervención en vivo que combina distintos lenguajes artísticos.", ["musica"], ["Ino Guridi"], ["imm", "ladiaria"]),
            A("22:00", None, "El Indio Solari y Oktubre: literatura, rock y revolución", "Carolina Bello y Gustavo Rey conversan sobre el libro de Bello y el universo de los Redondos.", ["presentacion", "charla"], ["Carolina Bello", "Gustavo Rey"], ["imm", "ladiaria"]),
            A("23:10", None, "Spuntone & Mendaro en vivo", "Cierre musical.", ["musica"], ["Spuntone & Mendaro"], ["imm", "ladiaria"]),
        ],
    },
    {
        "name": "La Lupa Libros", "barrio": "Ciudad Vieja", "addr": "Peatonal Bacacay 1318 bis",
        "acts": [
            A("19:30", None, "Shanghai sonoro", "Gabriel Peveroni y Sebastián Auyanet conversan sobre los paisajes musicales de «Los desiertos se conectan entre sí» y otras novelas del autor.", ["charla"], ["Gabriel Peveroni", "Sebastián Auyanet"]),
            A("20:15", None, "Urbanofilia, de El Gato y La Caja", "Libro argentino sobre cómo transformar las ciudades y recuperar los espacios colectivos.", ["presentacion"], ["El Gato y La Caja"]),
            A("21:15", None, "Un rayo cualquiera: historias sin héroe para reparar el desastre", "Natalia Ortiz Maldonado (autora, editora de Hekht) conversa con Lucía Naser y Elisa Carricajo.", ["presentacion", "charla"], ["Natalia Ortiz Maldonado", "Lucía Naser", "Elisa Carricajo"], ["imm", "elobservador"]),
            A("22:15", None, "Utopías feministas para una economía en crisis", "Verónica Diz (Madreselva) conversa con Daniela Osorio-Cabrera y Mariana García Grisoni.", ["charla"], ["Verónica Diz", "Daniela Osorio-Cabrera", "Mariana García Grisoni"]),
            A("23:00", None, "Malditos Planetas", "Abre la noche de rock.", ["musica"], ["Malditos Planetas"]),
            A("23:45", None, "¡Habrá que construir otro modo de vivir!", "Cierre musical con La Tabaré en vivo.", ["musica"], ["La Tabaré"],
              note="La banda tiene otro show esa misma noche a las 20:00 en Canelones; conviene confirmar el horario."),
        ],
    },
    {
        "name": "Librería Montevideo", "barrio": "Cordón", "addr": "Tristán Narvaja 1536",
        "acts": [
            A("20:15", None, "Tabaré Etcheverry, cantor y faro de nuestro canto popular", "Juan Carlos Albarado presenta la nueva edición de «Tabaré Etcheverry. Vida y obra de un intérprete popular» y conversa con el público.", ["presentacion", "charla"], ["Juan Carlos Albarado", "Tabaré Etcheverry"]),
            A("21:00", None, "Nuestras cárceles, nuestros presos y nuestras políticas", "Mesa sobre cárceles, educación y reinserción de las personas privadas de libertad.", ["charla"]),
        ],
    },
    {
        "name": "Biblioteca Popular El Cántaro Fresco", "barrio": "Larrañaga",
        "note": "El mapa de la Intendencia la ubica en el Buceo; la guía del MEC y el Municipio C, en Larrañaga.", "addr": "Altamirano esq. Luis Alberto de Herrera",
        "acts": [
            A("19:00", "22:00", "Cadáver exquisito", "", ["taller"]),
            A("19:00", "22:00", "Oráculo de la biblio", "", []),
            A("19:30", None, "Búsqueda del tesoro", "Para niñas y niños.", ["ninos"]),
            A("20:00", None, "Partida de Club de detectives", "", ["ninos"]),
            A("20:30", None, "Trueque de libros y secretos", "", []),
        ],
    },
    {
        "name": "Centro de Fotografía de Montevideo", "barrio": "Centro", "addr": "Av. 18 de Julio 885",
        "note": "El espacio no cuenta con accesibilidad universal.",
        "hours": ["19:30", "23:30"],
        "acts": [
            A(None, None, "El CdF abierto hasta las 23:30", "Azotea verde y balcón fotográfico, proyecciones, mesa de CdF Ediciones, mediateca, libros fotográficos y exposiciones.", [], [], ["imm", "ladiaria"]),
            A("19:30", "21:30", "Activación fanzinera: desarmá y armá tu publicación", "Fanzines a partir de historias ya publicadas. Libre participación hasta completar aforo.", ["taller"], [], ["imm", "ladiaria"]),
        ],
    },
    {
        "name": "Librería Linardi y Risso", "barrio": "Ciudad Vieja", "addr": "Juan Carlos Gómez 1435",
        "hours": ["18:00", "01:00"],
        "note": "Según la guía del MEC, la exposición está durante todo el evento.",
        "acts": [A(None, None, "Primeras ediciones de Joaquín Torres García", "Exposición de primeras ediciones y publicaciones raras.", [], ["Joaquín Torres García"])],
    },
    {
        "name": "Librería Trazo (FADU)", "barrio": "Parque Rodó", "addr": "Bv. Gral. Artigas 1031",
        "note": "En la sede central de la FADU. En el mapa oficial este programa aparece también, por error, bajo Librería Pocho.",
        "acts": [
            A("17:00", "00:00", "Exposición DCV x Filarmónica", "En la Ex cabina. Se puede visitar hasta la medianoche.", [], [], ["fadu"]),
            A("18:30", None, "Revista Textos de Tecnología n.º 11", "En el Patio Carré. Edición dedicada a la extensión universitaria.", ["presentacion"], [], ["fadu"]),
            A("19:00", "00:00", "Feria de libros y emprendimientos FADU", "Librería Trazo en el hall, feria de emprendimientos de la comunidad FADU, feria del Seminario Interdisciplinario de Producto y cantina en la terraza.", [], [], ["imm", "fadu"]),
            A("20:30", None, "Coro de la FADU", "En el Patio Carré.", ["musica"], [], ["fadu"]),
            A("21:00", None, "Excusa vocal y Mabel vocal", "En el Patio Carré.", ["musica"], ["Excusa vocal", "Mabel vocal"], ["fadu"]),
            A("21:20", None, "Coro Champagnat", "En el Patio Carré.", ["musica"], ["Coro Champagnat"], ["fadu"]),
            A("21:40", None, "Coro Vox Mundi", "En el Patio Carré.", ["musica"], ["Coro Vox Mundi"], ["fadu"]),
        ],
    },
    {
        "name": "Librería Pocho", "barrio": "Cordón", "addr": "Av. 18 de Julio 2198",
        "acts": [
            A("20:00", "23:30", "Encuentro con escritores de Editorial Moa Demkroff", "Ana María Rappanello, Mauricio Zieleniec, Olga Armand Ugon, Martín Olivera, Edison Aguiar, Cecilia Charquero y Giselle Petrides comparten sus libros. Coordina Daniel Corch.", ["presentacion", "charla"],
              ["Ana María Rappanello", "Mauricio Zieleniec", "Olga Armand Ugon", "Martín Olivera", "Edison Aguiar", "Cecilia Charquero", "Giselle Petrides", "Daniel Corch"]),
        ],
    },
    {
        "name": "Calle Tristán Narvaja (Intendencia)", "barrio": "Cordón", "addr": "Tristán Narvaja y Av. 18 de Julio",
        "note": "Actividades de la Intendencia en la calle; no figuran como punto en el mapa.",
        "acts": [
            A("20:00", "21:10", "Proyección de «Rada, la película»", "En Tristán Narvaja entre Mercedes y Uruguay. Documental de Luis Ara sobre Rubén Rada, 70 minutos.", [], ["Rada, la película"], ["ladiaria", "infouruguay"]),
            A("21:30", None, "Casanova-Supervielle", "En el escenario de Tristán Narvaja y 18 de Julio, con Matías Craciun y Leticia Gambaro como artistas invitados.", ["musica"], ["Casanova-Supervielle", "Matías Craciun", "Leticia Gambaro"], ["ladiaria"]),
        ],
    },
    {
        "name": "Centro Cultural de España", "barrio": "Ciudad Vieja", "addr": "Rincón 629",
        "note": "No figura en el mapa oficial; programa publicado por el CCE.",
        "acts": [
            A("18:00", "22:00", "Serigrafía en vivo en bolsas de tela", "En el hall.", ["taller"], [], ["cce"]),
            A("18:00", "21:00", "Libros y ajedrez: el enroque de páginas", "En la mediateca. Partidas libres, desafíos y modalidades de juego, a cargo de Enmanuel Campos.", ["taller"], ["Enmanuel Campos"], ["cce"]),
            A("19:00", "22:00", "Lecturas, dados y tableros", "En la cafetería. Juegos de mesa modernos inspirados en universos literarios, a cargo de Sabrina Lattanzio y Verónica Trokebetrygier.", [], ["Sabrina Lattanzio", "Verónica Trokebetrygier"], ["cce"]),
            A("19:30", None, "Goro Gocher en el ciclo ¡A mover las cachas!", "En el auditorio.", ["musica"], ["Goro Gocher"], ["cce"]),
        ],
    },
]


for _p in PLACES:
    for _a in _p["acts"]:
        if "imm" in _a["src"] and "mec" not in _a["src"] and (_p["name"], _a["title"]) not in NOT_IN_MEC:
            _a["src"].insert(1, "mec")
