# Como Forçar Atualização do Tema WordPress

Se você não está vendo as mudanças após atualizar o tema, siga estes passos:

## 1. Limpar Cache do WordPress

1. Acesse o painel administrativo do WordPress
2. Se você tiver plugins de cache instalados (WP Super Cache, W3 Total Cache, etc.):
   - Vá em **Configurações** > **WP Super Cache** (ou plugin de cache que você usa)
   - Clique em **Excluir Cache** ou **Limpar Cache**

## 2. Limpar Cache do Navegador

- **Chrome/Edge**: Pressione `Ctrl+Shift+R` (Windows) ou `Cmd+Shift+R` (Mac)
- **Firefox**: Pressione `Ctrl+F5` (Windows) ou `Cmd+Shift+R` (Mac)
- Ou abra o DevTools (F12) > aba Network > marque "Disable cache"

## 3. Verificar se o Tema está Ativo

1. Vá em **Aparência** > **Temas**
2. Certifique-se de que o tema "Insights Ambiental" está ativo
3. Se necessário, desative e reative o tema

## 4. Verificar Arquivos do Tema

Certifique-se de que os arquivos foram atualizados corretamente no servidor:
- `wp-content/themes/insights-ambiental/header.php`
- `wp-content/themes/insights-ambiental/style.css`

## 5. Mudanças Aplicadas (v1.1.0)

- ✅ Menu "Blog" alterado para "Artigos"
- ✅ Link do menu aponta para `/artigos`
- ✅ Logo ajustada para `max-height: 60px` (igual ao site principal)

## 6. Verificar no Código

Abra o código-fonte da página (Ctrl+U) e procure por:
- Texto "Artigos" no menu (não "Blog")
- `max-height: 60px` no CSS da logo
- Link `href="https://www.insightsambiental.com.br/artigos"`

Se ainda não aparecer, pode ser cache do servidor. Entre em contato com o suporte de hospedagem.

