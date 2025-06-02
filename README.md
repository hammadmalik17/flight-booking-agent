# Flight Booking AI Agent

A modular, multi-agent AI system for automated flight booking — built with Python CrewAI, LangChain, powered by Large Language Models (LLMs).

---

## 🚀 Project Overview

This project simulates an intelligent flight booking assistant composed of specialized AI agents working in concert:

- **Concierge Agent:** Collects user travel details (destination, date, passenger name).
- **Validator Agent:** Validates user input data for correctness and completeness.
- **Planner Agent:** Searches for suitable flights based on validated data.
- **Booker Agent:** Books the best available flight option.
- **Summarizer Agent:** Generates a natural language summary of the booking details.

The agents are orchestrated using the `CrewAI` library, following a **sequential process** where each task feeds its output to the next agent.

---

## 📂 Project Structure

- `app.py` — Main entry point: defines agents, tasks, assembles the Crew, and runs the booking workflow.
- `test_api.py` — Simple script to test your OpenAI (or compatible) API key setup.
- `agents/` — Folder containing agent implementations (concierge, validator, planner, booker, summarizer).
- `.env` — Environment file to securely store API keys (not included in repo).

---

## ⚙️ Technologies Used

- **Python 3.10+**
- **CrewAI:** For multi-agent orchestration and workflow management.
- **OpenAI GPT API** (or compatible LLMs like Google Gemini or Anthropic Claude) — for natural language processing.
- **dotenv:** To manage environment variables securely.
- **Requests / HTTP client:** For API communication (where applicable).

---

## 🔑 Prerequisites

- Python 3.10 or higher installed
- `pip` for dependency management
- Valid **OpenAI API key** or alternative LLM API key (Google Gemini, Anthropic Claude, etc.)

---

## 💡 Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/flight-booking-agent.git
   cd flight-booking-agent
````

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the root directory with your API key:

   ```
   OPENAI_API_KEY=sk-yourkeyhere
   ```

   Or configure your alternative LLM API key accordingly.

4. Test your API key:

   ```bash
   python test_api.py
   ```

5. Run the main app:

   ```bash
   python app.py
   ```

---

## 🛠️ How It Works

* User inputs are hardcoded in `app.py` for simulation but can be extended for real-time input.
* Each task is encapsulated as a `Task` object assigned to an agent.
* The `Crew` class manages the flow between agents sequentially.
* Agents communicate via passing structured outputs to the next task.
* Verbose mode enabled for detailed runtime logs.

---

## 🧩 Extensibility

* Easily swap out or add new agents to handle other travel-related tasks.
* Integrate real user input mechanisms (e.g., web forms, chat UI).
* Switch LLM providers by updating the API client and keys.
* Enhance validation and booking logic to connect to real airline APIs.

---

## ⚠️ Important Notes

* **API Key Required:** This project depends on external LLM APIs which require valid, active API keys with sufficient quota.
* **No keys included:** For security reasons, `.env` is excluded from version control.
* **Rate Limits & Billing:** Be aware of API usage costs and limits from your provider.
* **Currently a Simulation:** Flight search and booking are mock processes—replace with real APIs to go live.

---

## 🙏 Acknowledgments

* Inspired by advancements in multi-agent AI workflows and LLM integration.
* Thanks to the `CrewAI` framework for seamless agent orchestration.
* Inspired by open-source projects exploring AI-driven automation.

---

## 📞 Contact

For questions or collaboration, reach out via \[drhammadmalik2020@gmail.com] or open an issue.

---

> *Built with passion, powered by curiosity — ready to fly when the keys align.* ✈️


