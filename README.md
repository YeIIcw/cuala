# ʕ•ᴥ•ʔ Cuala 

_A State-of-the-Art Computer-Use Agent built with [Cua](https://github.com/trycua/cua) and benchmarked on [HUD](https://hud.so)._

---

### 📌 Overview
Cuala is my submission for the **Computer-Use Agent SOTA Challenge**.  
It’s designed as a **general-use operator** that prioritizes **deterministic actions, verifiable state changes, and robust evaluation alignment** rather than brittle, task-specific prompting.

---

### ⚙️ Technical Approach
I customized the agent across three layers:

1. **Prompting (primary method)**  
   - Added explicit **hard constraints** and **task-specific sub-rules** (e.g., always reopen dialogs to confirm persistence).  
   - Guarded against exploration by enforcing **menu-path or config-only actions**.  
   - Infeasible tasks (e.g., DRM media in VLC, VS Code Arabic w/o extension) are explicitly terminated with `"task is infeasible"`.

2. **Custom tools**  
   - Experimented with Python functions as callable tools.  
   - In this dataset (14 tasks), these were less impactful since most tasks were highly diverse.  
   - In larger datasets (e.g., multiple spreadsheet tasks), tools would shine — e.g., a custom Excel “fill blank cells down” function.

3. **Callbacks**  
   - Added `ImageRetentionCallback` and `TrajectorySaverCallback` to improve traceability and debugging.  
   - Helped avoid wasted steps and allowed replay for analysis.

**Future work**: building **custom agent loops** (`@register_agent`) for more structured task families.

P.S. also made response agent allowing submissions instead of constant prompting agent to continue ʕ•ᴥ•ʔ!
---

### 🧪 HUD Benchmark Results
Dataset: **OSWorld-Tiny-Public**  
Model: **anthropic/claude-sonnet-4-20250514**  
Job link: [View HUD Scorecard](https://app.hud.so/jobs/179e0916-e0a8-411d-ac5e-835713b69dd0)  

- **Score:** 42% (6/14 successful)  
- **Successful tasks:** Chrome rename, VS Code theme, autosave, lowercase conversion, GIMP dock removal, etc.  
- **Failures:** 8/14, with several being **near-successes blocked by technical submit/evaluation timing** (visible in traces).  

---

### 📊 Generalization vs. Overfitting
While I could have micro-prompted per-task for higher raw completion on the 14 tasks, that tends to produce:
- **Evaluation gaps** (HUD “No Score”)  
- **Non-transferable** behavior that breaks on unseen tasks  

Instead, I optimized for **generalization**:  
- Deterministic actions  
- Explicit verification + persistence checks  
- Standardized finish signaling  

Result: fewer “No Score” outcomes and traces that show **portable behaviors** beyond the benchmark.  
This matches the long-term goal of CUAs: **operators, not macros**.

---

### 🚀 How to Reproduce
Follow intructions in notebooks/sota_hackathon.ipynb!

---

### 🏆 Why this matters

Cuala demonstrates how **prompt engineering + HUD evaluation + careful verification** can push CUAs closer to **true general-use assistants**, not overfitted task macros.

