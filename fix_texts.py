#!/usr/bin/env python3
import re

with open('assets/index-Cfil0XwF.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Substituição 1: Desde 2011 produzindo trabalhos técnicos de excelência com equipe multidisciplinar
# O texto pode estar quebrado no arquivo minificado, então vamos procurar por partes
content = re.sub(
    r'Desde 2011 produzindo trabalhos t[^"]*cnicos de excel[^"]*ncia com equipe multidisciplinar',
    'Desde 2011, sinônimo de excelência em trabalhos técnicos com uma equipe multidisciplinar especializada',
    content
)

# Também tentar sem acentos que podem estar codificados diferente
content = re.sub(
    r'Desde 2011 produzindo trabalhos t[^"]*cnicos de excel[^"]*ncia com equipe multidisciplinar',
    'Desde 2011, sinônimo de excelência em trabalhos técnicos com uma equipe multidisciplinar especializada',
    content,
    flags=re.IGNORECASE
)

# Substituição 2: bióloga, engenheiros, advogados, arquitetos e arboristas trabalhando de forma integrada
content = re.sub(
    r'bióloga, engenheiros, advogados, arquitetos e arboristas trabalhando de forma integrada',
    'Bióloga, Engenheiros, Advogados, Arquitetos e Arboristas trabalhando de forma integrada',
    content
)

# Verificar se a substituição funcionou
if 'Desde 2011, sinônimo' in content:
    print('✓ Substituição 1 concluída')
else:
    print('✗ Substituição 1 não encontrada - tentando abordagem alternativa')
    # Tentar substituir apenas a parte que encontramos
    content = content.replace('Desde 2011 produzindo trabalhos t', 'Desde 2011, sinônimo de excelência em trabalhos técnicos com uma equipe multidisciplinar especializada'.split('trabalhos')[0] + 'trabalhos t')

if 'Bióloga, Engenheiros, Advogados, Arquitetos e Arboristas' in content:
    print('✓ Substituição 2 concluída')
else:
    print('✗ Substituição 2 não encontrada')

with open('assets/index-Cfil0XwF.js', 'w', encoding='utf-8') as f:
    f.write(content)

print('Processo concluído')

