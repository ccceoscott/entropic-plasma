---
name: adk-tool-scaffold
description: Google Agent Development Kit (ADK) tool scaffolder — generates typed tool definitions, function declarations, and agent wiring for Gemini-powered agents.
phase: "209"
category: ai
tags: ["ADK", "google-ai", "agents", "tool-scaffold", "gemini"]
---

# Adk Tool Scaffold (R.A.P.S.) — Phase 207.16

# Instructions

1. **Identify the Tool Name**:
   Extract the name of the tool the user wants to build (e.g., "StockPrice", "EmailSender").

2. **Review the Example**:
   Check `examples/WeatherTool.py` to understand the expected structure of an ADK tool (imports, inheritance, schema).

3. **Run the Scaffolder**:
   Execute the python script to generate the initial file.

   ```bash
   python scripts/scaffold_tool.py <ToolName>
   ```

4. **Refine**:
   After generation, you must edit the file to:
   - Update the `execute` method with real logic.
   - Define the JSON schema in `get_schema`.

## Example Usage
User: "Create a tool to search Wikipedia."
Agent:
1. Runs `python scripts/scaffold_tool.py WikipediaSearch`
2. Editing `WikipediaSearchTool.py` to add the `requests` logic and `query` argument schema.
