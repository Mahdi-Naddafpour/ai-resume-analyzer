# AI Resume Analyzer API

A backend project built with Python and Flask that analyzes resumes and evaluates their match against job descriptions.

## Features

- Analyze resume text
- Extract technical skills
- Identify strengths and weaknesses
- Generate improvement suggestions
- Compare resumes with job descriptions
- Return structured JSON responses through REST API endpoints

## Tech Stack

- Python
- Flask
- JSON
- REST API
- Modular backend architecture

## API Endpoints

### GET /
Returns API status.

### POST /analyze
Analyzes a resume.

Example request body:
```json
{
  "resume_text": "Python developer with SQL and API experience"
}