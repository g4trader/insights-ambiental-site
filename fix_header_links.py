#!/usr/bin/env python3
import re

with open('assets/index-Cfil0XwF.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Corrigir todas as 4 ocorrências de Nu com <a> dentro

# 1. Menu desktop - Início (linha 46)
pattern1 = r'N\.jsxDEV\(Nu,\{"data-loc":"client/src/components/Header\.tsx:46",href:"/",children:N\.jsxDEV\("a",\{"data-loc":"client/src/components/Header\.tsx:47",className:`([^`]+)`,children:([^}]+)\},void 0,[^)]+\)\},void 0,[^)]+\)'

def fix_desktop_home(match):
    className = match.group(1)
    children = match.group(2)
    return f'N.jsxDEV(Nu,{{"data-loc":"client/src/components/Header.tsx:46",href:"/",className:`{className}`,children:{children}}},void 0,!1,{{"fileName":"/home/ubuntu/insights-ambiental/client/src/components/Header.tsx","lineNumber":46,"columnNumber":13}},this)'

content = re.sub(pattern1, fix_desktop_home, content)

# 2. Menu desktop - Blog (linha 73)
pattern2 = r'N\.jsxDEV\(Nu,\{"data-loc":"client/src/components/Header\.tsx:73",href:"/blog",children:N\.jsxDEV\("a",\{"data-loc":"client/src/components/Header\.tsx:74",className:`([^`]+)`,children:([^}]+)\},void 0,[^)]+\)\},void 0,[^)]+\)'

def fix_desktop_blog(match):
    className = match.group(1)
    children = match.group(2)
    return f'N.jsxDEV(Nu,{{"data-loc":"client/src/components/Header.tsx:73",href:"/blog",className:`{className}`,children:{children}}},void 0,!1,{{"fileName":"/home/ubuntu/insights-ambiental/client/src/components/Header.tsx","lineNumber":73,"columnNumber":13}},this)'

content = re.sub(pattern2, fix_desktop_blog, content)

# 3. Menu mobile - Início (linha 105)
pattern3 = r'N\.jsxDEV\(Nu,\{"data-loc":"client/src/components/Header\.tsx:105",href:"/",children:N\.jsxDEV\("a",\{"data-loc":"client/src/components/Header\.tsx:106",onClick:\(\)=>s\(!1\),className:`([^`]+)`,children:([^}]+)\},void 0,[^)]+\)\},void 0,[^)]+\)'

def fix_mobile_home(match):
    className = match.group(1)
    children = match.group(2)
    return f'N.jsxDEV(Nu,{{"data-loc":"client/src/components/Header.tsx:105",href:"/",onClick:()=>s(!1),className:`{className}`,children:{children}}},void 0,!1,{{"fileName":"/home/ubuntu/insights-ambiental/client/src/components/Header.tsx","lineNumber":105,"columnNumber":15}},this)'

content = re.sub(pattern3, fix_mobile_home, content)

# 4. Menu mobile - Blog (linha 133)
pattern4 = r'N\.jsxDEV\(Nu,\{"data-loc":"client/src/components/Header\.tsx:133",href:"/blog",children:N\.jsxDEV\("a",\{"data-loc":"client/src/components/Header\.tsx:134",onClick:\(\)=>s\(!1\),className:`([^`]+)`,children:([^}]+)\},void 0,[^)]+\)\},void 0,[^)]+\)'

def fix_mobile_blog(match):
    className = match.group(1)
    children = match.group(2)
    return f'N.jsxDEV(Nu,{{"data-loc":"client/src/components/Header.tsx:133",href:"/blog",onClick:()=>s(!1),className:`{className}`,children:{children}}},void 0,!1,{{"fileName":"/home/ubuntu/insights-ambiental/client/src/components/Header.tsx","lineNumber":133,"columnNumber":15}},this)'

content = re.sub(pattern4, fix_mobile_blog, content)

# Salvar
with open('assets/index-Cfil0XwF.js', 'w', encoding='utf-8') as f:
    f.write(content)

# Verificar
remaining = len(list(re.finditer(r'N\.jsxDEV\(Nu[^}]*children:[^}]*N\.jsxDEV\("a"', content)))
print(f'✓ Correções aplicadas! Ocorrências restantes: {remaining}')

