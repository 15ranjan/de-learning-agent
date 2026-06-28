
from groq import Groq
from tools import explain_topic, find_resource, plan_today, read_file, list_files, analyze_csv, write_file, delete_file
from dotenv import load_dotenv
import os
import json

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# Define tools in Groq's format
# This tells Groq EXACTLY what tools exist and what they do
tools = [
    {
        "type": "function",
        "function": {
            "name": "list_files",
            "description": "Lists all files in a folder",
            "parameters": {
                "type": "object",
                "properties": {
                    "folder_path": {
                        "type": "string",
                        "description": "Path to folder. Use '.' for current folder"
                    }
                },
                "required": ["folder_path"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "read_file",
            "description": "Reads content of any file",
            "parameters": {
                "type": "object",
                "properties": {
                    "file_path": {
                        "type": "string",
                        "description": "Path to the file to read"
                    }
                },
                "required": ["file_path"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "analyze_csv",
            "description": "Reads and analyzes a CSV file showing rows, columns, nulls",
            "parameters": {
                "type": "object",
                "properties": {
                    "file_path": {
                        "type": "string",
                        "description": "Path to the CSV file"
                    }
                },
                "required": ["file_path"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "write_file",
            "description": "Creates or writes a new file with given content",
            "parameters": {
                "type": "object",
                "properties": {
                    "file_path": {
                        "type": "string",
                        "description": "Path and name of file to create"
                    },
                    "content": {
                        "type": "string",
                        "description": "Content to write into the file"
                    }
                },
                "required": ["file_path", "content"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "delete_file",
            "description": "Deletes a file from the system",
            "parameters": {
                "type": "object",
                "properties": {
                    "file_path": {
                        "type": "string",
                        "description": "Path to the file to delete"
                    }
                },
                "required": ["file_path"]
            }
        }
    }
]

# Map tool names to actual Python functions
tool_map = {
    "list_files": list_files,
    "read_file": read_file,
    "analyze_csv": analyze_csv,
    "write_file": write_file,
    "delete_file": delete_file
}

def run_agent(user_message: str):
    print(f"\nYOU: {user_message}")
    print("-" * 50)

    system_prompt = """
    You are a Data Engineering learning assistant AND a file analysis agent.

    You help someone who is:
    - Transitioning from analytics to Data Engineering
    - Following a 6-7 month learning roadmap
    - Working 9-5 and studying 2-3 hours daily
    - Has Java and Spring Boot background
    - Moderate in Python

    You have access to tools to read files, list folders, analyze CSVs, and write files.
    When user asks about files or folders, ALWAYS use the tools — never guess or hallucinate.

    Always:
    - Keep explanations practical with real examples
    - Be encouraging but honest
    - Relate concepts to Java when helpful
    """

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_message}
    ]

    # Agent loop — keeps running until task is done
    while True:
        try:
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=messages,
                tools=tools,
                tool_choice="auto"
            )

            choice = response.choices[0]

            if choice.finish_reason == "tool_calls":
                tool_calls = choice.message.tool_calls
                messages.append(choice.message)

                for tool_call in tool_calls:
                    tool_name = tool_call.function.name
                    tool_args = json.loads(tool_call.function.arguments)

                    print(f"\n→ Agent using tool: {tool_name}")
                    print(f"→ With args: {tool_args}")

                    tool_function = tool_map[tool_name]
                    tool_result = tool_function(**tool_args)

                    print(f"→ Tool result: {tool_result[:100]}...")

                    messages.append({
                        "role": "tool",
                        "tool_call_id": tool_call.id,
                        "content": tool_result
                    })

            else:
                final_answer = choice.message.content
                print(f"\nAGENT: {final_answer}")
                return final_answer

        except Exception as e:
            # If tool calling fails, retry without tools
            print(f"\n→ Tool calling failed, retrying without tools...")
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=messages
            )
            final_answer = response.choices[0].message.content
            print(f"\nAGENT: {final_answer}")
            return final_answer