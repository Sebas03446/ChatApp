# ChatApp

This is a personal project to explore and experiment with generative AI models. Initially, the model includes a specialized API that creates an initial character to generate the first prompt. The frontend is still a work in progress.


## Technologies
- Python
- FastAPI
- Pydantic
- Vue.js
- Tailwind CSS

## Installation
1. Clone the repository
2. Move into the project directory
```bash
cd backend
```
3. Create a virtual environment
```bash
python3 -m venv venv
```
4. Activate the virtual environment
```bash
source venv/bin/activate
```

5. Install the dependencies
```bash
pip install -r requirements.txt
```

6. Set up the Mistral API key
```bash
export MISTRAL_API_KEY=your_api_key_here
```

7. Run the FastAPI server
```bash
fastapi run app/main.py
```

## Testing
1. Run the tests
```bash
pytest backend/app/tests/api/
```
## Documentation
1. Open the browser and navigate to `http://localhost:8000/docs`


