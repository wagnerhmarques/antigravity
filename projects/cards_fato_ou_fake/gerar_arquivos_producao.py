#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Gerador de Cards Fato ou Fake — USP e as Profissões
- Símbolos de ciência profissionais prontos (Lucide Icons: DNA, Átomo, Microscópio, Radiação, Becker e Lâmpada)
- Renderização vetorial exata tanto nos SVGs quanto nos PDFs
- Frente:
  * Topo: "USP E AS PROFISSÕES" centralizado (sem a palavra "Feira")
  * Fonte da frase da frente aumentada em 1 (21px no SVG / 9.8pt no PDF)
  * Texto entre aspas perfeitamente centralizado no campo em branco fixo
  * "CIÊNCIA OU MITO?" em amarelo no rodapé
- Verso:
  * Texto explicativo JUSTIFICADO e com fonte reduzida em 1
  * Layout arejado e harmonioso
"""

import os
import re
import base64
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

FONTS_DIR = os.path.expanduser("~/Library/Fonts")
FONT_OUTFIT_REG = os.path.join(FONTS_DIR, "Outfit-400.ttf")
FONT_OUTFIT_SEMI = os.path.join(FONTS_DIR, "Outfit-600.ttf")
FONT_OUTFIT_BOLD = os.path.join(FONTS_DIR, "Outfit-700.ttf")
FONT_OUTFIT_EXTRA = os.path.join(FONTS_DIR, "Outfit-800.ttf")
FONT_OUTFIT_BLACK = os.path.join(FONTS_DIR, "Outfit-900.ttf")

HAS_OUTFIT = False
if os.path.exists(FONT_OUTFIT_BLACK):
    try:
        pdfmetrics.registerFont(TTFont("Outfit-Regular", FONT_OUTFIT_REG))
        pdfmetrics.registerFont(TTFont("Outfit-SemiBold", FONT_OUTFIT_SEMI))
        pdfmetrics.registerFont(TTFont("Outfit-Bold", FONT_OUTFIT_BOLD))
        pdfmetrics.registerFont(TTFont("Outfit-ExtraBold", FONT_OUTFIT_EXTRA))
        pdfmetrics.registerFont(TTFont("Outfit-Black", FONT_OUTFIT_BLACK))
        HAS_OUTFIT = True
        print("✓ Fontes oficiais Outfit registradas com sucesso no ReportLab!")
    except Exception as e:
        print("Aviso registro Outfit:", e)

OUTPUT_DIR = "/Users/user/.gemini/antigravity-ide/scratch/cards-fato-ou-fake-usp"
ASSETS_DIR = os.path.join(OUTPUT_DIR, "assets")
SVG_DIR = os.path.join(OUTPUT_DIR, "svg")
PDF_DIR = os.path.join(OUTPUT_DIR, "pdf")

os.makedirs(ASSETS_DIR, exist_ok=True)
os.makedirs(SVG_DIR, exist_ok=True)
os.makedirs(PDF_DIR, exist_ok=True)

IFUSP_IMG_PATH = os.path.join(ASSETS_DIR, "logo_ifusp.png")
FMUSP_IMG_PATH = os.path.join(ASSETS_DIR, "logo_fmusp.png")

# Carrega base64 das imagens para inclusão direta nos SVGs
with open(IFUSP_IMG_PATH, "rb") as f:
    B64_IFUSP = base64.b64encode(f.read()).decode("utf-8")

with open(FMUSP_IMG_PATH, "rb") as f:
    B64_FMUSP = base64.b64encode(f.read()).decode("utf-8")

# Paleta
COLOR_WINE = "#3e072b"
COLOR_WINE_LIGHT = "#5a1140"
COLOR_PINK = "#ff007f"
COLOR_GREEN = "#a2ff92"
COLOR_GREEN_DARK = "#0d5c22"
COLOR_YELLOW = "#e8ff3b"
COLOR_WHITE = "#ffffff"

# Definições vetoriais dos símbolos de ciência profissionais (Lucide 24x24)
LUCIDE_ATOM = [
    {'type': 'circle', 'cx': 12, 'cy': 12, 'r': 1.4, 'fill': 1},
    {'type': 'path', 'd': 'M20.2 20.2c2.04-2.03.02-7.36-4.5-11.9-4.54-4.52-9.87-6.54-11.9-4.5-2.04 2.03-.02 7.36 4.5 11.9 4.54 4.52 9.87 6.54 11.9 4.5Z'},
    {'type': 'path', 'd': 'M15.7 15.7c4.52-4.54 6.54-9.87 4.5-11.9-2.03-2.04-7.36-.02-11.9 4.5-4.52 4.54-6.54 9.87-4.5 11.9 2.03 2.04 7.36.02 11.9-4.5Z'}
]

LUCIDE_DNA = [
    {'type': 'path', 'd': 'M2 15c6.667-6 13.333 0 20-6'},
    {'type': 'path', 'd': 'M9 22c1.798-1.998 2.518-3.995 2.807-5.993'},
    {'type': 'path', 'd': 'M15 2c-1.798 1.998-2.518 3.995-2.807 5.993'},
    {'type': 'path', 'd': 'm17 6-2.891-2.891'},
    {'type': 'path', 'd': 'm7 18 2.891 2.891'},
    {'type': 'path', 'd': 'm10 16 1.5 1.5'},
    {'type': 'path', 'd': 'm14 8-1.5-1.5'},
    {'type': 'path', 'd': 'm16.5 10.5 1 1'},
    {'type': 'path', 'd': 'm6.5 12.5 1 1'},
    {'type': 'path', 'd': 'm20 9 .891.891'},
    {'type': 'path', 'd': 'M3.109 14.109 4 15'}
]

LUCIDE_MICROSCOPE = [
    {'type': 'path', 'd': 'M6 18h8'},
    {'type': 'path', 'd': 'M3 22h18'},
    {'type': 'path', 'd': 'M14 22c3.86 0 7-3.14 7-7c0-3.86-3.14-7-7-7h-1'},
    {'type': 'path', 'd': 'M9 14h2'},
    {'type': 'path', 'd': 'M7 10V6h6v4c0 1.1-0.9 2-2 2H9c-1.1 0-2-0.9-2-2Z'},
    {'type': 'path', 'd': 'M12 6V2M9 2h6'}
]

LUCIDE_FLASK = [
    {'type': 'path', 'd': 'M14 2v6a2 2 0 0 0 .245.96l5.51 10.08A2 2 0 0 1 18 22H6a2 2 0 0 1-1.755-2.96l5.51-10.08A2 2 0 0 0 10 8V2'},
    {'type': 'path', 'd': 'M6.453 15h11.094'},
    {'type': 'path', 'd': 'M8.5 2h7'}
]

LUCIDE_RADIATION = [
    {'type': 'circle', 'cx': 12, 'cy': 12, 'r': 1.6, 'fill': 1},
    {'type': 'path', 'd': 'M14 15.4641a4 4 0 0 1-4 0L7.52786 19.74597 A 1 1 0 0 0 7.99303 21.16211 10 10 0 0 0 16.00697 21.16211 1 1 0 0 0 16.47214 19.74597z'},
    {'type': 'path', 'd': 'M16 12a4 4 0 0 0-2-3.464l2.472-4.282a1 1 0 0 1 1.46-.305 10 10 0 0 1 4.006 6.94A1 1 0 0 1 21 12z'},
    {'type': 'path', 'd': 'M8 12a4 4 0 0 1 2-3.464L7.528 4.254a1 1 0 0 0-1.46-.305 10 10 0 0 0-4.006 6.94A1 1 0 0 0 3 12z'}
]

LUCIDE_LIGHTBULB = [
    {'type': 'path', 'd': 'M9 18h6M10 22h4M9 14c-0.2-1-0.7-1.7-1.5-2.5C6.8 10.6 6 9.4 6 8c0-3.313 2.686-6 6-6s6 2.686 6 6c0 1.4-0.8 2.6-1.5 3.5-0.8 0.8-1.3 1.5-1.5 2.5'}
]

LUCIDE_FOOTBALL = [
    {'type': 'path', 'd': 'M3 21C4 10 10 4 21 3C20 14 14 20 3 21Z'},
    {'type': 'path', 'd': 'M3 21L21 3'},
    {'type': 'path', 'd': 'M7.5 13.5L10.5 16.5'},
    {'type': 'path', 'd': 'M10.5 10.5L13.5 13.5'},
    {'type': 'path', 'd': 'M13.5 7.5L16.5 10.5'}
]

LUCIDE_GEAR = [
    {'type': 'circle', 'cx': 12, 'cy': 12, 'r': 3.2, 'fill': 0},
    {'type': 'circle', 'cx': 12, 'cy': 12, 'r': 6.8, 'fill': 0},
    {'type': 'path', 'd': 'M12 2v3.2M12 18.8v3.2M2 12h3.2M18.8 12h3.2M4.93 4.93l2.26 2.26M16.81 16.81l2.26 2.26M4.93 19.07l2.26-2.26M16.81 7.19l2.26-2.26'}
]


CARDS_DATA = [
    {
        "num": 1,
        "type": "FATO",
        "photo_file": "card_01_foto.jpg",
        "photo_caption": "📷 Banana & Potássio-40: radiação natural",
        "category": "Radiação no Cotidiano",
        "emoji": "🍌",
        "statement": "Comer uma banana faz você absorver radiação.",
        "headline": "O POTÁSSIO DA BANANA É NATURALMENTE RADIOATIVO!",
        "explanation": "A banana é rica em potássio, nutriente vital para os músculos e coração. Porém, cerca de 0,012% de todo o potássio natural na Terra é o isótopo <b>Potássio-40 (⁴⁰K)</b>, que é radioativo e emite partículas ao decair. Na Física Médica existe até uma unidade didática bem-humorada chamada <i>BED (Banana Equivalent Dose)</i> para comparar doses diárias de radiação. Fique tranquilo: nosso corpo mantém o nível de potássio em equilíbrio biológico e elimina o excesso. Você precisaria comer 10 milhões de bananas de uma vez para sofrer qualquer efeito nocivo!"
    },
    {
        "num": 2,
        "type": "FAKE",
        "category": "Ressonância Magnética",
        "emoji": "🧲",
        "statement": "O ímã gigante da ressonância magnética é desligado no botão quando a clínica fecha.",
        "headline": "O ÍMÃ FICA LIGADO 24 HORAS POR DIA, 365 DIAS NO ANO!",
        "explanation": "O ímã de uma máquina de ressonância é um <b>eletroímã supercondutor</b>. Suas bobinas ficam mergulhadas em Hélio Líquido a impressionantes <b>-269 °C</b> (quase o zero absoluto!), onde a resistência elétrica é nula e a corrente gira perpetuamente sem gastar energia da tomada. Desligar o campo magnético só ocorre em emergências extremas por um processo chamado <i>Quench</i>, que ferve milhares de litros de gás hélio e custa caro para restabelecer. Por isso, a sala é permanentemente magnética e objetos de ferro nunca podem entrar lá!"
    },
    {
        "num": 3,
        "type": "FATO",
        "photo_file": "card_03_foto.jpg",
        "photo_caption": "📷 PET Scan: aniquilação pósitron-elétron",
        "category": "Medicina Nuclear",
        "emoji": "⚛️",
        "statement": "Hospitais usam antimatéria para encontrar tumores escondidos no corpo.",
        "headline": "O EXAME DE PET SCAN USA PÓSITRONS (ANTIMATÉRIA REAL)!",
        "explanation": "Parece ficção científica, mas é rotina médica! No exame de <b>PET Scan (Tomografia por Emissão de Pósitrons)</b>, o paciente recebe uma dose de glicose ligada a um radioisótopo (como o Flúor-18). Como as células tumorais crescem rápido e consomem muito açúcar, o composto se acumula nelas. Ao decair, o átomo emite um <b>pósitron</b> (a antimatéria do elétron). Ao colidir com um elétron do tecido, ambos se <b>aniquilam</b>, gerando dois raios gama em sentidos opostos (180°). Detectores captam essa luz e mapeiam o tumor com precisão milimétrica!"
    },
    {
        "num": 4,
        "type": "FATO",
        "photo_file": "card_04_foto.jpg",
        "photo_caption": "📷 Fluoroscópio de sapatos em loja (c. 1945)",
        "category": "História da Ciência",
        "emoji": "👞",
        "statement": "Lojas de sapatos antigamente usavam máquinas de raios X para os clientes verem os ossos do pé dentro do calçado novo.",
        "headline": "SAPATARIAS TINHAM APARELHOS DE RAIO X NOS ANOS 1930 A 1950!",
        "explanation": "Entre as décadas de 1920 e 1950, era febre em lojas de calçados colocar os pés em <b>fluoroscópios de sapato</b>. Crianças e clientes olhavam por um visor e viam, em tempo real, os ossos dos pés se mexendo dentro do sapato novo para checar o ajuste. Como não havia blindagem e a radiação era vista como atração moderna, vendedores e clientes recebiam doses desnecessárias e contínuas de raios X. Quando a ciência comprovou os danos biológicos cumulativos, essas máquinas foram banidas, impulsionando o nascimento da <b>Proteção Radiológica</b> moderna."
    },
    {
        "num": 5,
        "type": "FATO",
        "photo_file": "card_05_foto.jpg",
        "photo_caption": "📷 Manuscritos de Marie Curie em cofre de chumbo",
        "category": "Pioneiros da Ciência",
        "emoji": "📓",
        "statement": "Os cadernos da cientista que descobriu a radioatividade ainda precisam ficar guardados em caixas de chumbo.",
        "headline": "OS MANUSCRITOS DE MARIE CURIE DURARÃO 1.500 ANOS RADIOATIVOS!",
        "explanation": "Marie Curie, primeira pessoa a conquistar dois Prêmios Nobel em ciências (Física e Química), descobriu o Polônio e o Rádio trabalhando sem qualquer proteção, numa época em que ninguém conhecia os perigos biológicos da radiação. Seus cadernos de anotações e roupas foram tão contaminados por <b>Rádio-226</b> (que tem meia-vida de 1.600 anos) que continuam ativos até hoje. Atualmente, os manuscritos ficam guardados em cofres blindados com chumbo na França e só podem ser abertos com trajes de proteção e dosímetros."
    },
    {
        "num": 6,
        "type": "FATO",
        "photo_file": "card_06_foto.jpg",
        "photo_caption": "📷 Segurança e compressas em ressonância",
        "category": "Eletromagnetismo & Saúde",
        "emoji": "🎨",
        "statement": "Pessoas tatuadas podem sentir a pele esquentar ou até queimar durante um exame de ressonância magnética.",
        "headline": "PIGMENTOS COM METAIS SOFREM INDUÇÃO E PODEM AQUECER!",
        "explanation": "Algumas tintas de tatuagem (especialmente escuras ou avermelhadas antigas) contêm óxidos metálicos, como compostos de ferro. Pela <b>Lei da Indução de Faraday</b>, as variações rápidas de radiofrequência e do campo magnético da ressonância induzem microcorrentes elétricas nas partículas metálicas da pele. Essas correntes geram calor por efeito Joule, podendo causar irritação ou queimação superficial. Por isso, a equipe de Física Médica aplica um questionário pré-exame rigoroso e coloca compressas frias se necessário."
    },
    {
        "num": 7,
        "type": "FATO",
        "photo_file": "card_07_foto.jpg",
        "photo_caption": "📷 Braquiterapia: micro-sementes x grãos de arroz",
        "category": "Tratamento do Câncer",
        "emoji": "🌾",
        "statement": "Os médicos colocam sementes radioativas do tamanho de um grão de arroz dentro do corpo de pacientes com câncer.",
        "headline": "A BRAQUITERAPIA IMPLANTA MICRO-SEMENTES RADIOATIVAS NO TUMOR!",
        "explanation": "Essa técnica avançada se chama <b>Braquiterapia</b> (do grego <i>brachys</i> = perto). Em vez de usar um feixe de radiação externo distante, os médicos implantam minúsculas cápsulas de titânio (do tamanho de grãos de arroz) contendo radioisótopos (como Iodo-125 ou Paládio-103) diretamente dentro do tumor, como no câncer de próstata. Pela <i>Lei do Inverso do Quadrado da Distância</i>, a dose é máxima para destruir as células doentes por dentro, mas cai para quase zero nos órgãos sadios vizinhos, com planejamento 3D milimétrico da Física Médica."
    },
    {
        "num": 8,
        "type": "FATO",
        "photo_file": "card_08_foto.jpg",
        "photo_caption": "📷 Produtos radioativos dos anos 1920 em museu",
        "category": "Curiosidades Históricas",
        "emoji": "💄",
        "statement": "Nos anos 1920, as farmácias vendiam pasta de dente e cremes de beleza radioativos.",
        "headline": "PRODUTOS COM RÁDIO E TÓRIO ERAM VENDIDOS COMO MILAGROSOS!",
        "explanation": "Logo após a descoberta da radioatividade, o público ficou fascinado pela energia invisível dos átomos. Marcas famosas vendiam pomadas, sabonetes e até pastas dentais como a <i>Doramad</i>, prometendo 'brilho celular e rejuvenescimento atômico'. As pessoas não sabiam que a radiação ionizante danifica o DNA das células. Quando consumidores e operários fabris desenvolveram anemias graves e lesões ósseas, a medicina interveio. Todos os produtos foram proibidos e a segurança radiológica virou lei internacional, hoje aplicada por físicos médicos."
    },
    {
        "num": 9,
        "type": "FATO",
        "photo_file": "card_09_foto.jpg",
        "photo_caption": "📷 Radioterapia veterinária com acelerador linear",
        "category": "Saúde Animal & Tecnologia",
        "emoji": "🐶",
        "statement": "Animais de estimação também fazem sessões de radioterapia em aceleradores lineares modernos.",
        "headline": "PETS COM CÂNCER SÃO TRATADOS COM ACELERADORES LINEARES!",
        "explanation": "A oncologia veterinária moderna utiliza exatamente os mesmos <b>aceleradores lineares de alta energia</b> e tomografias computadorizadas da medicina humana. Cães, gatos e até animais silvestres com câncer recebem feixes precisos de radiação para curar o tumor com máxima preservação dos tecidos sadios. A única diferença é que os pets recebem uma sedação leve e segura para ficarem imóveis durante os 2 ou 3 minutos do disparo. O Físico Médico calcula os ângulos dos feixes e a dose curativa exata para cada espécie."
    },
    {
        "num": 10,
        "type": "FATO",
        "photo_file": "card_10_foto.jpg",
        "photo_caption": "📷 Cíclotron hospitalar em bunker blindado",
        "category": "Aceleradores de Partículas",
        "emoji": "⚡",
        "statement": "Alguns hospitais possuem um acelerador de partículas escondido no subsolo para fabricar substâncias de exames.",
        "headline": "GRANDES HOSPITAIS TÊM ACELERADORES CÍCLOTRONS EM BUNKERS!",
        "explanation": "Grandes complexos hospitalares (como o Hospital das Clínicas da FMUSP e o IPEN em São Paulo) abrigam aceleradores circulares de partículas chamados <b>Cíclotrons</b>, protegidos por paredes de concreto maciço de 2 metros. Eles aceleram prótons a frações da velocidade da luz para produzir radioisótopos vitais para diagnósticos precoces de câncer, como o <b>Flúor-18</b>. Por ter meia-vida de apenas 110 minutos (em duas horas metade já decaiu), ele não pode viajar de longe: precisa ser sintetizado no próprio centro e injetado a tempo no paciente!"
    },
    {
        "num": 11,
        "type": "FAKE",
        "category": "Mitos do Raio X",
        "emoji": "🩻",
        "statement": "Você continua emitindo radiação por algumas horas depois de fazer um simples raios X do tórax.",
        "headline": "VOCÊ NÃO EMITE NENHUMA RADIAÇÃO APÓS O EXAME DE RAIO X!",
        "explanation": "Esse é um dos mitos mais comuns! O raio X é uma onda eletromagnética, exatamente como o flash de uma câmera fotográfica. No milissegundo em que o disparo elétrico é desligado, <b>a radiação desaparece instantaneamente</b>. O corpo não armazena raios X, não fica fosforescente e não emite nada ao redor. Você pode abraçar bebês ou gestantes imediatamente após o exame com 100% de segurança. (Atenção: só há emissão temporária em exames de Medicina Nuclear, onde um radiofármaco é injetado, mas no raio X comum isso nunca acontece!)."
    },
    {
        "num": 12,
        "type": "FATO",
        "photo_file": "card_12_foto.jpg",
        "photo_caption": "📷 Efeito Cherenkov: luz azul na água",
        "category": "Óptica & Partículas",
        "emoji": "👁️",
        "statement": "Pacientes que fazem radioterapia na região da cabeça às vezes enxergam flashes de luz azul mesmo estando de olhos fechados.",
        "headline": "É O EFEITO CHERENKOV ACONTECENDO DENTRO DO PRÓPRIO OLHO!",
        "explanation": "No vácuo, a luz viaja no limite cósmico de 300.000 km/s. Porém, dentro da água ou do humor vítreo do globo ocular, ela desacelera para cerca de 225.000 km/s. Quando partículas de alta energia emitidas pelo acelerador linear cruzam o olho do paciente mais rápido que a luz <i>naquele meio líquido</i>, geram uma onda de choque eletromagnética visível em azul-brilhante — o <b>Efeito Cherenkov</b> (o equivalente óptico ao 'boom sônico' de um caça supersônico!). O paciente literalmente enxerga a física quântica acontecendo dentro da retina!"
    },
    {
        "num": 13,
        "type": "FATO",
        "photo_file": "card_13_foto.jpg",
        "photo_caption": "📷 Hélio Líquido (-269 °C) em ressonância",
        "category": "Recursos do Planeta",
        "emoji": "🎈",
        "statement": "As máquinas de ressonância magnética dos hospitais consomem grande parte do gás hélio disponível no planeta.",
        "headline": "RESSONÂNCIAS USAM ATÉ 30% DO HÉLIO LÍQUIDO DO PLANETA!",
        "explanation": "O mesmo gás hélio que faz bexigas flutuarem tem um papel indispensável na medicina: na forma líquida a -269 °C, ele resfria os ímãs das ressonâncias para mantê-los em supercondutividade. Como o hélio é um recurso fóssil finito que escapa para o espaço quando liberado, a Física Médica e a engenharia desenvolveram tecnologias modernas de circuito fechado ('Zero Boil-Off'), que recirculam o gás sem perdas, garantindo que os hospitais continuem salvando vidas sem esgotar esse recurso natural raro da Terra."
    },
    {
        "num": 14,
        "type": "FAKE",
        "category": "Blindagem & Segurança",
        "emoji": "🛡️",
        "statement": "O colete de chumbo usado na radiografia absorve a radiação como uma esponja e precisa ser descartado quando fica 'cheio'.",
        "headline": "O COLETE DE CHUMBO NUNCA FICA 'CHEIO' DE RADIAÇÃO!",
        "explanation": "O avental de chumbo não funciona como uma esponja que se encharca de água. O chumbo atua como uma barreira física de altíssima densidade atômica (Z=82) que barra os fótons de raio X através de interações quânticas (como o <i>Efeito Fotoelétrico</i> e o <i>Espalhamento Compton</i>), dissipando a energia na forma de vibrações térmicas microscópicas imperceptíveis. O colete nunca satura e pode durar décadas, sendo descartado apenas se sofrer rasgos ou fissuras mecânicas no chumbo, testadas anualmente pelo Físico Médico."
    },
    {
        "num": 15,
        "type": "FATO",
        "photo_file": "card_15_foto.jpg",
        "photo_caption": "📷 IA na tomografia 3D: reconstrução sem ruído",
        "category": "Inteligência Artificial",
        "emoji": "🤖",
        "statement": "A inteligência artificial já consegue transformar exames de imagem feitos com doses muito baixas de radiação em imagens nítidas e de muito boa qualidade.",
        "headline": "A INTELIGÊNCIA ARTIFICIAL PERMITE EXAMES COM DOSES ULTRABAIXAS!",
        "explanation": "Em tomografias computadorizadas, reduzir a dose de radiação costumava gerar imagens cheias de 'ruído' granulado, como uma foto tirada no escuro. Hoje, redes neurais profundas de <b>Inteligência Artificial (Deep Learning)</b> treinadas com milhões de exames conseguem remover o ruído estocástico e reconstruir imagens perfeitamente nítidas a partir de frações mínimas da dose convencional. O Físico Médico calibra e valida esses modelos para garantir fidelidade diagnóstica total, protegendo especialmente crianças e pacientes oncológicos."
    }
]

B64_PHOTOS = {}
for card in CARDS_DATA:
    if "photo_file" in card:
        p_path = os.path.join(ASSETS_DIR, card["photo_file"])
        if os.path.exists(p_path):
            with open(p_path, "rb") as f:
                B64_PHOTOS[card["num"]] = base64.b64encode(f.read()).decode("utf-8")

def get_svg_science_symbols_markup():
    """Gera os 7 símbolos profissionais de ciência da Lucide em SVG com traço rosa translúcido."""
    return """
    <!-- 7 Símbolos de Ciência Profissionais Lucide (Translúcidos) -->
    <g stroke="#ff007f" stroke-opacity="0.22" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
      <!-- 1. DNA (Topo Esquerdo) -->
      <g transform="translate(45, 30) rotate(-35) scale(2.4)">
        <path d="M2 15c6.667-6 13.333 0 20-6" />
        <path d="M9 22c1.798-1.998 2.518-3.995 2.807-5.993" />
        <path d="M15 2c-1.798 1.998-2.518 3.995-2.807 5.993" />
        <path d="m17 6-2.891-2.891M7 18l2.891 2.891M10 16l1.5 1.5M14 8l-1.5-1.5M16.5 10.5l1 1M6.5 12.5l1 1M20 9l.891.891M3.109 14.109l.891.891" />
      </g>
      <!-- 2. Buckyball / Nanociência (Topo Centro) -->
      <g transform="translate(165, 20) rotate(15) scale(2.1)">
        <path d="M3 21C4 10 10 4 21 3C20 14 14 20 3 21Z" />
        <path d="M3 21L21 3M7.5 13.5L10.5 16.5M10.5 10.5L13.5 13.5M13.5 7.5L16.5 10.5" />
      </g>
      <!-- 3. Átomo (Topo Direito) -->
      <g transform="translate(275, 26) scale(2.4)">
        <circle cx="12" cy="12" r="1.4" fill="#ff007f" />
        <path d="M20.2 20.2c2.04-2.03.02-7.36-4.5-11.9-4.54-4.52-9.87-6.54-11.9-4.5-2.04 2.03-.02 7.36 4.5 11.9 4.54 4.52 9.87 6.54 11.9 4.5Z" />
        <path d="M15.7 15.7c4.52-4.54 6.54-9.87 4.5-11.9-2.03-2.04-7.36-.02-11.9 4.5-4.52 4.54-6.54 9.87-4.5 11.9 2.03 2.04 7.36.02 11.9-4.5Z" />
      </g>
      <!-- 4. Lâmpada da Inovação / Ciência (Lateral Esquerda) -->
      <g transform="translate(14, 168) rotate(-15) scale(2.0)">
        <path d="M9 18h6M10 22h4M9 14c-0.2-1-0.7-1.7-1.5-2.5C6.8 10.6 6 9.4 6 8c0-3.313 2.686-6 6-6s6 2.686 6 6c0 1.4-0.8 2.6-1.5 3.5-0.8 0.8-1.3 1.5-1.5 2.5" />
      </g>
      <!-- 5. Engrenagem da Tecnologia Médica (Lateral Direita) -->
      <g transform="translate(348, 168) scale(2.0)">
        <circle cx="12" cy="12" r="3.2" />
        <circle cx="12" cy="12" r="6.8" />
        <path d="M12 2v3.2M12 18.8v3.2M2 12h3.2M18.8 12h3.2M4.93 4.93l2.26 2.26M16.81 16.81l2.26 2.26M4.93 19.07l2.26-2.26M16.81 7.19l2.26-2.26" />
      </g>
      <!-- 6. DNA (Base Esquerda) -->
      <g transform="translate(24, 475) rotate(-35) scale(2.5)">
        <path d="M2 15c6.667-6 13.333 0 20-6" />
        <path d="M9 22c1.798-1.998 2.518-3.995 2.807-5.993" />
        <path d="M15 2c-1.798 1.998-2.518 3.995-2.807 5.993" />
        <path d="m17 6-2.891-2.891M7 18l2.891 2.891M10 16l1.5 1.5M14 8l-1.5-1.5M16.5 10.5l1 1M6.5 12.5l1 1M20 9l.891.891M3.109 14.109l.891.891" />
      </g>
      <!-- 7. Microscópio (Base Direita) -->
      <g transform="translate(328, 465) rotate(15) scale(2.5)">
        <path d="M6 18h8M3 22h18M14 22c3.86 0 7-3.14 7-7c0-3.86-3.14-7-7-7h-1M9 14h2M7 10V6h6v4c0 1.1-0.9 2-2 2H9c-1.1 0-2-0.9-2-2ZM12 6V2M9 2h6" />
      </g>
    </g>
    """

def format_front_statement_svg(statement):
    """
    Formata o texto da pergunta/afirmação para o SVG de forma dinâmica:
    Garante que textos curtos fiquem grandes e destacados, e textos longos
    (como os de 120 caracteres) fiquem em tamanho adequado e NUNCA sobreponham
    a tag de categoria ou a linha divisória inferior.
    """
    clean_stmt = statement.strip().replace('&', '&amp;')
    full_text = f'“{clean_stmt}”'
    text_len = len(statement.strip())
    
    if text_len <= 52:
        font_size = 20.0
        line_height = 28.0
        max_chars = 26
    elif text_len <= 80:
        font_size = 17.5
        line_height = 24.0
        max_chars = 32
    elif text_len <= 105:
        font_size = 15.0
        line_height = 21.0
        max_chars = 38
    else:
        font_size = 13.5
        line_height = 18.5
        max_chars = 44

    words = full_text.split()
    lines = []
    cur_line = []
    cur_len = 0
    for w in words:
        if cur_len + len(w) + (1 if cur_line else 0) <= max_chars:
            cur_line.append(w)
            cur_len += len(w) + (1 if cur_line else 0)
        else:
            if cur_line:
                lines.append(" ".join(cur_line))
            cur_line = [w]
            cur_len = len(w)
    if cur_line:
        lines.append(" ".join(cur_line))
        
    # Centro vertical do espaço útil da caixa:
    # A caixa vai de y=214 até y=468 (altura 254)
    # Tag no topo: y=228 até y=254
    # Divisória na base: y=420
    # Espaço útil: y=256 até y=418 -> Centro exato = 337
    center_y = 337.0
    total_h = (len(lines) - 1) * line_height
    start_y = center_y - total_h / 2.0
    
    svg_elements = ""
    for i, l in enumerate(lines):
        y_pos = start_y + i * line_height
        svg_elements += f'    <text x="200" y="{y_pos:.1f}" font-family="\'Outfit\', system-ui, -apple-system, sans-serif" font-size="{font_size:.1f}" font-weight="900" font-style="italic" fill="#1a0210" text-anchor="middle">{l}</text>\n'
        
    return svg_elements

def generate_svg_frente(card):
    """
    Gera o SVG da FRENTE com:
    - Fundo vinho profundo facetado e acentos geométricos nos 4 cantos
    - 7 símbolos de ciência em traço rosa translúcido
    - Selo Hero "FATO ou FAKE?" (+4.5°) com bordas justas e pílula "ou" sem sobrepor palavras
    - CAMPO DA PERGUNTA / AFIRMAÇÃO centralizado em caixa branca (sem número dentro do box)
    - Enumeração no canto superior direito no amarelo característico
    - Rodapé: "CIÊNCIA OU MITO?" e assinatura oficial USP
    """
    num_str = f"{card['num']:02d}"
    cat_str = card['category'].upper().replace('&', '&amp;')
    text_elements = format_front_statement_svg(card["statement"])
    science_symbols_svg = get_svg_science_symbols_markup()

    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 600" width="400" height="600">
  <defs>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Barlow:ital,wght@0,400;0,600;0,700;1,400;1,600&amp;family=Outfit:wght@400;600;700;800;900&amp;display=swap');
      text, p, div {{
        font-family: 'Outfit', system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      }}
    </style>
    <filter id="cardShadow" x="-10%" y="-10%" width="125%" height="125%">
      <feDropShadow dx="0" dy="6" stdDeviation="8" flood-color="#000000" flood-opacity="0.45"/>
    </filter>
    <clipPath id="cardClip">
      <rect width="400" height="600" rx="36"/>
    </clipPath>
  </defs>

  <g clip-path="url(#cardClip)">
    <!-- Fundo Base Vinho Profundo -->
    <rect width="400" height="600" fill="#2d031c"/>

    <!-- Facetas Poligonais em Tons de Vinho/Ameixa -->
    <polygon points="0,0 285,0 160,165 0,110" fill="#3c0627"/>
    <polygon points="285,0 400,115 250,225 160,165" fill="#4d0933"/>
    <polygon points="0,110 160,165 75,310 0,270" fill="#350421"/>
    <polygon points="160,165 250,225 235,370 75,310" fill="#46072e"/>
    <polygon points="250,225 400,115 400,340 315,385" fill="#31031e"/>
    <polygon points="400,340 400,475 310,600 235,465 315,385" fill="#520c36"/>
    <polygon points="0,270 75,310 235,465 115,600 0,470" fill="#380523"/>
    <polygon points="235,465 115,600 310,600" fill="#250217"/>

    <!-- Acentos Geométricos Exatos dos Cantos -->
    <polygon points="0,110 110,0 72,0 0,72" fill="#e8ff3b"/>
    <path d="M 285 0 L 400 0 L 400 115 Z" fill="#ff007f"/>
    <polygon points="0,470 0,600 115,600" fill="#a2ff92"/>
    <polygon points="310,600 400,600 400,475" fill="#e8ff3b"/>

    <!-- ENUMERAÇÃO DO CARD NO CANTO SUPERIOR DIREITO COM O AMARELO CARACTERÍSTICO -->
    <text x="358" y="46" font-family="'Outfit', system-ui, -apple-system, sans-serif" font-size="28" font-weight="900" fill="#e8ff3b" text-anchor="middle">#{num_str}</text>

    {science_symbols_svg}

    <!-- BADGE HERO FATO ou FAKE? (BORDAS JUSTAS, PÍLULA 'ou' REDUZIDA E COM FONTE +2, INCLINADO +4.5°) -->
    <g transform="rotate(4.5, 200, 118)">
      <!-- Traço decorativo Verde Menta contornando o topo da pílula branca -->
      <path d="M 94 96 C 94 66 118 58 148 58 L 256 58" fill="none" stroke="#a2ff92" stroke-width="4" stroke-linecap="round"/>

      <!-- Pílula Branca Superior: FATO (borda justa) -->
      <rect x="98" y="58" width="204" height="60" rx="30" fill="#ffffff" filter="url(#cardShadow)"/>
      <text x="200" y="103" font-family="'Outfit', system-ui, -apple-system, sans-serif" font-size="52" font-weight="900" fill="#350424" text-anchor="middle" letter-spacing="1.5">FATO</text>

      <!-- Traço decorativo Rosa Choque contornando a base da pílula rosa -->
      <path d="M 144 190 L 258 190 C 292 190 312 178 312 148" fill="none" stroke="#ff007f" stroke-width="4" stroke-linecap="round"/>

      <!-- Pílula Rosa Choque Inferior: FAKE? (borda justa, posicionada sem sobreposição da 'ou') -->
      <rect x="84" y="125" width="232" height="62" rx="31" fill="#ff007f" filter="url(#cardShadow)"/>
      <text x="200" y="172" font-family="'Outfit', system-ui, -apple-system, sans-serif" font-size="52" font-weight="900" fill="#ffffff" text-anchor="middle" letter-spacing="1.5">FAKE?</text>

      <!-- Pílula Escura Central 'ou': REDUZIDA e com FONTE AUMENTADA EM 2 (17px), sem sobrepor 'FAKE' -->
      <rect x="178" y="105" width="44" height="22" rx="11" fill="#350424" stroke="#ffffff" stroke-width="2.5"/>
      <text x="200" y="121.5" font-family="'Outfit', system-ui, -apple-system, sans-serif" font-size="17" font-weight="900" fill="#ffffff" text-anchor="middle">ou</text>
    </g>

    <!-- CAMPO DA PERGUNTA / AFIRMAÇÃO NA PARTE DA FRENTE -->
    <rect x="22" y="214" width="356" height="254" rx="22" fill="#ffffff" filter="url(#cardShadow)"/>
    <rect x="22" y="214" width="7" height="254" rx="3.5" fill="#ff007f"/>

    <!-- Tag de Categoria no topo da caixa (SEM A NUMERAÇÃO DO CARD) -->
    <rect x="75" y="228" width="250" height="26" rx="13" fill="#fceaf3"/>
    <text x="200" y="245.5" font-family="'Outfit', system-ui, -apple-system, sans-serif" font-size="11.5" font-weight="800" fill="#d8005b" text-anchor="middle" letter-spacing="0.5">
      {card['emoji']} {cat_str}
    </text>

    <!-- Texto da Pergunta entre aspas perfeitamente centralizado e com tamanho adaptativo -->
{text_elements}
    <!-- Divisória sutil e Chamada para Ação -->
    <line x1="45" y1="420" x2="355" y2="420" stroke="#f2d5e5" stroke-width="1.2"/>
    <text x="200" y="445" font-family="'Outfit', system-ui, -apple-system, sans-serif" font-size="12" font-weight="700" fill="#741d4f" text-anchor="middle">
      👉 O que você acha? Vire o card para descobrir!
    </text>

    <!-- Rodapé: CIÊNCIA OU MITO? -->
    <text x="200" y="510" font-family="'Outfit', system-ui, -apple-system, sans-serif" font-size="24" font-weight="900" fill="#e8ff3b" text-anchor="middle" letter-spacing="3">CIÊNCIA OU MITO?</text>
    <text x="200" y="535" font-family="'Outfit', system-ui, -apple-system, sans-serif" font-size="10.5" font-weight="800" fill="#ffc2eb" text-anchor="middle" letter-spacing="1">FEIRA USP E AS PROFISSÕES • FÍSICA MÉDICA</text>
  </g>
</svg>"""

