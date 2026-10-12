"""Batch 1 (2026-10-12): 10 썰가챠 stories rewritten in Mexican Spanish.

Each entry reuses the Korean script's visuals (pictures, stock video, sfx, caption
colours) and swaps every word a viewer hears or reads. A = universal emotion
(no Korea framing), K = "En Corea..." curiosity.

    python batch1/build.py      # writes batch1/NN-<slug>.json
"""
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
from adapt import adapt   # noqa: E402
AI = "\n\nNarración con voz generada por IA."

STORIES = [
 dict(src="2026-10-10-1800", n="01", lane="A", slug="es-baby-crying-neighbors-gift",
      title=["Pidió perdón", "porque su bebé lloraba"],
      lines=["Pidió perdón por su bebé\ny esto le dejaron",
             "Su bebé lloraba todas las noches y la mamá se sentía fatal.",
             "Dejó a cada vecino jabón y una carta escrita a mano.",
             "Días después, abrió la puerta y se quedó helada.",
             "¿Qué había en su puerta?",
             "Manzanas, galletas, algas y cartas de los vecinos.",
             "Le decían que no se preocupara, que los bebés crecen llorando.",
             "¿Tus vecinos harían eso?"],
      yt=("Pidió perdón porque su bebé lloraba… y esto le dejaron los vecinos #shorts",
          "Una mamá en Corea se sentía mal porque su recién nacido lloraba día y noche. Dejó jabón y una carta "
          "a mano a sus vecinos para pedir perdón. Días después encontró en su puerta manzanas, galletas, algas "
          "y cartas: «los bebés crecen llorando, no te preocupes».",
          ["vecinos", "bebé", "historias reales", "buenas noticias", "corea", "chisme"])),
 dict(src="2026-10-11-1200", n="02", lane="A", slug="es-boss-coffee-calculator",
      title=["Se acabó el café", "y el jefe sacó cuentas"],
      lines=["Pidieron más café\ny el jefe sacó la calculadora",
             "Se acabó el café y el jefe sacó la calculadora.",
             "Calculó cuántos sobres toma cada quien al día.",
             "Se quejó de que cada uno gasta 35 centavos diarios.",
             "Y al día siguiente pegó este aviso.",
             "Máximo dos sobres de café por persona al día.",
             "Y dicen que el papel de baño lo pagan los empleados.",
             "El que lo contó lleva tres meses y ya quiere renunciar.",
             "¿Cuántos cafés te dan a ti?"],
      say={3: "Se quejó de que cada uno gasta treinta y cinco centavos diarios."},
      yt=("Pidieron café y el jefe sacó la calculadora #shorts",
          "Se acabó el café instantáneo de la oficina y el jefe calculó cuánto toma cada empleado al día. "
          "Al día siguiente pegó un aviso: máximo dos sobres por persona. Según el empleado que lo contó, "
          "hasta el papel de baño lo pagan ellos.",
          ["jefe", "oficina", "trabajo", "café", "historias reales", "chisme"])),
 dict(src="2026-10-12-1800", n="03", lane="A", slug="es-fifty-tickets-same-number",
      title=["Todo a un número", "50 boletos iguales"],
      lines=["Compró 50 boletos\ncon el mismo número",
             "Un señor en Estados Unidos compró 50 boletos, todos con el 0500.",
             "Pero repetir el número no sube tus probabilidades.",
             "Si no salía, perdía los 50 boletos de golpe.",
             "Y llegó el sorteo.",
             "¡Y el número ganador fue el 0500!",
             "Ganó con los 50: 250 mil dólares en total.",
             "Pero dice que nunca volverá a jugar ese número.",
             "¿Tú harías lo mismo?"],
      say={0: "Compró cincuenta boletos con el mismo número",
           1: "Un señor en Estados Unidos compró cincuenta boletos, todos con el cero cinco cero cero.",
           3: "Si no salía, perdía los cincuenta boletos de golpe.",
           5: "¡Y el número ganador fue el cero cinco cero cero!",
           6: "Ganó con los cincuenta: doscientos cincuenta mil dólares en total."},
      yt=("Compró 50 boletos con el mismo número y pasó esto #shorts",
          "Un hombre de Carolina del Sur compró 50 boletos de la lotería Pick 4, todos con el 0-5-0-0. "
          "En el sorteo salió justo ese número: ganó 5 mil dólares por boleto, 250 mil en total. "
          "Dice que no volverá a jugarlo.",
          ["lotería", "suerte", "estados unidos", "ganador", "historias reales", "chisme"])),
 dict(src="2026-10-09-0700", n="04", lane="A", slug="es-wallet-lost-51-years",
      # Pixabay gave a basketball court for "floor wooden boards" and 500-euro notes for "dollar bills"
      patch={1: {"video": ["carpenter working wood", "woodworking hands", "carpenter hammer"]},
             3: {"video": ["american dollar bill", "us dollar banknote", "one dollar bill"]}},
      title=["Su cartera de 1975", "apareció bajo el piso"],
      lines=["Abrieron una cartera\nperdida hace 51 años",
             "Un carpintero en Canadá encontró bajo el piso una cartera de 1975.",
             "Y lo que había adentro era una cápsula del tiempo.",
             "Credencial de la prepa, licencia de manejo y un billete de un dólar.",
             "Hasta un acta de nacimiento escrita a mano.",
             "Pero el verdadero misterio era un boleto para ver Hamlet.",
             "Su dueño, de 68 años, no recuerda haber ido a esa obra.",
             "¿Qué traes tú en tu cartera?"],
      panel=["¿Y tu cartera?", "① Puros tickets", "② Solo una tarjeta"],
      say={0: "Abrieron una cartera perdida hace cincuenta y un años",
           1: "Un carpintero en Canadá encontró bajo el piso una cartera de mil novecientos setenta y cinco.",
           6: "Su dueño, de sesenta y ocho años, no recuerda haber ido a esa obra."},
      yt=("Encontró una cartera perdida hace 51 años #shorts",
          "Un carpintero en Nueva Escocia, Canadá, encontró bajo el piso de una casa una cartera perdida en 1975: "
          "credencial escolar, licencia, acta de nacimiento escrita a mano, un billete de un dólar y un boleto "
          "para Hamlet. Su dueño, de 68 años, no recuerda haber visto esa obra.",
          ["cartera", "cápsula del tiempo", "canadá", "misterio", "historias reales", "chisme"])),
 dict(src="2026-10-10-0700", n="05", lane="A", slug="es-dog-treat-from-mouth",
      title=["Golosina con la boca", "45 mil dólares"],
      lines=["La mordió un perro\ny le pagan 45 mil dólares",
             "Una empleada de café le dio a un perro una golosina con la boca.",
             "¡Y el perro le mordió el labio!",
             "Le quedó una cicatriz y el labio chueco.",
             "Ella fue la que se acercó. ¿Quién crees que pagó?",
             "El juez ordenó al seguro del dueño pagarle unos 45 mil dólares.",
             "Dijo que fue raro, pero el dueño debió advertirle.",
             "¿Y tú cómo le das premios?"],
      say={0: "La mordió un perro y le pagan cuarenta y cinco mil dólares",
           5: "El juez ordenó al seguro del dueño pagarle unos cuarenta y cinco mil dólares."},
      yt=("Le dio una golosina al perro con la boca… y terminó en juicio #shorts",
          "Una empleada de una cafetería en Seúl le ofreció a un perro una golosina sosteniéndola con la boca y "
          "el perro le mordió el labio. Un juez ordenó al seguro del dueño pagarle unos 63 millones de wones "
          "(cerca de 45 mil dólares): fue raro acercarse así, pero el dueño debió advertir del riesgo.",
          ["perro", "mordida", "juicio", "mascotas", "historias reales", "chisme"])),
 dict(src="2026-10-08-0700", n="06", lane="K", slug="es-kid-orders-noodles-police",
      title=["Llamó a la policía", "para pedir comida"],
      lines=["Un niño llamó a la policía\npara pedir fideos",
             "En Corea, un niño de 9 años llamó a emergencias para pedir fideos.",
             "Pero no era una broma.",
             "Escondido en su cuarto, explicó cuántas personas había en su casa.",
             "Lo que en verdad quería decir era esto.",
             "Su papá estaba a punto de golpear a su mamá.",
             "La policía llegó en tres minutos y el papá quedó bajo investigación.",
             "¿Tú habrías entendido la llamada?"],
      panel=["¿Tú qué harías?", "① Lo entiendo", "② Pienso que es broma"],
      say={1: "En Corea, un niño de nueve años llamó a emergencias para pedir fideos."},
      yt=("Un niño llamó a la policía para pedir fideos… pero no era broma #shorts",
          "En Ansan, Corea del Sur, un niño de 9 años llamó al 112 (el número de emergencias) y pidió "
          "«un plato de fideos» para que no lo descubrieran. Escondido en su cuarto, explicó que su papá "
          "quería golpear a su mamá. La policía llegó en unos tres minutos.",
          ["corea", "policía", "niño valiente", "emergencias", "historias reales", "chisme coreano"])),
 dict(src="2026-10-12-1200", n="07", lane="K", slug="es-freezer-unplugged-phone",
      title=["Para cargar su celular", "derritió la tienda"],
      lines=["Desconectó el congelador\npara cargar su celular",
             "En Corea hay heladerías sin empleados, y ahí una clienta desconectó el congelador.",
             "Cargó su celular y se fue sin volver a conectarlo.",
             "Todos los helados se derritieron.",
             "El dueño tiró todo y ya la está denunciando.",
             "Y no es la primera vez que pasa.",
             "En 2022, a otra mujer le dieron cuatro meses de cárcel, en suspenso.",
             "¿Tú dónde cargas el celular?"],
      say={6: "En dos mil veintidós, a otra mujer le dieron cuatro meses de cárcel, en suspenso."},
      yt=("Desconectó el congelador para cargar su celular #shorts",
          "En Corea del Sur hay heladerías de autoservicio sin empleados. En una de ellas, una clienta "
          "desconectó el congelador para cargar su teléfono y se fue sin volver a conectarlo: se derritió todo. "
          "En 2022 otra mujer recibió 4 meses de prisión con suspensión por algo parecido.",
          ["corea", "helados", "tienda sin empleados", "celular", "historias reales", "chisme coreano"])),
 dict(src="2026-10-11-1800", n="08", lane="K", slug="es-hungry-call-city-hall",
      title=["Llevaba 3 días", "sin comer"],
      lines=["Llevaba 3 días sin comer\ny llamó a la alcaldía",
             "En Corea, un funcionario contestó y salió corriendo con su propio ramen.",
             "Pero en todo el camino nunca colgó el teléfono.",
             "Un señor de 50 años que vive en un cuartito llevaba tres días sin comer.",
             "¿Por qué no colgaba?",
             "Tenía miedo de que se desmayara por llevar tanto sin comer.",
             "Le llevó pan, leche y hasta comida de voluntarios.",
             "¿Tú habrías ido corriendo?"],
      say={0: "Llevaba tres días sin comer y llamó a la alcaldía",
           3: "Un señor de cincuenta años que vive en un cuartito llevaba tres días sin comer."},
      yt=("Llevaba 3 días sin comer y llamó a la alcaldía #shorts",
          "Un domingo en Gwangju, Corea del Sur, un hombre de 50 años que vive solo en un cuarto diminuto "
          "llamó a la oficina de su distrito: llevaba tres días sin comer. El funcionario de guardia tomó el pan, "
          "la leche y el ramen que tenía para él y fue a verlo sin colgar, por si se desmayaba.",
          ["corea", "buenas personas", "solidaridad", "ramen", "historias reales", "chisme coreano"])),
 dict(src="2026-10-08-1800", n="09", lane="K", slug="es-same-name-same-birthday",
      # 役所 窓口 carries Japanese signboard text -> the OCR check drops it and the scene went blank
      patch={4: {"items": [{"type": "illust", "q": ["パソコン 困る 男性", "パソコン 困る", "困る 男性"], "pos": "center", "size": "l", "at": 0.0, "fx": "pop"},
                           {"type": "emoji", "text": "💦", "pos": "top-left", "size": "s", "at": 0.4, "fx": "pop"}]}},
      title=["Mismo nombre,", "mismo cumpleaños"],
      lines=["Él se llama Lee Do-kyung\ny ella también",
             "En Corea, su acta de matrimonio tiene dos veces el mismo nombre y cumpleaños.",
             "Y lo que les pasa por eso es todavía más chistoso.",
             "En la prepa descubrieron que había otro Lee Do-kyung en su escuela.",
             "Al mudarse, el registro en línea no funcionó y tuvieron que ir en persona.",
             "Pero lo mejor pasó cuando se conocieron las familias.",
             "La tienda pensó que era un error y grabó otro nombre en la botella.",
             "¿Conoces a alguien con tu mismo nombre?"],
      panel=["¿Y tú?", "① Sí, conozco", "② Nunca"],
      yt=("Él se llama Lee Do-kyung… y ella también #shorts",
          "Una pareja en Corea del Sur tiene el mismo nombre, Lee Do-kyung, y la misma fecha de nacimiento. "
          "Se conocieron en la prepa, se casaron tras 10 años de novios y hasta el registro en línea les falla. "
          "Para conocer a las familias mandaron grabar su nombre en una botella, y la tienda grabó otro creyendo "
          "que era un error.",
          ["corea", "pareja", "mismo nombre", "amor", "historias reales", "chisme coreano"])),
 dict(src="2026-10-07-2100", n="10", lane="K", slug="es-newbie-skips-meeting-class",
      title=["Faltó a la junta", "porque tenía clases"],
      lines=["Faltó a la junta\nporque tenía clases",
             "En Corea, el nuevo de la oficina no quiso ir a la junta del viernes a las cinco: tenía clases.",
             "La junta era lejísimos y terminaría después de las ocho de la noche.",
             "Y su jefe, ya harto, le dijo: haz lo que quieras.",
             "Pero en internet, la gente se dividió.",
             "Muchos dijeron que el error era hacer una junta tan lejos un viernes a las cinco.",
             "Si fueras el jefe, ¿lo dejas ir a clases?"],
      panel=["¿Tú qué harías?", "① Que vaya a clases", "② A la junta"],
      yt=("Faltó a la junta del viernes porque tenía clases #shorts",
          "En Corea del Sur, un empleado nuevo avisó que no iría a la junta de equipo del viernes a las 5 de la "
          "tarde porque tenía clases: la junta era lejos y terminaría después de las 8. Su jefe le dijo «haz lo "
          "que quieras» y en internet la gente se dividió.",
          ["corea", "trabajo", "oficina", "jefe", "generación z", "chisme coreano"])),
]


def build(st: dict) -> dict:
    src = json.loads((Path.home() / "issue-shorts" / "scripts" / f"{st['src']}.json").read_text(encoding="utf-8"))   # 썰가챠 원본
    title, desc, tags = st["yt"]
    return adapt(src, dict(st, yt={"title": title, "description": desc, "tags": tags}))


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.path.insert(0, str(ROOT))
    from rules import lint, validate
    for st in STORIES:
        s = build(st)
        out = ROOT / "batch1" / f"{st['n']}-{st['slug']}.json"
        out.write_text(json.dumps(s, ensure_ascii=False, indent=1), encoding="utf-8")
        chars = sum(len(x["say"]) for x in s["segments"])
        probs = validate(s) + lint(s)
        print(f"{out.name}: {chars} chars", "OK" if not probs else "")
        for p in probs:
            print("   ", p)
