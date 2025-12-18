import pytest
import sys
from pathlib import Path

# Add the src directory to the path so we can import app
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from fastapi.testclient import TestClient
from app import app, activities


@pytest.fixture
def client():
    """Create a test client for the FastAPI app"""
    return TestClient(app)


@pytest.fixture
def reset_activities():
    """Reset activities to a known state before each test"""
    # Store original activities
    original = {k: {"participants": v["participants"].copy()} for k, v in activities.items()}
    
    yield
    
    # Reset after test
    for activity_name, activity_data in activities.items():
        activity_data["participants"] = original[activity_name]["participants"]
