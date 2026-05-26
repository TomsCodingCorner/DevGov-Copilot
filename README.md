# DevGov Copilot

**Governance-aware AI assistant for pull request review and repository compliance.**

DevGov Copilot is an AI-powered GitHub pull request analyzer that reviews code changes against repository-specific governance rules, architecture guidelines, coding standards, and security policies.

Instead of only giving generic code-review feedback, DevGov Copilot evaluates whether a pull request fits the actual engineering standards of the project.

---

## Overview

Modern software projects often contain important engineering rules inside files such as:

- `governance.md`
- `architecture.md`
- `coding_standards.md`
- `security_policy.md`
- `README.md`
- `.github/copilot-instructions.md`

However, these rules are not always checked consistently during pull request reviews.

DevGov Copilot solves this by using AI to analyze pull requests against repository-specific governance documents. It helps reviewers detect architectural drift, missing tests, security concerns, maintainability risks, and violations of project-specific standards before code is merged.

The goal is not to replace human reviewers.

The goal is to make reviews more consistent, traceable, and aligned with the actual rules of the repository.

---

## Problem

Pull request reviews usually focus on whether the code works and whether the implementation looks clean.

However, teams often miss deeper project-level concerns such as:

- Does this change fit the existing architecture?
- Does this PR follow the repository’s governance rules?
- Are testing requirements followed?
- Does the change introduce security or privacy risks?
- Does the implementation violate internal coding standards?
- Are documentation updates required?
- Does the PR introduce architectural drift?
- Is the code maintainable within the current project structure?

Over time, these missed issues create technical debt, inconsistent architecture, weaker security, and lower engineering quality.

---

## Solution

DevGov Copilot analyzes a pull request by combining:

1. GitHub pull request metadata
2. PR diff and changed files
3. Repository governance documents
4. Architecture and coding standards
5. Security and testing requirements
6. AI-based reasoning
7. Risk scoring

The system then generates a structured governance review containing:

- Overall verdict
- Governance risk score
- Risk level
- Rule violations
- Architecture concerns
- Missing tests
- Documentation issues
- Security concerns
- Maintainability risks
- Suggested improvements
- Ready-to-use GitHub review comment

---

## Core Features

### Pull Request Analysis

DevGov Copilot retrieves and analyzes GitHub pull request data, including:

- PR title
- PR description
- Changed files
- Code diff
- Commit metadata
- Target branch
- Author information
- Labels

---

### Governance Document Loading

The system searches the repository for relevant project documents, such as:

```text
governance.md
architecture.md
coding_standards.md
security_policy.md
README.md
.github/copilot-instructions.md
```

These documents are used as the review framework for the AI analysis.

---

### AI Governance Review

The AI review engine evaluates the pull request against the project-specific standards found in the repository.

It checks for:

- Architecture fit
- Governance violations
- Missing tests
- Security concerns
- Maintainability risks
- Naming consistency
- Folder structure consistency
- Documentation impact
- Hidden side effects
- Risky implementation choices

---

### Risk Scoring

Each pull request receives a governance risk score.

Example:

```text
Governance Risk Score: 72/100
Risk Level: Medium
Verdict: Needs Changes
```

Scoring factors:

| Factor | Weight |
|---|---:|
| Architecture fit | 25% |
| Test coverage | 20% |
| Security risk | 20% |
| Maintainability | 15% |
| Documentation impact | 10% |
| Naming and structure consistency | 10% |

---

### Automated Review Report

DevGov Copilot generates a structured Markdown review that can be used directly in GitHub.

Example:

```markdown
## DevGov Copilot Review

**Verdict:** Needs Changes  
**Risk Level:** Medium  
**Governance Risk Score:** 72/100

### Main Issues

1. The new endpoint bypasses the existing service layer.
2. No unit test was added for the new validation logic.
3. The implementation introduces a naming inconsistency with the current module structure.

### Recommended Changes

- Move business logic into the service layer.
- Add tests for both success and failure scenarios.
- Rename the new utility file to match the existing naming convention.

### Governance References

- `architecture.md`: API endpoints should not directly access persistence logic.
- `coding_standards.md`: New features require unit tests.
- `security_policy.md`: Input validation is required for externally exposed endpoints.
```

---

## Architecture

```text
GitHub Repository
        ↓
GitHub API
        ↓
Pull Request Diff Fetcher
        ↓
Governance Document Loader
        ↓
Context Builder
        ↓
AI Review Engine
        ↓
Risk Scoring Layer
        ↓
Review Report Generator
        ↓
CLI / Dashboard / GitHub Comment
```

