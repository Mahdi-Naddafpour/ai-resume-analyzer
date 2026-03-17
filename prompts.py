RESUME_ANALYSIS_PROMPT = """
You are a professional resume analyzer.

Analyze the following resume and return:
1. Professional summary
2. Key technical skills
3. Strengths
4. Weaknesses
5. Suggestions for improvement

Resume:
{resume_text}
"""

MATCHING_PROMPT = """
You are a hiring assistant.

Compare the following resume with the job description and return:
1. Match score out of 100
2. Matching skills
3. Missing skills
4. Final evaluation

Resume:
{resume_text}

Job Description:
{job_description}
"""