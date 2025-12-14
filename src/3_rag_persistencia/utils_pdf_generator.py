"""
Utilitário para gerar PDFs de exemplo para o laboratório de RAG.

Este módulo cria PDFs com conteúdos realistas para demonstrar:
- Processamento de documentos reais
- Chunking de texto
- Busca semântica em documentos longos
- RAG com múltiplas fontes
"""

from pathlib import Path
from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER
from datetime import datetime


def criar_pdf_manual_smartphone(output_path: Path):
    """
    Cria um PDF com manual técnico de smartphone.
    
    Conteúdo: Especificações, recursos, guia de uso do iPhone 15 Pro Max.
    Propósito: Testar busca de informações técnicas específicas.
    """
    doc = SimpleDocTemplate(str(output_path), pagesize=letter)
    styles = getSampleStyleSheet()
    story = []
    
    # Estilo customizado
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor='darkblue',
        spaceAfter=30,
        alignment=TA_CENTER
    )
    
    # Título
    story.append(Paragraph("Manual do Usuário", title_style))
    story.append(Paragraph("iPhone 15 Pro Max", title_style))
    story.append(Spacer(1, 0.5*inch))
    
    # Introdução
    story.append(Paragraph("Bem-vindo ao seu novo iPhone 15 Pro Max", styles['Heading2']))
    intro_text = """
    O iPhone 15 Pro Max representa o ápice da tecnologia móvel da Apple. 
    Este manual fornece informações detalhadas sobre os recursos, especificações 
    e guia de uso do seu novo dispositivo.
    """
    story.append(Paragraph(intro_text, styles['BodyText']))
    story.append(Spacer(1, 0.3*inch))
    
    # Especificações Técnicas
    story.append(Paragraph("Especificações Técnicas", styles['Heading2']))
    
    specs = [
        "<b>Processador:</b> Apple A17 Pro com GPU de 6 núcleos e Neural Engine de 16 núcleos",
        "<b>Tela:</b> Super Retina XDR OLED de 6,7 polegadas com ProMotion 120Hz e Always-On Display",
        "<b>Resolução:</b> 2796 x 1290 pixels (460 ppi) com suporte a HDR, Dolby Vision e True Tone",
        "<b>Câmera Principal:</b> Sistema triplo com sensor principal de 48MP (f/1.78), ultra-wide de 12MP (f/2.2) e teleobjetiva periscópica de 12MP com zoom óptico de 5x",
        "<b>Câmera Frontal:</b> TrueDepth de 12MP com autofoco e gravação 4K",
        "<b>Armazenamento:</b> Opções de 256GB, 512GB ou 1TB (NVMe SSD)",
        "<b>Memória RAM:</b> 8GB LPDDR5",
        "<b>Bateria:</b> 4.422 mAh com carregamento rápido de 27W via USB-C, carregamento sem fio MagSafe de 15W e Qi de 7,5W",
        "<b>Conectividade:</b> 5G (sub-6GHz e mmWave), Wi-Fi 6E, Bluetooth 5.3, UWB (Ultra Wideband), NFC",
        "<b>Dimensões:</b> 159,9 x 76,7 x 8,25 mm",
        "<b>Peso:</b> 221 gramas",
        "<b>Material:</b> Chassis de titânio aeroespacial grau 5 com vidro Ceramic Shield",
        "<b>Resistência:</b> IP68 (resistente a água até 6 metros por 30 minutos)",
    ]
    
    for spec in specs:
        story.append(Paragraph(spec, styles['BodyText']))
        story.append(Spacer(1, 0.1*inch))
    
    story.append(PageBreak())
    
    # Sistema de Câmera
    story.append(Paragraph("Sistema de Câmera Avançado", styles['Heading2']))
    
    camera_text = """
    <b>Sensor Principal de 48 Megapixels:</b><br/>
    O sensor quad-pixel de 48MP permite capturar imagens em resolução máxima 
    ou combinar pixels para fotos de 12MP com melhor desempenho em baixa luminosidade. 
    O sistema usa pixel binning 2x2 para produzir fotos de 12MP com excelente 
    qualidade e menor ruído.<br/><br/>
    
    <b>Teleobjetiva Periscópica com Zoom 5x:</b><br/>
    A inovadora lente periscópica utiliza um sistema de prisma que dobra a luz 
    em 90 graus, permitindo um caminho óptico mais longo dentro do corpo compacto 
    do telefone. Isso resulta em zoom óptico de 5x (120mm equivalente) sem perda 
    de qualidade. O sistema de estabilização óptica de imagem (OIS) de sensor 
    shift trabalha em conjunto com o OIS da lente para reduzir tremores.<br/><br/>
    
    <b>Modo Retrato Avançado:</b><br/>
    O modo retrato agora funciona automaticamente ao detectar pessoas ou animais 
    de estimação no enquadramento. O sistema captura informações de profundidade 
    durante a foto, permitindo ajustar o ponto focal e a intensidade do bokeh 
    posteriormente na galeria. Suporta até 9 níveis de abertura virtual (f/1.4 a f/16).<br/><br/>
    
    <b>ProRAW e ProRes:</b><br/>
    Fotógrafos profissionais podem capturar em Apple ProRAW de 48MP, mantendo 
    controle total sobre processamento de imagem. Para vídeo, o ProRes 4K a 60fps 
    oferece qualidade cinematográfica com taxa de bits de até 6Gbps quando gravado 
    em armazenamento externo via USB-C.<br/><br/>
    
    <b>Modo Noturno Aprimorado:</b><br/>
    Todas as câmeras (principal, ultra-wide e teleobjetiva) agora suportam modo 
    noturno. O processamento de Deep Fusion combina múltiplas exposições usando 
    aprendizado de máquina para produzir fotos nítidas mesmo com apenas 1 lux de luz.
    """
    story.append(Paragraph(camera_text, styles['BodyText']))
    
    story.append(PageBreak())
    
    # Recursos de Software
    story.append(Paragraph("Recursos de Software iOS 17", styles['Heading2']))
    
    software_text = """
    <b>Action Button Personalizável:</b><br/>
    O novo botão Action substitui o switch de silencioso e pode ser programado 
    para executar diversas funções: ativar câmera, lanterna, gravar memo de voz, 
    iniciar foco personalizado, traduzir texto, executar atalho do app Atalhos, 
    ou controlar acessibilidade.<br/><br/>
    
    <b>Dynamic Island Interativa:</b><br/>
    A Dynamic Island expande e contrai para mostrar alertas, notificações e 
    atividades em tempo real como música, chamadas, timers, navegação GPS e status 
    de entrega. Suporta múltiplas atividades simultâneas com toque longo para expandir.<br/><br/>
    
    <b>StandBy Mode:</b><br/>
    Quando carregando horizontalmente, o iPhone transforma-se em display inteligente 
    mostrando relógio grande, fotos, widgets personalizáveis e controles de casa 
    inteligente. Modo noturno vermelho ativa automaticamente em ambientes escuros.<br/><br/>
    
    <b>Bateria e Desempenho:</b><br/>
    O chip A17 Pro oferece até 29 horas de reprodução de vídeo. O Modo de Baixo 
    Consumo reduz consumo de energia desativando refresh de 120Hz, efeitos visuais 
    e downloads automáticos. Carregamento otimizado aprende sua rotina para 
    preservar a saúde da bateria a longo prazo, mantendo carga em 80% até pouco 
    antes de você desconectar o dispositivo.
    """
    story.append(Paragraph(software_text, styles['BodyText']))
    
    story.append(Spacer(1, 0.3*inch))
    
    # Guia Rápido
    story.append(Paragraph("Guia de Início Rápido", styles['Heading2']))
    
    quick_guide = """
    <b>Configuração Inicial:</b><br/>
    1. Ligue o iPhone pressionando o botão lateral por 3 segundos<br/>
    2. Aproxime seu iPhone antigo para transferir dados via Quick Start<br/>
    3. Configure Face ID olhando para a câmera frontal<br/>
    4. Restaure backup do iCloud ou configure como novo<br/><br/>
    
    <b>Gestos Essenciais:</b><br/>
    • Deslizar de baixo para cima: Tela inicial<br/>
    • Deslizar de baixo e segurar: Multitarefas<br/>
    • Deslizar da direita superior: Central de Controle<br/>
    • Deslizar da esquerda superior: Notificações<br/><br/>
    
    <b>Manutenção:</b><br/>
    • Use apenas cabos USB-C certificados MFi<br/>
    • Limpe a tela com pano de microfibra levemente umedecido<br/>
    • Evite temperaturas extremas (operar entre 0°C e 35°C)<br/>
    • Atualize o iOS regularmente em Ajustes → Geral → Atualização de Software
    """
    story.append(Paragraph(quick_guide, styles['BodyText']))
    
    # Build do PDF
    doc.build(story)
    print(f"✅ PDF criado: {output_path}")
    return output_path


