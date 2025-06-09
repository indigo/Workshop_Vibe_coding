**Workshop: Vibe Coding – Make Worlds, Tell Stories, Build Faster with AI**

**Target Audience:** Creative Professionals, Developers, Project Managers, Technical Writers interested in leveraging AI for content/world creation with enhanced control. (Assumes basic computer literacy, comfort with code editors like VS Code, and ideally some familiarity with Git concepts).

**Core Philosophy:** Shift creative focus from manual asset generation to meticulous description and structured approval, leveraging AI agents and specialized tools (MCPs) for generation and process management.

**Key Deliverables for Attendees:**
1.  Understanding of the Description-Driven Creation paradigm.
2.  A functional local development environment (VS Code, AI Agent, Git, `uv`).
3.  Installation and basic configuration of the World Builder MCP.
4.  Hands-on experience initiating a simple project using the World Builder MCP.
5.  Demonstration of AI image generation integrated into the workflow via an Image Generation MCP (API-based).
6.  Access to workshop materials (slides, code repositories, `plan.md`, session guides).
7.  **Guaranteed:** A post-workshop 1-on-1 session (scheduled via your website) to ensure their setup is successful.

**Materials & Tools:**
*   **Instructor:** Polished presentation slides, `plan.md` (workshop outline), `session_morning.md`, `session_afternoon.md`, `session_closing.md` (detailed guides/scripts), potentially pre-recorded demo segments ("vibe coding" style) for specific complex flows, working World Builder MCP repository, working Image Generation MCP (wrapper around paid API), example project files.
*   **Attendees:** Laptop meeting prerequisites, VS Code, Git, relevant AI Agent account/access, API key for Image Generation service (if requiring individual keys), access to instructor's GitHub repositories.

**Prerequisites (Communicate Clearly Beforehand):**
*   Laptop (macOS, Windows, Linux - specify if tested).
*   VS Code installed.
*   Git installed and basic familiarity (or willingness to follow precise steps).
*   GitHub account created.
*   Python installed (specify version). Recommend installing `uv` beforehand via provided instructions (`pip install uv`).
*   Account for the chosen AI Agent (e.g., OpenAI API key, Anthropic access, Roo/Windsurf setup if needed).
*   Sign up for the chosen Image Generation API service (e.g., Stability AI, Clipdrop) and obtain an API key (specify if free tier sufficient for workshop).
*   Reliable internet connection.

---

**Detailed Workshop Plan:**

**Session 1: Foundations & Setup (Morning - Approx 3 - 3.5 hours including breaks)**

*   **(0:00-0:15) Welcome & Introduction**
    *   Instructor introduction, workshop goals.
    *   High-level overview: The challenge of complex creation, the promise of AI, the "Description-Driven" paradigm shift.
    *   Briefly showcase an exciting end result (e.g., a generated image linked to a description).
    *   Mention the 1-on-1 setup guarantee upfront to build confidence.
    *   Agenda overview (`plan.md` reference).
*   **(0:15-1:15) Part 1: Core Environment Setup (Guided Hands-on)**
    *   **VS Code Quick Tour:** Essential UI elements (Explorer, Editor, Terminal, Source Control, Extensions).
    *   **Terminal & `uv`:** Ensure everyone can open the VS Code terminal. Quick check/install of `uv`. Create a project directory, initialize a virtual environment with `uv venv`.
    *   **AI Agent Setup:**
        *   Choose *one* primary Agent (e.g., Roo or integrate directly with OpenAI/Anthropic via an extension).
        *   Guided installation/configuration within VS Code (e.g., installing extension, adding API keys securely).
        *   Basic interaction test: Ask the agent a simple question to confirm functionality.
        *   *Brief Demo (Optional):* Show the interface of an alternative agent (e.g., Windsurf) to illustrate the *concept* of interchangeable agents without requiring setup.
    *   **Git Setup & Integration:**
        *   Initialize Git repo (`git init`).
        *   Configure username/email if needed.
        *   Using VS Code Source Control panel: Stage & commit initial project files.
        *   Explain the "why": Versioning, backup, "time travel" for iterating on descriptions. Show how the Agent *can* assist with Git commands (demo a simple `git status` or `git log` via agent).
    *   *(Buffer Time & Quick Q&A)*
*   **(1:15-1:30) Break**
*   **(1:30-2:15) Part 2: Concepts - MCPs & The Paradigm Shift (Presentation & Discussion)**
    *   **What are MCPs?** Your definition, purpose (structured interaction, state management, task execution). Analogy: Specialized assistants.
    *   **Why MCPs with AI?** Bridging natural language with structured processes, managing complex state, enabling focused workflows.
    *   **The Description-Driven Paradigm:**
        *   "Brain Only Mode" metaphor. Focusing effort on specification and approval.
        *   Analogy: Painter (sketch to masterpiece), Movie production (ingredients).
        *   Goal: Achieving control and predictability in AI-assisted creation via detailed description.
        *   How it differs from traditional methods (e.g., Scrum) - focusing on specification *before* generation.
