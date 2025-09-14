# Read the .env file
# HUD requires the .env file to be in the same directory
import os
from dotenv import load_dotenv
load_dotenv(dotenv_path='.env', override=True)

assert os.getenv("HUD_API_KEY")

import logging
from pathlib import Path
from agent import ComputerAgent

# Here you can set the model and tools for your agent.
# Computer use models: https://www.trycua.com/docs/agent-sdk/supported-agents/computer-use-agents
# Composed agent models: https://www.trycua.com/docs/agent-sdk/supported-agents/composed-agents
# Custom tools: https://www.trycua.com/docs/agent-sdk/custom-tools
agent_config = {
    "model": "anthropic/claude-sonnet-4-20250514",
    "trajectory_dir": str(Path("trajectories")),
    "only_n_most_recent_images": 3,
    "verbosity": logging.INFO
}

from computer import Computer, VMProviderType
import webbrowser

# Connect to your existing cloud container
computer = Computer(
    os_type="linux",
    provider_type=VMProviderType.DOCKER,
    verbosity=logging.INFO
)
await computer.run()

agent_config["tools"] = [ computer ]

webbrowser.open("http://localhost:8006/", new=0, autoraise=True)