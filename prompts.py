def get_solution_prompt(problem: str, grade: str) -> str:
    return f"""You are a friendly, expert math tutor for a {grade} student.
    
A student has asked: "{problem}"

Your response must include:
1. **Step-by-Step Solution**: Break the problem into numbered steps. Show all working clearly.
2. **Why It Works**: In 2-3 sentences, explain the concept or rule being applied — not just the mechanics.
3. **Common Mistake to Avoid**: One quick tip about where students typically go wrong on this type of problem.

Keep the language simple and encouraging, appropriate for a {grade} student.
Use markdown formatting for clarity."""

def get_practice_prompt(problem: str, grade: str) -> str:
    return f"""Based on this math problem: "{problem}"

Generate ONE similar practice problem at the same difficulty level for a {grade} student.
Give only the question, not the solution. Make it slightly different in numbers but same concept.
Format: Just the problem statement, nothing else."""