def format_verso_headline_svg(headline, stroke_color, has_photo=False):
    words = headline.split()
    lines = []
    cur = []
    cur_l = 0
    max_chars = 40 if has_photo else 36
    for w in words:
        if cur_l + len(w) + (1 if cur else 0) <= max_chars:
            cur.append(w)
            cur_l += len(w) + (1 if cur else 0)
        else:
            if cur: lines.append(" ".join(cur))
            cur = [w]
            cur_l = len(w)
    if cur: lines.append(" ".join(cur))
    
    svg = ""
    lines = lines[:2]
    if has_photo:
        font_size = 11.5
        y_starts = [102.5] if len(lines) == 1 else [95.0, 109.5]
    else:
        font_size = 13.8
        y_starts = [120.0] if len(lines) == 1 else [112.0, 128.5]
        
    for i, l in enumerate(lines):
        y = y_starts[i]
        esc_l = l.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
        svg += f'    <text x="200" y="{y:.1f}" font-family="\'Outfit\', system-ui, -apple-system, sans-serif" font-size="{font_size}" font-style="italic" font-weight="900" fill="{stroke_color}" text-anchor="middle" letter-spacing="0.3">{esc_l}</text>\n'
    return svg

def format_verso_explanation_svg(text, max_chars=50, start_y=127.0, line_height=14.0, font_size=10.5, text_x=20, max_width=358.0):
    tokens = re.findall(r"(<[^>]+>|[^\s<]+|\s+)", text)
    lines = []
    cur_tokens = []
    font_name = 'Outfit-SemiBold' if HAS_OUTFIT else 'Helvetica-Bold'
    
    for t in tokens:
        if t.startswith("<"):
            cur_tokens.append(t)
            continue
        if t.isspace():
            if cur_tokens and cur_tokens[-1] != " ":
                cur_tokens.append(" ")
            continue
        
        # Trial width using pdfmetrics if available
        trial_words = []
        for tok in cur_tokens + [t]:
            if not tok.startswith("<") and tok != " ":
                trial_words.append(tok)
            elif tok == " ":
                trial_words.append(" ")
        trial_str = "".join(trial_words)
        
        if HAS_OUTFIT:
            w = pdfmetrics.stringWidth(trial_str, font_name, font_size)
            fits = (w <= max_width)
        else:
            fits = (len(trial_str) <= max_chars)
            
        if fits:
            cur_tokens.append(t)
        else:
            if cur_tokens:
                lines.append(cur_tokens)
            cur_tokens = [t]
            
    if cur_tokens:
        lines.append(cur_tokens)
        
    svg_out = ""
    is_bold = False
    is_italic = False
    
    for i, l_tokens in enumerate(lines):
        y_pos = start_y + i * line_height
        line_content = ""
        for t in l_tokens:
            if t == "<b>":
                is_bold = True
            elif t == "</b>":
                is_bold = False
            elif t == "<i>":
                is_italic = True
            elif t == "</i>":
                is_italic = False
            else:
                esc_t = t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
                if is_bold and is_italic:
                    line_content += f'<tspan font-weight="900" font-style="italic" fill="#2d031c">{esc_t}</tspan>'
                elif is_bold:
                    line_content += f'<tspan font-weight="900" fill="#2d031c">{esc_t}</tspan>'
                elif is_italic:
                    line_content += f'<tspan font-style="italic">{esc_t}</tspan>'
                else:
                    line_content += esc_t
        svg_out += f'    <text x="{text_x}" y="{y_pos:.1f}" font-family="\'Outfit\', system-ui, -apple-system, sans-serif" font-size="{font_size}" font-weight="500" fill="#1f0013">{line_content.strip()}</text>\n'
        
    return svg_out

