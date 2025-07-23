# AI Agent MBI - Jira Ticket Classification System

An intelligent AI-powered agent designed to classify and process Jira tickets using advanced machine learning techniques. MBI (codename) leverages multiple LLM providers and vector search capabilities to provide accurate ticket classification and insights.

## 🚀 Features

- **Multi-LLM Support**: Integrates with OpenAI, GPT4All, and HuggingFace models
- **Vector Search**: Powered by FAISS for efficient similarity search
- **Jira Integration**: Direct integration with Jira API for ticket management
- **Flexible Configuration**: Environment-based configuration management
- **Extensible Architecture**: Modular design supporting multiple LLM clients
- **REST API**: Built-in API server for easy integration

## 🛠️ Tech Stack

- **Python 3.9+**: Core programming language
- **OpenAI API**: Primary LLM provider
- **LlamaIndex**: Document indexing and retrieval
- **FAISS**: Vector similarity search
- **Jira API**: Ticket management integration
- **Pydantic**: Data validation and settings management
- **Uvicorn**: ASGI server for API endpoints
- **Sentence Transformers**: Text embeddings

## 📋 Requirements

- Python 3.9 or higher
- Poetry (for dependency management)
- Active Jira instance with API access
- OpenAI API key (optional: HuggingFace API key)

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

Or using pip:

```bash
pip install -r requirements.txt
```

### 3. Environment Configuration

Create a `.env` file in the project root with the following variables:

```env
# OpenAI Configuration
OPENAI_API_KEY=your_openai_api_key_here
OPENAI_API_BASE=https://api.openai.com/v1

# Jira Configuration
JIRA_SERVER=https://your-company.atlassian.net
JIRA_EMAIL=your-email@company.com
JIRA_API_TOKEN=your_jira_api_token

# Optional: HuggingFace
HUGGINGFACE_API_KEY=your_huggingface_api_key

# Optional: LlamaIndex
LLAMA_INDEX_API_KEY=your_llama_index_api_key

# API Server Configuration
API_HOST=0.0.0.0
API_PORT=8000

# Application Settings
LOG_LEVEL=INFO
ENV=development
```

### 4. Set Up Jira API Token

1. Go to your Atlassian Account Settings
2. Navigate to Security → API tokens
3. Create a new API token
4. Copy the token to your `.env` file

## 🚀 Usage

### Starting the Application

```bash
# Using Poetry
PYTHONPATH=src poetry run python -m uvicorn src.main:app --host 0.0.0.0 --port 8000

# Or directly with Python
PYTHONPATH=src python -m uvicorn src.main:app --host 0.0.0.0 --port 8000
```
👉 http://0.0.0.0:8000/

### Basic Usage Example

```python
from src.config import config
from src.llm.client_factory import LLMClientFactory
from src.services.search_vector import VectorSearchService

# Initialize LLM client
llm_client = LLMClientFactory.create_client("openai")

# Classify a ticket
ticket_description = "User cannot login to the application"
classification = llm_client.chat([
    {"role": "user", "content": f"Classify this ticket: {ticket_description}"}
])

print(f"Classification: {classification}")
```

## 📁 Project Structure

```
ai-agent-mbi/
├── src/
│   ├── agent/
│   │   └── agent_007.py          # Main agent implementation
│   ├── llm/
│   │   ├── base_client.py        # Abstract base class for LLM clients
│   │   ├── client_factory.py     # Factory pattern for client creation
│   │   ├── openai_client.py      # OpenAI API client
│   │   └── gpt4all_client.py     # GPT4All local client
│   ├── services/
│   │   └── search_vector.py      # Vector search service
│   ├── tests/                    # Test files
│   └── config.py                 # Configuration management
├── data_mock/                    # Mock data for testing
├── .env                          # Environment variables
├── pyproject.toml               # Poetry configuration
└── README.md                    # This file
```

## 🔌 API Endpoints

The application exposes REST API endpoints for ticket classification:

### POST `/classify`
Classify a Jira ticket based on its content.

**Request Body:**
```json
{
    "ticket_id": "PROJ-123",
    "summary": "User login issue",
    "description": "User cannot access the application after password reset"
}
```

**Response:**
```json
{
    "ticket_id": "PROJ-123",
    "classification": "Authentication Issue",
    "confidence": 0.95,
    "suggested_assignee": "security-team",
    "priority": "high"
}
```

## 🧪 Testing

Run the test suite:

```bash
# Using Poetry
poetry run pytest src/tests/

# Or directly
python -m pytest src/tests/
```

## 📊 Configuration Options

The application supports various configuration options through environment variables:

| Variable         | Default       | Description             |
|------------------|---------------|-------------------------|
| `OPENAI_API_KEY` | Required      | OpenAI API key          |
| `JIRA_SERVER`    | Required      | Jira server URL         |
| `JIRA_EMAIL`     | Required      | Jira user email         |
| `JIRA_API_TOKEN` | Required      | Jira API token          |
| `API_HOST`       | `0.0.0.0`     | API server host         |
| `API_PORT`       | `8000`        | API server port         |
| `LOG_LEVEL`      | `INFO`        | Logging level           |
| `ENV`            | `development` | Environment mode        |

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Marius Iordache**
- Email: marius.technical.leader@gmail.com
- GitHub: [@mariusroyale](https://github.com/mariusroyale)

## 🙏 Acknowledgments

- OpenAI for providing the GPT models
- Meta for LlamaIndex framework
- Facebook AI Research for FAISS
- The open-source community for the amazing tools and libraries

## 📞 Support

If you have any questions or need help setting up the project, please:

1. Check the existing [Issues](https://github.com/mariusroyale/ai-agent-mbi/issues)
2. Create a new issue if your question isn't already addressed
3. Reach out via email for urgent matters

---

**Note**: This project is under active development. Features and API endpoints may change. Please check the latest documentation before deploying to production.