def criar_pdf_receitas(output_path: Path):
    """
    Cria um PDF com livro de receitas culinárias.
    
    Conteúdo: Receitas detalhadas de diversos pratos.
    Propósito: Testar busca de receitas e ingredientes específicos.
    """
    doc = SimpleDocTemplate(str(output_path), pagesize=letter)
    styles = getSampleStyleSheet()
    story = []
    
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor='darkred',
        spaceAfter=30,
        alignment=TA_CENTER
    )
    
    story.append(Paragraph("Livro de Receitas Práticas", title_style))
    story.append(Paragraph("Sabores do Mundo em Casa", title_style))
    story.append(Spacer(1, 0.5*inch))
    
    # Receita 1: Lasanha
    story.append(Paragraph("Lasanha à Bolonhesa Tradicional", styles['Heading2']))
    
    lasanha = """
    <b>Rendimento:</b> 8 porções | <b>Tempo de preparo:</b> 2 horas<br/><br/>
    
    <b>Ingredientes para o molho bolonhesa:</b><br/>
    • 500g de carne moída (patinho ou acém)<br/>
    • 300g de linguiça calabresa sem pele, picada<br/>
    • 1 cebola grande picada<br/>
    • 4 dentes de alho amassados<br/>
    • 2 latas de tomate pelado (800g)<br/>
    • 3 colheres (sopa) de extrato de tomate<br/>
    • 1 xícara de vinho tinto seco<br/>
    • 1 folha de louro<br/>
    • Manjericão fresco a gosto<br/>
    • Sal, pimenta-do-reino e orégano a gosto<br/>
    • 3 colheres (sopa) de azeite<br/><br/>
    
    <b>Ingredientes para o molho branco (bechamel):</b><br/>
    • 4 colheres (sopa) de manteiga<br/>
    • 4 colheres (sopa) de farinha de trigo<br/>
    • 1 litro de leite integral<br/>
    • Noz-moscada ralada na hora<br/>
    • Sal e pimenta branca a gosto<br/><br/>
    
    <b>Montagem:</b><br/>
    • 500g de massa para lasanha pré-cozida<br/>
    • 400g de muçarela ralada<br/>
    • 200g de presunto fatiado<br/>
    • 100g de parmesão ralado<br/><br/>
    
    <b>Modo de preparo do molho bolonhesa:</b><br/>
    1. Em uma panela grande, aqueça o azeite e refogue a cebola até ficar translúcida (3-4 minutos)<br/>
    2. Adicione o alho e refogue por mais 1 minuto até perfumar<br/>
    3. Junte a carne moída e a linguiça, mexendo constantemente para desmanchar bem. 
       Cozinhe em fogo alto até dourar (cerca de 8-10 minutos)<br/>
    4. Despeje o vinho tinto e deixe evaporar o álcool (3 minutos)<br/>
    5. Adicione os tomates pelados esmagados com as mãos, o extrato de tomate e o louro<br/>
    6. Tempere com sal, pimenta e orégano. Adicione 1 xícara de água<br/>
    7. Cozinhe em fogo baixo, semi-tampado, por 45 minutos, mexendo ocasionalmente. 
       O molho deve reduzir e engrossar<br/>
    8. Nos últimos 5 minutos, adicione o manjericão fresco picado<br/><br/>
    
    <b>Modo de preparo do molho branco:</b><br/>
    1. Em uma panela média, derreta a manteiga em fogo médio-baixo<br/>
    2. Adicione a farinha de trigo de uma vez e mexa vigorosamente com fouet por 2 minutos 
       para formar um roux (pasta dourada)<br/>
    3. Adicione o leite aos poucos, mexendo constantemente para evitar grumos. 
       Comece com 1/4 do leite, incorpore bem, depois adicione o restante em 3 etapas<br/>
    4. Continue mexendo até engrossar e começar a ferver (8-10 minutos)<br/>
    5. Tempere com sal, pimenta branca e noz-moscada ralada na hora<br/>
    6. Cozinhe por mais 2 minutos e desligue. O molho deve ter consistência cremosa 
       que cubra as costas de uma colher<br/><br/>
    
    <b>Montagem da lasanha:</b><br/>
    1. Pré-aqueça o forno a 180°C<br/>
    2. Unte um refratário grande (35x25cm) com manteiga<br/>
    3. Espalhe 2 conchas de molho bolonhesa no fundo<br/>
    4. Faça a primeira camada de massa para lasanha, sobrepondo levemente as placas<br/>
    5. Espalhe molho bolonhesa, depois molho branco, presunto e muçarela<br/>
    6. Repita as camadas: massa, bolonhesa, bechamel, presunto, muçarela<br/>
    7. Continue até terminar os ingredientes, finalizando com massa, bechamel e 
       uma camada generosa de queijos<br/>
    8. Polvilhe parmesão ralado por cima<br/>
    9. Cubra com papel alumínio e leve ao forno por 30 minutos<br/>
    10. Retire o papel alumínio e deixe gratinar por mais 15-20 minutos até dourar<br/>
    11. Deixe descansar 10 minutos antes de cortar para firmar as camadas<br/><br/>
    
    <b>Dicas da chef:</b><br/>
    • Para um molho mais rico, adicione 100ml de creme de leite ao molho branco<br/>
    • Se preferir massa fresca, compre 600g de massa fresca para lasanha<br/>
    • O segredo da lasanha cremosa é não economizar no molho branco<br/>
    • Pode congelar antes de assar por até 3 meses (descongele na geladeira)<br/>
    • Acompanha bem com salada verde simples com vinagrete balsâmico
    """
    story.append(Paragraph(lasanha, styles['BodyText']))
    
    story.append(PageBreak())
    
    # Receita 2: Bolo de Chocolate
    story.append(Paragraph("Bolo de Chocolate com Cobertura de Ganache", styles['Heading2']))
    
    bolo = """
    <b>Rendimento:</b> 12 fatias | <b>Tempo de preparo:</b> 1h 30min<br/><br/>
    
    <b>Ingredientes da massa:</b><br/>
    • 2 xícaras (chá) de farinha de trigo peneirada (280g)<br/>
    • 1 e 3/4 xícara (chá) de açúcar (350g)<br/>
    • 3/4 xícara (chá) de cacau em pó 100% (75g)<br/>
    • 2 ovos grandes em temperatura ambiente<br/>
    • 1 xícara (chá) de leite integral (240ml)<br/>
    • 1/2 xícara (chá) de óleo vegetal (120ml)<br/>
    • 2 colheres (chá) de essência de baunilha<br/>
    • 1 xícara (chá) de água fervente (240ml)<br/>
    • 2 colheres (chá) de fermento em pó<br/>
    • 1 colher (chá) de bicarbonato de sódio<br/>
    • 1/2 colher (chá) de sal<br/><br/>
    
    <b>Ingredientes da ganache:</b><br/>
    • 300g de chocolate meio amargo picado (50-60% cacau)<br/>
    • 300ml de creme de leite fresco<br/>
    • 2 colheres (sopa) de manteiga sem sal<br/>
    • 1 colher (sopa) de mel ou glucose<br/><br/>
    
    <b>Modo de preparo da massa:</b><br/>
    1. Pré-aqueça o forno a 180°C. Unte e enfarinhe duas formas redondas de 20cm<br/>
    2. Em uma tigela grande, peneire juntos a farinha, açúcar, cacau, fermento, 
       bicarbonato e sal. Mexa bem para incorporar<br/>
    3. Em outra tigela, bata os ovos levemente com um fouet<br/>
    4. Adicione o leite, óleo e baunilha aos ovos. Misture bem<br/>
    5. Faça um buraco no centro dos ingredientes secos e despeje os líquidos<br/>
    6. Mexa delicadamente com uma espátula até começar a incorporar<br/>
    7. Adicione a água fervente aos poucos, mexendo suavemente. A massa ficará 
       bem líquida - isso é normal e desejável para um bolo muito úmido<br/>
    8. Divida a massa entre as duas formas<br/>
    9. Asse por 30-35 minutos ou até que um palito saia limpo do centro<br/>
    10. Deixe esfriar nas formas por 10 minutos, depois desenforme sobre uma grade 
        e deixe esfriar completamente (importante para não derreter a cobertura)<br/><br/>
    
    <b>Modo de preparo da ganache:</b><br/>
    1. Pique o chocolate em pedaços pequenos e uniformes e coloque em uma tigela<br/>
    2. Aqueça o creme de leite em uma panela até começar a ferver nas bordas 
       (não deixe ferver completamente)<br/>
    3. Despeje o creme quente sobre o chocolate e deixe descansar por 2 minutos 
       sem mexer<br/>
    4. Mexa delicadamente do centro para as bordas até obter uma mistura lisa e brilhante<br/>
    5. Adicione a manteiga e o mel, mexendo até incorporar completamente<br/>
    6. Deixe a ganache esfriar em temperatura ambiente por 20-30 minutos até 
       atingir consistência de creme espesso (ideal para espalhar)<br/><br/>
    
    <b>Montagem do bolo:</b><br/>
    1. Coloque a primeira camada de bolo em um prato ou base giratória<br/>
    2. Espalhe uma camada generosa de ganache (cerca de 1/3) sobre o bolo<br/>
    3. Cubra com a segunda camada de bolo, pressionando levemente<br/>
    4. Use o restante da ganache para cobrir o topo e as laterais do bolo<br/>
    5. Para um acabamento profissional, use uma espátula lisa e passe pela lateral 
       enquanto gira a base. Alise o topo com movimentos circulares<br/>
    6. Decore com raspas de chocolate, morangos frescos ou deixe a ganache lisa<br/>
    7. Leve à geladeira por pelo menos 1 hora antes de servir para firmar a cobertura<br/><br/>
    
    <b>Dicas importantes:</b><br/>
    • O segredo deste bolo é a água fervente, que ativa o cacau e deixa a massa úmida<br/>
    • Use cacau em pó de qualidade (não achocolatado) para sabor intenso<br/>
    • Todos os ingredientes devem estar em temperatura ambiente para massa homogênea<br/>
    • Não abra o forno nos primeiros 25 minutos para o bolo não murchar<br/>
    • Para variação, adicione 1 xícara de café forte no lugar da água<br/>
    • O bolo fica ainda melhor no dia seguinte quando os sabores se integram<br/>
    • Pode ser congelado por até 3 meses (sem cobertura)
    """
    story.append(Paragraph(bolo, styles['BodyText']))
    
    story.append(PageBreak())
    
    # Receita 3: Risoto
    story.append(Paragraph("Risoto de Funghi Porcini com Parmesão", styles['Heading2']))
    
    risoto = """
    <b>Rendimento:</b> 4 porções | <b>Tempo de preparo:</b> 45 minutos<br/><br/>
    
    <b>Ingredientes:</b><br/>
    • 30g de funghi porcini secos<br/>
    • 1 e 1/2 xícara de arroz arbóreo (300g)<br/>
    • 1 litro de caldo de legumes caseiro (ou galinha)<br/>
    • 1 cebola pequena picada finamente<br/>
    • 3 dentes de alho picados<br/>
    • 1/2 xícara de vinho branco seco (120ml)<br/>
    • 100g de manteiga sem sal (divida em 50g + 50g)<br/>
    • 100g de parmesão ralado na hora<br/>
    • 2 colheres (sopa) de azeite extra virgem<br/>
    • Salsinha fresca picada<br/>
    • Sal e pimenta-do-reino moída na hora<br/><br/>
    
    <b>Modo de preparo:</b><br/>
    1. Hidrate os funghi porcini em 1 xícara de água morna por 20 minutos. 
       Reserve a água (coe com papel toalha para remover areia). Pique os cogumelos<br/>
    2. Em uma panela, aqueça o caldo até ferver, depois mantenha em fogo baixo (quente)<br/>
    3. Em uma panela funda e larga (tipo caçarola), aqueça o azeite e 50g de manteiga<br/>
    4. Refogue a cebola em fogo médio por 5 minutos até ficar translúcida (não dourar)<br/>
    5. Adicione o alho e refogue por 1 minuto<br/>
    6. Junte os funghi porcini picados e refogue por 2 minutos<br/>
    7. Adicione o arroz arbóreo e mexa bem para "nacarar" - cada grão deve ficar 
       brilhante e levemente tostado (2-3 minutos). Não pare de mexer<br/>
    8. Despeje o vinho branco e mexa até evaporar completamente o álcool (2 minutos)<br/>
    9. Adicione a água dos funghi coada e mexa até ser absorvida<br/>
    10. Comece a adicionar o caldo quente: 1 concha por vez, mexendo constantemente 
        em movimentos circulares. Só adicione mais caldo quando o anterior for 
        quase totalmente absorvido<br/>
    11. Continue o processo por 18-20 minutos. O arroz deve ficar "al dente" 
        (levemente firme ao morder) e o risoto cremoso, não seco nem muito aguado<br/>
    12. Desligue o fogo e adicione os 50g de manteiga restantes e o parmesão ralado<br/>
    13. Mexa vigorosamente por 1 minuto para "mantecare" (criar cremosidade)<br/>
    14. Tampe e deixe descansar por 2 minutos<br/>
    15. Sirva imediatamente polvilhado com parmesão extra e salsinha fresca<br/><br/>
    
    <b>Técnica profissional:</b><br/>
    • A técnica "nacarar" (tostar o arroz) é essencial - selará o amido externo<br/>
    • Nunca adicione todo o caldo de uma vez - o processo gradual libera o amido<br/>
    • Mexa constantemente mas sem pressionar o arroz (evita quebrar os grãos)<br/>
    • O movimento correto é circular, "arrastando" o arroz do fundo para cima<br/>
    • Teste o ponto após 16 minutos - o arroz deve ter resistência leve ao morder<br/>
    • O "mantecare" final é o segredo da cremosidade - mexa com energia!<br/>
    • Risoto não espera: deve ser servido imediatamente após pronto<br/><br/>
    
    <b>Variações:</b><br/>
    • Adicione 200g de cogumelos frescos (shiitake, shimeji) junto com os porcini<br/>
    • Para versão com carne: acrescente 150g de bacon em cubos no início do refogado<br/>
    • Risoto primavera: substitua funghi por aspargos e ervilhas frescas<br/>
    • Use caldo de cogumelos secos para intensificar o sabor umami
    """
    story.append(Paragraph(risoto, styles['BodyText']))
    
    doc.build(story)
    print(f"✅ PDF criado: {output_path}")
    return output_path


