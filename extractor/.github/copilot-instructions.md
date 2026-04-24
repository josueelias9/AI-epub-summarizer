---
description: 'Generate a new React form component'
---


# general rule
- keep it simple

# frontend
- React with Next.js
- use taildwind for beauty

# services
- use fastapi
- SOLID principles
- use "REST Client.http" for API testing and documentation
- use clean architecture: directories entity, application, adapters, infrastructure
- ports and use cases for application layer

# documentation
- markdown for documentation

# orchestration
- docker compose for local development
- .env will be passed only trought docker compose

# infra
- terraform for infrastructure as code
- use modules for better organization

```
.devcontainer
frontend
├── Dockerfile
├── README.md
└── ...
service_1
├── app
│   ├── core
│   |   ├── config.py
│   |   └── ...
│   ├── domain
│   ├── application
│   ├── infrastructure
│   ├── scripts
│   ├── main.py
│   └── ...
├── REST Client.http
├── Dockerfile
├── README.md
└── ...
docker-compose.yml
.gitignore
.env
```