<div align="center">

# 🚀 Notebook FastAPI

<h3>Lightweight CRUD Note-Taking Application</h3>

[![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.70%2B-009688?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![MongoDB](https://img.shields.io/badge/MongoDB-4.4-green?style=for-the-badge&logo=mongodb&logoColor=white)](https://www.mongodb.com/)
[![Docker](https://img.shields.io/badge/Docker-20.10-blue?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-Workflow-success?style=for-the-badge&logo=github&logoColor=white)](https://github.com/features/actions)

</div>

---


## 🌟 Overview

Notebook FastAPI is a lightweight note-taking application built using FastAPI and MongoDB. This CRUD-based API allows users to create, read, update, and delete notes effortlessly. Designed for simplicity and scalability, it integrates continuous testing via GitHub Actions and is fully containerized with Docker for easy deployment.

### 🎯 Core Features

- **CRUD Operations**
  - Create, read, update, and delete notes via RESTful API endpoints.
- **FastAPI Powered**
  - High-performance API framework with automatic interactive documentation.
- **MongoDB Integration**
  - Robust NoSQL database for storing notes.
- **Continuous Integration**
  - Automated testing using GitHub Actions.
- **Dockerized Deployment**
  - Containerization for seamless development and production setups.

## 🛠 Technical Architecture

### Architecture Overview

```yaml
Application Architecture:
  - Framework: FastAPI
  - Database: MongoDB
  - Testing: GitHub Actions
  - Containerization: Docker
```

The application follows a minimalist design, ensuring rapid development cycles and easy deployment across various environments.

## 🚀 Quick Start

### Prerequisites

```bash
# Python 3.9 or above
python --version

# A running MongoDB instance
# Docker installed for containerized deployment
```

### Development Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/notebook-fastapi.git
   cd notebook-fastapi
   ```

2. **Create a virtual environment and activate it:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   - Create a `.env` file in the root directory.
   - Add the following:
     ```
     DATABASE_URL=mongodb://username:password@localhost:27017/notes_db
     ```

5. **Run the application:**
   ```bash
   uvicorn app.main:app --host 0.0.0.0 --port 8000
   ```

6. **Access the API documentation:**
   - Open your browser and navigate to `http://127.0.0.1:8000/docs` to explore the interactive API docs.

## 🐳 Docker Instructions

1. **Build the Docker image:**
   ```bash
   docker build -t notebook-fastapi .
   ```

2. **Run the Docker container:**
   ```bash
   docker run -p 8000:8000 --env-file .env notebook-fastapi
   ```

3. **Access the application at:**
   - [http://localhost:8000](http://localhost:8000)

## 🔧 Continuous Integration

This project leverages GitHub Actions for automated testing and code quality checks. Every push triggers the CI workflow defined in `.github/workflows/test.yml` to ensure the application remains reliable and robust.

## 📐 Documentation

- **API Documentation:**
  - Automatically generated with FastAPI and available at `/docs`.
- **Developer Guide:**
  - Detailed instructions for setting up the development environment and contributing.
- **Configuration Guide:**
  - Explanation of environment variables and application settings.

---

## 📄 License

This project is licensed under the MIT License.

<div align="center">
  <p>Made with ❤️ using FastAPI and MongoDB</p>
</div>