*   **(2:15-3:00) Part 3: World Builder MCP Setup (Presentation & Guided Hands-on)**
    *   **Introducing the World Builder MCP:** Explain its specific role – managing creative assets (characters, locations, etc.), their descriptions, relationships, and approval states based on project templates.
    *   **Guided Install:**
        *   Clone the World Builder MCP repository from GitHub (`git clone ...`).
        *   Navigate into the directory.
        *   Install dependencies (using `uv pip install -r requirements.txt` if Python-based).
        *   Initial configuration steps (e.g., setting up a base directory for projects, explaining core config files).
    *   *(Buffer Time & Quick Q&A - Ensure MCP is installed)*

**Session 2: Application & Generation (Afternoon - Approx 3 - 3.5 hours including breaks)**

*   **(0:00-1:00) Part 4: World Builder MCP in Action - Simple Project (Demo & Hands-on)**
    *   **Recap:** Connect morning setup to afternoon's goal: using the tools.
    *   **Starting a New Project (Demo & Replicate):**
        *   Use WB MCP commands/interactions (via Agent/Terminal) to initialize a new project (e.g., "My First Story").
        *   Explain the directory structure created by the MCP.
    *   **Defining an Item (Demo & Replicate):**
        *   Use WB MCP to define a simple item type (e.g., `Character`).
        *   Add a specific character (e.g., "Captain Eva").
        *   Fill in descriptive fields (e.g., `description`, `appearance`, `personality_traits`) using the Agent for suggestions or writing directly. Emphasize detailed description.
        *   Show the approval process (how the MCP tracks status, how approval is marked).
    *   **Interaction:** Show how to query the WB MCP via the Agent ("Tell me about Captain Eva").
    *   *(Hands-on Time for Attendees to replicate)*
*   **(1:00-1:15) Break**
*   **(1:15-2:15) Part 5: Integrating AI Generation - Images (Demo Focused)**
    *   **Concept:** Explain the need for an "Image Generation MCP" - a specialized tool to interact with image APIs based on descriptions.
    *   **API Key Setup (Quick Guided Step):** Show attendees where to add their pre-obtained Image Generation API key (e.g., in a config file or environment variable used by the Image Gen MCP wrapper).
    *   **Demo Workflow:**
        1.  Use the Agent to retrieve the detailed description of "Captain Eva" from the World Builder MCP.
        2.  Instruct the Agent: "Generate an image of Captain Eva based on her description."
        3.  *(Behind the scenes explanation)* Agent extracts key details -> Formats prompt -> Calls the Image Generation MCP.
        4.  Image Generation MCP calls the paid API (e.g., Stability AI).
        5.  Display the generated image within VS Code or browser.
    *   **Discussion:** Highlight how the detailed description influenced the output. Discuss prompt engineering concepts briefly (how the Agent/MCP helps). Discuss potential iteration (modifying description, regenerating).
    *   *(Optional Hands-on):* Attendees trigger image generation for their own "Captain Eva" if time and API keys permit. Focus is on seeing the description-to-image link.
*   **(2:15-2:45) Part 6: Expanding (Demo & Optional Hands-on)**
    *   **Demo:** Show adding another related item (e.g., a `Location` like "Starship Bridge") and linking it to "Captain Eva" using the World Builder MCP.
    *   **Demo:** Show how relationships are tracked and can be queried ("Where is Captain Eva often found?").
    *   *(Optional Hands-on):* Attendees add a second item if comfortable and time allows.
*   **(2:45-3:00) Buffer & Q&A**

**Session 3: Closing & Next Steps (Approx 30 minutes)**

*   **(0:00-0:15) Recap & Key Takeaways**
    *   Reiterate the description-driven paradigm shift.
    *   Review the tools and workflow established (VS Code -> Agent -> WB MCP -> Gen AI).
    *   Emphasize the power of structured description for controlling AI output.
    *   Reinforce the value proposition for their own projects.
*   **(0:15-0:30) Q&A and Future**
    *   Open floor for final questions.
    *   **The Guarantee:** Remind attendees of the 1-on-1 setup guarantee.
    *   **Scheduling:** Clearly explain how to book their session via your website/scheduling link.
    *   Provide links to resources: Workshop slides, code repositories, relevant documentation, your contact/website.
    *   Briefly mention potential future workshops or consulting services.
    *   Thank attendees.

---

This detailed plan provides structure, incorporates all your requirements, manages complexity by separating setup/concepts/application, and highlights the value proposition, especially the critical 1-on-1 support for your premium clients. Remember to be flexible with timing based on the group's pace, especially during hands-on sections.