def criar_pdf_manual_futebol(output_path: Path):
    """
    Cria um PDF com regras e táticas de futebol.
    
    Conteúdo: Regras oficiais, formações táticas, termos técnicos.
    Propósito: Testar busca de informações específicas sobre esportes.
    """
    doc = SimpleDocTemplate(str(output_path), pagesize=letter)
    styles = getSampleStyleSheet()
    story = []
    
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor='darkgreen',
        spaceAfter=30,
        alignment=TA_CENTER
    )
    
    story.append(Paragraph("Manual Completo de Futebol", title_style))
    story.append(Paragraph("Regras, Táticas e Estratégias", title_style))
    story.append(Spacer(1, 0.5*inch))
    
    # Regras Básicas
    story.append(Paragraph("Regras Oficiais da FIFA", styles['Heading2']))
    
    regras = """
    <b>Dimensões do Campo:</b><br/>
    O campo de futebol deve ter formato retangular com as seguintes dimensões:<br/>
    • Comprimento: mínimo de 90m e máximo de 120m<br/>
    • Largura: mínimo de 45m e máximo de 90m<br/>
    • Campos internacionais: 100-110m x 64-75m<br/>
    • Área de meta: 18,32m x 5,5m em frente ao gol<br/>
    • Área de grande penalidade: 40,32m x 16,5m<br/>
    • Círculo central: raio de 9,15m<br/>
    • Marca de pênalti: 11m da linha de gol<br/><br/>
    
    <b>Número de Jogadores:</b><br/>
    • Cada equipe é composta por 11 jogadores (incluindo o goleiro)<br/>
    • Mínimo de 7 jogadores para iniciar ou continuar a partida<br/>
    • Máximo de 3-5 substituições por jogo (varia conforme a competição)<br/>
    • Substituição só pode ser feita com a bola fora de jogo e autorização do árbitro<br/>
    • Jogador substituído não pode retornar (exceto em competições amadoras)<br/><br/>
    
    <b>Duração da Partida:</b><br/>
    • Dois tempos de 45 minutos cada (total de 90 minutos)<br/>
    • Intervalo de 15 minutos entre os tempos<br/>
    • Acréscimos determinados pelo árbitro para compensar paralisações<br/>
    • Prorrogação de 30 minutos (dois tempos de 15) em caso de empate em eliminatórias<br/>
    • Disputa de pênaltis após prorrogação se persistir empate<br/><br/>
    
    <b>Início e Reinício do Jogo:</b><br/>
    • Sorteio define quem escolhe lado do campo ou pontapé inicial<br/>
    • Bola deve ser chutada para frente do círculo central<br/>
    • Adversários devem estar fora do círculo central (9,15m)<br/>
    • Após gol, time que sofreu o gol faz o reinício<br/>
    • Tiros de meta quando a bola sai pela linha de fundo após toque do ataque<br/>
    • Escanteio quando a bola sai pela linha de fundo após toque da defesa<br/>
    • Arremesso lateral quando a bola cruza completamente a linha lateral<br/><br/>
    
    <b>Regra do Impedimento:</b><br/>
    Um jogador está em posição de impedimento se:<br/>
    1. Estiver mais próximo da linha de gol adversária que a bola e o penúltimo adversário<br/>
    2. Estiver na metade do campo adversário<br/>
    3. Estiver participando ativamente da jogada (tocando na bola, interferindo no adversário ou tirando vantagem)<br/>
    
    Não há impedimento quando o jogador recebe a bola diretamente de:<br/>
    • Tiro de meta<br/>
    • Arremesso lateral<br/>
    • Escanteio<br/>
    
    O impedimento é marcado no momento do passe, não quando o jogador recebe a bola.<br/><br/>
    
    <b>Faltas e Conduta Incorreta:</b><br/>
    Falta direta (tiro livre direto ou pênalti se dentro da área):<br/>
    • Chutar ou tentar chutar adversário<br/>
    • Derrubar ou tentar derrubar (rasteira, carrinho por trás)<br/>
    • Pular sobre adversário<br/>
    • Carregar violentamente<br/>
    • Segurar, empurrar adversário<br/>
    • Tocar a bola com as mãos deliberadamente (exceto goleiro na área)<br/>
    
    Falta indireta (tiro livre indireto):<br/>
    • Jogo perigoso sem contato<br/>
    • Obstrução do progresso do adversário<br/>
    • Goleiro segurar a bola por mais de 6 segundos<br/>
    • Goleiro tocar a bola com as mãos após recuo intencional de companheiro<br/><br/>
    
    <b>Cartões:</b><br/>
    <b>Cartão Amarelo (advertência):</b><br/>
    • Conduta antidesportiva<br/>
    • Desaprovar com palavras ou gestos<br/>
    • Retardar o reinício do jogo<br/>
    • Não respeitar distância no tiro livre<br/>
    • Entrar/sair do campo sem autorização<br/>
    
    <b>Cartão Vermelho (expulsão):</b><br/>
    • Falta violenta grave<br/>
    • Cuspir em alguém<br/>
    • Negar oportunidade clara de gol com falta ou mão<br/>
    • Linguagem ou gestos ofensivos<br/>
    • Receber segundo cartão amarelo na mesma partida<br/>
    
    Jogador expulso não pode ser substituído (time fica com 10 jogadores).
    """
    story.append(Paragraph(regras, styles['BodyText']))
    
    story.append(PageBreak())
    
    # Formações Táticas
    story.append(Paragraph("Formações Táticas Clássicas", styles['Heading2']))
    
    taticas = """
    <b>4-4-2 (Formação Equilibrada Clássica):</b><br/>
    A formação mais tradicional e equilibrada do futebol moderno.<br/>
    
    Estrutura:<br/>
    • 4 defensores: 2 laterais (direito e esquerdo) + 2 zagueiros centrais<br/>
    • 4 meio-campistas: 2 alas (direita e esquerda) + 2 volantes/meias centrais<br/>
    • 2 atacantes: dupla de centroavantes<br/>
    
    Características:<br/>
    • Boa cobertura defensiva com linha de 4 zagueiros<br/>
    • Meio-campo povoado permite controle do jogo<br/>
    • Dupla de ataque facilita cruzamentos e jogadas aéreas<br/>
    • Laterais têm liberdade para apoiar o ataque<br/>
    • Compacta: distância curta entre linhas (ideal 10-12 metros)<br/>
    
    Variação 4-4-2 losango:<br/>
    • 1 volante de contenção<br/>
    • 2 meias laterais<br/>
    • 1 meia armador (ponta do losango)<br/>
    • Mais controle no meio, menos largura<br/><br/>
    
    <b>4-3-3 (Formação Ofensiva com Wingers):</b><br/>
    Formação ofensiva popularizada pelo Barcelona e Liverpool.<br/>
    
    Estrutura:<br/>
    • 4 defensores: mesma linha do 4-4-2<br/>
    • 3 meio-campistas: 1 volante + 2 meias (ou 2 volantes + 1 meia)<br/>
    • 3 atacantes: 1 centroavante + 2 extremos/pontas (abertos)<br/>
    
    Características:<br/>
    • Alta amplitude ofensiva (três atacantes abertos)<br/>
    • Domínio de posse com triângulos no meio-campo<br/>
    • Pontas cortam para dentro ou ficam abertos para receber<br/>
    • Exige laterais com boa condição física (cobrem toda a lateral)<br/>
    • Volante crucial como "pivô" entre defesa e ataque<br/>
    
    Variação 4-3-3 falso 9:<br/>
    • Centroavante recua para criar espaço<br/>
    • Pontas infiltram na área deixada pelo 9<br/>
    • Meia armador sobe para ocupar posição de 10<br/><br/>
    
    <b>3-5-2 (Formação com Ala-defensores):</b><br/>
    Sistema com três zagueiros e domínio do meio-campo.<br/>
    
    Estrutura:<br/>
    • 3 defensores: zagueiro central (líbero) + 2 zagueiros laterais<br/>
    • 5 meio-campistas: 2 alas (wing-backs) + 3 meio-campistas centrais<br/>
    • 2 atacantes: dupla de centroavantes<br/>
    
    Características:<br/>
    • Superioridade numérica no meio-campo (5 vs 4 ou 5 vs 3)<br/>
    • Alas têm função híbrida (defesa e ataque)<br/>
    • Zagueiros centrais podem marcar individualmente ou em zona<br/>
    • Exige excelente condicionamento dos alas<br/>
    • Eficaz contra times com 1 atacante<br/>
    
    Pontos fracos:<br/>
    • Vulnerável nas costas dos alas quando estes sobem<br/>
    • Espaços entre zagueiros se marcação for individual<br/><br/>
    
    <b>4-2-3-1 (Formação Moderna de Controle):</b><br/>
    Sistema tático mais usado por seleções nas últimas Copas do Mundo.<br/>
    
    Estrutura:<br/>
    • 4 defensores: linha tradicional<br/>
    • 2 volantes: dupla de contenção<br/>
    • 3 meio-atacantes: 2 meias abertos + 1 meia central (camisa 10)<br/>
    • 1 centroavante: referência fixa<br/>
    
    Características:<br/>
    • Dupla de volantes protege a defesa<br/>
    • Meia central (#10) tem liberdade criativa<br/>
    • Transições rápidas com meias abertos em velocidade<br/>
    • Centroavante segura a bola e finaliza<br/>
    • Compacto defensivamente, fluido no ataque<br/>
    
    Varia para 4-4-2 na defesa:<br/>
    • Meia central recua para linha do meio<br/>
    • Meias abertos fecham como alas<br/>
    • Atacante não fica isolado (meia dá apoio)<br/><br/>
    
    <b>Conceitos Táticos Modernos:</b><br/>
    
    <b>Marcação por Zona:</b><br/>
    • Cada jogador responsável por uma zona do campo<br/>
    • Marca o adversário que entrar em sua zona<br/>
    • Mantém organização espacial do time<br/>
    • Dificulta movimentação adversária<br/>
    
    <b>Marcação Individual:</b><br/>
    • Cada defensor marca um atacante específico<br/>
    • Segue o adversário por todo o campo<br/>
    • Usado em bolas paradas<br/>
    • Arriscado: pode ser desorganizado com movimentações<br/>
    
    <b>Marcação Pressão:</b><br/>
    • Pressionar adversário com a bola imediatamente<br/>
    • Reduzir tempo e espaço para pensar<br/>
    • Forçar erros e recuperar bola no campo de ataque<br/>
    • Exige condicionamento físico excepcional<br/>
    • Popularizado por Klopp (Gegenpressing)<br/>
    
    <b>Transições Rápidas (Contra-ataque):</b><br/>
    • Velocidade na passagem defesa-ataque<br/>
    • Aproveitar desorganização adversária<br/>
    • Lançamentos longos ou passes rápidos<br/>
    • Jogadores velozes nas pontas<br/>
    
    <b>Posse de Bola (Tiki-Taka):</b><br/>
    • Manter posse com passes curtos<br/>
    • Movimentação constante sem bola<br/>
    • Triângulos de passe (3 jogadores próximos)<br/>
    • Cansar adversário e controlar ritmo<br/>
    • Popularizado pelo Barcelona de Guardiola
    """
    story.append(Paragraph(taticas, styles['BodyText']))
    
    doc.build(story)
    print(f"✅ PDF criado: {output_path}")
    return output_path


