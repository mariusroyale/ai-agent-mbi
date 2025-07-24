# AI Agent MBI - FastAPI-based AI Agent System

An intelligent AI-powered agent system built with FastAPI, designed to integrate with multiple LLM providers for various AI tasks. The project currently features Agent 007, a conversational agent with message management capabilities.

## 🚀 Features

- **FastAPI Backend**: Modern, fast web framework with automatic API documentation
- **Agent 007**: Conversational AI agent with message history management
- **Multi-LLM Support**: Extensible architecture supporting GPT4All and other LLM providers
- **Message Management**: Add, retrieve, and clear conversation messages via REST API
- **Environment Configuration**: Flexible configuration management with Pydantic settings
- **Modular Architecture**: Clean separation of concerns with agent, LLM, and service layers

## 🛠️ Tech Stack

- **Python 3.9+**: Core programming language
- **FastAPI**: Modern web framework for building APIs
- **Pydantic**: Data validation and settings management
- **GPT4All**: Local LLM integration (planned)
- **Uvicorn**: ASGI server for running the application
- **Poetry**: Dependency management and packaging

## 📋 Requirements

- Python 3.9 or higher
- Poetry (for dependency management)

## 🔧 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/mariusroyale/ai-agent-mbi.git
cd ai-agent-mbi
```

### 2. Install Dependencies

Using Poetry (recommended):

```bash
poetry install
```

### 3. Environment Configuration

The project includes a `.env` file with default configuration. You can modify these settings as needed:

```env
PYTHONPATH=src

# ==== OpenAI ====
OPENAI_API_KEY=
OPENAI_API_BASE=

# ==== LlamaIndex ====
LLAMA_INDEX_API_KEY=

# ==== HuggingFace ====
HUGGINGFACE_API_KEY=

# ==== Jira ====
JIRA_SERVER=
JIRA_EMAIL=
JIRA_API_TOKEN=

# ==== FastAPI ====
API_HOST=0.0.0.0
API_PORT=8000

# ==== Optional ====
LOG_LEVEL=INFO
ENV=development
```

## 🚀 Usage

### Starting the Application

```bash
# Using Poetry
poetry run uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload

# Or with environment variables
PYTHONPATH=src poetry run uvicorn src.main:app --host 0.0.0.0 --port 8000 --reload
```

The application will be available at:
- **API**: http://localhost:8000
- **Interactive API Docs**: http://localhost:8000/docs
- **Alternative API Docs**: http://localhost:8000/redoc

### API Usage Examples

**Get welcome message:**
```bash
curl http://localhost:8000/
```

**Add a message:**
```bash
curl -X POST "http://localhost:8000/messages" \
  -H "Content-Type: application/json" \
  -d '{"role": "user", "content": "Hello, Agent 007!"}'
```

**Get all messages:**
```bash
curl http://localhost:8000/messages
```

**Clear all messages:**
```bash
curl -X DELETE http://localhost:8000/messages
```

## 📁 Project Structure

```
ai-agent-mbi/
├── src/
│   ├── agent/
│   │   └── agent_007.py          # Agent 007 implementation
│   ├── llm/
│   │   ├── base_client.py        # Abstract base class for LLM clients
│   │   └── gpt4all_client.py     # GPT4All client implementation
│   ├── services/
│   │   └── search_vector.py      # Vector search service (placeholder)
│   ├── tests/                    # Test directory (empty)
│   ├── main.py                   # FastAPI application entry point
│   └── settings.py               # Application settings and configuration
├── bin/                          # Binary files directory
├── data_mock/                    # Mock data for testing
├── .env                          # Environment variables
├── pyproject.toml               # Poetry configuration and dependencies
├── poetry.lock                  # Poetry lock file
└── README.md                    # This file
```

## 🔌 API Endpoints

### Core Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | Welcome message and settings display |
| `POST` | `/messages` | Add a new message to Agent 007 |
| `GET` | `/messages` | Retrieve all messages from Agent 007 |
| `DELETE` | `/messages` | Clear all messages from Agent 007 |

### API Documentation

The FastAPI application automatically generates interactive API documentation:
- **Swagger UI**: Available at `/docs`
- **ReDoc**: Available at `/redoc`

## 🤖 Agent 007

Agent 007 is the main conversational agent in the system with the following capabilities:

- **Message Storage**: Maintains conversation history
- **Role-based Messages**: Supports different message roles (user, assistant, system)
- **Session Management**: Can reset conversation history
- **LLM Integration**: Designed to work with various LLM providers

## 🧪 Testing

The project includes a test structure ready for implementation:

```bash
# Run tests (when implemented)
poetry run pytest src/tests/
```

## ⚙️ Configuration

The application uses Pydantic Settings for configuration management. Current settings include:

| Setting | Default | Description |
|---------|---------|-------------|
| `API_HOST` | `0.0.0.0` | API server host |
| `API_PORT` | `8000` | API server port |
| `LOG_LEVEL` | `INFO` | Logging level |
| `ENV` | `development` | Environment mode |

Additional settings for OpenAI, LlamaIndex, HuggingFace, and Jira are available but currently commented out in the settings file.

## 🔄 Development Status

**Current Implementation:**
- ✅ FastAPI application setup
- ✅ Agent 007 with message management
- ✅ REST API endpoints for message operations
- ✅ Basic LLM client architecture
- ✅ Configuration management with Pydantic

**Planned Features:**
- 🔄 GPT4All integration (partially implemented)
- 📋 OpenAI client implementation
- 📋 Vector search functionality
- 📋 Jira integration
- 📋 Comprehensive test suite
- 📋 Advanced agent capabilities

## 🛠️ Dependencies

Key dependencies from `pyproject.toml`:

- **FastAPI** (0.116.x): Web framework
- **Pydantic** (2.11.x): Data validation
- **Uvicorn** (0.35.x): ASGI server
- **GPT4All** (2.8.x): Local LLM support
- **OpenAI** (1.95.x): OpenAI API client
- **LlamaIndex** (0.12.x): Document indexing
- **FAISS** (1.11.x): Vector similarity search
- **Pytest** (8.4.x): Testing framework

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Add tests for new functionality
5. Commit your changes (`git commit -m 'Add amazing feature'`)
6. Push to the branch (`git push origin feature/amazing-feature`)
7. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Marius Iordache**
- Email: marius.technical.leader@gmail.com
- GitHub: [@mariusroyale](https://github.com/mariusroyale)

## 🙏 Acknowledgments

- FastAPI team for the excellent web framework
- Pydantic team for robust data validation
- GPT4All project for local LLM capabilities
- The open-source community for amazing tools and libraries

## 📞 Support

If you have any questions or need help:

1. Check the [FastAPI documentation](https://fastapi.tiangolo.com/)
2. Review the interactive API docs at `/docs` when running the application
3. Create an issue on GitHub for bugs or feature requests
4. Contact the author for urgent matters

---

**Note**: This project is under active development. The Agent 007 system is currently in a basic implementation phase with plans for enhanced LLM integration and advanced features.