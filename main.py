import os
import sys
from typing import Dict, Any, Optional

def get_root_path() -> str:
    """Get the root path of the project."""
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def append_path() -> None:
    """Append the root path to sys.path."""
    root_path = get_root_path()
    if root_path not in sys.path:
        sys.path.append(root_path)

append_path()

def register() -> Dict[str, Any]:
    """
    Register the plugin.
    Returns the plugin's API routes, middlewares, error handlers, and dependencies.
    """
    from flask import Blueprint
    from flask_restful import Api
    
    blueprint = Blueprint('reading_scene', __name__)
    api = Api(blueprint)
    
    # Plugin routes are defined in manifest.yaml and will be automatically loaded
    
    return {
        'blueprint': blueprint,
        'api': api,
        'routes': []
    }

def setup(config: Dict[str, Any]) -> bool:
    """
    Set up the plugin.
    Args:
        config: The plugin configuration.
    Returns:
        True if the setup is successful, False otherwise.
    """
    # Initialize any required resources here
    try:
        # You could initialize any resources needed by your SVG rendering here
        # For example, loading templates, initializing cache, etc.
        return True
    except Exception as e:
        print(f"Error setting up reading-scene plugin: {e}")
        return False

def load_credentials(credentials: Optional[Dict[str, Any]]) -> None:
    """
    Load the plugin credentials.
    Args:
        credentials: The plugin credentials.
    """
    # This plugin doesn't require external credentials
    pass 