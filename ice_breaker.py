import os
from dotenv import load_dotenv
from langchain.chains import LLMChain
from langchain_community.chat_models import ChatOpenAI
from langchain_core.prompts import PromptTemplate

if __name__ == '__main__':
    load_dotenv()

    information="""Yanis Varoufakis (en griego: Ἰωάννης Βαρουφάκης, conocido también como Yanis Varufakis;1​ Atenas, 24 de marzo de 1961) es un economista con doble nacionalidad greco-australiana, catedrático universitario, político y activo bloguero y escritor, autor de varios libros de política y economía. Es líder del nuevo partido MeRA25 presentado el 21 de marzo de 2018, con el que se presentó a las elecciones griegas.2​ Es también cofundador del movimiento paneuropeo DiEM25 presentado en febrero de 2016.3​4​ Asimismo es cofundador junto a Bernie Sanders de la organización Internacional Progresista (IP) (en inglés, Progressive International, PI).5​6​

En 2015 fue elegido diputado del Consejo de los Helenos en las elecciones parlamentarias por la Coalición de la Izquierda (SYRIZA) y luego nombrado ministro de Finanzas de Grecia. Con este cargo, fue miembro del primer gabinete del gobierno de Alexis Tsipras, desde el 27 de enero, hasta su dimisión, el 6 de julio de 2015, por diferencias con la posición del gobierno griego frente a la troika europea en el marco de la Crisis de la zona euro.7​ Fue profesor de Teoría Económica en la Universidad de Atenas y antes colaborador, como economista, en la empresa Valve Corporation.8​9​ Actualmente combina su labor política internacional con la docencia en la Universidad de Texas en Austin.10​
Biografía
Vida académica

Tras realizar sus estudios secundarios en la escuela privada de Moraitis de Atenas Varoufakis estudió Economía matemática en la Universidad de Essex, y Estadística matemática en la Universidad de Birmingham.11​ Entre 1983 y 1985 fue profesor de Economía Econometría en la Universidad de Essex, donde dos años más tarde obtuvo su grado de doctor en Economía. Desde 1986 trabajó como investigador y profesor (Research Fellow) en la Universidad de Cambridge. Además, ya era docente de otras universidades: Universidad de Anglia del Este, Glasgow y Sídney, antes de que en septiembre de 2000 recibiese su nombramiento como titular de la cátedra de Economía en la Universidad Nacional y Kapodistríaca de Atenas. A partir de 2013 ha trabajado también como profesor invitado de la Lyndon B. Johnson School of Public Affairs de la Universidad de Texas en Austin.12​ Durante su desempeño en cargos públicos, mantuvo su posición como profesor de Teoría Económica en la Universidad de Atenas, aunque en excedencia. Varoufakis, estableció en el año 2002 en la Universidad de Atenas el Programa de Doctorado en Economía (UADPhilEcon) que dirigió hasta 2008.
Actividad política
En una entrevista en febrero de 2016 en Madrid
Véanse también: Crisis económica de 2008-2015, Crisis del euro, Crisis financiera de 2008, Crisis de la deuda soberana en Grecia y Referéndum de Grecia de 2015.

Desde enero de 2004 a diciembre de 2006 Varoufakis fue asesor económico de Yorgos Papandréu, por aquel entonces máximo dirigente del PASOK, de cuyo gobierno iba a convertirse en un ferviente crítico unos años más tarde. Varoufakis es autor de varios libros sobre teoría de juegos y es un popular analista económico de medios de noticias como BBC Today, CNN, Sky News, Bloomberg TV y Russia Today entre otros. En noviembre de 2010 junto a Stuart Holland formó el Partido Laborista MP y como profesor de Economía en la Universidad de Coímbra, Portugal, publicó A Modest Proposal, un conjunto de líneas políticas económicas orientadas a la superación de la crisis del euro.13​ Desde septiembre de 2011, Truman Factor14​ publica artículos de Varoufakis en inglés y en español. Varoufakis compara el papel de la economía de los Estados Unidos desde 1970 con el resto del mundo y con la figura del minotauro.15​ Dimitió como ministro el 6 de julio de 2015.16​
Cofundador del DIEM25 y MeRA25

Junto a otros activistas y políticos preparó entonces la creación del movimiento paneuropeo Movimiento Democracia en Europa 2025 DIEM25, del que fue cofundador, presentado el 8 de febrero de 2016 en Berlín y publicó: "no se que pasará en Berlin, si esto va a ser el fin"3​

El 21 de marzo de 2018 presentó un nuevo partido, el MeRA25 relacionado con el movimiento DIEM25 con el que concurrirá a las elecciones griegas.17​18​19​

En las elecciones del 7 de julio de 2019, Varoufakis regresó al parlamento griego. Su partido, MeRA25, obtuvo nueve escaños.20​
Activismo social - Los muros de la globalización

Durante 2005 y 2006 Varoufakis viajó, junto con la artista Danae Stratou, a lo largo de siete muros o líneas establecidos a lo largo del mundo (en Palestina, Etiopía-Eritrea, Kosovo, Belfast, Chipre, Cachemira y la Frontera entre Estados Unidos y México). Stratou produjo "CUT: 7 dividing lines"21​ ("CUT: 7 líneas divisorias") mientras Varoufakis escribió textos que se convirtieron de considerable importancia político-económica en aquel momento, titulado "The Globalising Wall"22​ ("Los muros de la globalización"). En 2010 Stratu y Varoufakis fundaron el proyecto Vital Space.23​
Valve Software

En marzo de 2012 Varoufakis fue economista residente en Valve Software, una gran compañía de videojuegos, donde investigó la economía digital que tomó forma espontáneamente en las comunidades transfronterizas de los jugadores de videojuegos, publicando un influyente blog sobre su investigación en Valve.24​
Obra de Varoufakis

El grueso de sus libros se ha centrado en los aspectos económicos y políticos de la globalización y más concretamente de la situación de Estados Unidos y Europa ante la crisis financiera de 2008 y la Gran Recesión, así como sus causas y sus posibles soluciones. Critica la gestión de la crisis por las instituciones 'no democráticas europeas' (Eurogrupo, Ecofin) y señala como Estados Unidos, preocupado por sí mismo, también tiene una visión global más realista que la Unión Europea. Destaca las contradicciones de macroeconomía básica que se han impuesto en Europa para exclusivo beneficio de las élites del complejo industrial centroeuropeo -básicamente alemán- y de los tenedores del capital financiero, los rentistas, poniendo en la peor situación a los países períféricos y a todos los trabajadores del mundo.

En relación con el comportamiento de la Fed en Estados Unidos señala, en su libro ¿Y los pobres sufren lo que deben?:

    Los tipos de interés altos son fantásticos para aquellos que viven del dinero que no han ganado, los llamados rentistas, pero no tan buenos para los fabricantes que ven dispararse el coste de sus inversiones y derrumbarse el poder adquistivo de sus clientes. Combinar alto rendimiento del capital financiero con unas tasas de beneficios altas para las empresas estadounidenses no iba a ser nunca fácil, y Volcker lo sabía. Era una combinación que sólo podía darse si, por un lado, la Fed empujaba los tipos de interés hacia arriba mientras, al mismo tiempo, el gobierno federal fingía no darse cuenta y, de hecho, promovía legislaciones que aplastaran las perspectivas salariales reales de los trabajadores estadounidenses.25​

En su libro Comportarse como adultos: Mi batalla contra el establishment europeo critica la construcción europea y la defensa de los intereses de los acreedores frente a los ciudadanos de los líderes europeos así como su falta de representatividad democrática:

    Europa es exactamente lo opuesto a democracia. Aunque es verdad que nuestros estados miembros son democracias en su funcionamiento, "Europa" (es decir, la Unión Europea) es una "zona libre de democracia". Y aquí está el enigma: Estados perfectamente democráticos han transferido todas las decisiones cruciales a un centro que carece totalmente de carácter democrático. En comparación, los defectuosos y muy problemáticos Estados Unidos son un parangón de democracia.26​

El director Costa Gavras dirigió en 2019 la película A puertas cerradas basada en el libro de Varoufakis Comportarse como adultos"""

    summary_template="""
    given the {information} about a person I want to create: 
    1. A shor summary
    2. Two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(input_variables=["information"], template=summary_template)

    llm= ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
    chain = LLMChain(llm=llm, prompt=summary_prompt_template)
    res = chain.invoke(input={"information": information})