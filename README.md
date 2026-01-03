## EDW-2 Snowflake Reasoning Assistant

The EDW-2 Reasoning Assistant is a Snowflake-native analytical and AI reasoning system designed to analyze enterprise revenue data, generate structured evidence, and produce business-grade explanations using Snowflake Cortex.

This project is the evolution of an earlier Google Colab prototype, fully rebuilt on Snowflake to achieve:
	•	Warehouse-level scalability
	•	Secure, governed data execution
	•	Native Streamlit UX
	•	LLM-driven reasoning inside the data platform

The system integrates SQL models, Snowpark Python, Cortex LLMs, and an agentic reasoning pipeline to answer business questions over structured data.

⸻

#  Authors
	•	Mehjabeen T Shaik
	•	Myles Green
	•	Sherin Kiruba Prem Anand
	•	Jeevith Doddalingegowda Rama

⸻

#  Features

1. Snowflake-Native Data Models

All analytics are computed dynamically using Snowflake SQL views:
	•	V_REVENUE_BY_QUARTER
	•	V_REVENUE_BY_REGION
	•	V_REVENUE_BY_PRODUCT

These views derive key metrics:
	•	Total Revenue
	•	Total Cost
	•	Total Profit

and power the reasoning pipeline.

⸻

2. Snowpark-Driven Analytics

The Streamlit app fetches view results using Snowpark:

    rev = session.sql("SELECT * FROM ...").to_pandas()

This ensures-
	•	zero external compute
	•	secure, in-warehouse execution
	•	low-latency analysis

⸻

3. Agentic LLM Reasoning Pipeline

The reasoning system includes four core agents:

Router:
Classifies the incoming question as:
	•	simple → requires no planning
	•	reasoning → requires multistep analysis

Planner:
Uses Cortex LLM to generate:
	•	sub-questions
	•	a structured JSON reasoning plan tied to quarter/region/product analytics

Executor:
Runs Snowflake analytics based on the plan:
	•	fetches relevant SQL views
	•	builds structured evidence objects

Synthesizer:
Calls Cortex again with:
	•	the user question
	•	the generated plan
	•	the evidence

and returns a polished, multi-paragraph business explanation.

⸻

4. Automated Sub-Question Generation

For reasoning queries, the system calls Cortex to generate clarifying sub-questions that help shape the plan.

These appear in the UI for transparency.

⸻

5. Simple Question Mode

If the query is straightforward (e.g., “Which product had the most revenue last quarter?”):
	•	the router skips planning
	•	evidence is passed directly to Cortex
	•	the model produces a concise factual answer

This ensures efficiency and prevents unnecessary reasoning overhead.

⸻

6. Snowflake Streamlit Application

The entire application runs inside Snowflake, providing:
	•	question input
	•	sub-question display
	•	plan visualization
	•	data previews (quarter/region/product)
	•	final AI explanation

All compute occurs in-warehouse.

⸻

#  Project Structure

app/
│
├── config.py            # Global configuration (models, constants, metadata)
├── session.py           # Snowflake Snowpark session helpers
├── analytics.py         # Fetch quarter/region/product analytics via Snowpark
├── routing.py           # classify_question() → simple vs reasoning
├── planning.py          # Generate subquestions + LLM-driven planning
├── evidence.py          # Build structured evidence objects
├── reasoning.py         # Synthesize final explanation (Cortex)
├── cortex_client.py     # Wrapper for SNOWFLAKE.CORTEX.COMPLETE
└── __init__.py
│
streamlit_app.py         # Main Snowflake Streamlit application
sql/
│   ├── create_schema.sql
│   ├── mock_data_inserts.sql
│   └── views.sql
README.md


⸻

