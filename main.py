import json
import os

from ai_compiler import AICompiler

COMPILER_PATH = 'ai_programs/'

with open('credentials.json', 'r') as file:
    credentials = json.load(file)

with open('main.ai.txt', 'r') as file:
    main_ai = file.read()

compiler = AICompiler(COMPILER_PATH, credentials["api_key"])

compiler.write_and_compile_program('main', [
    {'role': 'system', 'content': """
        1. You must write program in Python.
    """},
    {'role': 'user', 'content': main_ai},
], 'py')

# run COMPILER_PATH/main.ai.js in console
os.system('python3 ' + COMPILER_PATH + 'out/main.ai.py')
