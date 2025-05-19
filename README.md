# 📘 Plataforma de Ensino Interativa em Python

Este é um sistema de ensino interativo em Python com autenticação de usuários, visualização de módulos/aulas e aplicação de questionários. Ele simula uma pequena plataforma de estudos em linha de comando.

## 📂 Estrutura do Projeto

- `main.py` – Arquivo principal do sistema.
- `usuarios.json` – Armazena os usuários cadastrados com senha criptografada.
- `modulos.json` – Contém os dados dos módulos, aulas e questionários.

## 🔐 Funcionalidades

- Cadastro e login de usuários com senhas criptografadas (SHA-256).
- Acesso a módulos organizados com:
  - Vídeos e resumos de aulas.
  - Questionários interativos com correção automática.
- Sistema de pontuação e feedback baseado no desempenho nos testes.

## ▶️ Como Executar

1. Certifique-se de ter o Python instalado (versão 3.x).
2. Execute o projeto com:
   ```bash
   python main.py
   ```
3. Navegue pelo menu para registrar-se, fazer login e acessar os conteúdos.

## 📁 Exemplo de Módulo

Cada módulo tem:
- Aulas com links do YouTube e resumos.
- Um questionário de múltipla escolha com validação.

## 🧠 Tecnologias Utilizadas

- Python 3
- JSON para armazenamento de dados
- Hashlib para criptografia

## 📌 Requisitos

- Python 3.x
- Sistema operacional com suporte a terminal (Windows, Linux, macOS)