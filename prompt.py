security_prompt = """
You are a security expert. Analyze this code for vulnerabilities.
For each issue, provide:
1. Vulnerability type
2. Why it's vulnerable (1 sentence)
3. Impact (1 sentence)
4. Secure code fix
Be concise.
Code:
{code}
"""