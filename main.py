import json

from ai_compiler import AICompiler

COMPILER_PATH = 'ai_programs/'

with open('credentials.json', 'r') as file:
    credentials = json.load(file)

compiler = AICompiler(COMPILER_PATH, credentials["api_key"])

compiler.write_program('print_date', [
    {'role': 'system', 'content': """
        1. You must write program in JavaScript.
    """},
    {'role': 'user', 'content': """
    1. Create a function which takes a string in seconds and returns a string in 00:00:00 format using local timezone.
    2. Call this function with the current system time in seconds.
    3. Print the result.
    4. Make all function variables with underscores.
    """},
    ])

compiler.compile_program('print_date.ai.json', 'print_date.ai.js')