# How It Works (High-Level Workflow)
	1.	User submits a business question
	2.	Router classifies it as simple or reasoning
	3.	If reasoning:
        •	LLM generates sub-questions
        •	LLM generates a multi-step JSON plan
	4.	Executor runs analytics views based on the plan
	5.	Evidence is packaged into structured JSON
	6.	Synthesizer calls Cortex to generate the final narrative explanation
	7.	UI displays:
        •	sub-questions
        •	plan
        •	evidence previews
        •	final explanation

⸻

#  Cortex LLM Integration

Cortex is used in three places:
	1.	Sub-question generation
	2.	Planning (JSON step generation)
	3.	Final reasoning synthesis

The system uses:
	•	SNOWFLAKE.CORTEX.COMPLETE
	•	Model: snowflake-arctic (or any allowed LLM)

All prompts are securely escaped for SQL execution.

⸻

#  Data Layer (SQL Models)

Your SQL models:
	•	auto-compute revenue metrics
	•	eliminate redundant logic
	•	offer consistent inputs to the LLM reasoning chain

This design supports future expansion: forecasts, anomalies, cost-driver analysis, etc.

⸻

#  Development Challenges Resolved
	•	Git integration and conflicts
	•	Snowflake schema mismatches (PUBLIC vs REASONING)
	•	Warehouse suspension issues
	•	Import path problems inside Snowflake UDF containers
	•	Cortex model availability errors

All were resolved through schema standardization, better SQL organization, and code restructuring.

⸻

#  Final Capabilities

The EDW-2 Reasoning Assistant now:
	•	answers business questions in natural language
	•	performs root-cause revenue analysis
	•	dynamically creates multi-step reasoning plans
	•	surfaces structured evidence
	•	runs entirely inside Snowflake
	•	provides enterprise-grade scalability and governance

⸻

#  Database & Data Setup (Snowflake)

This project includes a complete Snowflake SQL setup script that creates all required objects for the EDW-2 Reasoning Assistant. This removes guesswork for contributors and ensures that everyone works from the same canonical dataset.

What the Setup Script Creates

Running sql/setup_revenue_data.sql will create:
	•	A Snowflake database: EDW_2_DB
	•	A schema: REASONING
	•	A base fact table: REVENUE_TABLE
	•	Four core attributes per row:
        •	QUARTER
        •	REGION
        •	PRODUCT
        •	REVENUE
        •	COST
	•	The 16-row Honeywell-style sample dataset used in this project
	•	Three analytics views used by the Streamlit app:
        •	V_REVENUE_BY_QUARTER
        •	V_REVENUE_BY_REGION
        •	V_REVENUE_BY_PRODUCT

These are the exact structures that fetch_views() expects inside the application. If a contributor’s Snowflake environment does not contain these objects, the Streamlit app will not be able to function.

How to Run It
	1.	Open Snowflake → Worksheets
	2.	Select a warehouse (e.g., EDW_COMPUTE_WH)
	3.	Open the file sql/setup_revenue_data.sql
	4.	Run the entire script

Within seconds, the database is deployed and ready for the EDW-2 Streamlit app.

This SQL script ensures:
	•	Every team member works from the same consistent dataset
	•	The reasoning assistant behaves predictably across environments
	•	No manual table creation or data loading is required
	•	Snowflake-native analytics views align perfectly with the pipeline inside the app

This also supports future extensions: contributors may swap out the mock data for live Honeywell EDW data simply by replacing REVENUE_TABLE.

#  Deployment Instructions

Upload to Snowflake Git Integration
	1.	Create a new Snowflake Git repository mapping
	2.	Upload the project folder structure as-is
	3.	Ensure the following files appear in Git:

streamlit_app.py
app/*
sql/*

Create Streamlit App

In Snowflake UI:
	1.	Navigate to Projects → Streamlit
	2.	Create new app
	3.	Point to: <repo>/streamlit_app.py
	4.	Set execution role: ACCOUNTADMIN (or a custom role with SELECT + USAGE on EDW_2_DB.REASONING)
	5.	Select warehouse: EDW_COMPUTE_WH

The app will launch immediately.





#  License

Enterprise demonstration project — internal use only.