def generate_svg_verso(card):
    """
    Gera o SVG do VERSO com:
    - Topo: Card # e Categoria
    - Selo resultado (FATO! ou FAKE!)
    - Headline explicativa em destaque (sem a pergunta repetida)
    - Para FATO: texto didático + foto científica/histórica com legenda + caixa USP compacta
    - Para FAKE: texto didático centralizado em destaque + caixa USP
    - Rodapé institucional
    """
    num_str = f"{card['num']:02d}"
    is_fato = (card["type"] == "FATO")
    has_photo = is_fato and (card["num"] in B64_PHOTOS)
    
    badge_bg = "#bdf7c9" if is_fato else "#ffb3d9"
    badge_stroke = "#1f6133" if is_fato else "#d8005b"
    badge_text_color = "#0a5222" if is_fato else "#3e072b"
    verdict_str = "FATO!" if is_fato else "FAKE!"
    
    cat_str_verso = card['category'].upper().replace('&', '&amp;')
    
    hd_svg = format_verso_headline_svg(card["headline"], badge_stroke, has_photo=has_photo)
    
    if has_photo:
        b64_photo = B64_PHOTOS[card["num"]]
        caption_txt = card.get("photo_caption", "").replace("&", "&amp;")
        caption_w = min(340, len(card.get("photo_caption", "")) * 6.5 + 20)
        exp_svg = format_verso_explanation_svg(card["explanation"], max_chars=50, start_y=127.0, line_height=14.0, font_size=10.5, text_x=20, max_width=358.0)
        
        return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 600" width="400" height="600">
  <defs>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800;900&amp;display=swap');
      text {{
        font-family: 'Outfit', system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      }}
    </style>
    <filter id="cardShadow" x="-10%" y="-10%" width="125%" height="125%">
      <feDropShadow dx="0" dy="6" stdDeviation="8" flood-color="#000000" flood-opacity="0.25"/>
    </filter>
    <filter id="photoShadow{num_str}" x="-5%" y="-5%" width="110%" height="115%">
      <feDropShadow dx="0" dy="3" stdDeviation="4" flood-color="#000000" flood-opacity="0.18"/>
    </filter>
    <clipPath id="cardClip">
      <rect width="400" height="600" rx="36"/>
    </clipPath>
    <clipPath id="photoClip{num_str}">
      <rect x="20" y="252" width="360" height="172" rx="12"/>
    </clipPath>
  </defs>

  <g clip-path="url(#cardClip)">
    <!-- Moldura Externa Vinho -->
    <rect width="400" height="600" fill="#3e072b"/>

    <!-- Acentos Geométricos nos Cantos -->
    <path d="M 0 0 L 75 0 L 0 75 Z" fill="#ff007f"/>
    <path d="M 325 0 L 400 0 L 400 75 Z" fill="#a2ff92"/>
    <path d="M 0 525 L 0 600 L 75 600 Z" fill="#a2ff92"/>
    <path d="M 325 600 L 400 600 L 400 525 Z" fill="#e8ff3b"/>

    <!-- Corpo Central Branco da Resposta -->
    <rect x="14" y="14" width="372" height="572" rx="26" fill="#ffffff" filter="url(#cardShadow)"/>

    <!-- Topo: Número e Categoria -->
    <g transform="translate(200, 32)">
      <rect x="-115" y="-12" width="230" height="22" rx="11" fill="#f8edf4"/>
      <text x="0" y="3.5" font-family="'Outfit', sans-serif" font-size="11" font-weight="800" fill="#741d4f" text-anchor="middle" letter-spacing="0.5">
        CARD #{num_str} • {card['emoji']} {cat_str_verso}
      </text>
    </g>

    <!-- SELO PÍLULA RESULTADO -->
    <g transform="translate(200, 64)">
      <rect x="-85" y="-16" width="170" height="32" rx="16" fill="{badge_bg}" stroke="{badge_stroke}" stroke-width="2.5"/>
      <text x="0" y="6.5" font-family="'Outfit', sans-serif" font-size="21" font-weight="900" fill="{badge_text_color}" text-anchor="middle" letter-spacing="1">{verdict_str}</text>
    </g>

    <!-- HEADLINE EXPLICATIVA VETORIAL -->
{hd_svg}
    <!-- TEXTO EXPLICATIVO DIDÁTICO -->
{exp_svg}
    <!-- FOTO REAL/DIDÁTICA DO FATO -->
    <g filter="url(#photoShadow{num_str})">
      <rect x="19" y="251" width="362" height="174" rx="13" fill="#ffffff" stroke="#dfc2d3" stroke-width="1.5"/>
      <image href="data:image/jpeg;base64,{b64_photo}" x="20" y="252" width="360" height="172" preserveAspectRatio="xMidYMid slice" clip-path="url(#photoClip{num_str})"/>
      <!-- Pill de Legenda Educativa -->
      <g transform="translate(26, 414)">
        <rect x="0" y="-14" width="{caption_w}" height="18" rx="9" fill="rgba(15, 0, 10, 0.78)"/>
        <text x="8" y="-1.5" font-family="'Outfit', sans-serif" font-size="8.8" font-weight="700" fill="#ffffff">{caption_txt}</text>
      </g>
    </g>

    <!-- SEÇÃO FÍSICA MÉDICA USP COMPACTA ELEGANTE -->
    <g transform="translate(16, 436)">
      <rect width="368" height="122" rx="14" fill="#f8edf4" stroke="#e8ccd9" stroke-width="1.2"/>
      
      <text x="184" y="16" font-family="'Outfit', sans-serif" font-size="9.8" font-weight="800" fill="#741d4f" letter-spacing="0.8" text-anchor="middle">ESTUDE FÍSICA MÉDICA NA UNIVERSIDADE DE SÃO PAULO:</text>
      <text x="184" y="30" font-family="'Outfit', sans-serif" font-size="12.5" font-weight="900" fill="#3e072b" text-anchor="middle">Bacharelado Interunidades • Campus Capital</text>

      <!-- FIGURAS IFUSP & FMUSP -->
      <g transform="translate(14, 38)">
        <g transform="translate(0, 0)">
          <rect width="164" height="72" rx="8" fill="#ffffff" stroke="#c0dbe8" stroke-width="1.0"/>
          <image href="data:image/png;base64,{B64_IFUSP}" x="6" y="3" width="152" height="66" preserveAspectRatio="xMidYMid meet"/>
        </g>
        <g transform="translate(176, 0)">
          <rect width="164" height="72" rx="8" fill="#ffffff" stroke="#bfe3cf" stroke-width="1.0"/>
          <image href="data:image/png;base64,{B64_FMUSP}" x="6" y="3" width="152" height="66" preserveAspectRatio="xMidYMid meet"/>
        </g>
      </g>
    </g>

    <!-- Micro Rodapé -->
    <g transform="translate(200, 574)">
      <text x="0" y="0" font-family="'Outfit', sans-serif" font-size="9.5" font-weight="800" fill="#741d4f" text-anchor="middle" letter-spacing="1">FEIRA USP E AS PROFISSÕES • IFUSP &amp; FMUSP</text>
    </g>
  </g>
