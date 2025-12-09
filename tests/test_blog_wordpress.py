"""
Teste para verificar a integração do blog com WordPress
"""
import requests
import json
from pathlib import Path

# URLs
WORDPRESS_API_URL = "https://insightsambiental.com.br/wp-json/wp/v2/posts"
BLOG_INDEX_PATH = Path(__file__).parent.parent / "blog" / "index.html"


def test_wordpress_api_accessible():
    """Testa se a API do WordPress está acessível"""
    print("🔍 Testando acessibilidade da API do WordPress...")
    try:
        response = requests.get(WORDPRESS_API_URL, timeout=10)
        assert response.status_code == 200, f"API retornou status {response.status_code}"
        print(f"✅ API acessível (status: {response.status_code})")
        return True
    except requests.exceptions.RequestException as e:
        print(f"❌ Erro ao acessar API: {e}")
        return False


def test_wordpress_api_returns_posts():
    """Testa se a API retorna posts"""
    print("\n🔍 Testando se a API retorna posts...")
    try:
        response = requests.get(f"{WORDPRESS_API_URL}?per_page=1", timeout=10)
        assert response.status_code == 200, f"API retornou status {response.status_code}"
        data = response.json()
        assert isinstance(data, list), "Resposta não é uma lista"
        print(f"✅ API retorna posts (tipo: {type(data).__name__})")
        if len(data) > 0:
            print(f"   📝 Encontrado {len(data)} post(s) no teste")
            print(f"   📌 Primeiro post: {data[0].get('title', {}).get('rendered', 'Sem título')}")
        return True
    except Exception as e:
        print(f"❌ Erro ao verificar posts: {e}")
        return False


def test_wordpress_api_with_embed():
    """Testa se a API retorna dados com _embed (para imagens)"""
    print("\n🔍 Testando API com parâmetro _embed...")
    try:
        response = requests.get(f"{WORDPRESS_API_URL}?per_page=1&_embed=true", timeout=10)
        assert response.status_code == 200, f"API retornou status {response.status_code}"
        data = response.json()
        if len(data) > 0:
            post = data[0]
            has_embed = "_embedded" in post
            print(f"✅ API com _embed funcionando: {has_embed}")
            if has_embed:
                print(f"   📸 Dados de embed disponíveis")
            return True
        return True
    except Exception as e:
        print(f"❌ Erro ao testar _embed: {e}")
        return False


def test_blog_index_exists():
    """Testa se o arquivo blog/index.html existe"""
    print("\n🔍 Verificando se blog/index.html existe...")
    if BLOG_INDEX_PATH.exists():
        print(f"✅ Arquivo encontrado: {BLOG_INDEX_PATH}")
        return True
    else:
        print(f"❌ Arquivo não encontrado: {BLOG_INDEX_PATH}")
        return False


def test_blog_index_contains_api_url():
    """Testa se o arquivo contém a URL da API correta"""
    print("\n🔍 Verificando se blog/index.html contém a URL da API...")
    try:
        content = BLOG_INDEX_PATH.read_text(encoding='utf-8')
        assert WORDPRESS_API_URL in content, "URL da API não encontrada no arquivo"
        print(f"✅ URL da API encontrada no arquivo")
        return True
    except Exception as e:
        print(f"❌ Erro ao verificar arquivo: {e}")
        return False


def test_blog_index_contains_fetch():
    """Testa se o arquivo contém código de fetch"""
    print("\n🔍 Verificando se blog/index.html contém código de fetch...")
    try:
        content = BLOG_INDEX_PATH.read_text(encoding='utf-8')
        assert "fetch" in content.lower(), "Código de fetch não encontrado"
        assert "loadPosts" in content or "async" in content, "Função de carregamento não encontrada"
        print(f"✅ Código de fetch encontrado")
        return True
    except Exception as e:
        print(f"❌ Erro ao verificar código: {e}")
        return False


def test_cors_headers():
    """Testa se há headers CORS (opcional)"""
    print("\n🔍 Verificando headers CORS...")
    try:
        response = requests.get(WORDPRESS_API_URL, timeout=10)
        cors_header = response.headers.get('Access-Control-Allow-Origin')
        if cors_header:
            print(f"✅ CORS configurado: {cors_header}")
        else:
            print("⚠️  CORS não configurado (pode causar problemas no navegador)")
        return True
    except Exception as e:
        print(f"❌ Erro ao verificar CORS: {e}")
        return False


def main():
    """Executa todos os testes"""
    print("=" * 60)
    print("TESTE DE INTEGRAÇÃO BLOG WORDPRESS")
    print("=" * 60)
    
    results = []
    
    # Testes da API
    results.append(("API Acessível", test_wordpress_api_accessible()))
    results.append(("API Retorna Posts", test_wordpress_api_returns_posts()))
    results.append(("API com _embed", test_wordpress_api_with_embed()))
    results.append(("CORS Headers", test_cors_headers()))
    
    # Testes do arquivo
    results.append(("Arquivo Existe", test_blog_index_exists()))
    results.append(("Contém URL API", test_blog_index_contains_api_url()))
    results.append(("Contém Fetch", test_blog_index_contains_fetch()))
    
    # Resumo
    print("\n" + "=" * 60)
    print("RESUMO DOS TESTES")
    print("=" * 60)
    
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for name, result in results:
        status = "✅ PASSOU" if result else "❌ FALHOU"
        print(f"{status}: {name}")
    
    print(f"\n📊 Resultado: {passed}/{total} testes passaram")
    
    if passed == total:
        print("🎉 Todos os testes passaram!")
        return 0
    else:
        print("⚠️  Alguns testes falharam. Verifique os erros acima.")
        return 1


if __name__ == "__main__":
    exit(main())

