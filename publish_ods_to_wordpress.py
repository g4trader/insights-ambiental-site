#!/usr/bin/env python3
"""
Script para publicar o artigo sobre ODS no WordPress via API REST
"""
import requests
import json
from datetime import datetime

# Configurações
WORDPRESS_URL = "https://insightsambiental.com.br"
API_ENDPOINT = f"{WORDPRESS_URL}/wp-json/wp/v2/posts"

# Credenciais do WordPress (você precisa criar uma Application Password)
# Acesse: WordPress Admin > Usuários > Seu Perfil > Application Passwords
USERNAME = input("Digite seu usuário do WordPress: ").strip()
PASSWORD = input("Digite sua Application Password do WordPress: ").strip()

# Conteúdo do artigo em HTML
POST_CONTENT = """<h2>O Que São os ODS?</h2>
<p>Os Objetivos de Desenvolvimento Sustentável (ODS) são uma coleção de 17 objetivos globais estabelecidos pela Organização das Nações Unidas em 2015. Fazem parte da Agenda 2030 para o Desenvolvimento Sustentável, um plano de ação para as pessoas, o planeta e a prosperidade.</p>

<p><img class="aligncenter size-full wp-image-1" src="https://insightsambiental.com.br/images/ods-capa.jpg" alt="Os 17 Objetivos de Desenvolvimento Sustentável da ONU" /></p>

<p>Os ODS foram criados para substituir os Objetivos de Desenvolvimento do Milênio (ODM) e abrangem questões de desenvolvimento social e econômico, incluindo pobreza, fome, saúde, educação, mudanças climáticas, igualdade de gênero, água, saneamento, energia, urbanização, meio ambiente e justiça social.</p>

<h2>Estatísticas dos ODS</h2>
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 1.5rem; margin: 2rem 0;">
<div style="background: #f0fdf4; padding: 1.5rem; border-radius: 0.5rem; text-align: center; border: 2px solid #86efac;">
<div style="font-size: 2.5rem; font-weight: 700; color: #059669; margin-bottom: 0.5rem;">17</div>
<div style="font-size: 1rem; color: #047857;">Objetivos</div>
</div>
<div style="background: #f0fdf4; padding: 1.5rem; border-radius: 0.5rem; text-align: center; border: 2px solid #86efac;">
<div style="font-size: 2.5rem; font-weight: 700; color: #059669; margin-bottom: 0.5rem;">169</div>
<div style="font-size: 1rem; color: #047857;">Metas</div>
</div>
<div style="background: #f0fdf4; padding: 1.5rem; border-radius: 0.5rem; text-align: center; border: 2px solid #86efac;">
<div style="font-size: 2.5rem; font-weight: 700; color: #059669; margin-bottom: 0.5rem;">193</div>
<div style="font-size: 1rem; color: #047857;">Países</div>
</div>
<div style="background: #f0fdf4; padding: 1.5rem; border-radius: 0.5rem; text-align: center; border: 2px solid #86efac;">
<div style="font-size: 2.5rem; font-weight: 700; color: #059669; margin-bottom: 0.5rem;">2030</div>
<div style="font-size: 1rem; color: #047857;">Prazo</div>
</div>
</div>

<h2>Os 17 Objetivos</h2>
<div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 1.5rem; margin: 2rem 0;">
<div style="background: white; border: 2px solid #e5e7eb; border-left: 4px solid #E5243B; border-radius: 0.75rem; padding: 1.5rem;">
<div style="font-size: 2rem; font-weight: 700; color: #E5243B; margin-bottom: 0.5rem;">1</div>
<div style="font-size: 1.125rem; font-weight: 600; margin-bottom: 0.75rem; color: #1f2937;">Erradicação da Pobreza</div>
<div style="font-size: 0.875rem; color: #6b7280; line-height: 1.5;">Acabar com a pobreza em todas as suas formas, em todos os lugares.</div>
</div>
<div style="background: white; border: 2px solid #e5e7eb; border-left: 4px solid #DDA63A; border-radius: 0.75rem; padding: 1.5rem;">
<div style="font-size: 2rem; font-weight: 700; color: #DDA63A; margin-bottom: 0.5rem;">2</div>
<div style="font-size: 1.125rem; font-weight: 600; margin-bottom: 0.75rem; color: #1f2937;">Fome Zero e Agricultura Sustentável</div>
<div style="font-size: 0.875rem; color: #6b7280; line-height: 1.5;">Acabar com a fome, alcançar a segurança alimentar e melhoria da nutrição e promover a agricultura sustentável.</div>
</div>
<div style="background: white; border: 2px solid #e5e7eb; border-left: 4px solid #4C9F38; border-radius: 0.75rem; padding: 1.5rem;">
<div style="font-size: 2rem; font-weight: 700; color: #4C9F38; margin-bottom: 0.5rem;">3</div>
<div style="font-size: 1.125rem; font-weight: 600; margin-bottom: 0.75rem; color: #1f2937;">Saúde e Bem-Estar</div>
<div style="font-size: 0.875rem; color: #6b7280; line-height: 1.5;">Assegurar uma vida saudável e promover o bem-estar para todos, em todas as idades.</div>
</div>
<div style="background: white; border: 2px solid #e5e7eb; border-left: 4px solid #C5192D; border-radius: 0.75rem; padding: 1.5rem;">
<div style="font-size: 2rem; font-weight: 700; color: #C5192D; margin-bottom: 0.5rem;">4</div>
<div style="font-size: 1.125rem; font-weight: 600; margin-bottom: 0.75rem; color: #1f2937;">Educação de Qualidade</div>
<div style="font-size: 0.875rem; color: #6b7280; line-height: 1.5;">Assegurar a educação inclusiva e equitativa e de qualidade, e promover oportunidades de aprendizagem ao longo da vida para todos.</div>
</div>
<div style="background: white; border: 2px solid #e5e7eb; border-left: 4px solid #FF3A21; border-radius: 0.75rem; padding: 1.5rem;">
<div style="font-size: 2rem; font-weight: 700; color: #FF3A21; margin-bottom: 0.5rem;">5</div>
<div style="font-size: 1.125rem; font-weight: 600; margin-bottom: 0.75rem; color: #1f2937;">Igualdade de Gênero</div>
<div style="font-size: 0.875rem; color: #6b7280; line-height: 1.5;">Alcançar a igualdade de gênero e empoderar todas as mulheres e meninas.</div>
</div>
<div style="background: white; border: 2px solid #e5e7eb; border-left: 4px solid #26BDE2; border-radius: 0.75rem; padding: 1.5rem;">
<div style="font-size: 2rem; font-weight: 700; color: #26BDE2; margin-bottom: 0.5rem;">6</div>
<div style="font-size: 1.125rem; font-weight: 600; margin-bottom: 0.75rem; color: #1f2937;">Água Limpa e Saneamento</div>
<div style="font-size: 0.875rem; color: #6b7280; line-height: 1.5;">Garantir disponibilidade e manejo sustentável da água e saneamento para todos.</div>
</div>
<div style="background: white; border: 2px solid #e5e7eb; border-left: 4px solid #FCC30B; border-radius: 0.75rem; padding: 1.5rem;">
<div style="font-size: 2rem; font-weight: 700; color: #FCC30B; margin-bottom: 0.5rem;">7</div>
<div style="font-size: 1.125rem; font-weight: 600; margin-bottom: 0.75rem; color: #1f2937;">Energia Limpa e Acessível</div>
<div style="font-size: 0.875rem; color: #6b7280; line-height: 1.5;">Garantir acesso à energia barata, confiável, sustentável e renovável para todos.</div>
</div>
<div style="background: white; border: 2px solid #e5e7eb; border-left: 4px solid #A21942; border-radius: 0.75rem; padding: 1.5rem;">
<div style="font-size: 2rem; font-weight: 700; color: #A21942; margin-bottom: 0.5rem;">8</div>
<div style="font-size: 1.125rem; font-weight: 600; margin-bottom: 0.75rem; color: #1f2937;">Trabalho Decente e Crescimento Econômico</div>
<div style="font-size: 0.875rem; color: #6b7280; line-height: 1.5;">Promover o crescimento econômico sustentado, inclusivo e sustentável, emprego pleno e produtivo e trabalho decente para todos.</div>
</div>
<div style="background: white; border: 2px solid #e5e7eb; border-left: 4px solid #FD6925; border-radius: 0.75rem; padding: 1.5rem;">
<div style="font-size: 2rem; font-weight: 700; color: #FD6925; margin-bottom: 0.5rem;">9</div>
<div style="font-size: 1.125rem; font-weight: 600; margin-bottom: 0.75rem; color: #1f2937;">Indústria, Inovação e Infraestrutura</div>
<div style="font-size: 0.875rem; color: #6b7280; line-height: 1.5;">Construir infraestruturas resilientes, promover a industrialização inclusiva e sustentável e fomentar a inovação.</div>
</div>
<div style="background: white; border: 2px solid #e5e7eb; border-left: 4px solid #DD1367; border-radius: 0.75rem; padding: 1.5rem;">
<div style="font-size: 2rem; font-weight: 700; color: #DD1367; margin-bottom: 0.5rem;">10</div>
<div style="font-size: 1.125rem; font-weight: 600; margin-bottom: 0.75rem; color: #1f2937;">Redução das Desigualdades</div>
<div style="font-size: 0.875rem; color: #6b7280; line-height: 1.5;">Reduzir a desigualdade dentro dos países e entre eles.</div>
</div>
<div style="background: white; border: 2px solid #e5e7eb; border-left: 4px solid #FD9D24; border-radius: 0.75rem; padding: 1.5rem;">
<div style="font-size: 2rem; font-weight: 700; color: #FD9D24; margin-bottom: 0.5rem;">11</div>
<div style="font-size: 1.125rem; font-weight: 600; margin-bottom: 0.75rem; color: #1f2937;">Cidades e Comunidades Sustentáveis</div>
<div style="font-size: 0.875rem; color: #6b7280; line-height: 1.5;">Tornar as cidades e os assentamentos humanos inclusivos, seguros, resilientes e sustentáveis.</div>
</div>
<div style="background: white; border: 2px solid #e5e7eb; border-left: 4px solid #BF8B2E; border-radius: 0.75rem; padding: 1.5rem;">
<div style="font-size: 2rem; font-weight: 700; color: #BF8B2E; margin-bottom: 0.5rem;">12</div>
<div style="font-size: 1.125rem; font-weight: 600; margin-bottom: 0.75rem; color: #1f2937;">Consumo e Produção Responsáveis</div>
<div style="font-size: 0.875rem; color: #6b7280; line-height: 1.5;">Garantir padrões de produção e de consumo sustentáveis.</div>
</div>
<div style="background: white; border: 2px solid #e5e7eb; border-left: 4px solid #3F7E44; border-radius: 0.75rem; padding: 1.5rem;">
<div style="font-size: 2rem; font-weight: 700; color: #3F7E44; margin-bottom: 0.5rem;">13</div>
<div style="font-size: 1.125rem; font-weight: 600; margin-bottom: 0.75rem; color: #1f2937;">Ação Contra a Mudança Global do Clima</div>
<div style="font-size: 0.875rem; color: #6b7280; line-height: 1.5;">Tomar medidas urgentes para combater a mudança climática e seus impactos.</div>
</div>
<div style="background: white; border: 2px solid #e5e7eb; border-left: 4px solid #0A97D9; border-radius: 0.75rem; padding: 1.5rem;">
<div style="font-size: 2rem; font-weight: 700; color: #0A97D9; margin-bottom: 0.5rem;">14</div>
<div style="font-size: 1.125rem; font-weight: 600; margin-bottom: 0.75rem; color: #1f2937;">Vida na Água</div>
<div style="font-size: 0.875rem; color: #6b7280; line-height: 1.5;">Conservar e promover o uso sustentável dos oceanos, dos mares e dos recursos marinhos para o desenvolvimento sustentável.</div>
</div>
<div style="background: white; border: 2px solid #e5e7eb; border-left: 4px solid #56C02B; border-radius: 0.75rem; padding: 1.5rem;">
<div style="font-size: 2rem; font-weight: 700; color: #56C02B; margin-bottom: 0.5rem;">15</div>
<div style="font-size: 1.125rem; font-weight: 600; margin-bottom: 0.75rem; color: #1f2937;">Vida Terrestre</div>
<div style="font-size: 0.875rem; color: #6b7280; line-height: 1.5;">Proteger, recuperar e promover o uso sustentável dos ecossistemas terrestres, gerir de forma sustentável as florestas, combater a desertificação, deter e reverter a degradação da terra e deter a perda de biodiversidade.</div>
</div>
<div style="background: white; border: 2px solid #e5e7eb; border-left: 4px solid #00689D; border-radius: 0.75rem; padding: 1.5rem;">
<div style="font-size: 2rem; font-weight: 700; color: #00689D; margin-bottom: 0.5rem;">16</div>
<div style="font-size: 1.125rem; font-weight: 600; margin-bottom: 0.75rem; color: #1f2937;">Paz, Justiça e Instituições Eficazes</div>
<div style="font-size: 0.875rem; color: #6b7280; line-height: 1.5;">Promover sociedades pacíficas e inclusivas para o desenvolvimento sustentável, proporcionar o acesso à justiça para todos e construir instituições eficazes, responsáveis e inclusivas em todos os níveis.</div>
</div>
<div style="background: white; border: 2px solid #e5e7eb; border-left: 4px solid #19486A; border-radius: 0.75rem; padding: 1.5rem;">
<div style="font-size: 2rem; font-weight: 700; color: #19486A; margin-bottom: 0.5rem;">17</div>
<div style="font-size: 1.125rem; font-weight: 600; margin-bottom: 0.75rem; color: #1f2937;">Parcerias e Meios de Implementação</div>
<div style="font-size: 0.875rem; color: #6b7280; line-height: 1.5;">Fortalecer os meios de implementação e revitalizar a parceria global para o desenvolvimento sustentável.</div>
</div>
</div>

<h2>Por Que os ODS São Importantes?</h2>
<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 1.5rem; margin: 2rem 0;">
<div style="background: #f9fafb; padding: 2rem; border-radius: 0.75rem; border-left: 4px solid #059669;">
<h3 style="margin-top: 0; color: #059669;">🌍 Impacto Global</h3>
<p>Os ODS abordam os desafios mais urgentes que a humanidade enfrenta, desde a pobreza até as mudanças climáticas, criando um plano de ação unificado para todos os países.</p>
</div>
<div style="background: #f9fafb; padding: 2rem; border-radius: 0.75rem; border-left: 4px solid #059669;">
<h3 style="margin-top: 0; color: #059669;">🤝 Colaboração</h3>
<p>Eles promovem a cooperação entre governos, empresas e sociedade civil para alcançar objetivos comuns, criando sinergias e maximizando o impacto das ações.</p>
</div>
<div style="background: #f9fafb; padding: 2rem; border-radius: 0.75rem; border-left: 4px solid #059669;">
<h3 style="margin-top: 0; color: #059669;">📊 Medição</h3>
<p>Cada objetivo tem metas específicas e indicadores mensuráveis, permitindo acompanhar o progresso e ajustar estratégias conforme necessário.</p>
</div>
</div>

<h2>Como Implementar os ODS?</h2>
<h3>Para Empresas</h3>
<p>As empresas podem integrar os ODS em suas estratégias de negócio, identificando quais objetivos são mais relevantes para suas operações e desenvolvendo ações concretas para contribuir com o alcance das metas.</p>

<h3>Para Governos</h3>
<p>Os governos devem alinhar suas políticas públicas com os ODS, criando planos nacionais de implementação e garantindo que as ações sejam coordenadas entre diferentes setores.</p>

<h3>Para Indivíduos</h3>
<p>Cada pessoa pode contribuir através de escolhas conscientes no consumo, participação em ações comunitárias e advocacy por políticas que promovam o desenvolvimento sustentável.</p>

<div style="background: linear-gradient(135deg, #059669 0%, #047857 100%); color: white; padding: 3rem; border-radius: 1rem; text-align: center; margin-top: 3rem;">
<h2 style="color: white; margin-bottom: 1rem;">Quer Saber Mais?</h2>
<p>Visite o site oficial da ONU para conhecer mais detalhes sobre cada objetivo e acompanhar o progresso global.</p>
<p><a href="https://www.un.org/sustainabledevelopment/" target="_blank" rel="noopener noreferrer" style="display: inline-block; background: white; color: #059669; padding: 1rem 2rem; border-radius: 0.5rem; text-decoration: none; font-weight: 600; margin-top: 1rem;">Visitar Site da ONU</a></p>
</div>"""

