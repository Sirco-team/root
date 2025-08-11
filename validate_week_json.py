import json
import sys

def validate_week_json(data):
    errors = []
    if not isinstance(data, dict):
        errors.append('Root should be a JSON object.')
        return errors
    if 'title' not in data or not isinstance(data['title'], str):
        errors.append('Missing or invalid "title" (should be a string).')
    if 'sections' not in data or not isinstance(data['sections'], list):
        errors.append('Missing or invalid "sections" (should be a list).')
        return errors
    for i, section in enumerate(data['sections']):
        if not isinstance(section, dict):
            errors.append(f'Section {i} is not an object.')
            continue
        if 'title' not in section or not isinstance(section['title'], str):
            errors.append(f'Section {i} missing or invalid "title".')
        if 'color' not in section or not isinstance(section['color'], str):
            errors.append(f'Section {i} missing or invalid "color".')
        if 'content' not in section or not isinstance(section['content'], list):
            errors.append(f'Section {i} missing or invalid "content" (should be a list).')
            continue
        for j, item in enumerate(section['content']):
            if not isinstance(item, dict):
                errors.append(f'Section {i} content[{j}] is not an object.')
                continue
            if 'type' not in item or item['type'] not in ['text', 'image']:
                errors.append(f'Section {i} content[{j}] missing or invalid "type" (should be "text" or "image").')
            if item['type'] == 'text':
                if 'text' not in item or not isinstance(item['text'], str):
                    errors.append(f'Section {i} content[{j}] missing or invalid "text".')
            if item['type'] == 'image':
                if 'src' not in item or not isinstance(item['src'], str):
                    errors.append(f'Section {i} content[{j}] missing or invalid "src" for image.')
                if 'alt' not in item or not isinstance(item['alt'], str):
                    errors.append(f'Section {i} content[{j}] missing or invalid "alt" for image.')
    return errors

def main():
    if len(sys.argv) < 2:
        print('Usage: python validate_week_json.py <json_file>')
        sys.exit(1)
    with open(sys.argv[1], 'r') as f:
        try:
            data = json.load(f)
        except Exception as e:
            print(f'Error loading JSON: {e}')
            sys.exit(1)
    errors = validate_week_json(data)
    if errors:
        print('Validation errors:')
        for err in errors:
            print('-', err)
        sys.exit(1)
    print('JSON is valid for the template.')

if __name__ == '__main__':
    main()