</svg>"""
    else:
        # Layout para cards FAKE (espaço total de texto)
        exp_svg = format_verso_explanation_svg(card["explanation"], max_chars=43, start_y=170.0, line_height=20.5, font_size=13.2, text_x=22, max_width=356.0)
        return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 600" width="400" height="600">
  <defs>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700;800;900&amp;display=swap');
      text {{
        font-family: 'Outfit', system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      }}
    </style>
    <filter id="cardShadow" x="-10%" y="-10%" width="125%" height="125%">
      <feDropShadow dx="0" dy="6" stdDeviation="8" flood-color="#000000" flood-opacity="0.3"/>
    </filter>
    <clipPath id="cardClip">
      <rect width="400" height="600" rx="36"/>
    </clipPath>
  </defs>

  <g clip-path="url(#cardClip)">
    <!-- Moldura Externa Vinho -->
    <rect width="400" height="600" fill="#3e072b"/>

    <!-- Acentos Geométricos nos Cantos -->
    <path d="M 0 0 L 75 0 L 0 75 Z" fill="#ff007f"/>
    <path d="M 325 0 L 400 0 L 400 75 Z" fill="#a2ff92"/>
    <path d="M 0 525 L 0 600 L 75 600 Z" fill="#a2ff92"/>
    <path d="M 325 600 L 400 600 L 400 525 Z" fill="#e8ff3b"/>

    <!-- Corpo Central Branco da Resposta -->
    <rect x="14" y="14" width="372" height="572" rx="26" fill="#ffffff" filter="url(#cardShadow)"/>

    <!-- Topo: Número e Categoria -->
    <g transform="translate(200, 34)">
      <rect x="-115" y="-12" width="230" height="22" rx="11" fill="#f8edf4"/>
      <text x="0" y="3.5" font-family="'Outfit', sans-serif" font-size="11.5" font-weight="800" fill="#741d4f" text-anchor="middle" letter-spacing="0.5">
        CARD #{num_str} • {card['emoji']} {cat_str_verso}
      </text>
    </g>

    <!-- SELO PÍLULA RESULTADO -->
    <g transform="translate(200, 68)">
      <rect x="-90" y="-18" width="180" height="36" rx="18" fill="{badge_bg}" stroke="{badge_stroke}" stroke-width="3"/>
      <text x="0" y="7.5" font-family="'Outfit', sans-serif" font-size="24" font-weight="900" fill="{badge_text_color}" text-anchor="middle" letter-spacing="1">{verdict_str}</text>
    </g>

    <!-- HEADLINE EXPLICATIVA VETORIAL PURA (SEM PERGUNTA REPETIDA) -->
{hd_svg}
    <!-- TEXTO EXPLICATIVO VETORIAL PURO COM DESTAQUES EM NEGRITO -->
{exp_svg}
    <!-- SEÇÃO FÍSICA MÉDICA USP COMPACTA (INTERUNIDADES IFUSP & FMUSP) -->
    <g transform="translate(16, 420)">
      <!-- Container do Curso -->
      <rect width="368" height="136" rx="14" fill="#f8edf4" stroke="#e8ccd9" stroke-width="1.2"/>
      
      <!-- Cabeçalho Institucional -->
      <text x="184" y="18" font-family="'Outfit', sans-serif" font-size="10.5" font-weight="800" fill="#741d4f" letter-spacing="0.8" text-anchor="middle">ESTUDE FÍSICA MÉDICA NA UNIVERSIDADE DE SÃO PAULO:</text>
      <text x="184" y="34" font-family="'Outfit', sans-serif" font-size="14" font-weight="900" fill="#3e072b" text-anchor="middle">Bacharelado Interunidades • Campus Capital</text>

      <!-- FIGURAS EXATAS COLADAS (LADO A LADO) -->
      <g transform="translate(14, 44)">
        <!-- CARD COM A FIGURA EXATA DO IFUSP -->
        <g transform="translate(0, 0)">
          <rect width="164" height="80" rx="8" fill="#ffffff" stroke="#c0dbe8" stroke-width="1.0"/>
          <image href="data:image/png;base64,{B64_IFUSP}" x="6" y="4" width="152" height="72" preserveAspectRatio="xMidYMid meet"/>
        </g>

        <!-- CARD COM A FIGURA EXATA DA FMUSP -->
        <g transform="translate(176, 0)">
          <rect width="164" height="80" rx="8" fill="#ffffff" stroke="#bfe3cf" stroke-width="1.0"/>
          <image href="data:image/png;base64,{B64_FMUSP}" x="6" y="4" width="152" height="72" preserveAspectRatio="xMidYMid meet"/>
        </g>
      </g>
    </g>

    <!-- Micro Rodapé -->
    <g transform="translate(200, 574)">
      <text x="0" y="0" font-family="'Outfit', sans-serif" font-size="9.5" font-weight="800" fill="#741d4f" text-anchor="middle" letter-spacing="1">FEIRA USP E AS PROFISSÕES • IFUSP &amp; FMUSP</text>
    </g>
  </g>
</svg>"""

def draw_svg_paths_on_canvas(c, paths_list, x, y, size_mm, stroke_color='#ff007f', line_width=0.32*mm, rotation_deg=0, alpha=0.22):
    """
    Desenha os ícones profissionais da biblioteca Lucide com precisão vetorial no canvas do ReportLab.
    """
    c.saveState()
    if rotation_deg != 0:
        c.translate(x + size_mm / 2.0, y + size_mm / 2.0)
        c.rotate(rotation_deg)
        c.translate(-(x + size_mm / 2.0), -(y + size_mm / 2.0))
    c.setStrokeColor(HexColor(stroke_color))
    c.setFillColor(HexColor(stroke_color))
    try:
        c.setStrokeAlpha(alpha)
        c.setFillAlpha(alpha)
    except Exception:
        pass
    c.setLineWidth(line_width)
    c.setLineCap(1)  # Round cap
    c.setLineJoin(1) # Round join
    
    scale = size_mm / 24.0
    
    for item in paths_list:
        if item.get('type') == 'circle':
            cx = x + item['cx'] * scale
            cy = y + (24 - item['cy']) * scale
            r = item['r'] * scale
            fill = item.get('fill', 0)
            c.circle(cx, cy, r, fill=fill, stroke=1 if not fill else 0)
        elif item.get('type') == 'path':
            d = item['d']
            tokens = re.findall(r'([a-zA-Z]|[-+]?(?:\d*\.\d+|\d+)(?:[eE][-+]?\d+)?)', d)
            if not tokens:
                continue
                
            p = c.beginPath()
            curr_cmd = None
            i = 0
            cur_x, cur_y = 0.0, 0.0
            start_x, start_y = 0.0, 0.0
            
            while i < len(tokens):
                t = tokens[i]
                if t.isalpha():
                    curr_cmd = t
                    i += 1
                
                if curr_cmd in ('M', 'm'):
                    nx, ny = float(tokens[i]), float(tokens[i+1])
                    i += 2
                    if curr_cmd == 'm':
                        cur_x += nx
                        cur_y += ny
                    else:
                        cur_x, cur_y = nx, ny
                    start_x, start_y = cur_x, cur_y
                    p.moveTo(x + cur_x * scale, y + (24 - cur_y) * scale)
                    curr_cmd = 'l' if curr_cmd == 'm' else 'L'
                elif curr_cmd in ('L', 'l'):
                    nx, ny = float(tokens[i]), float(tokens[i+1])
                    i += 2
                    if curr_cmd == 'l':
                        cur_x += nx
                        cur_y += ny
                    else:
                        cur_x, cur_y = nx, ny
                    p.lineTo(x + cur_x * scale, y + (24 - cur_y) * scale)
                elif curr_cmd in ('H', 'h'):
                    nx = float(tokens[i])
                    i += 1
                    cur_x = cur_x + nx if curr_cmd == 'h' else nx
                    p.lineTo(x + cur_x * scale, y + (24 - cur_y) * scale)
                elif curr_cmd in ('V', 'v'):
                    ny = float(tokens[i])
                    i += 1
                    cur_y = cur_y + ny if curr_cmd == 'v' else ny
                    p.lineTo(x + cur_x * scale, y + (24 - cur_y) * scale)
                elif curr_cmd in ('C', 'c'):
                    x1, y1 = float(tokens[i]), float(tokens[i+1])
                    x2, y2 = float(tokens[i+2]), float(tokens[i+3])
                    ex, ey = float(tokens[i+4]), float(tokens[i+5])
                    i += 6
                    if curr_cmd == 'c':
                        p.curveTo(x + (cur_x + x1)*scale, y + (24 - (cur_y + y1))*scale,
                                  x + (cur_x + x2)*scale, y + (24 - (cur_y + y2))*scale,
                                  x + (cur_x + ex)*scale, y + (24 - (cur_y + ey))*scale)
                        cur_x += ex
                        cur_y += ey
                    else:
                        p.curveTo(x + x1*scale, y + (24 - y1)*scale,
                                  x + x2*scale, y + (24 - y2)*scale,
                                  x + ex*scale, y + (24 - ey)*scale)
                        cur_x, cur_y = ex, ey
                elif curr_cmd in ('Z', 'z'):
                    p.close()
                    cur_x, cur_y = start_x, start_y
                else:
                    i += 1
            c.drawPath(p, fill=0, stroke=1)
            
    c.restoreState()

