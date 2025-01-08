def load_config(config_path):
    import json
    with open(config_path, 'r') as f:
        config = json.load(f)
    return config

def save_model(model, save_path):
    import torch
    torch.save(model.state_dict(), save_path)