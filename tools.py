def explain_topic(topic: str) -> str:
    """
    Tool 1: Explains any Data Engineering concept
    Input: topic name (string)
    Output: explanation (string)
    """
    return f"Explaining the topic: {topic}"

def find_resource(topic: str) -> str:
    """
    Tool 2: Finds learning resources for a topic
    Input: topic name (string)
    Output: resource suggestion (string)
    """
    return f"Finding best resources for: {topic}"

def plan_today(current_month: int, weak_areas: list) -> str:
    """
    Tool 3: Creates a study plan for today
    Input: current month number (int), weak areas (list)
    Output: study plan (string)
    """
    return f"Creating study plan for month {current_month}, weak areas: {weak_areas}"

def read_file(file_path: str) -> str:
    """
    Tool 4: Reads any file from your project
    Input: file path (string)
    Output: file content (string)
    """
    try:
        with open(file_path, 'r') as f:
            content = f.read()
        return f"File content of {file_path}:\n{content}"
    except FileNotFoundError:
        return f"Error: File {file_path} not found"
    except Exception as e:
        return f"Error reading file: {str(e)}"
    
def list_files(folder_path: str) -> str:
    """
    Tool 5: Lists all files in a folder
    Input: folder path (string)
    Output: list of files (string)
    """
    try:
        import os
        files = []
        for f in os.listdir(folder_path):
            files.append(f)
        return f"Files in {folder_path}:\n" + "\n".join(files)
    except FileNotFoundError:
        return f"Error: Folder {folder_path} not found"
    except Exception as e:
        return f"Error listing files: {str(e)}"
    
def analyze_csv(file_path: str) -> str:
    """
    Tool 6: Reads and analyzes a CSV file
    Input: file path (string)
    Output: analysis summary (string)
    """
    try:
        import pandas as pd
        df = pd.read_csv(file_path)
        
        summary = f"""
        CSV Analysis for {file_path}:
        → Rows: {df.shape[0]}
        → Columns: {df.shape[1]}
        → Column names: {list(df.columns)}
        → Null values: {df.isnull().sum().to_dict()}
        → Data types: {df.dtypes.to_dict()}
        → First 3 rows:
        {df.head(3).to_string()}
                """
        return summary
    except FileNotFoundError:
                return f"Error: File {file_path} not found"
    except Exception as e:
                return f"Error analyzing CSV: {str(e)}"
    
def write_file(file_path: str, content: str) -> str:
    """
    Tool 7: Creates or overwrites a file with given content
    Input: file path (string), content to write (string)
    Output: confirmation (string)
    """
    try:
        with open(file_path, 'w') as f:
            f.write(content)
        return f"✅ File created successfully: {file_path}"
    except Exception as e:
        return f"Error writing file: {str(e)}"

def delete_file(file_path: str) -> str:
    """
    Tool 8: Deletes a file
    Input: file path (string)
    Output: confirmation (string)
    """
    try:
        import os
        if os.path.exists(file_path):
            os.remove(file_path)
            return f"✅ File deleted successfully: {file_path}"
        else:
            return f"Error: File {file_path} not found"
    except Exception as e:
        return f"Error deleting file: {str(e)}"