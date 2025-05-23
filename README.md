<div align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" alt="Cua logo" height="150" srcset="img/logo_white.png">
    <source media="(prefers-color-scheme: light)" alt="Cua logo" height="150" srcset="img/logo_black.png">
    <img alt="Cua logo" height="150" src="img/logo_black.png">
  </picture>

  [![Python](https://img.shields.io/badge/Python-333333?logo=python&logoColor=white&labelColor=333333)](#)
  [![Swift](https://img.shields.io/badge/Swift-F05138?logo=swift&logoColor=white)](#)
  [![macOS](https://img.shields.io/badge/macOS-000000?logo=apple&logoColor=F0F0F0)](#)
  [![Discord](https://img.shields.io/badge/Discord-%235865F2.svg?&logo=discord&logoColor=white)](https://discord.com/invite/mVnXXpdE85)
  <br>
  <a href="https://trendshift.io/repositories/13685" target="_blank"><img src="https://trendshift.io/api/badge/repositories/13685" alt="trycua%2Fcua | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>
</div>

**c/ua** (pronounced "koo-ah") enables AI agents to control full operating systems in high-performance virtual containers with near-native speed on Apple Silicon.

<div align="center">
  <video src="https://github.com/user-attachments/assets/c619b4ea-bb8e-4382-860e-f3757e36af20" width="800" controls></video>
</div>

# 🚀 Quick Start

**Recommended for users who want to get started with a VM and Agent UI immediately.**

Serve a ready-to-use Computer-Use Agent UI and VM locally with a single command:

```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/trycua/cua/main/scripts/playground.sh)"
```

<details>
<summary><strong>What does this command do?</strong></summary>

You can view the full script source here: [scripts/playground.sh](https://github.com/trycua/cua/blob/main/scripts/playground.sh). To follow along yourself, use the steps below:

1. **Install/Update the [Lume CLI](./libs/lume/README.md)**  
   Lume is our tool for managing VMs that run efficiently using Apple's Virtualization framework.
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/trycua/cua/main/libs/lume/scripts/install.sh)"
   ```
2. **Pull the macOS CUA image from the trycua repo**  
   This step downloads a prebuilt macOS Sequoia VM image (~30GB disk space required) with a `lume` default user (password: `lume`) and the [CUA Computer Server](https://github.com/trycua/cua/tree/main/libs/computer-server) preinstalled.  
   The CUA Computer Server allows the VM to be controlled programmatically by the Computer Python SDK.
   ```bash
   lume pull macos-sequoia-cua:latest
   ```
3. **Start a macOS VM using the pulled image**  
   ```bash
   lume run macos-sequoia-cua:latest
   ```
   See [Lume docs](./libs/lume/README.md) for more VM management commands.
4. **Install/Update the [Computer](https://github.com/trycua/cua/tree/main/libs/computer) and [Agent](https://github.com/trycua/cua/tree/main/libs/agent) Python SDKs**  
   - **Computer** lets Python developers automate Lume VMs using code.
   - **Agent** provides both a Python and GUI interface for interacting with multiple different computer-use agents.
   ```bash
   pip install -U "cua-computer[all]" "cua-agent[all]"
   ```
5. **Start the Agent UI**  
   This launches a chat UI for prompting computer-use agents to control the running macOS VM. Access it at [http://localhost:7860](http://localhost:7860):
   ```bash
   python -m agent.ui.gradio.app
   ```
</details>

#### Supported [Agent Loops](https://github.com/trycua/cua/blob/main/libs/agent/README.md#agent-loops)
- [UITARS-1.5](https://github.com/trycua/cua/blob/main/libs/agent/README.md#agent-loops): Run locally on Apple Silicon with MLX, or use cloud providers
- [OpenAI CUA](https://github.com/trycua/cua/blob/main/libs/agent/README.md#agent-loops): Use OpenAI's Computer-Use Preview model (*requires tier 3, select users only*)
- [Anthropic CUA](https://github.com/trycua/cua/blob/main/libs/agent/README.md#agent-loops): Use Anthropic's Computer-Use capabilities
- [OmniParser-v2.0](https://github.com/trycua/cua/blob/main/libs/agent/README.md#agent-loops): Control UI with [Set-of-Marks prompting](https://som-gpt4v.github.io/) using any vision model

### System Requirements
- Mac with Apple Silicon (M1/M2/M3/M4 series)
- macOS 15 (Sequoia) or newer
- Disk space for VM images (30GB+ recommended)


# 💻 For Developers

**For advanced users: use our modules directly in your Python code for custom automation, integration, or research.**

1. **Install Lume CLI**
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/trycua/cua/main/libs/lume/scripts/install.sh)"
   ```
2. **Pull the macOS CUA image**
   ```bash
   lume pull macos-sequoia-cua:latest
   ```
3. **Install the Python SDKs**
   ```bash
   pip install -U "cua-computer[all]" "cua-agent[all]"
   ```
4. **Import and use in your Python code:**
   ```python
   from computer import Computer
   from agent import ComputerAgent, LLM

    async def main():
        # Start a local macOS VM with a 1024x768 display
        async with Computer(os_type="macos", display="1024x768") as computer:

            # Example: Direct control of a macOS VM with Computer
            await computer.interface.left_click(100, 200)
            await computer.interface.type_text("Hello, world!")
            screenshot_bytes = await computer.interface.screenshot()
            
            # Example: Create and run an agent locally using mlx-community/UI-TARS-1.5-7B-6bit
            agent = ComputerAgent(
              computer=computer,
              loop="UITARS",
              model=LLM(provider="MLXVLM", name="mlx-community/UI-TARS-1.5-7B-6bit")
            )
            await agent.run("Find the trycua/cua repository on GitHub and follow the quick start guide")

    main()
   ```
   See the [Developer Guide](./docs/Developer-Guide.md) for advanced usage and building from source.

---


For ready-to-use examples, check out our [Notebooks](./notebooks/) collection.

### Lume CLI Reference

```bash
# Install Lume CLI and background service
curl -fsSL https://raw.githubusercontent.com/trycua/cua/main/libs/lume/scripts/install.sh | bash

# List all VMs
lume ls

# Pull a VM image
lume pull macos-sequoia-cua:latest

# Create a new VM
lume create my-vm --os macos --cpu 4 --memory 8GB --disk-size 50GB

# Run a VM (creates and starts if it doesn't exist)
lume run macos-sequoia-cua:latest

# Stop a VM
lume stop macos-sequoia-cua_latest

# Delete a VM
lume delete macos-sequoia-cua_latest
```

### Lumier CLI Reference

For advanced container-like virtualization, check out [Lumier](./libs/lumier/README.md) - a Docker interface for macOS and Linux VMs.

```bash
# Install Lume CLI and background service
curl -fsSL https://raw.githubusercontent.com/trycua/cua/main/libs/lume/scripts/install.sh | bash

# Run macOS in a Docker container
docker run -it --rm \
    --name lumier-vm \
    -p 8006:8006 \
    -v $(pwd)/storage:/storage \
    -v $(pwd)/shared:/shared \
    -e VM_NAME=lumier-vm \
    -e VERSION=ghcr.io/trycua/macos-sequoia-cua:latest \
    -e CPU_CORES=4 \
    -e RAM_SIZE=8192 \
    -e HOST_STORAGE_PATH=$(pwd)/storage \
    -e HOST_SHARED_PATH=$(pwd)/shared \
    trycua/lumier:latest
```

## Resources

- [How to use the MCP Server with Claude Desktop or other MCP clients](./libs/mcp-server/README.md) - One of the easiest ways to get started with C/ua
- [How to use OpenAI Computer-Use, Anthropic, OmniParser, or UI-TARS for your Computer-Use Agent](./libs/agent/README.md)
- [How to use Lume CLI for managing desktops](./libs/lume/README.md)
- [Training Computer-Use Models: Collecting Human Trajectories with C/ua (Part 1)](https://www.trycua.com/blog/training-computer-use-models-trajectories-1)
- [Build Your Own Operator on macOS (Part 1)](https://www.trycua.com/blog/build-your-own-operator-on-macos-1)

## Modules

| Module | Description | Installation |
|--------|-------------|---------------|
| [**Lume**](./libs/lume/README.md) | VM management for macOS/Linux using Apple's Virtualization.Framework | `curl -fsSL https://raw.githubusercontent.com/trycua/cua/main/libs/lume/scripts/install.sh \| bash` |
| [**Lumier**](./libs/lumier/README.md) | Docker interface for macOS and Linux VMs | `docker pull trycua/lumier:latest` |
| [**Computer**](./libs/computer/README.md) | Interface for controlling virtual machines | `pip install "cua-computer[all]"` |
| [**Agent**](./libs/agent/README.md) | AI agent framework for automating tasks | `pip install "cua-agent[all]"` |
| [**MCP Server**](./libs/mcp-server/README.md) | MCP server for using CUA with Claude Desktop | `pip install cua-mcp-server` |
| [**SOM**](./libs/som/README.md) | Self-of-Mark library for Agent | `pip install cua-som` |
| [**PyLume**](./libs/pylume/README.md) | Python bindings for Lume | `pip install pylume` |
| [**Computer Server**](./libs/computer-server/README.md) | Server component for Computer | `pip install cua-computer-server` |
| [**Core**](./libs/core/README.md) | Core utilities | `pip install cua-core` |

## Computer Interface Reference

For complete examples, see [computer_examples.py](./examples/computer_examples.py) or [computer_nb.ipynb](./notebooks/computer_nb.ipynb)

```python
# Mouse Actions
await computer.interface.left_click(x, y)       # Left click at coordinates
await computer.interface.right_click(x, y)      # Right click at coordinates
await computer.interface.double_click(x, y)     # Double click at coordinates
await computer.interface.move_cursor(x, y)      # Move cursor to coordinates
await computer.interface.drag_to(x, y, duration)  # Drag to coordinates
await computer.interface.get_cursor_position()  # Get current cursor position

# Keyboard Actions
await computer.interface.type_text("Hello")     # Type text
await computer.interface.press_key("enter")     # Press a single key
await computer.interface.hotkey("command", "c") # Press key combination

# Screen Actions
await computer.interface.screenshot()           # Take a screenshot
await computer.interface.get_screen_size()      # Get screen dimensions

# Clipboard Actions
await computer.interface.set_clipboard(text)    # Set clipboard content
await computer.interface.copy_to_clipboard()    # Get clipboard content

# File System Operations
await computer.interface.file_exists(path)      # Check if file exists
await computer.interface.directory_exists(path) # Check if directory exists
await computer.interface.run_command(cmd)       # Run shell command

# Accessibility
await computer.interface.get_accessibility_tree() # Get accessibility tree
```

## ComputerAgent Reference

For complete examples, see [agent_examples.py](./examples/agent_examples.py) or [agent_nb.ipynb](./notebooks/agent_nb.ipynb)

```python
# Import necessary components
from agent import ComputerAgent, LLM, AgentLoop, LLMProvider

# UI-TARS-1.5 agent for local execution with MLX
ComputerAgent(loop=AgentLoop.UITARS, model=LLM(provider=LLMProvider.MLXVLM, name="mlx-community/UI-TARS-1.5-7B-6bit"))   
# OpenAI Computer-Use agent using OPENAI_API_KEY  
ComputerAgent(loop=AgentLoop.OPENAI, model=LLM(provider=LLMProvider.OPENAI, name="computer-use-preview"))
# Anthropic Claude agent using ANTHROPIC_API_KEY
ComputerAgent(loop=AgentLoop.ANTHROPIC, model=LLM(provider=LLMProvider.ANTHROPIC))

# OmniParser loop for UI control using Set-of-Marks (SOM) prompting and any vision LLM
ComputerAgent(loop=AgentLoop.OMNI, model=LLM(provider=LLMProvider.OLLAMA, name="gemma3:12b-it-q4_K_M"))      
# OpenRouter example using OAICOMPAT provider
ComputerAgent(
    loop=AgentLoop.OMNI,
    model=LLM(
        provider=LLMProvider.OAICOMPAT, 
        name="openai/gpt-4o-mini",
        provider_base_url="https://openrouter.ai/api/v1"
    ),
    api_key="your-openrouter-api-key"
)
```

## Demos

Check out these demos of the Computer-Use Agent in action:

<details open>
<summary><b>MCP Server: Work with Claude Desktop and Tableau</b></summary>
<br>
<div align="center">
    <video src="https://github.com/user-attachments/assets/9f573547-5149-493e-9a72-396f3cff29df" width="800" controls></video>
</div>
</details>

<details>
<summary><b>AI-Gradio: Multi-app workflow with browser, VS Code and terminal</b></summary>
<br>
<div align="center">
    <video src="https://github.com/user-attachments/assets/723a115d-1a07-4c8e-b517-88fbdf53ed0f" width="800" controls></video>
</div>
</details>

<details>
<summary><b>Notebook: Fix GitHub issue in Cursor</b></summary>
<br>
<div align="center">
    <video src="https://github.com/user-attachments/assets/f67f0107-a1e1-46dc-aa9f-0146eb077077" width="800" controls></video>
</div>
</details>

## Community

Join our [Discord community](https://discord.com/invite/mVnXXpdE85) to discuss ideas, get assistance, or share your demos!

## License

Cua is open-sourced under the MIT License - see the [LICENSE](LICENSE) file for details.

Microsoft's OmniParser, which is used in this project, is licensed under the Creative Commons Attribution 4.0 International License (CC-BY-4.0) - see the [OmniParser LICENSE](https://github.com/microsoft/OmniParser/blob/master/LICENSE) file for details.

## Contributing

We welcome contributions to CUA! Please refer to our [Contributing Guidelines](CONTRIBUTING.md) for details.

## Trademarks

Apple, macOS, and Apple Silicon are trademarks of Apple Inc. Ubuntu and Canonical are registered trademarks of Canonical Ltd. Microsoft is a registered trademark of Microsoft Corporation. This project is not affiliated with, endorsed by, or sponsored by Apple Inc., Canonical Ltd., or Microsoft Corporation.

## Stargazers

Thank you to all our supporters!

[![Stargazers over time](https://starchart.cc/trycua/cua.svg?variant=adaptive)](https://starchart.cc/trycua/cua)

## Contributors

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/f-trycua"><img src="https://avatars.githubusercontent.com/u/195596869?v=4?s=100" width="100px;" alt="f-trycua"/><br /><sub><b>f-trycua</b></sub></a><br /><a href="#code-f-trycua" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://pepicrft.me"><img src="https://avatars.githubusercontent.com/u/663605?v=4?s=100" width="100px;" alt="Pedro Piñera Buendía"/><br /><sub><b>Pedro Piñera Buendía</b></sub></a><br /><a href="#code-pepicrft" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://iamit.in"><img src="https://avatars.githubusercontent.com/u/5647941?v=4?s=100" width="100px;" alt="Amit Kumar"/><br /><sub><b>Amit Kumar</b></sub></a><br /><a href="#code-aktech" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://productsway.com/"><img src="https://avatars.githubusercontent.com/u/870029?v=4?s=100" width="100px;" alt="Dung Duc Huynh (Kaka)"/><br /><sub><b>Dung Duc Huynh (Kaka)</b></sub></a><br /><a href="#code-jellydn" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="http://zaydkrunz.com"><img src="https://avatars.githubusercontent.com/u/70227235?v=4?s=100" width="100px;" alt="Zayd Krunz"/><br /><sub><b>Zayd Krunz</b></sub></a><br /><a href="#code-ShrootBuck" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/PrashantRaj18198"><img src="https://avatars.githubusercontent.com/u/23168997?v=4?s=100" width="100px;" alt="Prashant Raj"/><br /><sub><b>Prashant Raj</b></sub></a><br /><a href="#code-PrashantRaj18198" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://www.mobile.dev"><img src="https://avatars.githubusercontent.com/u/847683?v=4?s=100" width="100px;" alt="Leland Takamine"/><br /><sub><b>Leland Takamine</b></sub></a><br /><a href="#code-Leland-Takamine" title="Code">💻</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/ddupont808"><img src="https://avatars.githubusercontent.com/u/3820588?v=4?s=100" width="100px;" alt="ddupont"/><br /><sub><b>ddupont</b></sub></a><br /><a href="#code-ddupont808" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/Lizzard1123"><img src="https://avatars.githubusercontent.com/u/46036335?v=4?s=100" width="100px;" alt="Ethan Gutierrez"/><br /><sub><b>Ethan Gutierrez</b></sub></a><br /><a href="#code-Lizzard1123" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://ricterz.me"><img src="https://avatars.githubusercontent.com/u/5282759?v=4?s=100" width="100px;" alt="Ricter Zheng"/><br /><sub><b>Ricter Zheng</b></sub></a><br /><a href="#code-RicterZ" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://www.trytruffle.ai/"><img src="https://avatars.githubusercontent.com/u/50844303?v=4?s=100" width="100px;" alt="Rahul Karajgikar"/><br /><sub><b>Rahul Karajgikar</b></sub></a><br /><a href="#code-rahulkarajgikar" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/trospix"><img src="https://avatars.githubusercontent.com/u/81363696?v=4?s=100" width="100px;" alt="trospix"/><br /><sub><b>trospix</b></sub></a><br /><a href="#code-trospix" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://wavee.world/invitation/b96d00e6-b802-4a1b-8a66-2e3854a01ffd"><img src="https://avatars.githubusercontent.com/u/22633385?v=4?s=100" width="100px;" alt="Ikko Eltociear Ashimine"/><br /><sub><b>Ikko Eltociear Ashimine</b></sub></a><br /><a href="#code-eltociear" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/dp221125"><img src="https://avatars.githubusercontent.com/u/10572119?v=4?s=100" width="100px;" alt="한석호(MilKyo)"/><br /><sub><b>한석호(MilKyo)</b></sub></a><br /><a href="#code-dp221125" title="Code">💻</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://www.encona.com/"><img src="https://avatars.githubusercontent.com/u/891558?v=4?s=100" width="100px;" alt="Rahim Nathwani"/><br /><sub><b>Rahim Nathwani</b></sub></a><br /><a href="#code-rahimnathwani" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://mjspeck.github.io/"><img src="https://avatars.githubusercontent.com/u/20689127?v=4?s=100" width="100px;" alt="Matt Speck"/><br /><sub><b>Matt Speck</b></sub></a><br /><a href="#code-mjspeck" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/FinnBorge"><img src="https://avatars.githubusercontent.com/u/9272726?v=4?s=100" width="100px;" alt="FinnBorge"/><br /><sub><b>FinnBorge</b></sub></a><br /><a href="#code-FinnBorge" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/jklapacz"><img src="https://avatars.githubusercontent.com/u/5343758?v=4?s=100" width="100px;" alt="Jakub Klapacz"/><br /><sub><b>Jakub Klapacz</b></sub></a><br /><a href="#code-jklapacz" title="Code">💻</a></td>
    </tr>
  </tbody>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->