def draw_front_card_exact(c, ox, oy, card):
    """
    Desenha a FRENTE do card no ReportLab com:
    - Fundo vinho facetado e acentos geométricos nos 4 cantos
    - Símbolos de ciência translúcidos
    - Badge Hero FATO ou FAKE? (+4.5°) com bordas justas e detalhes contornados
    - CAMPO DA PERGUNTA / AFIRMAÇÃO centralizado em caixa branca de destaque
    - Rodapé: CIÊNCIA OU MITO? e assinatura oficial USP
    """
    num_str = f"{card['num']:02d}"
    
    # Fundo Base Vinho
    c.setFillColor(HexColor("#2d031c"))
    c.rect(ox, oy, 80*mm, 120*mm, fill=1, stroke=0)
    
    # 1. Topo Esquerdo Faixa Amarela
    c.setFillColor(HexColor("#e8ff3b"))
    p = c.beginPath()
    for sx, sy in [(0,110), (110,0), (72,0), (0,72)]:
        px = ox + sx * 0.2 * mm
        py = oy + (600 - sy) * 0.2 * mm
        if sx == 0 and sy == 110: p.moveTo(px, py)
        else: p.lineTo(px, py)
    p.close()
    c.drawPath(p, fill=1, stroke=0)
    
    # 2. Topo Direito Rosa Choque
    c.setFillColor(HexColor("#ff007f"))
    p = c.beginPath()
    for sx, sy in [(285,0), (400,0), (400,115)]:
        px = ox + sx * 0.2 * mm
        py = oy + (600 - sy) * 0.2 * mm
        if sx == 285 and sy == 0: p.moveTo(px, py)
        else: p.lineTo(px, py)
    p.close()
    c.drawPath(p, fill=1, stroke=0)
    
    # 3. Base Esquerda Verde Menta
    c.setFillColor(HexColor("#a2ff92"))
    p = c.beginPath()
    for sx, sy in [(0,470), (0,600), (115,600)]:
        px = ox + sx * 0.2 * mm
        py = oy + (600 - sy) * 0.2 * mm
        if sx == 0 and sy == 470: p.moveTo(px, py)
        else: p.lineTo(px, py)
    p.close()
    c.drawPath(p, fill=1, stroke=0)
    
    # 4. Base Direita Amarelo
    c.setFillColor(HexColor("#e8ff3b"))
    p = c.beginPath()
    for sx, sy in [(310,600), (400,600), (400,475)]:
        px = ox + sx * 0.2 * mm
        py = oy + (600 - sy) * 0.2 * mm
        if sx == 310 and sy == 600: p.moveTo(px, py)
        else: p.lineTo(px, py)
    p.close()
    c.drawPath(p, fill=1, stroke=0)
    
    font_black = "Outfit-Black" if HAS_OUTFIT else "Helvetica-Bold"
    font_bold = "Outfit-Bold" if HAS_OUTFIT else "Helvetica-Bold"

    # ENUMERAÇÃO DO CARD NO CANTO SUPERIOR DIREITO NO AMARELO CARACTERÍSTICO
    c.setFillColor(HexColor(COLOR_YELLOW))
    c.setFont(font_black, 15)
    c.drawCentredString(ox + 71.5*mm, oy + 111.0*mm, f"#{num_str}")
    
    # 7 Símbolos Profissionais de Ciência Lucide
    draw_svg_paths_on_canvas(c, LUCIDE_DNA, ox + 8*mm, oy + 98*mm, 15*mm, stroke_color='#ff007f', line_width=0.35*mm, rotation_deg=-35, alpha=0.22)
    draw_svg_paths_on_canvas(c, LUCIDE_FOOTBALL, ox + 33*mm, oy + 107*mm, 13*mm, stroke_color='#ff007f', line_width=0.35*mm, rotation_deg=15, alpha=0.22)
    draw_svg_paths_on_canvas(c, LUCIDE_ATOM, ox + 55*mm, oy + 97*mm, 15*mm, stroke_color='#ff007f', line_width=0.35*mm, rotation_deg=0, alpha=0.22)
    draw_svg_paths_on_canvas(c, LUCIDE_LIGHTBULB, ox + 3*mm, oy + 76*mm, 13*mm, stroke_color='#ff007f', line_width=0.35*mm, rotation_deg=-15, alpha=0.22)
    draw_svg_paths_on_canvas(c, LUCIDE_GEAR, ox + 63*mm, oy + 76*mm, 13*mm, stroke_color='#ff007f', line_width=0.35*mm, rotation_deg=10, alpha=0.22)
    draw_svg_paths_on_canvas(c, LUCIDE_DNA, ox + 5*mm, oy + 18*mm, 15*mm, stroke_color='#ff007f', line_width=0.35*mm, rotation_deg=-35, alpha=0.22)
    draw_svg_paths_on_canvas(c, LUCIDE_MICROSCOPE, ox + 60*mm, oy + 20*mm, 15*mm, stroke_color='#ff007f', line_width=0.35*mm, rotation_deg=15, alpha=0.22)
    
    # BADGE HERO FATO ou FAKE? (+4.5°)
    c.saveState()
    c.translate(ox + 40*mm, oy + 96.4*mm)
    c.rotate(4.5)
    c.translate(-(ox + 40*mm), -(oy + 96.4*mm))
    
    # Contorno Verde Menta
    c.setStrokeColor(HexColor("#a2ff92"))
    c.setLineWidth(0.8*mm)
    c.setLineCap(1)
    p = c.beginPath()
    p.moveTo(ox + 18.8*mm, oy + 99.4*mm)
    p.curveTo(ox + 18.8*mm, oy + 105.4*mm, ox + 23.6*mm, oy + 107.0*mm, ox + 51.2*mm, oy + 107.0*mm)
    c.drawPath(p, fill=0, stroke=1)
    
    # Pílula Branca FATO (borda justa)
    c.setFillColor(HexColor("#ffffff"))
    c.roundRect(ox + 19.6*mm, oy + 96.5*mm, 40.8*mm, 12.0*mm, 6.0*mm, fill=1, stroke=0)
    c.setFillColor(HexColor("#350424"))
    c.setFont(font_black, 16.5)
    c.drawCentredString(ox + 40.0*mm, oy + 100.0*mm, "FATO")
    
    # Contorno Rosa Choque
    c.setStrokeColor(HexColor("#ff007f"))
    c.setLineWidth(0.8*mm)
    p = c.beginPath()
    p.moveTo(ox + 28.8*mm, oy + 79.8*mm)
    p.lineTo(ox + 51.6*mm, oy + 79.8*mm)
    p.curveTo(ox + 58.4*mm, oy + 79.8*mm, ox + 62.4*mm, oy + 82.2*mm, ox + 62.4*mm, oy + 88.2*mm)
    c.drawPath(p, fill=0, stroke=1)
    
    # Pílula Rosa FAKE? (borda justa, posicionada sem sobreposição)
    c.setFillColor(HexColor("#ff007f"))
    c.roundRect(ox + 16.8*mm, oy + 82.2*mm, 46.4*mm, 12.4*mm, 6.2*mm, fill=1, stroke=0)
    c.setFillColor(HexColor("#ffffff"))
    c.setFont(font_black, 16.5)
    c.drawCentredString(ox + 40.0*mm, oy + 85.8*mm, "FAKE?")
    
    # Pílula Escura 'ou': REDUZIDA e com FONTE +2 (8.8pt), sem cobrir o 'FAKE'
    c.setFillColor(HexColor("#350424"))
    c.setStrokeColor(HexColor("#ffffff"))
    c.setLineWidth(0.5*mm)
    c.roundRect(ox + 35.6*mm, oy + 92.4*mm, 8.8*mm, 4.4*mm, 2.2*mm, fill=1, stroke=1)
    c.setFillColor(HexColor("#ffffff"))
    c.setFont(font_black, 8.8)
    c.drawCentredString(ox + 40.0*mm, oy + 93.6*mm, "ou")
    
    c.restoreState()
    
    # CAMPO DA PERGUNTA / AFIRMAÇÃO NA FRENTE
    c.setFillColor(HexColor("#ffffff"))
    c.roundRect(ox + 4.4*mm, oy + 26.5*mm, 71.2*mm, 50.8*mm, 4.4*mm, fill=1, stroke=0)
    c.setFillColor(HexColor("#ff007f"))
    c.roundRect(ox + 4.4*mm, oy + 26.5*mm, 1.4*mm, 50.8*mm, 0.7*mm, fill=1, stroke=0)
    
    # Tag Categoria (SEM A NUMERAÇÃO DO CARD)
    tag_w = min(62.0*mm, len(card['category']) * 2.2*mm + 10.0*mm)
    c.setFillColor(HexColor("#fceaf3"))
    c.roundRect(ox + 40.0*mm - tag_w/2, oy + 71.0*mm, tag_w, 5.2*mm, 2.6*mm, fill=1, stroke=0)
    c.setFillColor(HexColor("#d8005b"))
    c.setFont(font_bold, 5.2)
    c.drawCentredString(ox + 40.0*mm, oy + 72.4*mm, card['category'].upper())
    
    # Texto da Pergunta com tamanho dinâmico para garantir encaixe perfeito sem sobreposições
    clean_stmt = card["statement"].strip()
    text_len = len(clean_stmt)
    if text_len <= 52:
        stmt_font_size = 11.8
        stmt_leading = 15.5
    elif text_len <= 80:
        stmt_font_size = 10.2
        stmt_leading = 13.5
    elif text_len <= 105:
        stmt_font_size = 9.0
        stmt_leading = 12.0
    else:
        stmt_font_size = 8.2
        stmt_leading = 10.8

    style_q = ParagraphStyle(
        'QuestionFront',
        fontName=font_black,
        fontSize=stmt_font_size,
        leading=stmt_leading,
        textColor=HexColor("#1a0210"),
        alignment=TA_CENTER
    )
    p_q = Paragraph(f'“{clean_stmt}”', style_q)
    p_w, p_h = p_q.wrap(62*mm, 33*mm)
    stmt_y = oy + 36.0*mm + (34.0*mm - p_h) / 2
    p_q.drawOn(c, ox + 9.0*mm, stmt_y)
    
    # Divisória e Call to Action
    c.setStrokeColor(HexColor("#f2d5e5"))
    c.setLineWidth(0.25*mm)
    c.line(ox + 9.0*mm, oy + 34.5*mm, ox + 71.0*mm, oy + 34.5*mm)
    
    c.setFillColor(HexColor("#741d4f"))
    c.setFont(font_bold, 4.8)
    c.drawCentredString(ox + 40.0*mm, oy + 30.0*mm, "👉 O que você acha? Vire o card para descobrir!")
    
    # Rodapé
    c.setFillColor(HexColor(COLOR_YELLOW))
    c.setFont(font_black, 9.6)
    c.drawCentredString(ox + 40.0*mm, oy + 17.5*mm, "CIÊNCIA OU MITO?")
    
    c.setFillColor(HexColor("#ffc2eb"))
    c.setFont(font_bold, 4.2)
    c.drawCentredString(ox + 40.0*mm, oy + 12.5*mm, "FEIRA USP E AS PROFISSÕES • FÍSICA MÉDICA")

