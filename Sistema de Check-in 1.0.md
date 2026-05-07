Sistema de Check-in 1.0
Objetivo

Criar um sistema simples de check-in para eventos, com armazenamento em banco de dados e controle de presença dos participantes.
______________________________________________
MVP (Foco Atual)
-Modelagem do banco de dados
-Backend conectado ao banco
-Realizar check-in simples (sem QR Code)
-Atualizar status de presença no banco
______________________________________________
Regras de Negócio
-Um participante só pode realizar check-in uma vez
-O sistema deve registrar se o participante está     presente
______________________________________________
Tecnologias
-Backend: Python + FastAPI
-Banco: SQLite (inicial) → PostgreSQL (futuro)
-ORM: SQLAlchemy
-Testes: Postman ou Insomnia
-Editor: VS Code
-Versionamento: Git + GitHub
______________________________________________
📅 Status

Em desenvolvimento – fase inicial (estrutura e banco de dados)