# Configuração de Sitemap para SEO

## Estrutura de Sitemaps Implementada

### 1. Sitemap Index (`sitemap-index.xml`)
O sitemap index combina todos os sitemaps do site:
- **Sitemap do site estático** (`sitemap.xml`) - Páginas principais do site na Vercel
- **Sitemap do WordPress** (`wp-sitemap.xml`) - Posts e páginas do blog WordPress

### 2. Sitemap do Site Estático (`sitemap.xml`)
Inclui as páginas principais:
- Home (`/`) - Prioridade 1.0
- Artigos (`/artigos`) - Prioridade 0.9

### 3. Robots.txt
Atualizado para referenciar todos os sitemaps:
- Sitemap index (principal)
- Sitemap do site estático
- Sitemap do WordPress

## URLs Incluídas no Sitemap

### Site Estático (Vercel)
- `https://insightsambiental.com.br/` - Home page
- `https://insightsambiental.com.br/artigos` - Página de artigos

### WordPress
- Gerenciado automaticamente pelo WordPress
- Inclui todos os posts, páginas, categorias e tags

## Próximos Passos para Melhorar SEO

### 1. Enviar Sitemap para o Google Search Console
1. Acesse [Google Search Console](https://search.google.com/search-console)
2. Adicione a propriedade `insightsambiental.com.br`
3. Vá em **Sitemaps**
4. Adicione: `https://insightsambiental.com.br/sitemap-index.xml`

### 2. Enviar Sitemap para o Bing Webmaster Tools
1. Acesse [Bing Webmaster Tools](https://www.bing.com/webmasters)
2. Adicione o site
3. Envie o sitemap: `https://insightsambiental.com.br/sitemap-index.xml`

### 3. Verificar Meta Tags
Certifique-se de que todas as páginas têm:
- `<title>` único e descritivo
- `<meta name="description">` com 150-160 caracteres
- `<link rel="canonical">` apontando para a URL canônica
- Open Graph tags para redes sociais

### 4. Estrutura de Dados (Schema.org)
A home já tem Schema.org para Organization. Considere adicionar:
- **Article** para posts do blog
- **BreadcrumbList** para navegação
- **LocalBusiness** se aplicável

### 5. Performance
- Verificar Core Web Vitals no Google Search Console
- Otimizar imagens (WebP, lazy loading)
- Minificar CSS e JavaScript

### 6. Links Internos
- Garantir que todas as páginas importantes estão linkadas
- Usar texto âncora descritivo
- Criar uma estrutura de navegação clara

### 7. Conteúdo
- Publicar conteúdo regularmente no blog
- Usar palavras-chave relevantes naturalmente
- Criar conteúdo de qualidade e útil para o público-alvo

## Manutenção

### Atualizar Sitemap
O sitemap do site estático deve ser atualizado quando:
- Novas páginas são adicionadas ao site estático
- A estrutura do site muda

O sitemap do WordPress é atualizado automaticamente quando:
- Novos posts são publicados
- Páginas são criadas ou modificadas

### Verificar Sitemaps
- Teste os sitemaps em: https://www.xml-sitemaps.com/validate-xml-sitemap.html
- Verifique no Google Search Console se há erros

## URLs Importantes

- **Sitemap Index**: https://insightsambiental.com.br/sitemap-index.xml
- **Sitemap Estático**: https://insightsambiental.com.br/sitemap.xml
- **Sitemap WordPress**: https://insightsambiental.com.br/wp-sitemap.xml
- **Robots.txt**: https://insightsambiental.com.br/robots.txt

