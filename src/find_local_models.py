import ollama
import yaml
import os

# --- 1. CONFIGURATION ---
CONFIG_FILE = 'config.yaml'

# Keywords used to filter out non-chat models (case-insensitive check)
EXCLUSIONS = ["embed", "coder"] 
# NOTE: 'coder' is removed from exclusions here as they are typically chat-optimized

# --- 2. FETCH AND FILTER MODELS ---
try:
    client = ollama.Client()
    local_models = client.list()
    filtered_models = []
    
    print("--- Ollama Model Filtering Process ---")
    
    for model_info in local_models.get('models', []):
        model_name = model_info.get('model', 'UNKNOWN_MODEL')
        
        # Check for non-chat/embedding models
        if any(keyword in model_name.lower() for keyword in EXCLUSIONS):
            print(f"❌ Skipping non-chat model: {model_name}")
            continue
            
        filtered_models.append(model_name)
        print(f"✅ Including chat model: {model_name}")

except Exception as e:
    print(f"\nFATAL ERROR: Could not connect to or query Ollama server. Details: {e}")
    print("Please ensure Ollama is installed and running.")
    # Exit or use an empty list, depending on error handling preference
    filtered_models = [] 

# -------------------------------------------------------------
## 3. LOAD, MODIFY, AND REWRITE THE CONFIG FILE
# -------------------------------------------------------------

# Initialize config_data to handle the case where the file doesn't exist
config_data = {}

# A. Load Existing Data (if file exists)
if os.path.exists(CONFIG_FILE):
    try:
        with open(CONFIG_FILE, 'r') as f:
            # Load the existing structure, preserving all other fields
            config_data = yaml.safe_load(f)
            # Handle empty file case
            if config_data is None:
                config_data = {}
        print(f"\nLoaded existing configuration from {CONFIG_FILE}")
    except Exception as e:
        print(f"Warning: Could not read existing YAML file. Starting fresh. Details: {e}")
        config_data = {} # Reset to empty if loading fails

# B. Modify ONLY the 'models' field
config_data['models'] = filtered_models

# C. Dump the entire, now-modified structure back to the file
try:
    with open(CONFIG_FILE, 'w') as f:
        # The default_flow_style=False ensures the list is written in block style (one item per line)
        yaml.dump(config_data, f, default_flow_style=False, sort_keys=False) 

    print(f"\n--- SUCCESS ---")
    print(f"Updated the 'models' field in {CONFIG_FILE} (Other fields preserved).")

except Exception as e:
    print(f"\nERROR: Could not write to {CONFIG_FILE}. Details: {e}")