def draw_verso_card_exact(c, ox, oy, card, style_exp):
    """
    Desenha o VERSO do card no ReportLab com:
    - Moldura vinho com acentos nos cantos
    - Corpo central branco com tag do card e categoria
    - Selo resultado (FATO! ou FAKE!)
    - Headline explicativa (subtítulo) destacada (sem a frase da frente repetida)
    - Explicação científica super didática, detalhada e justificada
    - Seção compacta Física Médica USP com as figuras originais do IFUSP e FMUSP
    - Rodapé institucional
    """
    c.saveState()
    
    # Fundo Moldura Vinho
    c.setFillColor(HexColor(COLOR_WINE))
    c.roundRect(ox, oy, 80*mm, 120*mm, 6*mm, fill=1, stroke=0)
    
    # Acentos dos cantos
    c.setFillColor(HexColor(COLOR_PINK))
    p = c.beginPath()
    p.moveTo(ox, oy + 108*mm); p.lineTo(ox + 12*mm, oy + 120*mm); p.lineTo(ox, oy + 120*mm); p.close()
    c.drawPath(p, fill=1, stroke=0)
    c.setFillColor(HexColor(COLOR_GREEN))
    p = c.beginPath()
    p.moveTo(ox + 68*mm, oy + 120*mm); p.lineTo(ox + 80*mm, oy + 120*mm); p.lineTo(ox + 80*mm, oy + 108*mm); p.close()
    c.drawPath(p, fill=1, stroke=0)
    p = c.beginPath()
    p.moveTo(ox, oy); p.lineTo(ox + 12*mm, oy); p.lineTo(ox, oy + 12*mm); p.close()
    c.drawPath(p, fill=1, stroke=0)
    c.setFillColor(HexColor(COLOR_YELLOW))
    p = c.beginPath()
    p.moveTo(ox + 68*mm, oy); p.lineTo(ox + 80*mm, oy); p.lineTo(ox + 80*mm, oy + 12*mm); p.close()
    c.drawPath(p, fill=1, stroke=0)
    
    # Corpo Branco
    c.setFillColor(HexColor(COLOR_WHITE))
    c.roundRect(ox + 2.8*mm, oy + 2.8*mm, 74.4*mm, 114.4*mm, 4.5*mm, fill=1, stroke=0)
    
    num_str = f"{card['num']:02d}"
    is_fato = (card["type"] == "FATO")
    
    # Topo: CARD # e Categoria
    font_bold = "Outfit-Bold" if HAS_OUTFIT else "Helvetica-Bold"
    font_extra = "Outfit-ExtraBold" if HAS_OUTFIT else "Helvetica-Bold"
    font_black = "Outfit-Black" if HAS_OUTFIT else "Helvetica-Bold"
    
    c.setFillColor(HexColor("#f8edf4"))
    c.roundRect(ox + 17*mm, oy + 108.5*mm, 46*mm, 4.2*mm, 2.1*mm, fill=1, stroke=0)
    c.setFillColor(HexColor("#741d4f"))
    c.setFont(font_bold, 5.4)
    c.drawCentredString(ox + 40*mm, oy + 109.6*mm, f"CARD #{num_str} • {card['category'].upper()}")
    
    # Selo Resultado Pílula
    c.setFillColor(HexColor("#bdf7c9" if is_fato else "#ffb3d9"))
    c.setStrokeColor(HexColor("#1f6133" if is_fato else "#d8005b"))
    c.setLineWidth(0.6*mm)
    c.roundRect(ox + 21*mm, oy + 99.2*mm, 38*mm, 7.8*mm, 3.9*mm, fill=1, stroke=1)
    
    c.setFillColor(HexColor("#0a5222" if is_fato else "#3e072b"))
    c.setFont(font_black, 11.5)
    c.drawCentredString(ox + 40*mm, oy + 101.4*mm, "FATO!" if is_fato else "FAKE!")
    
    has_photo = is_fato and ("photo_file" in card)
    photo_path = os.path.join(ASSETS_DIR, card.get("photo_file", "")) if has_photo else None
    
    if has_photo and os.path.exists(photo_path):
        # Headline Explicativa
        c.setFillColor(HexColor("#1f6133"))
        c.setFont(font_bold, 7.2)
        lines_hd = wrap_text(card["headline"], 30)
        y_hd = oy + 94.0*mm
        for l in lines_hd:
            c.drawCentredString(ox + 40*mm, y_hd, l)
            y_hd -= 3.2*mm
            
        # Explicação Científica
        style_exp_photo = ParagraphStyle(
            'ExplanationVersoPhoto',
            fontName=font_bold,
            fontSize=5.1,
            leading=6.7,
            textColor=HexColor("#1f0013"),
            alignment=TA_JUSTIFY
        )
        p_exp = Paragraph(card["explanation"], style_exp_photo)
        p_w, p_h = p_exp.wrap(68*mm, 35*mm)
        y_exp = max(oy + 66.5*mm, (y_hd - 1.2*mm) - p_h)
        p_exp.drawOn(c, ox + 6.0*mm, y_exp)
        
        # Foto com recorte arredondado
        c.saveState()
        p_clip = c.beginPath()
        p_clip.roundRect(ox + 5.0*mm, oy + 32.5*mm, 70.0*mm, 33.0*mm, 2.4*mm)
        c.clipPath(p_clip, stroke=0)
        c.drawImage(photo_path, ox + 5.0*mm, oy + 32.5*mm, width=70.0*mm, height=33.0*mm, preserveAspectRatio=True, anchor='c')
        c.restoreState()
        
        # Borda elegante da foto
        c.setStrokeColor(HexColor("#dfc2d3"))
        c.setLineWidth(0.25*mm)
        c.roundRect(ox + 5.0*mm, oy + 32.5*mm, 70.0*mm, 33.0*mm, 2.4*mm, fill=0, stroke=1)
        
        # Pill da Legenda Educativa
        caption_clean = card.get("photo_caption", "").replace("📷 ", "").strip()
        caption_w = min(66.0*mm, len(caption_clean) * 1.35*mm + 6.0*mm)
        c.setFillColor(HexColor("#0f000a"))
        try: c.setFillAlpha(0.78)
        except Exception: pass
        c.roundRect(ox + 6.2*mm, oy + 33.8*mm, caption_w, 3.8*mm, 1.9*mm, fill=1, stroke=0)
        try: c.setFillAlpha(1.0)
        except Exception: pass
        c.setFillColor(HexColor(COLOR_WHITE))
        c.setFont(font_bold, 3.8)
        c.drawString(ox + 8.0*mm, oy + 34.9*mm, f"📷 {caption_clean}")
        
        # SEÇÃO COMPACTA FÍSICA MÉDICA USP
        c.setFillColor(HexColor("#f8edf4"))
        c.setStrokeColor(HexColor("#e8ccd9"))
        c.setLineWidth(0.3*mm)
        c.roundRect(ox + 4.5*mm, oy + 6.8*mm, 71.0*mm, 24.5*mm, 2.2*mm, fill=1, stroke=1)
        
        c.setFillColor(HexColor(COLOR_WINE_LIGHT))
        c.setFont(font_extra, 4.5)
        c.drawCentredString(ox + 40*mm, oy + 28.5*mm, "ESTUDE FÍSICA MÉDICA NA UNIVERSIDADE DE SÃO PAULO:")
        
        c.setFillColor(HexColor(COLOR_WINE))
        c.setFont(font_black, 7.0)
        c.drawCentredString(ox + 40*mm, oy + 25.4*mm, "Bacharelado Interunidades • Campus Capital")
        
        # LOGOS
        c.setFillColor(HexColor(COLOR_WHITE))
        c.setStrokeColor(HexColor("#c0dbe8"))
        c.setLineWidth(0.25*mm)
        c.roundRect(ox + 6.2*mm, oy + 8.2*mm, 32.5*mm, 15.0*mm, 1.6*mm, fill=1, stroke=1)
        c.drawImage(IFUSP_IMG_PATH, ox + 7.2*mm, oy + 8.7*mm, width=30.5*mm, height=14.0*mm, preserveAspectRatio=True, mask='auto')
        
        c.setFillColor(HexColor(COLOR_WHITE))
        c.setStrokeColor(HexColor("#bfe3cf"))
        c.setLineWidth(0.25*mm)
        c.roundRect(ox + 41.3*mm, oy + 8.2*mm, 32.5*mm, 15.0*mm, 1.6*mm, fill=1, stroke=1)
        c.drawImage(FMUSP_IMG_PATH, ox + 42.3*mm, oy + 8.7*mm, width=30.5*mm, height=14.0*mm, preserveAspectRatio=True, mask='auto')
        
        # Micro Rodapé
        c.setFillColor(HexColor(COLOR_WINE_LIGHT))
        c.setFont(font_bold, 4.2)
        c.drawCentredString(ox + 40*mm, oy + 3.8*mm, "FEIRA USP E AS PROFISSÕES • IFUSP & FMUSP")
        
        c.restoreState()
    else:
        # Layout original para cards FAKE
        c.setFillColor(HexColor("#d8005b"))
        c.setFont(font_bold, 7.5)
        lines_hd = wrap_text(card["headline"], 30)
        y_hd = oy + 94.0*mm
        for l in lines_hd:
            c.drawCentredString(ox + 40*mm, y_hd, l)
            y_hd -= 3.3*mm
            
        p_exp = Paragraph(card["explanation"], style_exp)
        p_w, p_h = p_exp.wrap(68*mm, 52*mm)
        y_exp = max(oy + 34.5*mm, (y_hd - 2.0*mm) - p_h)
        p_exp.drawOn(c, ox + 6.0*mm, y_exp)
        
        c.setFillColor(HexColor("#f8edf4"))
        c.setStrokeColor(HexColor("#e8ccd9"))
        c.setLineWidth(0.3*mm)
        c.roundRect(ox + 4.5*mm, oy + 6.8*mm, 71.0*mm, 26.5*mm, 2.2*mm, fill=1, stroke=1)
        
        c.setFillColor(HexColor(COLOR_WINE_LIGHT))
        c.setFont(font_extra, 4.8)
        c.drawCentredString(ox + 40*mm, oy + 30.2*mm, "ESTUDE FÍSICA MÉDICA NA UNIVERSIDADE DE SÃO PAULO:")
        
        c.setFillColor(HexColor(COLOR_WINE))
        c.setFont(font_black, 7.5)
        c.drawCentredString(ox + 40*mm, oy + 26.8*mm, "Bacharelado Interunidades • Campus Capital")
        
        c.setFillColor(HexColor(COLOR_WHITE))
        c.setStrokeColor(HexColor("#c0dbe8"))
        c.setLineWidth(0.25*mm)
        c.roundRect(ox + 6.2*mm, oy + 8.2*mm, 32.5*mm, 16.2*mm, 1.6*mm, fill=1, stroke=1)
        c.drawImage(IFUSP_IMG_PATH, ox + 7.2*mm, oy + 8.7*mm, width=30.5*mm, height=15.2*mm, preserveAspectRatio=True, mask='auto')
        
        c.setFillColor(HexColor(COLOR_WHITE))
        c.setStrokeColor(HexColor("#bfe3cf"))
        c.setLineWidth(0.25*mm)
        c.roundRect(ox + 41.3*mm, oy + 8.2*mm, 32.5*mm, 16.2*mm, 1.6*mm, fill=1, stroke=1)
        c.drawImage(FMUSP_IMG_PATH, ox + 42.3*mm, oy + 8.7*mm, width=30.5*mm, height=15.2*mm, preserveAspectRatio=True, mask='auto')
        
        c.setFillColor(HexColor(COLOR_WINE_LIGHT))
        c.setFont(font_bold, 4.2)
        c.drawCentredString(ox + 40*mm, oy + 4.2*mm, "FEIRA USP E AS PROFISSÕES • IFUSP & FMUSP")
        
        c.restoreState()

def wrap_text(text, max_chars):
    """Quebra de texto balanceada para renderização no ReportLab."""
    words = text.split()
    lines = []
    cur_line = []
    cur_len = 0
    for w in words:
        w_len = len(w)
        if cur_line and (cur_len + 1 + w_len > max_chars):
            lines.append(" ".join(cur_line))
            cur_line = [w]
            cur_len = w_len
        else:
            cur_line.append(w)
            cur_len += (1 + w_len) if cur_len > 0 else w_len
    if cur_line:
        lines.append(" ".join(cur_line))
    return lines

def update_all_svgs():
    """Gera e substitui todos os 30 SVGs."""
    for card in CARDS_DATA:
        num_str = f"{card['num']:02d}"
        
        frente_path = os.path.join(SVG_DIR, f"card_{num_str}_frente.svg")
        with open(frente_path, "w", encoding="utf-8") as f:
            f.write(generate_svg_frente(card))
            
        verso_path = os.path.join(SVG_DIR, f"card_{num_str}_verso.svg")
        with open(verso_path, "w", encoding="utf-8") as f:
            f.write(generate_svg_verso(card))
    print("✓ 30 arquivos SVG atualizados com layout exato do modelo!")

def update_master_pdf():
    """Gera o Master PDF 80x120mm com layout exato da frente e verso completo."""
    pdf_path = os.path.join(PDF_DIR, "Cards_Fato_ou_Fake_USP_Completo_80x120mm.pdf")
    c = canvas.Canvas(pdf_path, pagesize=(80*mm, 120*mm))
    
    style_exp = ParagraphStyle(
        'ExpJustifiedMaster',
        fontName='Outfit-SemiBold' if HAS_OUTFIT else 'Helvetica',
        fontSize=6.5,
        leading=8.6,
        textColor=HexColor("#240016"),
        alignment=TA_JUSTIFY
    )
    
    for card in CARDS_DATA:
        # PÁGINA FRENTE (PERGUNTA + BADGE FATO OU FAKE JUSTO)
        draw_front_card_exact(c, 0, 0, card)
        c.showPage()
        
        # PÁGINA VERSO (RESPOSTA + EXPLICAÇÃO + IFUSP & FMUSP)
        draw_verso_card_exact(c, 0, 0, card, style_exp)
        c.showPage()
        
    c.save()
    print("✓ Master PDF atualizado com layout exato!")

def update_imposition_a4_pdf():
    """Gera as folhas A4 Duplex de imposição gráfica com o layout exato da frente."""
    pdf_path = os.path.join(PDF_DIR, "Folhas_Impressao_A4_Frente_Verso.pdf")
    c = canvas.Canvas(pdf_path, pagesize=A4)
    
    style_exp = ParagraphStyle(
        'ExpJustifiedImposition',
        fontName='Outfit-SemiBold' if HAS_OUTFIT else 'Helvetica',
        fontSize=6.5,
        leading=8.6,
        textColor=HexColor("#240016"),
        alignment=TA_JUSTIFY
    )
    
    chunks = [CARDS_DATA[i:i + 4] for i in range(0, len(CARDS_DATA), 4)]
    card_w = 80 * mm
    card_h = 120 * mm
    
    pos_frente = [
        (18*mm, 150*mm),
        (112*mm, 150*mm),
        (18*mm, 18*mm),
        (112*mm, 18*mm)
    ]
    pos_verso = [
        (112*mm, 150*mm),
        (18*mm, 150*mm),
        (112*mm, 18*mm),
        (18*mm, 18*mm)
    ]
    
    def draw_crop_marks(c, x, y):
        c.setStrokeColor(HexColor("#999999"))
        c.setLineWidth(0.2*mm)
        c.line(x - 5*mm, y, x - 1*mm, y)
        c.line(x, y - 5*mm, x, y - 1*mm)
        c.line(x + card_w + 1*mm, y, x + card_w + 5*mm, y)
        c.line(x + card_w, y - 5*mm, x + card_w, y - 1*mm)
        c.line(x - 5*mm, y + card_h, x - 1*mm, y + card_h)
        c.line(x, y + card_h + 1*mm, x, y + card_h + 5*mm)
        c.line(x + card_w + 1*mm, y + card_h, x + card_w + 5*mm, y + card_h)
        c.line(x + card_w, y + card_h + 1*mm, x + card_w, y + card_h + 5*mm)
    
    for page_idx, chunk in enumerate(chunks):
        # FOLHA DE FRENTES
        c.setFont("Helvetica-Bold", 8)
        c.setFillColor(HexColor("#888888"))
        c.drawString(18*mm, 285*mm, f"USP E AS PROFISSÕES • CARDS FATO OU FAKE • FOLHA {page_idx+1} (FRENTES) • IMPRIMIR COUCHÉ 300g")
        
        for idx, card in enumerate(chunk):
            x, y = pos_frente[idx]
            draw_crop_marks(c, x, y)
            draw_front_card_exact(c, x, y, card)
            
        c.showPage()
        
        # FOLHA DE VERSOS
        c.setFont("Helvetica-Bold", 8)
        c.setFillColor(HexColor("#888888"))
        c.drawString(18*mm, 285*mm, f"USP E AS PROFISSÕES • CARDS FATO OU FAKE • FOLHA {page_idx+1} (VERSOS) • IMPRIMIR COUCHÉ 300g")
        
        for idx, card in enumerate(chunk):
            x, y = pos_verso[idx]
            draw_crop_marks(c, x, y)
            draw_verso_card_exact(c, x, y, card, style_exp)
            
        c.showPage()
        
    c.save()
    print("✓ Folhas A4 Duplex atualizadas!")

