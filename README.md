# Project [00]: [Project name]

**Starter**: Project based off the [Flask Python Starter](https://github.com/davedonnellydev/flask-python-starter)
**Date**: [Project build date here]

This project has been built as part of my AI Project-a-Day Challenge. You can read more information on the full project here: [https://github.com/davedonnellydev/ai-august-2025-challenge](https://github.com/davedonnellydev/ai-august-2025-challenge).

**Project Objective**: _Write up any project objectives here_

## 🚀 Features

- List project features here

## 🖥️ Demo

**[Live Demo](https://your-demo-url.com)**
_(Link will be added after deployment)_

## Quick Start

### Prerequisites

- Python 3.11+
- pip

### Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd flask-python-starter
```

2. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Set up environment variables:

```bash
cp .env.example .env
# Edit .env with your configuration
```

5. Run the application:

```bash
# Option 1: Using Flask CLI (recommended)
FLASK_APP=run.py python -m flask run --host=0.0.0.0 --port=8000

# Option 2: Using Python directly (alternative)
python run.py
```

The application will be available at `http://localhost:8000`

**Note**: On macOS, port 5000 is often used by AirPlay Receiver. If you encounter "Address already in use" errors, use port 8000 or another available port.

## Development

### Running Tests

![CI](https://github.com/davedonnellydev/flask-python-starter/actions/workflows/ci.yml/badge.svg)  
*Link should be amended so that correct repo is specified*  

```bash
# Run all tests (with coverage by default)
pytest

# Run tests with coverage
pytest --cov=app

# Run tests and generate HTML coverage report
pytest --cov=app --cov-report=html

# Run tests without coverage
pytest --no-cov
```

**Note**: The pytest configuration in `pyproject.toml` automatically includes coverage reporting and sets the Python path to find the `app` module.

### Code Quality

```bash
# Format code
black .

# Check code style
flake8

# Run all quality checks
black --check .
flake8
pytest
```

## API Endpoints

### Health Checks

- `GET /health` - Basic health check
- `GET /health/detailed` - Detailed health check with version info

### Proxy

- `POST /api/proxy` - Proxy endpoint for external API calls

### Root

- `GET /` - Welcome message

## Configuration

The application uses environment-based configuration:

- `SECRET_KEY` - Flask secret key (required)
- `FLASK_ENV` - Environment (development/testing/production)
- `LOG_LEVEL` - Logging level (DEBUG/INFO/WARNING/ERROR)

## Deployment

### Production

1. Set environment variables:

```bash
export FLASK_ENV=production
export SECRET_KEY=your-secure-secret-key
export LOG_LEVEL=WARNING
```

2. Run with a production WSGI server:

```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:8000 app.main:app
```

### Docker (Optional)

```bash
# Build image
docker build -t flask-starter .

# Run container
docker run -p 8000:8000 flask-starter
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests and quality checks
5. Submit a pull request

## License

This project is licensed under the MIT License.
