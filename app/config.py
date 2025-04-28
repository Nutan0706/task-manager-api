import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the environment variables
DATABASE_URL = os.getenv("DATABASE_URL")
