images = [
  "https://www.saobernardo.sp.gov.br/image/journal/article?img_id=1884658&t=1712093806454", 
  "https://static.ndmais.com.br/2023/08/bocha.jpeg",
  "https://www.funcel.org.br/arquivos/Image/Funcel/Comunicacao/SITE/bocha1.jpg",
  "https://tanabi.sp.gov.br/media/capas/fed15f87fe418d8836516a234a6b95a5.jpeg",
  "https://piracicaba.sp.gov.br/wp-content/uploads/kceditor/images/bocha.jpg",
  "https://clubepaineiras.org.br/wp-content/uploads/2016/07/Esporte-Bocha-800x533.jpg"
]

import random
def get_random_duration():
  return random.randint(1, 8)

def get_random_review():
  return random.randint(1, 500)

def get_random_image(list):
  listLength = len(list)
  
  random_quantity = random.randint(1, listLength)
  random_selection = random.sample(list, k=random_quantity)
  
  return random_selection


mockProducts = [
  {
    "id": 1,
    "images": get_random_image(images),
    "location": "Horizontina, RS",
    "address": "Rua Placeholder, 101",
    "dateRange": "Out 22 - 24",
    "price": 60,
    "rating": 4.91,
    "currency": "R$",
    "reviews": get_random_review(),
    "details": "Cancha familiar com 2 quadras de bocha, sem bar, 1 banheiro. Disponibilidade da modalidade 48.",
    "description": "Bem-vindos à Cancha do Zé! Localizada em Horizontina, esta cancha é perfeita para encontros familiares e prática casual. Possuímos duas quadras cobertas, mantidas com carinho. Embora não tenhamos serviço de bar, você pode trazer suas próprias bebidas. O local é conhecido por ser ideal para quem busca tranquilidade e espaço para a modalidade '48'."
  },
  {
    "id": 2,
    "images": get_random_image(images),
    "location": "Porto Alegre, RS",
    "address": "Av. Example, 202",
    "dateRange": "Out 22 - 24",
    "price": 60,
    "rating": 4.91,
    "discountPercentage": 50,
    "discountDuration": get_random_duration(),
    "currency": "R$",
    "reviews": get_random_review(),
    "details": "Estrutura moderna no centro. Possui 4 canchas e bar completo. 3 banheiros e área de descanso.",
    "description": "O Bocha Club Central oferece uma experiência premium no coração de Porto Alegre. Nossa estrutura é moderna, com quatro canchas climatizadas e um bar completo que serve desde petiscos a drinks especiais. É o local ideal para happy hour com amigos ou para torneios corporativos. Fácil acesso e ampla área de descanso."
  },
  {
    "id": 3,
    "images": get_random_image(images),
    "location": "Canoas, RS",
    "address": "Rua Fictícia, 303",
    "dateRange": "Out 25 - 27",
    "price": 80,
    "rating": 4.85,
    "discountPercentage": 65,
    "discountDuration": get_random_duration(),
    "currency": "R$",
    "reviews": get_random_review(),
    "details": "Espaço de bocha com 3 quadras e serviço de bar. Inclui 2 banheiros e permite a prática de 48.",
    "description": "A Cancha Três Marias é um ponto de encontro tradicional em Canoas. Oferecemos três quadras bem cuidadas, ideais para o jogo de bocha e a modalidade 48. Nosso bar serve lanches rápidos e bebidas geladas. O ambiente é acolhedor e perfeito para quem busca diversão e competitividade em um só lugar."
  },
  {
    "id": 4,
    "images": get_random_image(images),
    "location": "Canoas, RS",
    "address": "Rua Fictícia, 404",
    "dateRange": "Out 28 - 30",
    "price": 100,
    "rating": 4.95,
    "currency": "R$",
    "reviews": get_random_review(),
    "details": "Clube com foco em competições, possui 6 canchas oficiais. Sem bar, mas com vending machines. 4 banheiros.",
    "description": "O Complexo Olímpico de Bocha é focado em treinamento e competições de alto nível. Com seis canchas oficiais, oferecemos o piso perfeito para o desempenho máximo. Não há bar, mas máquinas de venda automática estão disponíveis. É o lugar certo para atletas sérios e amantes do esporte que buscam excelência."
},
  {
    "id": 5,
    "images": get_random_image(images),
    "location": "Ijuí, RS",
    "address": "Rua do Comércio, 789",
    "dateRange": "Nov 01 - 04",
    "price": 45,
    "rating": 4.72,
    "currency": "R$",
    "reviews": get_random_review(),
    "details": "Cancha simples e tradicional, ideal para iniciantes. 1 quadra, sem bar. 1 banheiro. Não oferece 48.",
    "description": "A Cancha do Bairro é um local acolhedor e com preço acessível em Ijuí. Com apenas uma quadra, é perfeita para iniciantes que querem aprender as regras do bocha sem pressão. É um local simples, sem bar, mas onde a comunidade se reúne. Focamos no bocha tradicional e não oferecemos a modalidade 48."
},
  {
    "id": 6,
    "images": get_random_image(images),
    "location": "Ijuí, RS",
    "address": "Rua do Comércio, 789",
    "dateRange": "Nov 05 - 07",
    "price": 55,
    "rating": 4.68,
    "currency": "R$",
    "reviews": get_random_review(),
    "details": "Ambiente coberto com 2 canchas. Bar e petiscos disponíveis. 2 banheiros limpos. Possui 48.",
    "description": "O Galpão da Bocha oferece um ambiente coberto e protegido do clima, garantindo o jogo em qualquer estação. Contamos com duas canchas e um bar que serve petiscos deliciosos. A infraestrutura inclui banheiros limpos e é um dos poucos locais na região que suporta o jogo '48'."
},
  {
    "id": 7,
    "images": get_random_image(images),
    "location": "Santo Ângelo, RS",
    "address": "Av. Brasil, 1010",
    "dateRange": "Nov 08 - 10",
    "price": 75,
    "rating": 4.88,
    "discountPercentage": 75,
    "discountDuration": get_random_duration(),
    "currency": "R$",
    "reviews": get_random_review(),
    "details": "Complexo esportivo com 5 canchas de alto padrão. Bar e restaurante no local. 5 banheiros, incluindo acessibilidade.",
    "description": "O Arena Bocha Santo Ângelo é o maior complexo da região, com cinco canchas de alto padrão e tecnologia. Nossos serviços vão além do jogo, oferecendo um restaurante completo e bar. Perfeito para grandes eventos e conta com total acessibilidade e banheiros modernos."
  },
  {
    "id": 8,
    "images": get_random_image(images),
    "location": "Cruz Alta, RS",
    "address": "Rua General Osório, 300",
    "dateRange": "Nov 11 - 13",
    "price": 50,
    "rating": 4.65,
    "currency": "R$",
    "reviews": get_random_review(),
    "details": "Ótimo custo-benefício. 3 canchas abertas. Sem bar. 2 banheiros. Ideal para lazer.",
    "description": "A Cancha Aberta de Cruz Alta oferece três quadras ao ar livre, sendo uma excelente opção para dias de sol. O foco é lazer e diversão descompromissada. Não temos serviço de bar, mas a área permite que você traga seu próprio lanche e bebida. Preço baixo e diversão garantida!"
},
  {
    "id": 9,
    "images": get_random_image(images),
    "location": "Santa Maria, RS",
    "address": "Estrada do Morro, s/n",
    "dateRange": "Nov 14 - 16",
    "price": 90,
    "rating": 4.92,
    "currency": "R$",
    "reviews": get_random_review(),
    "details": "Cancha com vista panorâmica. 2 quadras. Bar com cervejas artesanais. 2 banheiros. Oferece 48.",
    "description": "Localizada no topo do morro, a Cancha Mirante oferece uma experiência única de jogo com uma vista espetacular de Santa Maria. São duas quadras e um bar especializado em cervejas artesanais. O pôr do sol aqui é o cenário perfeito para a bocha ou para a modalidade 48."
},
  {
    "id": 10,
    "images": get_random_image(images),
    "location": "Pelotas, RS",
    "address": "Praça Coronel Pedro Osório, 1",
    "dateRange": "Nov 17 - 19",
    "price": 110,
    "rating": 4.96,
    "discountPercentage": 55,
    "discountDuration": get_random_duration(),
    "currency": "R$",
    "reviews": get_random_review(),
    "details": "Clube tradicional com 4 canchas e serviço completo de alimentação. 4 banheiros e estacionamento amplo. Possui 48.",
    "description": "Fundado em 1950, o Clube da Bocha Pelotense é a tradição do esporte na cidade. Contamos com quatro canchas históricas, mas muito bem conservadas. Oferecemos serviço completo de restaurante, ideal para almoços e jantares após o jogo. É o ambiente perfeito para quem aprecia a história do bocha e a modalidade 48."
  },
  {
    "id": 11,
    "images": get_random_image(images),
    "location": "Rio Grande, RS",
    "address": "Av. Atlântica, 2500",
    "dateRange": "Nov 20 - 22",
    "price": 85,
    "rating": 4.89,
    "currency": "R$",
    "reviews": get_random_review(),
    "details": "Bocha à beira-mar (coberta). 2 canchas. Bar de drinks e petiscos. 3 banheiros. Sem 48.",
    "description": "Desfrute do bocha com a brisa do mar no Bocha Marítimo. Nossas duas quadras são cobertas para garantir a diversão, faça chuva ou faça sol. Temos um bar especializado em drinks e petiscos de verão. Embora não ofereçamos a modalidade 48, a experiência de jogo perto do oceano é inigualável."
},
  {
    "id": 12,
    "images": get_random_image(images),
    "location": "Passo Fundo, RS",
    "address": "Campus Universitário",
    "dateRange": "Nov 23 - 25",
    "price": 65,
    "rating": 4.78,
    "currency": "R$",
    "reviews": get_random_review(),
    "details": "Cancha dentro de área universitária, ambiente jovem. 1 quadra. Vending machines. 2 banheiros.",
    "description": "A Cancha Universitária é o ponto de encontro dos estudantes e jovens de Passo Fundo. Com uma única quadra, o ambiente é dinâmico e energético. Não há bar, mas máquinas de venda automática estão disponíveis. Ideal para um jogo rápido entre as aulas ou para quem busca um público mais jovem."
},
  {
    "id": 13,
    "images": get_random_image(images),
    "location": "Horizontina, RS",
    "address": "Linha 15, Interior",
    "dateRange": "Nov 26 - 28",
    "price": 40,
    "rating": 4.6,
    "discountPercentage": 60,
    "discountDuration": get_random_duration(),
    "currency": "R$",
    "reviews": get_random_review(),
    "details": "Cancha rústica e acolhedora. 2 quadras. Bar com comidas típicas. 1 banheiro. Possui 48.",
    "description": "Para uma experiência autêntica, visite a Cancha da Linha 15 no interior de Horizontina. Ambiente rústico, mas muito acolhedor, com duas quadras. Nosso bar é famoso pelas comidas típicas gaúchas e petiscos caseiros. É o lugar perfeito para um bocha raiz e onde a modalidade 48 é sempre bem-vinda."
  },
  {
    "id": 14,
    "images": get_random_image(images),
    "location": "Caxias do Sul, RS",
    "address": "Rua das Indústrias, 1234",
    "dateRange": "Nov 29 - Dez 01",
    "price": 120,
    "rating": 4.98,
    "currency": "R$",
    "reviews": get_random_review(),
    "details": "Instalações de luxo. 3 canchas climatizadas. Bar premium e 6 banheiros. Área VIP e modalidade 48.",
    "description": "A Bocha Prime é o auge do luxo em Caxias do Sul. Oferecemos três canchas climatizadas com a mais alta tecnologia de piso. Nosso bar premium tem uma carta de vinhos e destilados exclusiva. Perfeito para eventos de alto padrão ou para quem exige o melhor em conforto e serviço. Inclui área VIP e suporte para a modalidade 48."
},
  {
    "id": 15,
    "images": get_random_image(images),
    "location": "Novo Hamburgo, RS",
    "address": "Rua das Fábricas, 567",
    "dateRange": "Dez 02 - 04",
    "price": 70,
    "rating": 4.82,
    "currency": "R$",
    "reviews": get_random_review(),
    "details": "Bocha em galpão industrial reformado. 2 canchas modernas. Bar básico. 2 banheiros. Possui 48.",
    "description": "A Cancha Industrial oferece um toque moderno e descolado. Localizada em um galpão reformado, possui duas quadras com piso de concreto polido. O bar é básico, mas eficiente. Ideal para quem procura um ambiente diferente para jogar bocha e praticar a modalidade 48."
},
]