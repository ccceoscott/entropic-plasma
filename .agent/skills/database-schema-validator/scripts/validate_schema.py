import sys
import re

def validate_schema(filename):
    
    try:
        with open(filename, 'r') as f:
            content = f.read()
            
        lines = content.split('\n')
        errors = []
        
        
        if re.search(r'DROP TABLE', content, re.IGNORECASE):
            errors.append("ERROR: 'DROP TABLE' statements are forbidden.")
            
        
        table_defs = re.finditer(r'CREATE TABLE\s+(?P<name>\w+)\s*\((?P<body>.*?)\);', content, re.DOTALL | re.IGNORECASE)
        
        for match in table_defs:
            table_name = match.group('name')
            body = match.group('body')
            
            
            if not re.match(r'^[a-z][a-z0-9_]*$', table_name):
                errors.append(f"ERROR: Table '{table_name}' must be snake_case.")
                
            
            if not re.search(r'\bid\b.*PRIMARY KEY', body, re.IGNORECASE):
                errors.append(f"ERROR: Table '{table_name}' is missing a primary key named 'id'.")

        if errors:
            for err in errors:
                print(err)
            sys.exit(1)
        else:
            print("Schema validation passed.")
            sys.exit(0)
            
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python validate_schema.py <schema_file>")
        sys.exit(1)
        
    validate_schema(sys.argv[1])