---

## Tech Stack

| Component | Technology |
|---|---|
| Backend | Python, FastAPI |
| CLI | Typer |
| AI | Azure OpenAI / Azure AI Foundry |
| GitHub Integration | GitHub REST API / GraphQL API |
| Storage | SQLite / PostgreSQL |
| Frontend | React / Next.js |
| Deployment | Azure App Service / Azure Container Apps |
| Logging | Azure Application Insights |

---

## MVP Scope

The first version focuses on a simple but useful workflow.

### Included in MVP

- Fetch a GitHub pull request by repository and PR number
- Retrieve PR metadata and diff
- Load governance documents from the repository
- Build a structured review context
- Generate an AI-based governance review
- Calculate a governance risk score
- Export the review as Markdown
- Save review output locally

### Not Included in MVP

- Automatic GitHub commenting
- Automatic merge blocking
- Full CI/CD integration
- Multi-repository support
- Autonomous code changes
- User management
- Team permissions

---

## CLI Usage

Example command:

```bash
devgov review --repo owner/project --pr 12
```

Example output:

```text
Verdict: Needs Changes
Risk Score: 68/100
Risk Level: Medium

Top Issues:
1. Missing test coverage for new service logic.
2. Endpoint violates architecture rule: controllers should not access storage directly.
3. Documentation was not updated.

Generated review saved to:
outputs/pr_12_review.md
```

---

## Example Review Output

```markdown
# DevGov Copilot Review

## Pull Request

**Repository:** owner/project  
**Pull Request:** #12  
**Title:** Add user profile endpoint  
**Target Branch:** main  

---

## Verdict

**Needs Changes**

The pull request introduces useful functionality, but it does not fully comply with the repository’s architecture and testing standards.

---

## Governance Risk Score

**68/100**

Risk level: **Medium**

---

## Main Issues

### 1. Architecture Violation

The new API endpoint contains business logic directly inside the controller layer.

According to the repository architecture guidelines, controllers should only handle request validation and response formatting. Business logic should be placed inside the service layer.

**Recommended change:**  
Move the user profile update logic into the existing service layer.

---

### 2. Missing Test Coverage

The pull request adds new behavior but does not include tests for the new functionality.

**Recommended change:**  
Add tests for:

- Successful profile update
- Invalid input
- Unauthorized access
- User not found

---

### 3. Documentation Not Updated

The pull request introduces a new API endpoint, but the API documentation was not updated.

**Recommended change:**  
Update the relevant documentation file with the new endpoint, request body, response format, and error cases.

---

## Security Notes

No critical security issue was detected, but the new endpoint should include explicit input validation before being considered production-ready.

---

## Suggested GitHub Review Comment

This PR adds useful functionality, but it needs changes before merge.

Main concerns:

1. Business logic is currently placed inside the controller layer.
2. No tests were added for the new endpoint.
3. API documentation was not updated.
4. Input validation should be made explicit.

Please move the business logic into the service layer, add tests for success and failure paths, and update the API documentation.
```

---

## Repository Governance Files

A repository can define its own engineering rules using files such as:

```text
/governance.md
/architecture.md
/coding_standards.md
/security_policy.md
/.github/copilot-instructions.md
```

Example `architecture.md`:

```markdown
# Architecture Rules

- API routes should only handle request validation and response formatting.
- Business logic must be placed inside the service layer.
- Database access must go through repository classes.
- Every new feature must include tests.
- Security-sensitive changes require explicit validation checks.
- Public APIs must be documented.
```

DevGov Copilot uses these rules as part of the AI review context.

---

## Project Structure

Planned structure:

```text
devgov-copilot/
│
├── app/
│   ├── main.py
│   ├── config.py
│   │
│   ├── github/
│   │   ├── client.py
│   │   ├── pr_fetcher.py
│   │   └── diff_parser.py
│   │
│   ├── governance/
│   │   ├── document_loader.py
│   │   ├── context_builder.py
│   │   └── rules_extractor.py
│   │
│   ├── ai/
│   │   ├── review_engine.py
│   │   ├── prompts.py
│   │   └── scoring.py
│   │
│   ├── reports/
│   │   ├── markdown_writer.py
│   │   └── json_writer.py
│   │
│   └── cli.py
│
├── outputs/
│   └── .gitkeep
│
├── tests/
│   ├── test_diff_parser.py
│   ├── test_document_loader.py
│   └── test_scoring.py
│
├── .env.example
├── requirements.txt
├── README.md
└── LICENSE
```

---

## Environment Variables