def generate_catalog_html():
    """Gera o catálogo web oficial."""
    html_path = os.path.join(OUTPUT_DIR, "catalogo_cards_prontos.html")
    
    cards_html = ""
    for card in CARDS_DATA:
        num_str = f"{card['num']:02d}"
        is_fato = (card["type"] == "FATO")
        badge_class = "badge-fato" if is_fato else "badge-fake"
        
        cards_html += f"""
        <div class="card-item-container">
          <div class="card-item-header">
            <span class="card-num-tag">Card #{num_str}</span>
            <span class="card-status-badge {badge_class}">{card['type']}</span>
            <span class="card-cat-name">{card['emoji']} {card['category']}</span>
          </div>

          <div class="card-pair-view">
            <!-- Frente -->
            <div class="card-svg-wrapper">
              <div class="svg-label">Frente (Símbolos de Ciência &amp; Layout Oficial)</div>
              <img src="svg/card_{num_str}_frente.svg" alt="Card #{num_str} Frente" class="svg-render">
              <a href="svg/card_{num_str}_frente.svg" download class="dl-btn">Baixar SVG Frente</a>
            </div>

            <!-- Verso -->
            <div class="card-svg-wrapper">
              <div class="svg-label">Verso (Texto Justificado + IFUSP &amp; FMUSP)</div>
              <img src="svg/card_{num_str}_verso.svg" alt="Card #{num_str} Verso" class="svg-render">
              <a href="svg/card_{num_str}_verso.svg" download class="dl-btn">Baixar SVG Verso</a>
            </div>
          </div>
        </div>
        """
        
    html_content = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Catálogo Oficial de Cards Fato ou Fake • USP e as Profissões</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Outfit:wght@400;600;700;800;900&display=swap" rel="stylesheet">
  <style>
    :root {{
      --wine: #3e072b;
      --wine-dark: #240017;
      --pink: #ff007f;
      --green: #a2ff92;
      --yellow: #e8ff3b;
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    body {{
      font-family: 'Outfit', sans-serif;
      background: var(--wine-dark);
      color: #ffffff;
      padding: 30px 20px 80px;
    }}
    .catalog-header {{
      max-width: 1200px;
      margin: 0 auto 40px;
      background: linear-gradient(135deg, #4d0936 0%, var(--wine) 100%);
      border: 2px solid var(--yellow);
      border-radius: 20px;
      padding: 30px;
      box-shadow: 0 10px 30px rgba(0,0,0,0.5);
    }}
    .catalog-header h1 {{
      font-size: 28px;
      font-weight: 900;
      color: var(--yellow);
      margin-bottom: 8px;
    }}
    .catalog-header p {{
      font-size: 15px;
      color: #ffc2eb;
      font-weight: 500;
      margin-bottom: 20px;
    }}
    .action-bar {{
      display: flex;
      gap: 12px;
      flex-wrap: wrap;
    }}
    .btn-main {{
      background: var(--yellow);
      color: var(--wine);
      font-weight: 800;
      padding: 10px 22px;
      border-radius: 30px;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      font-size: 14px;
      transition: transform 0.2s, background 0.2s;
    }}
    .btn-main:hover {{
      background: #ffffff;
      transform: translateY(-2px);
    }}
    .btn-outline {{
      background: transparent;
      color: #ffffff;
      border: 2px solid rgba(255,255,255,0.4);
      font-weight: 700;
      padding: 10px 22px;
      border-radius: 30px;
      text-decoration: none;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      font-size: 14px;
      transition: all 0.2s;
    }}
    .btn-outline:hover {{
      border-color: #ffffff;
      background: rgba(255,255,255,0.1);
    }}
    .cards-list {{
      max-width: 1200px;
      margin: 0 auto;
      display: flex;
      flex-direction: column;
      gap: 36px;
    }}
    .card-item-container {{
      background: rgba(62, 7, 43, 0.7);
      border: 1px solid rgba(255, 0, 127, 0.3);
      border-radius: 18px;
      padding: 24px;
      box-shadow: 0 6px 20px rgba(0,0,0,0.4);
    }}
    .card-item-header {{
      display: flex;
      align-items: center;
      gap: 12px;
      margin-bottom: 20px;
      flex-wrap: wrap;
    }}
    .card-num-tag {{
      background: var(--yellow);
      color: var(--wine);
      font-weight: 900;
      font-size: 13px;
      padding: 4px 12px;
      border-radius: 20px;
    }}
    .card-status-badge {{
      font-weight: 900;
      font-size: 13px;
      padding: 4px 14px;
      border-radius: 20px;
    }}
    .badge-fato {{
      background: var(--green);
      color: #0a5222;
    }}
    .badge-fake {{
      background: var(--pink);
      color: #ffffff;
    }}
    .card-cat-name {{
      font-size: 16px;
      font-weight: 700;
      color: #ffffff;
    }}
    .card-pair-view {{
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
      gap: 24px;
      justify-items: center;
    }}
    .card-svg-wrapper {{
      display: flex;
      flex-direction: column;
      align-items: center;
      gap: 12px;
      width: 100%;
      max-width: 380px;
    }}
    .svg-label {{
      font-size: 13px;
      font-weight: 700;
      color: #e0b0d0;
      letter-spacing: 0.5px;
    }}
    .svg-render {{
      width: 100%;
      height: auto;
      border-radius: 24px;
      box-shadow: 0 10px 25px rgba(0,0,0,0.5);
      border: 1px solid rgba(255,255,255,0.1);
    }}
    .dl-btn {{
      background: rgba(255,255,255,0.12);
      color: #ffffff;
      border: 1px solid rgba(255,255,255,0.25);
      padding: 6px 16px;
      border-radius: 20px;
      font-size: 12px;
      font-weight: 700;
      text-decoration: none;
      transition: all 0.2s;
    }}
    .dl-btn:hover {{
      background: var(--pink);
      border-color: var(--pink);
      color: #ffffff;
    }}
    .card-pair-view.reversed-order {{
      direction: rtl;
    }}
    .card-pair-view.reversed-order > * {{
      direction: ltr;
    }}
  </style>
</head>
<body>

  <header class="catalog-header">
    <h1>Catálogo Oficial • 15 Cards Fato ou Fake</h1>
    <p>USP e as Profissões • Bacharelado Interunidades em Física Médica (IFUSP &amp; FMUSP)</p>
    <div class="action-bar">
      <a href="pdf/Folhas_Impressao_A4_Frente_Verso.pdf" download class="btn-main">
        📄 Baixar PDF Imposição A4 (Duplex com Marcas de Corte)
      </a>
      <a href="pdf/Cards_Fato_ou_Fake_USP_Completo_80x120mm.pdf" download class="btn-outline">
        📑 Baixar Master PDF (Páginas Individuais 80x120mm)
      </a>
      <button onclick="toggleCardOrder()" class="btn-outline" id="btnToggleOrder" style="cursor: pointer;">
        🔄 Inverter Ordem (Verso à Esquerda / Frente à Direita)
      </button>
      <a href="index.html" class="btn-outline">
        🎲 Abrir Simulador 3D Interativo
      </a>
    </div>
  </header>

  <main class="cards-list">
    {cards_html}
  </main>

  <script>
    function toggleCardOrder() {{
      const pairs = document.querySelectorAll('.card-pair-view');
      pairs.forEach(p => p.classList.toggle('reversed-order'));
      const btn = document.getElementById('btnToggleOrder');
      if (pairs[0] && pairs[0].classList.contains('reversed-order')) {{
        btn.innerHTML = '🔄 Inverter Ordem (Frente à Esquerda / Verso à Direita)';
      }} else {{
        btn.innerHTML = '🔄 Inverter Ordem (Verso à Esquerda / Frente à Direita)';
      }}
    }}
  </script>
</body>
</html>
"""
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    print("✓ Catálogo HTML atualizado com sucesso!")

def update_master_template_svg():
    """Gera o gabarito mestre cards_template_vetorial.svg."""
    template_path = os.path.join(OUTPUT_DIR, "cards_template_vetorial.svg")
    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 1200" width="1600" height="1200">
  <defs>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=Barlow:ital,wght@0,400;0,600;0,700;1,400;1,600&amp;family=Outfit:wght@400;600;700;800;900&amp;display=swap');
      text, p, div {{
        font-family: 'Outfit', system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
      }}
    </style>
    <linearGradient id="wineBg" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#3e072b"/>
      <stop offset="60%" stop-color="#300421"/>
      <stop offset="100%" stop-color="#200115"/>
    </linearGradient>
    <filter id="cardShadow" x="-10%" y="-10%" width="125%" height="125%">
      <feDropShadow dx="0" dy="8" stdDeviation="12" flood-color="#000000" flood-opacity="0.45"/>
    </filter>
    <clipPath id="cardClip">
      <rect width="380" height="570" rx="34"/>
    </clipPath>
  </defs>

  <!-- Fundo da Área de Trabalho -->
  <rect width="100%" height="100%" fill="#1a0010"/>

  <!-- Título do Gabarito -->
  <g transform="translate(80, 65)">
    <text font-family="'Outfit', sans-serif" font-size="28" font-weight="900" fill="#e8ff3b">GABARITO VETORIAL • FÍSICA MÉDICA USP (IFUSP &amp; FMUSP)</text>
    <text font-family="'Outfit', sans-serif" font-size="16" font-weight="600" fill="#ff97eb" y="30">Bacharelado Interunidades em Física Médica (Campus São Paulo / Capital) • Formato Oficial: 80 x 120 mm</text>
  </g>

  <!-- CARD 1: FRENTE OFICIAL (EXATA COMO NO MODELO DA FOTO) -->
  <g transform="translate(100, 150)" filter="url(#cardShadow)">
    <g clip-path="url(#cardClip)">
      <!-- Fundo Base Vinho Profundo -->
      <rect width="380" height="570" fill="#2d031c"/>

      <!-- Facetas Poligonais em Tons de Vinho/Ameixa -->
      <polygon points="0,0 270,0 152,156 0,104" fill="#3c0627"/>
      <polygon points="270,0 380,109 237,213 152,156" fill="#4d0933"/>
      <polygon points="0,104 152,156 71,294 0,256" fill="#350421"/>
      <polygon points="152,156 237,213 223,351 71,294" fill="#46072e"/>
      <polygon points="237,213 380,109 380,323 299,365" fill="#31031e"/>
      <polygon points="380,323 380,451 294,570 223,441 299,365" fill="#520c36"/>
      <polygon points="0,256 71,294 223,441 109,570 0,446" fill="#380523"/>
      <polygon points="223,441 109,570 294,570" fill="#250217"/>

      <!-- Acentos Geométricos Exatos dos Cantos -->
      <polygon points="0,104 104,0 68,0 0,68" fill="#e8ff3b"/>
      <path d="M 270 0 L 380 0 L 380 109 Z" fill="#ff007f"/>
      <polygon points="0,446 0,570 109,570" fill="#a2ff92"/>
      <polygon points="294,570 380,570 380,451" fill="#e8ff3b"/>

      <!-- 7 Símbolos de Ciência Exatos em Traço Rosa Translúcido (Maiores e Mais Transparentes) -->
      <g stroke="#ff007f" stroke-opacity="0.22" stroke-width="2.2" fill="none" stroke-linecap="round" stroke-linejoin="round">
        <g transform="translate(56, 46) rotate(-35) scale(2.9)">
          <path d="M2 15c6.667-6 13.333 0 20-6" />
          <path d="M9 22c1.798-1.998 2.518-3.995 2.807-5.993" />
          <path d="M15 2c-1.798 1.998-2.518 3.995-2.807 5.993" />
          <path d="m17 6-2.891-2.891" />
          <path d="m7 18 2.891 2.891" />
          <path d="m10 16 1.5 1.5" />
          <path d="m14 8-1.5-1.5" />
          <path d="m16.5 10.5 1 1" />
          <path d="m6.5 12.5 1 1" />
          <path d="m20 9 .891.891" />
          <path d="M3.109 14.109 4 15" />
        </g>
        <g transform="translate(166, 12) rotate(15) scale(2.5)">
          <path d="M3 21C4 10 10 4 21 3C20 14 14 20 3 21Z" />
          <path d="M3 21L21 3" />
          <path d="M7.5 13.5L10.5 16.5" />
          <path d="M10.5 10.5L13.5 13.5" />
          <path d="M13.5 7.5L16.5 10.5" />
        </g>
        <g transform="translate(270, 50) scale(2.9)">
          <circle cx="12" cy="12" r="1.4" fill="#ff007f" />
          <path d="M20.2 20.2c2.04-2.03.02-7.36-4.5-11.9-4.54-4.52-9.87-6.54-11.9-4.5-2.04 2.03-.02 7.36 4.5 11.9 4.54 4.52 9.87 6.54 11.9 4.5Z" />
          <path d="M15.7 15.7c4.52-4.54 6.54-9.87 4.5-11.9-2.03-2.04-7.36-.02-11.9 4.5-4.52 4.54-6.54 9.87-4.5 11.9 2.03 2.04 7.36.02 11.9-4.5Z" />
        </g>
        <g transform="translate(26, 162) rotate(-15) scale(2.6)">
          <path d="M9 18h6M10 22h4M9 14c-0.2-1-0.7-1.7-1.5-2.5C6.8 10.6 6 9.4 6 8c0-3.313 2.686-6 6-6s6 2.686 6 6c0 1.4-0.8 2.6-1.5 3.5-0.8 0.8-1.3 1.5-1.5 2.5" />
        </g>
        <g transform="translate(305, 160) scale(2.7)">
          <circle cx="12" cy="12" r="3.2" />
          <circle cx="12" cy="12" r="6.8" />
          <path d="M12 2v3.2M12 18.8v3.2M2 12h3.2M18.8 12h3.2M4.93 4.93l2.26 2.26M16.81 16.81l2.26 2.26M4.93 19.07l2.26-2.26M16.81 7.19l2.26-2.26" />
        </g>
        <g transform="translate(38, 345) rotate(-35) scale(2.9)">
          <path d="M2 15c6.667-6 13.333 0 20-6" />
          <path d="M9 22c1.798-1.998 2.518-3.995 2.807-5.993" />
          <path d="M15 2c-1.798 1.998-2.518 3.995-2.807 5.993" />
          <path d="m17 6-2.891-2.891" />
          <path d="m7 18 2.891 2.891" />
        </g>
        <g transform="translate(310, 320) rotate(15) scale(2.8)">
          <path d="M6 18h8" />
          <path d="M3 22h18" />
          <path d="M14 22c3.86 0 7-3.14 7-7c0-3.86-3.14-7-7-7h-1" />
          <path d="M9 14h2" />
          <path d="M7 10V6h6v4c0 1.1-0.9 2-2 2H9c-1.1 0-2-0.9-2-2Z" />
          <path d="M12 6V2M9 2h6" />
        </g>
      </g>

      <!-- ENUMERAÇÃO DO CARD NO CANTO SUPERIOR DIREITO NO AMARELO CARACTERÍSTICO -->
      <text x="340" y="44" font-family="'Outfit', system-ui, -apple-system, sans-serif" font-size="26" font-weight="900" fill="#e8ff3b" text-anchor="middle">#01</text>

      <!-- BADGE HERO FATO ou FAKE? (+4.5° COM BORDAS JUSTAS E 'ou' REDUZIDO COM FONTE +2) -->
      <g transform="rotate(4.5, 190, 112)">
        <path d="M 88 92 C 88 64 112 56 140 56 L 242 56" fill="none" stroke="#a2ff92" stroke-width="4" stroke-linecap="round"/>
        <rect x="92" y="56" width="196" height="58" rx="29" fill="#ffffff"/>
        <text x="190" y="100" font-family="'Outfit', system-ui, -apple-system, sans-serif" font-size="48" font-weight="900" fill="#350424" text-anchor="middle" letter-spacing="1.5">FATO</text>

        <path d="M 136 180 L 244 180 C 276 180 296 168 296 140" fill="none" stroke="#ff007f" stroke-width="4" stroke-linecap="round"/>
        <rect x="78" y="118" width="224" height="60" rx="30" fill="#ff007f"/>
        <text x="190" y="162" font-family="'Outfit', system-ui, -apple-system, sans-serif" font-size="48" font-weight="900" fill="#ffffff" text-anchor="middle" letter-spacing="1.5">FAKE?</text>

        <!-- Pílula Escura Central 'ou': REDUZIDA e com FONTE +2 (16px), sem cobrir o 'FAKE' -->
        <rect x="168" y="99" width="44" height="22" rx="11" fill="#350424" stroke="#ffffff" stroke-width="2.5"/>
        <text x="190" y="115.5" font-family="'Outfit', system-ui, -apple-system, sans-serif" font-size="16" font-weight="900" fill="#ffffff" text-anchor="middle">ou</text>
      </g>

      <!-- CAMPO DA PERGUNTA NO GABARITO (SEM NÚMERO DENTRO DO BOX) -->
      <rect x="20" y="200" width="340" height="242" rx="20" fill="#ffffff" filter="url(#cardShadow)"/>
      <rect x="20" y="200" width="7" height="242" rx="3.5" fill="#ff007f"/>
      <rect x="70" y="214" width="240" height="24" rx="12" fill="#fceaf3"/>
      <text x="190" y="230" font-family="'Outfit', system-ui, -apple-system, sans-serif" font-size="11" font-weight="800" fill="#d8005b" text-anchor="middle">🍌 RADIAÇÃO NO COTIDIANO</text>
      <text x="190" y="300" font-family="'Outfit', system-ui, -apple-system, sans-serif" font-size="19" font-weight="900" font-style="italic" fill="#1a0210" text-anchor="middle">“Comer uma banana faz você</text>
      <text x="190" y="330" font-family="'Outfit', system-ui, -apple-system, sans-serif" font-size="19" font-weight="900" font-style="italic" fill="#1a0210" text-anchor="middle">absorver radiação.”</text>
      <line x1="40" y1="395" x2="340" y2="395" stroke="#f2d5e5" stroke-width="1.2"/>
      <text x="190" y="420" font-family="'Outfit', system-ui, -apple-system, sans-serif" font-size="11.5" font-weight="700" fill="#741d4f" text-anchor="middle">👉 O que você acha? Vire o card para descobrir!</text>

      <!-- Texto Centralizado Abaixo do Badge: CIÊNCIA OU MITO? (ÚNICO E EM AMARELO) -->
      <text x="190" y="485" font-family="'Outfit', system-ui, -apple-system, sans-serif" font-size="22" font-weight="900" fill="#e8ff3b" text-anchor="middle" letter-spacing="2.5">CIÊNCIA OU MITO?</text>
    </g>
  </g>

  <!-- CARD 2: VERSO COM TEXTO JUSTIFICADO + LOGOS IFUSP & FMUSP (FATO!) -->
  <g transform="translate(560, 150)" filter="url(#cardShadow)">
    <g clip-path="url(#cardClip)">
      <rect width="380" height="570" fill="#3e072b"/>
      <path d="M 0 0 L 70 0 L 0 70 Z" fill="#ff007f"/>
      <path d="M 310 0 L 380 0 L 380 70 Z" fill="#a2ff92"/>
      <path d="M 0 500 L 0 570 L 70 570 Z" fill="#a2ff92"/>
      <path d="M 310 570 L 380 570 L 380 500 Z" fill="#e8ff3b"/>

      <rect x="14" y="14" width="352" height="542" rx="24" fill="#ffffff"/>

      <!-- Topo: Número e Categoria -->
      <g transform="translate(190, 34)">
        <rect x="-115" y="-12" width="230" height="22" rx="11" fill="#f8edf4"/>
        <text x="0" y="3.5" font-family="'Outfit', sans-serif" font-size="11" font-weight="800" fill="#741d4f" text-anchor="middle" letter-spacing="0.5">
          CARD #01 • 🍌 RADIAÇÃO NO COTIDIANO
        </text>
      </g>

      <!-- Selo Pílula FATO! -->
      <g transform="translate(190, 68)">
        <rect x="-90" y="-18" width="180" height="36" rx="18" fill="#bdf7c9" stroke="#1f6133" stroke-width="3"/>
        <text x="0" y="7.5" font-family="'Outfit', sans-serif" font-size="24" font-weight="900" fill="#0a5222" text-anchor="middle" letter-spacing="1">FATO!</text>
      </g>

      <!-- HEADLINE EXPLICATIVA (SEM PERGUNTA REPETIDA) -->
      <g transform="translate(18, 96)">
        <foreignObject width="344" height="42">
          <div xmlns="http://www.w3.org/1999/xhtml" style="display: flex; align-items: center; justify-content: center; height: 100%; width: 100%; box-sizing: border-box; padding: 0 4px;">
            <p style="font-family: 'Outfit', sans-serif; font-size: 13.5px; font-style: italic; font-weight: 900; color: #1f6133; line-height: 1.2; text-align: center; margin: 0; text-transform: uppercase;">
              O POTÁSSIO DA BANANA É NATURALMENTE RADIOATIVO!
            </p>
          </div>
        </foreignObject>
      </g>

      <!-- Explicação Científica Super Didática Justificada -->
      <g transform="translate(20, 144)">
        <foreignObject width="340" height="260">
          <div xmlns="http://www.w3.org/1999/xhtml" style="height: 100%; width: 100%; box-sizing: border-box;">
            <p style="font-family: 'Outfit', sans-serif; font-size: 12.2px; font-weight: 500; color: #1f0013; line-height: 1.40; text-align: justify; text-justify: inter-word; hyphens: auto; margin: 0;">
              A banana é rica em potássio, nutriente vital para os músculos e coração. Porém, cerca de 0,012% de todo o potássio natural na Terra é o isótopo <b>Potássio-40 (⁴⁰K)</b>, que é radioativo e emite partículas ao decair. Na Física Médica existe até uma unidade didática bem-humorada chamada <i>BED (Banana Equivalent Dose)</i> para comparar doses diárias de radiação. Fique tranquilo: nosso corpo mantém o nível de potássio em equilíbrio biológico e elimina o excesso. Você precisaria comer 10 milhões de bananas de uma vez para sofrer qualquer efeito nocivo!
            </p>
          </div>
        </foreignObject>
      </g>

      <!-- SEÇÃO FÍSICA MÉDICA USP COMPACTA (IFUSP & FMUSP) -->
      <g transform="translate(16, 412)">
        <rect width="348" height="130" rx="14" fill="#f8edf4" stroke="#e8ccd9" stroke-width="1.2"/>
        <text x="174" y="18" font-family="'Outfit', sans-serif" font-size="9.5" font-weight="800" fill="#741d4f" letter-spacing="0.6" text-anchor="middle">ESTUDE FÍSICA MÉDICA NA UNIVERSIDADE DE SÃO PAULO:</text>
        <text x="174" y="32" font-family="'Outfit', sans-serif" font-size="13" font-weight="900" fill="#3e072b" text-anchor="middle">Bacharelado Interunidades • Campus Capital</text>

        <!-- LOGOS OFICIAIS IFUSP & FMUSP -->
        <g transform="translate(12, 40)">
          <rect width="154" height="76" rx="8" fill="#ffffff" stroke="#c0dbe8" stroke-width="1.0"/>
          <image href="data:image/png;base64,{B64_IFUSP}" x="6" y="4" width="142" height="68" preserveAspectRatio="xMidYMid meet"/>

          <g transform="translate(170, 0)">
            <rect width="154" height="76" rx="8" fill="#ffffff" stroke="#bfe3cf" stroke-width="1.0"/>
            <image href="data:image/png;base64,{B64_FMUSP}" x="6" y="4" width="142" height="68" preserveAspectRatio="xMidYMid meet"/>
          </g>
        </g>
      </g>

      <!-- Micro Rodapé -->
      <g transform="translate(190, 548)">
        <text x="0" y="0" font-family="'Outfit', sans-serif" font-size="9" font-weight="800" fill="#741d4f" text-anchor="middle" letter-spacing="0.8">FEIRA USP E AS PROFISSÕES • IFUSP &amp; FMUSP</text>
      </g>
    </g>
  </g>

  <!-- CARD 3: VERSO COM TEXTO JUSTIFICADO + LOGOS IFUSP & FMUSP (FAKE!) -->
  <g transform="translate(1020, 150)" filter="url(#cardShadow)">
    <g clip-path="url(#cardClip)">
      <rect width="380" height="570" fill="#3e072b"/>
      <path d="M 0 0 L 70 0 L 0 70 Z" fill="#ff007f"/>
      <path d="M 310 0 L 380 0 L 380 70 Z" fill="#a2ff92"/>
      <path d="M 0 500 L 0 570 L 70 570 Z" fill="#a2ff92"/>
      <path d="M 310 570 L 380 570 L 380 500 Z" fill="#e8ff3b"/>

      <rect x="14" y="14" width="352" height="542" rx="24" fill="#ffffff"/>

      <!-- Topo: Número e Categoria -->
      <g transform="translate(190, 34)">
        <rect x="-115" y="-12" width="230" height="22" rx="11" fill="#f8edf4"/>
        <text x="0" y="3.5" font-family="'Outfit', sans-serif" font-size="11" font-weight="800" fill="#741d4f" text-anchor="middle" letter-spacing="0.5">
          CARD #02 • 🧲 RESSONÂNCIA MAGNÉTICA
        </text>
      </g>

      <!-- Selo Pílula FAKE! -->
      <g transform="translate(190, 68)">
        <rect x="-90" y="-18" width="180" height="36" rx="18" fill="#ffb3d9" stroke="#d8005b" stroke-width="3"/>
        <text x="0" y="7.5" font-family="'Outfit', sans-serif" font-size="24" font-weight="900" fill="#3e072b" text-anchor="middle" letter-spacing="1">FAKE!</text>
      </g>

      <!-- HEADLINE EM FONTE DESTACADA (SEM A PERGUNTA REPETIDA) -->
      <g transform="translate(18, 96)">
        <foreignObject width="344" height="42">
          <div xmlns="http://www.w3.org/1999/xhtml" style="display: flex; align-items: center; justify-content: center; height: 100%; width: 100%; box-sizing: border-box; padding: 0 4px;">
            <p style="font-family: 'Outfit', sans-serif; font-size: 13.5px; font-style: italic; font-weight: 900; color: #d8005b; line-height: 1.2; text-align: center; margin: 0; text-transform: uppercase;">
              O ÍMÃ FICA LIGADO 24 HORAS POR DIA, 365 DIAS NO ANO!
            </p>
          </div>
        </foreignObject>
      </g>

      <!-- Explicação Científica Super Didática Justificada -->
      <g transform="translate(20, 144)">
        <foreignObject width="340" height="260">
          <div xmlns="http://www.w3.org/1999/xhtml" style="height: 100%; width: 100%; box-sizing: border-box;">
            <p style="font-family: 'Outfit', sans-serif; font-size: 12.2px; font-weight: 500; color: #1f0013; line-height: 1.40; text-align: justify; text-justify: inter-word; hyphens: auto; margin: 0;">
              O ímã de uma máquina de ressonância é um <b>eletroímã supercondutor</b>. Suas bobinas ficam mergulhadas em Hélio Líquido a impressionantes <b>-269 °C</b> (quase o zero absoluto!), onde a resistência elétrica é nula e a corrente gira perpetuamente sem gastar energia da tomada. Desligar o campo magnético só ocorre em emergências extremas por um processo chamado <i>Quench</i>, que ferve milhares de litros de gás hélio e custa caro para restabelecer. Por isso, a sala é permanentemente magnética e objetos de ferro nunca podem entrar lá!
            </p>
          </div>
        </foreignObject>
      </g>

      <!-- SEÇÃO FÍSICA MÉDICA USP COMPACTA (IFUSP & FMUSP) -->
      <g transform="translate(16, 412)">
        <rect width="348" height="130" rx="14" fill="#f8edf4" stroke="#e8ccd9" stroke-width="1.2"/>
        <text x="174" y="18" font-family="'Outfit', sans-serif" font-size="9.5" font-weight="800" fill="#741d4f" letter-spacing="0.6" text-anchor="middle">ESTUDE FÍSICA MÉDICA NA UNIVERSIDADE DE SÃO PAULO:</text>
        <text x="174" y="32" font-family="'Outfit', sans-serif" font-size="13" font-weight="900" fill="#3e072b" text-anchor="middle">Bacharelado Interunidades • Campus Capital</text>

        <!-- LOGOS OFICIAIS IFUSP & FMUSP -->
        <g transform="translate(12, 40)">
          <rect width="154" height="76" rx="8" fill="#ffffff" stroke="#c0dbe8" stroke-width="1.0"/>
          <image href="data:image/png;base64,{B64_IFUSP}" x="6" y="4" width="142" height="68" preserveAspectRatio="xMidYMid meet"/>

          <g transform="translate(170, 0)">
            <rect width="154" height="76" rx="8" fill="#ffffff" stroke="#bfe3cf" stroke-width="1.0"/>
            <image href="data:image/png;base64,{B64_FMUSP}" x="6" y="4" width="142" height="68" preserveAspectRatio="xMidYMid meet"/>
          </g>
        </g>
      </g>

      <!-- Micro Rodapé -->
      <g transform="translate(190, 548)">
        <text x="0" y="0" font-family="'Outfit', sans-serif" font-size="9" font-weight="800" fill="#741d4f" text-anchor="middle" letter-spacing="0.8">FEIRA USP E AS PROFISSÕES • IFUSP &amp; FMUSP</text>
      </g>
    </g>
  </g>
</svg>"""
    with open(template_path, "w", encoding="utf-8") as f:
        f.write(svg_content)
    print("✓ Gabarito mestre cards_template_vetorial.svg atualizado!")

def sync_to_dock_folder():
    """
    Sincroniza todos os arquivos de produção para a pasta do Dock (~/Cards_Fato_ou_Fake_USP)
    e para a pasta no Desktop (~/Desktop/Cards_Fato_ou_Fake_USP).
    """
    import shutil
    dock_dir = os.path.expanduser("~/Cards_Fato_ou_Fake_USP")
    desktop_dir = os.path.expanduser("~/Desktop/Cards_Fato_ou_Fake_USP")
    
    for base in [dock_dir, desktop_dir]:
        os.makedirs(base, exist_ok=True)
        pdf_dest = os.path.join(base, "pdf")
        svg_dest = os.path.join(base, "svg")
        assets_dest = os.path.join(base, "assets")
        os.makedirs(pdf_dest, exist_ok=True)
        os.makedirs(svg_dest, exist_ok=True)
        os.makedirs(assets_dest, exist_ok=True)
        
        # PDFs
        for f in os.listdir(PDF_DIR):
            if f.endswith(".pdf"):
                shutil.copy2(os.path.join(PDF_DIR, f), os.path.join(pdf_dest, f))
                shutil.copy2(os.path.join(PDF_DIR, f), os.path.join(base, f))
                
        # SVGs
        for f in os.listdir(SVG_DIR):
            if f.endswith(".svg"):
                shutil.copy2(os.path.join(SVG_DIR, f), os.path.join(svg_dest, f))
                
        # Assets
        for f in os.listdir(ASSETS_DIR):
            shutil.copy2(os.path.join(ASSETS_DIR, f), os.path.join(assets_dest, f))
            
        # Catálogo e Gabarito
        html_file = os.path.join(OUTPUT_DIR, "catalogo_cards_prontos.html")
        if os.path.exists(html_file):
            shutil.copy2(html_file, os.path.join(base, "catalogo_cards_prontos.html"))
            
        template_file = os.path.join(OUTPUT_DIR, "cards_template_vetorial.svg")
        if os.path.exists(template_file):
            shutil.copy2(template_file, os.path.join(base, "cards_template_vetorial.svg"))
            
    print(f"✓ Todos os arquivos sincronizados na pasta do Dock ({dock_dir}) e no Desktop!")

if __name__ == "__main__":
    print("Gerando todos os arquivos atualizados com símbolos profissionais de ciência...")
    update_all_svgs()
    update_master_pdf()
    update_imposition_a4_pdf()
    generate_catalog_html()
    update_master_template_svg()
    sync_to_dock_folder()
    print("✓ TUDO ATUALIZADO COM SUCESSO!")
