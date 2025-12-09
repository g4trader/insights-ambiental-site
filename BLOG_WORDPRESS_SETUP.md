# Configuração do Blog WordPress

## O que foi implementado

Foi criada a página `/blog/index.html` que carrega automaticamente os posts do WordPress através da API REST.

## Como funciona

A página faz uma requisição para a API REST do WordPress em:
```
https://insightsambiental.com.br/wp-json/wp/v2/posts
```

A página exibe:
- Lista de posts em cards responsivos
- Imagem destacada de cada post (se disponível)
- Título, data de publicação e autor
- Resumo do conteúdo
- Link para o post completo no WordPress

## Configurações necessárias no WordPress

### 1. Verificar se a API REST está habilitada

A API REST do WordPress geralmente está habilitada por padrão. Para verificar, acesse:
```
https://insightsambiental.com.br/wp-json/wp/v2/posts
```

Se retornar uma lista de posts em JSON, está funcionando corretamente.

### 2. Configurar CORS (se necessário)

Se houver problemas de CORS ao carregar os posts, você pode precisar adicionar um plugin ou configuração no WordPress para permitir requisições do domínio `www.insightsambiental.com.br`.

**Opção 1: Plugin**
- Instale um plugin como "CORS Headers" ou "REST API - Filter Fields"

**Opção 2: Adicionar no functions.php do tema**
```php
add_action('rest_api_init', function() {
    remove_filter('rest_pre_serve_request', 'rest_send_cors_headers');
    add_filter('rest_pre_serve_request', function($value) {
        header('Access-Control-Allow-Origin: *');
        header('Access-Control-Allow-Methods: GET');
        header('Access-Control-Allow-Credentials: true');
        return $value;
    });
}, 15);
```

### 3. Configurar imagens destacadas

Para que as imagens dos posts apareçam, certifique-se de:
- Definir uma imagem destacada para cada post no WordPress
- A API retorna as imagens através do parâmetro `_embed=true` na URL

### 4. Verificar permissões de leitura

A API REST do WordPress permite leitura pública por padrão. Se você tiver posts privados ou protegidos por senha, eles não aparecerão na lista.

## Personalização

### Alterar número de posts exibidos

No arquivo `blog/index.html`, linha ~470, altere:
```javascript
const POSTS_PER_PAGE = 12;
```

### Alterar URL da API

No arquivo `blog/index.html`, linha ~469, altere:
```javascript
const WORDPRESS_API_URL = 'https://insightsambiental.com.br/wp-json/wp/v2/posts';
```

### Filtrar posts por categoria

Para exibir apenas posts de uma categoria específica, adicione o parâmetro `categories` na URL:
```javascript
const url = `${WORDPRESS_API_URL}?per_page=${POSTS_PER_PAGE}&_embed=true&categories=1`;
```

Onde `1` é o ID da categoria no WordPress.

## Testando

1. Acesse `https://www.insightsambiental.com.br/blog/`
2. A página deve carregar os posts do WordPress automaticamente
3. Se não carregar, verifique o console do navegador (F12) para ver erros

## Troubleshooting

### Erro: "Failed to fetch"
- Verifique se a URL da API está correta
- Verifique se há problemas de CORS
- Verifique se o WordPress está acessível

### Posts não aparecem
- Verifique se há posts publicados no WordPress
- Verifique se a API REST está retornando dados: `https://insightsambiental.com.br/wp-json/wp/v2/posts`
- Verifique o console do navegador para erros

### Imagens não aparecem
- Certifique-se de que cada post tem uma imagem destacada definida
- Verifique se a API está retornando `_embedded` com as imagens

## Estrutura de arquivos

```
/blog/
  ├── index.html    # Página principal do blog (lista de posts)
  └── ods.html      # Artigo estático sobre ODS
```

## Próximos passos (opcional)

1. Adicionar paginação para exibir mais posts
2. Adicionar filtros por categoria ou tag
3. Adicionar busca de posts
4. Adicionar página de detalhes do post (atualmente os links abrem no WordPress)

