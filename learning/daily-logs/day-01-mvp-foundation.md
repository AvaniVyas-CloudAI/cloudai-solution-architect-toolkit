# Day 01: MVP Foundation

## What I worked on today

Today I started building the first working version of my CloudAI Solution Architect Toolkit.

The goal was not to build a perfect AI product immediately. The goal was to create a simple foundation that I can improve step by step.

## Why I decided to work in phases

At first, the number of AI and cloud terms felt overwhelming.

Some of the terms I came across were:

- LLMs
- RAG
- Embeddings
- Vector databases
- Agents
- Prompt engineering
- Cloud deployment
- Monitoring
- Observability
- Feedback loops

I realized that trying to learn everything at once would make the project confusing.

So I decided to divide the project into phases.

Phase 1 is focused only on the MVP foundation.

## Phase 1 focus

The first phase is about building a simple working app before adding advanced AI features.

For now, the app is template-based.

It does not use a real LLM yet.
It does not use real RAG yet.
It does not connect to cloud services yet.

This is intentional because I first want to understand the structure of the solution.

## What I built

Today I worked on:

- Setting up the GitHub repository
- Creating the project folder structure
- Building a basic Streamlit app
- Creating a template-based AI/cloud solution brief generator
- Adding user input fields
- Adding generated solution brief sections
- Adding basic validation
- Testing the app locally
- Fixing Python indentation errors
- Committing the fixes locally
- Pushing the working version to GitHub

## What I learned

### 1. Building starts with a foundation

I learned that I do not need to understand every advanced AI concept before starting.

A small working foundation is more useful than waiting until everything is clear.

### 2. Streamlit helps create a simple app quickly

Streamlit allows me to create a web app using Python.

In this project, I used Streamlit to collect user inputs and display a structured AI/cloud solution brief.

### 3. AI solutions need structure

An AI/cloud solution is not only about using a model.

A good solution brief should include:

- Business problem
- AI use case
- Data sources
- Cloud services
- Security considerations
- Cost considerations
- Observability considerations
- Implementation approach

### 4. Data sources are important

I learned that an AI solution needs trusted data sources.

For example:

- FAQs
- Support tickets
- Product documentation
- Knowledge base articles
- Internal policies

Without trusted data, the output may not be reliable.

### 5. Validation improves the app

I added validation so the app does not generate a solution brief when the main business problem is empty.

This helps avoid weak or incomplete output.

### 6. Python indentation matters

I faced indentation errors while running the app locally.

This helped me understand that Python uses indentation to decide which lines belong together.

Fixing these errors was frustrating, but useful.

### 7. GitHub is part of the building process

Today I also pushed the working version to GitHub.

This helped me understand the flow of:

Local changes → commit → push → GitHub repository update

## Current project status

The current version is a simple MVP.

It can:

- Accept user inputs
- Generate a structured AI/cloud solution brief
- Show suggested architecture flow
- Suggest cloud services based on selected cloud preference
- Include security, cost, observability, and implementation sections
- Run locally using Streamlit

## Current limitations

The app does not yet include:

- Real LLM integration
- Real RAG
- Document upload
- Vector database
- Cloud deployment
- User feedback logging
- Monitoring dashboard
- Authentication

These may be added in later phases.

## Reflection

Today I learned that building an AI/cloud project can feel overwhelming because there are many terms and concepts involved.

Instead of trying to learn everything at once, I am learning to break the project into smaller phases.

Phase 1 helped me create a working foundation.

The app is still simple, but now it exists, runs locally, and has been pushed to GitHub.

That is a good first step.