Create a `.env` file based on `.env.example`.

```env
GITHUB_TOKEN=your_github_token
AZURE_OPENAI_ENDPOINT=your_azure_openai_endpoint
AZURE_OPENAI_API_KEY=your_azure_openai_api_key
AZURE_OPENAI_DEPLOYMENT=your_model_deployment_name
AZURE_OPENAI_API_VERSION=your_api_version
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/devgov-copilot.git
cd devgov-copilot
```

Create a virtual environment:

```bash
python -m venv .venv
```

Activate the virtual environment:

Windows:

```bash
.venv\Scripts\activate
```

macOS / Linux:

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create your environment file:

```bash
cp .env.example .env
```

Add your GitHub and Azure OpenAI credentials to `.env`.

---

## Usage

Run a pull request review:

```bash
python -m app.cli review --repo owner/project --pr 12
```

Expected output:

```text
Fetching pull request...
Loading governance documents...
Building review context...
Generating AI governance review...
Calculating risk score...

Verdict: Needs Changes
Risk Score: 68/100
Risk Level: Medium

Review saved to:
outputs/pr_12_review.md
```

---

## Output Files

For each analyzed pull request, DevGov Copilot can generate:

```text
outputs/
├── pr_12_review.md
├── pr_12_review.json
└── pr_12_context.json
```

### Markdown Output

The Markdown file is designed to be readable and usable as a GitHub review comment.

### JSON Output

The JSON file is designed for future dashboarding, automation, and integration with CI/CD workflows.

### Context Output

The context file stores the structured review context used by the AI model. This helps with debugging, reproducibility, and evaluation.

---

## Roadmap

### V0.1 — CLI Prototype

- Connect to GitHub API
- Fetch PR metadata
- Fetch PR diff
- Load governance documents
- Build review context
- Generate Markdown review output

### V0.2 — Risk Scoring

- Add structured scoring system
- Add severity levels
- Add rule violation categories
- Add JSON output
- Add confidence indicators

### V0.3 — Dashboard

- Add simple web interface
- Show PR review history
- Show risk score trends
- Display governance violations visually
- Add filtering by repository, risk level, and verdict

### V0.4 — GitHub Integration

- Post review comments directly to GitHub
- Support GitHub Actions
- Add repository configuration file
- Add automatic PR review triggers

### V0.5 — Agentic Workflow

- Generate implementation plans
- Suggest concrete fixes
- Create issues from review findings
- Prepare human-approved pull request improvements

---

## Future Vision

The long-term vision is to turn DevGov Copilot into a governance-aware developer workflow layer.

Possible future capabilities:

- Automatic PR comments
- GitHub Actions integration
- Repository-specific governance configuration
- Multi-repository support
- Pull request risk history
- Architecture drift detection
- Security policy enforcement
- Documentation impact detection
- Developer productivity analytics
- Human-approved agentic code improvement workflows

---

## Why This Project Matters

DevGov Copilot explores how AI can improve software engineering workflows without replacing human reviewers.

The goal is not to let AI blindly approve or reject code.

The goal is to support human reviewers by detecting:

- Project-specific rule violations
- Architectural drift
- Missing tests
- Security concerns
- Maintainability risks
- Documentation gaps

This makes the review process more consistent, traceable, and aligned with engineering standards.

---

## Microsoft-Relevant Concepts

This project connects to several enterprise AI and developer productivity themes:

- AI-assisted software engineering
- GitHub workflow automation
- Governance-aware AI systems
- Human-in-the-loop review
- Azure AI integration
- Developer productivity
- Responsible AI
- Enterprise copilots
- Agentic developer workflows
- Software delivery governance
- Repository-specific AI reasoning

---

## Portfolio Pitch

DevGov Copilot is a governance-aware AI pull request analyzer that reviews GitHub pull requests against repository-specific engineering standards.

It combines GitHub workflow automation, Azure AI, repository context, architecture rules, and risk scoring to help teams detect architectural drift, missing tests, security concerns, and governance violations before code is merged.

---

## Interview Pitch

I built DevGov Copilot because I wanted to create something closer to enterprise AI than a basic chatbot.

It is a governance-aware pull request analyzer that connects GitHub workflow data with repository-specific architecture and coding standards. The system uses Azure AI to analyze pull requests, detect governance violations, score risk, and generate actionable review comments.

The project explores how AI can improve software delivery while keeping human review, engineering standards, and traceability central.

---

## License:

This project is intended as a portfolio and learning project.

License: MIT
This project is intended as a portfolio and learning project.

License: MIT
