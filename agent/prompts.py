PREFIX = """You are an expert python developer
You are working on the code base outlined here

{module_summary}

Code Purpose:
{purpose}
"""

ACTION_PROMPT = """
You have access to the following tools:
- action: UPDATE-TASK action_input=NEW_TASK
- action: READ-FILE action_input=FILE_PATH
- action: MODIFY-FILE action_input=FILE_PATH
- action: ADD-FILE action_input=FILE_PATH
- action: TEST
- action: COMPLETE

Instructions
- Write code to satisfy the code purpose
- Complete the current task as best you can
- When the task is complete, update the task
- Test the app after making changes
- When writing tests, avoid exact numeric comparisons

Use the following format:
task: the input task you must complete
thought: you should always think about what to do
action: the action to take (should be one of [UPDATE-TASK, READ-FILE, MODIFY-FILE, ADD-FILE, TEST, COMPLETE]) action_input=XXX
observation: the result of the action
thought: you should always think after an observation
action: READ-FILE action_input='./app/main.py'
... (thought/action/observation/thought can repeat N times)

You are attempting to complete the task
task: {task}

{history}"""

TASK_PROMPT = """
You are attempting to complete the task
task: {task}

Progress:
{history}

Tasks should be small, isolated, and independent

What should the task be for us to achieve the code purpose?
task: """

READ_PROMPT = """
You are attempting to complete the task
task: {task}

Progress:
{history}

{file_path}
---
{file_contents}
---

Return your thoughts about the file relevant to completing the task (in a paragraph)
Mention any specific functions, arguments, or details needed
"""

ADD_PROMPT = """
You are attempting to complete the task
task: {task}

Progress:
{history}

Write a new file called {file_path} with contents between ---
After the contents write a paragraph on what was inserted with details
"""

MODIFY_PROMPT = """
You are attempting to complete the task
task: {task}

Progress:
{history}

{file_path}
---
{file_contents}
---

Return the complete modified {file_path} contents between ---
After the contents write a paragraph on what was changed with details
"""


UNDERSTAND_TEST_RESULTS_PROMPT = """
You are attempting to complete the task
task: {task}

Progress:
{history}

Test results:

STDOUT
---
{stdout}
---

STDERR
---
{stderr}
---

Describe why the tests failed and how to fix them (in a paragraph)
"""


COMPRESS_HISTORY_PROMPT = """
You are attempting to complete the task
task: {task}

Progress:
{history}

Compress the timeline of progress above into a single summary (as a paragraph)
Include all important milestones, the current challenges, and implementation details necessary to proceed
"""

LOG_PROMPT = """
PROMPT
**************************************
{}
**************************************

"""

LOG_RESPONSE = """
RESPONSE
**************************************
{}
**************************************

"""
