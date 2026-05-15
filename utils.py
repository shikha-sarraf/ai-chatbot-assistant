# Helper utilities

# Add requirements.txt with openai and langchain
import yaml
with open('config.yaml') as f:
    config = yaml.safe_load(f)

# Create basic prompt template for conversation
from langchain.memory import ConversationBufferMemory

# Add memory capability using ConversationBufferMemory
client = openai.OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))
