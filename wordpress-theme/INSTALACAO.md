# Instalação do Tema WordPress - Insights Ambiental

Este tema personalizado replica exatamente o header e footer do site principal para que o blog WordPress pareça estar integrado ao site.

## Estrutura de Arquivos

```
wordpress-theme/
├── header.php          # Header idêntico ao site principal
├── footer.php           # Footer idêntico ao site principal
├── functions.php        # Funções do tema
├── index.php            # Template principal
├── single.php           # Template de post individual
├── style.css            # Arquivo de estilo do tema
└── INSTALACAO.md        # Este arquivo
```

## Instalação

### Opção 1: Via FTP/cPanel

1. **Acesse o servidor WordPress via FTP ou cPanel File Manager**

2. **Navegue até a pasta de temas:**
   ```
   /wp-content/themes/
   ```

3. **Crie uma nova pasta chamada `insights-ambiental`:**
   ```
   /wp-content/themes/insights-ambiental/
   ```

4. **Faça upload de todos os arquivos do tema para esta pasta:**
   - `header.php`
   - `footer.php`
   - `functions.php`
   - `index.php`
   - `single.php`
   - `style.css`

5. **Ative o tema:**
   - Acesse WordPress Admin > Aparência > Temas
   - Encontre "Insights Ambiental"
   - Clique em "Ativar"

### Opção 2: Via WordPress Admin (se tiver acesso)

1. **Compacte a pasta `wordpress-theme` em um arquivo ZIP**

2. **Acesse WordPress Admin > Aparência > Temas > Adicionar Novo**

3. **Clique em "Enviar tema"**

4. **Selecione o arquivo ZIP e clique em "Instalar agora"**

5. **Ative o tema após a instalação**

## Configuração

### 1. Verificar URLs

O tema usa URLs absolutas para o site principal. Certifique-se de que as URLs estão corretas:

- **Site principal:** `https://www.insightsambiental.com.br/`
- **Imagens:** `https://www.insightsambiental.com.br/images/`

Se necessário, edite os arquivos `header.php` e `footer.php` para ajustar as URLs.

### 2. Configurar Menu de Navegação

O header já está configurado com os links corretos:
- Início → `https://www.insightsambiental.com.br/`
- Sobre → `https://www.insightsambiental.com.br/#sobre`
- Serviços → `https://www.insightsambiental.com.br/#servicos`
- Áreas de Atuação → `https://www.insightsambiental.com.br/#areas`
- Blog → Link do WordPress (dinâmico)
- Contato → `https://www.insightsambiental.com.br/#contato`

### 3. Personalizar Estilos (Opcional)

Se precisar ajustar estilos, edite:
- `header.php` - Estilos do header
- `footer.php` - Estilos do footer
- `functions.php` - Estilos do conteúdo dos posts

## Características do Tema

✅ **Header fixo** - Igual ao site principal
✅ **Footer idêntico** - Com informações de contato
✅ **Botão WhatsApp flutuante** - Mesmo estilo e posição
✅ **Navegação responsiva** - Funciona em mobile e desktop
✅ **Estilos consistentes** - Mesmas cores e tipografia

## Compatibilidade

- WordPress 5.0+
- PHP 7.4+
- Navegadores modernos (Chrome, Firefox, Safari, Edge)

## Suporte

Se tiver problemas com a instalação:

1. Verifique se todos os arquivos foram enviados corretamente
2. Certifique-se de que o tema está ativado
3. Limpe o cache do WordPress (se usar plugin de cache)
4. Verifique as permissões dos arquivos (644 para arquivos, 755 para pastas)

## Notas Importantes

- O tema usa URLs absolutas para imagens e recursos do site principal
- O header e footer são fixos e não podem ser editados via Customizer
- Para edições, modifique diretamente os arquivos PHP
- Faça backup antes de fazer alterações

