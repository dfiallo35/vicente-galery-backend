from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
import yaml
import sys

from main import app


def export_openapi_yaml(app: FastAPI, output_file: str):
    # Generate OpenAPI schema
    openapi_schema = get_openapi(
        title="Your API",
        version="1.0.0",
        description="This is a sample API",
        routes=app.routes,
        openapi_version="3.0.3"
    )

    # Convert to YAML
    yaml_schema = yaml.dump(openapi_schema, default_flow_style=False)

    # Save to file
    with open(output_file, 'w') as file:
        file.write(yaml_schema)

def export_openapi_json(app: FastAPI, output_file: str):
    # Generate OpenAPI schema
    openapi_schema = get_openapi(
        title="Your API",
        version="1.0.0",
        description="This is a sample API",
        routes=app.routes,
        openapi_version="3.0.3"
    )

    # Save to file
    with open(output_file, 'w') as file:
        file.write(openapi_schema)


if __name__ == '__main__':
    # make options
    if len(sys.argv) != 2:
        print('Usage: python utils.py [yaml|json]')
        sys.exit(1)
    
    option = sys.argv[1]
    if option not in ['yaml', 'json']:
        print('Usage: python utils.py [yaml|json]')
        sys.exit(1)
    
    match option:
        case 'json':
            export_openapi_json(app, 'openapi.json')
        case 'yaml':
            export_openapi_yaml(app, 'openapi.yaml')
        case _:
            print('Usage: python utils.py [yaml|json]')
            sys.exit(1)
    
    print(f'OpenAPI schema exported to openapi.{option}')