def criar_pdf_documentacao_tecnica(output_path: Path):
    """
    Cria um PDF com documentação técnica de API.
    
    Conteúdo: Documentação de API REST fictícia.
    Propósito: Testar busca de endpoints, parâmetros e códigos de erro.
    """
    doc = SimpleDocTemplate(str(output_path), pagesize=letter)
    styles = getSampleStyleSheet()
    story = []
    
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor='darkblue',
        spaceAfter=30,
        alignment=TA_CENTER
    )
    
    code_style = ParagraphStyle(
        'Code',
        parent=styles['BodyText'],
        fontName='Courier',
        fontSize=9,
        leftIndent=20,
        spaceAfter=10
    )
    
    story.append(Paragraph("Documentação da API", title_style))
    story.append(Paragraph("E-commerce Platform REST API v2.0", title_style))
    story.append(Spacer(1, 0.5*inch))
    
    intro = """
    <b>Visão Geral:</b><br/>
    Esta documentação descreve os endpoints da API REST do nosso sistema de e-commerce. 
    A API utiliza autenticação via JWT (JSON Web Tokens) e retorna dados no formato JSON.
    Base URL: https://api.exemplo.com/v2<br/><br/>
    
    <b>Autenticação:</b><br/>
    Todas as requisições (exceto /auth/login) devem incluir o header:<br/>
    Authorization: Bearer {seu_token_jwt}<br/><br/>
    
    <b>Rate Limiting:</b><br/>
    • 100 requisições por minuto para usuários autenticados<br/>
    • 20 requisições por minuto para requisições anônimas<br/>
    • Header 'X-RateLimit-Remaining' indica quantas requisições restam<br/>
    """
    story.append(Paragraph(intro, styles['BodyText']))
    
    # Endpoints
    story.append(Paragraph("Endpoints de Produtos", styles['Heading2']))
    
    produtos = """
    <b>GET /products</b><br/>
    Retorna lista paginada de produtos.<br/><br/>
    
    <b>Query Parameters:</b><br/>
    • page (int, opcional): Número da página (padrão: 1)<br/>
    • limit (int, opcional): Items por página (padrão: 20, máximo: 100)<br/>
    • category (string, opcional): Filtrar por categoria<br/>
    • min_price (float, opcional): Preço mínimo<br/>
    • max_price (float, opcional): Preço máximo<br/>
    • sort (string, opcional): Ordenação (price_asc, price_desc, name, newest)<br/><br/>
    
    <b>Exemplo de Requisição:</b><br/>
    """
    story.append(Paragraph(produtos, styles['BodyText']))
    
    code1 = """
GET /products?category=eletronicos&min_price=1000&sort=price_asc&page=1&limit=10
    """
    story.append(Paragraph(code1, code_style))
    
    response1 = """
    <b>Resposta 200 OK:</b><br/>
    """
    story.append(Paragraph(response1, styles['BodyText']))
    
    json1 = """
{
  "data": [
    {
      "id": "prod_12345",
      "name": "Smartphone Galaxy S23 Ultra",
      "description": "Tela 6.8' Dynamic AMOLED, 256GB",
      "price": 5999.99,
      "category": "eletronicos",
      "stock": 45,
      "images": ["https://cdn.exemplo.com/img1.jpg"],
      "created_at": "2024-01-15T10:30:00Z"
    }
  ],
  "pagination": {
    "current_page": 1,
    "total_pages": 15,
    "total_items": 150,
    "per_page": 10
  }
}
    """
    story.append(Paragraph(json1, code_style))
    
    story.append(Spacer(1, 0.2*inch))
    
    get_product = """
    <b>GET /products/{product_id}</b><br/>
    Retorna detalhes de um produto específico.<br/><br/>
    
    <b>Path Parameters:</b><br/>
    • product_id (string, obrigatório): ID único do produto<br/><br/>
    
    <b>Resposta 200 OK:</b> Objeto completo do produto com reviews e especificações<br/>
    <b>Resposta 404 Not Found:</b> Produto não encontrado<br/>
    """
    story.append(Paragraph(get_product, styles['BodyText']))
    
    story.append(PageBreak())
    
    story.append(Paragraph("Endpoints de Pedidos", styles['Heading2']))
    
    orders = """
    <b>POST /orders</b><br/>
    Cria um novo pedido.<br/><br/>
    
    <b>Request Body (JSON):</b><br/>
    """
    story.append(Paragraph(orders, styles['BodyText']))
    
    order_body = """
{
  "items": [
    {
      "product_id": "prod_12345",
      "quantity": 2,
      "price": 5999.99
    }
  ],
  "shipping_address": {
    "street": "Rua Exemplo, 123",
    "city": "São Paulo",
    "state": "SP",
    "zip_code": "01234-567"
  },
  "payment_method": "credit_card",
  "payment_details": {
    "card_token": "tok_xxxxxxxxxxxx"
  }
}
    """
    story.append(Paragraph(order_body, code_style))
    
    order_response = """
    <b>Resposta 201 Created:</b><br/>
    """
    story.append(Paragraph(order_response, styles['BodyText']))
    
    order_resp_json = """
{
  "order_id": "ord_67890",
  "status": "processing",
  "total_amount": 11999.98,
  "estimated_delivery": "2024-02-20",
  "tracking_code": null,
  "created_at": "2024-02-15T14:22:00Z"
}
    """
    story.append(Paragraph(order_resp_json, code_style))
    
    errors = """
    <b>Códigos de Erro Comuns:</b><br/>
    • 400 Bad Request: Dados inválidos no body<br/>
    • 401 Unauthorized: Token ausente ou inválido<br/>
    • 403 Forbidden: Sem permissão para acessar recurso<br/>
    • 404 Not Found: Recurso não encontrado<br/>
    • 422 Unprocessable Entity: Validação falhou (ex: estoque insuficiente)<br/>
    • 429 Too Many Requests: Rate limit excedido<br/>
    • 500 Internal Server Error: Erro no servidor<br/>
    """
    story.append(Paragraph(errors, styles['BodyText']))
    
    doc.build(story)
    print(f"✅ PDF criado: {output_path}")
    return output_path


