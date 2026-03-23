# 🔮 Cortex CRM - Premium AI-Powered Workspace

Este documento contiene el contexto general y la arquitectura de **Cortex CRM**, un sistema de gestión de relaciones con clientes diseñado con una estética **Glassmorphism** y potenciado por Python.

---

## 🌟 Propuesta de Valor
1.  **Velocidad & Eficiencia**: Backend asíncrono implementado en **FastAPI**.
2.  **Estética Premium**: Interfaz oscura con transparencias (Backdrop blur), gradientes de neón y animaciones fluidas sin la sobrecarga de un framework JS pesado.
3.  **Inteligencia Artificial**: Lógica de resúmenes y análisis descriptivos para Leads y Negocios.

---

## 🛠️ Stack Tecnológico
-   **Backend**: Python 3.10+ | **FastAPI** (Servidor y API) | **SQLModel** (ORM para SQLite/MariaDB).
-   **Base de Datos**: SQLite (`crm.db`) para prototipado rápido.
-   **Frontend**:
    -   **HTML5** (Semántico).
    -   **CSS3** (Variables CSS, Glassmorphism, Flex/Grid Layouts).
    -   **Vanilla Javascript** (Interacciones asíncronas / Drag & Drop).
    -   **Librerías externas (CDN)**: Chart.js (Gráficos), FontAwesome (Iconos).

---

## 📁 Estructura del Proyecto
```text
/crm
├── backend/
│   ├── api/           # Endpoints divididos por recursos
│   │   ├── leads.py   # Módulos de Prospectos (CRUD + AI)
│   │   └── deals.py   # Módulos de Tratos (Kanban movement)
│   ├── main.py        # Punto de entrada FastAPI & Ruteo
│   ├── models.py      # Declaración de Tablas (SQLModel)
│   └── database.py    # Configuración de sesión y motor SQL
├── frontend/
│   ├── static/        # Archivos estáticos
│   │   ├── css/style.css  # Tema Glassmorphism Master
│   │   └── js/        # Controladores específicos (leads.js, pipeline.js)
│   └── templates/     # Vistas HTML (Jinja2)
├── requirements.txt   # Dependencias de Python
└── seed_db.py         # Script para poblar datos de prueba
```

---

## 🚀 Cómo Ejecutar el Proyecto
1.  **Instalar dependencias**:
    ```bash
    pip install -r requirements.txt
    ```
2.  **Inicializar Base de Datos**:
    ```bash
    python seed_db.py
    ```
3.  **Lanzar Servidor**:
    ```bash
    python -m backend.main
    ```
    *El servidor correrá en `http://localhost:8000` con recarga en vivo activa.*

---

## 📋 Módulos Implementados (Fase 1)
-   [x] **Panel (Dashboard)**: Métricas de KPIs, visualización de ingresos con Chart.js y feeds de actividad.
-   [x] **Prospectos (Leads)**: Tablas dinámicas, estado de contactos y asistente de resúmenes IA (Modal).
-   [x] **Embudo (Kanban)**: Gestión visual de tratos por etapas con soporte Drag & Drop nativo.

---
*Este archivo se mantendrá actualizado con cada nueva característica o cambio arquitectónico.*