POST_EXCERPT = """Os Objetivos de Desenvolvimento Sustentável (ODS) são uma coleção de 17 objetivos globais estabelecidos pela Organização das Nações Unidas em 2015. Fazem parte da Agenda 2030 para o Desenvolvimento Sustentável, um plano de ação para as pessoas, o planeta e a prosperidade."""

def create_post():
    """Cria um novo post no WordPress"""
    
    # Dados do post
    post_data = {
        "title": "Os 17 Objetivos de Desenvolvimento Sustentável da ONU",
        "content": POST_CONTENT,
        "excerpt": POST_EXCERPT,
        "status": "publish",
        "slug": "os-17-objetivos-de-desenvolvimento-sustentavel-da-onu",
        "date": datetime.now().strftime("%Y-%m-%dT%H:%M:%S"),
        "categories": [],  # Adicione IDs de categorias se necessário
        "tags": [],  # Adicione IDs de tags se necessário
        "featured_media": 0,  # ID da imagem destacada (se já estiver no WordPress)
    }
    
    # Headers para autenticação
    headers = {
        "Content-Type": "application/json",
    }
    
    # Autenticação básica
    auth = (USERNAME, PASSWORD)
    
    print("📝 Publicando post no WordPress...")
    print(f"   URL: {API_ENDPOINT}")
    print(f"   Título: {post_data['title']}")
    
    try:
        response = requests.post(
            API_ENDPOINT,
            json=post_data,
            headers=headers,
            auth=auth,
            timeout=30
        )
        
        if response.status_code == 201:
            post = response.json()
            print(f"\n✅ Post criado com sucesso!")
            print(f"   ID: {post['id']}")
            print(f"   Link: {post['link']}")
            print(f"   Status: {post['status']}")
            return post
        else:
            print(f"\n❌ Erro ao criar post:")
            print(f"   Status: {response.status_code}")
            print(f"   Resposta: {response.text}")
            return None
            
    except requests.exceptions.RequestException as e:
        print(f"\n❌ Erro na requisição: {e}")
        return None


if __name__ == "__main__":
    print("=" * 60)
    print("PUBLICAÇÃO DE POST NO WORDPRESS")
    print("=" * 60)
    print("\n⚠️  IMPORTANTE: Você precisa criar uma Application Password no WordPress")
    print("   1. Acesse: WordPress Admin > Usuários > Seu Perfil")
    print("   2. Role até 'Application Passwords'")
    print("   3. Crie uma nova senha de aplicativo")
    print("   4. Use essa senha aqui (não sua senha normal)\n")
    
    result = create_post()
    
    if result:
        print("\n🎉 Publicação concluída com sucesso!")
    else:
        print("\n⚠️  Falha na publicação. Verifique as credenciais e tente novamente.")

