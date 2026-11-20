{
  "name": "streaming-ingestion-lab",
  "image": "mcr.microsoft.com/devcontainers/python:1-3.11-bookworm",
  "features": {
    "ghcr.io/devcontainers/features/docker-in-docker:2": {}
  },
  "postCreateCommand": "pip install -r requirements.txt && chmod +x scripts/*.sh",
  "forwardPorts": [8080, 9092],
  "portsAttributes": {
    "8080": { "label": "Kafka UI", "onAutoForward": "notify" },
    "9092": { "label": "Kafka broker" }
  },
  "customizations": {
    "vscode": {
      "extensions": ["ms-python.python", "ms-azuretools.vscode-docker"]
    }
  }
}
