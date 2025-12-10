# Instruções para Atualizar o Cache do WordPress

Após atualizar o tema, é importante limpar todos os caches para que as mudanças sejam visíveis:

## 1. Limpar Cache do WordPress

### Se usar plugin de cache (WP Super Cache, W3 Total Cache, etc.):
1. Vá em **Plugins** > **Plugins Instalados**
2. Encontre o plugin de cache
3. Clique em **Limpar Cache** ou **Purge Cache**

### Se usar cache do servidor:
- Entre em contato com o provedor de hospedagem para limpar o cache do servidor

## 2. Limpar Cache do Navegador

### Chrome/Edge:
- Pressione `Ctrl + Shift + Delete` (Windows) ou `Cmd + Shift + Delete` (Mac)
- Selecione "Imagens e arquivos em cache"
- Clique em "Limpar dados"

### Firefox:
- Pressione `Ctrl + Shift + Delete` (Windows) ou `Cmd + Shift + Delete` (Mac)
- Selecione "Cache"
- Clique em "Limpar agora"

## 3. Atualizar o Tema no WordPress

1. Vá em **Aparência** > **Temas**
2. Certifique-se de que o tema "Insights Ambiental" está ativo
3. Se necessário, desative e reative o tema

## 4. Verificar a Versão do Tema

A versão atual do tema é: **1.2.0.20250129120000**

Para verificar:
1. Vá em **Aparência** > **Editor de Temas**
2. Abra o arquivo `style.css`
3. Verifique se a linha `Version:` mostra a versão acima

## 5. Forçar Atualização (Hard Refresh)

No navegador:
- **Windows**: `Ctrl + F5` ou `Ctrl + Shift + R`
- **Mac**: `Cmd + Shift + R`

## 6. Verificar se as Mudanças Foram Aplicadas

Após limpar o cache, verifique se:
- A barra verde superior (top bar) está visível e fixa no topo
- O header principal está posicionado abaixo da top bar (32px do topo)
- O logo tem o tamanho correto (60px de altura máxima)
- O menu mostra "Artigos" em vez de "Blog"
- O link "Artigos" aponta para `/artigos`

## Problemas Comuns

### Se as mudanças ainda não aparecem:

1. **Verifique se o tema está ativo**: Vá em **Aparência** > **Temas** e confirme que "Insights Ambiental" está ativo

2. **Desative plugins de cache temporariamente**: Alguns plugins podem estar servindo versões antigas em cache

3. **Verifique se há CDN**: Se o site usa CDN (Cloudflare, etc.), limpe o cache do CDN também

4. **Verifique o arquivo header.php**: Certifique-se de que o arquivo `header.php` foi atualizado corretamente no servidor

5. **Teste em modo anônimo**: Abra o site em uma janela anônima/privada para evitar cache do navegador

## Contato

Se após seguir todos os passos as mudanças ainda não aparecerem, entre em contato com o suporte técnico.