def gerar_todos_pdfs(output_dir=None):
    """
    Gera todos os PDFs de exemplo de uma vez.
    
    Args:
        output_dir: Diretório onde os PDFs serão salvos.
                   Se None, usa data/pdfs/ relativo ao script.
    """
    if output_dir is None:
        output_dir = Path(__file__).parent.parent.parent / "data" / "pdfs"
    
    output_dir.mkdir(parents=True, exist_ok=True)
    
    print("🚀 Gerando PDFs de exemplo...\n")
    
    pdf_files = []
    
    pdf_files.append(criar_pdf_manual_smartphone(output_dir / "manual_iphone15.pdf"))
    pdf_files.append(criar_pdf_receitas(output_dir / "livro_receitas.pdf"))
    pdf_files.append(criar_pdf_manual_futebol(output_dir / "manual_futebol.pdf"))
    pdf_files.append(criar_pdf_documentacao_tecnica(output_dir / "api_documentation.pdf"))
    
    print(f"\n✅ Todos os PDFs foram criados em: {output_dir}")
    print("\nPDFs gerados:")
    print("  1. manual_iphone15.pdf - Manual técnico de smartphone")
    print("  2. livro_receitas.pdf - Receitas culinárias detalhadas")
    print("  3. manual_futebol.pdf - Regras e táticas de futebol")
    print("  4. api_documentation.pdf - Documentação técnica de API")
    
    return pdf_files


if __name__ == "__main__":
    # Executar este arquivo diretamente para gerar os PDFs
    gerar_todos_pdfs()
