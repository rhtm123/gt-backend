import re


def determine_key(class_name):
    if class_name.startswith("text-"):
        if class_name in ["text-left", "text-center", "text-right", "text-justify"]:
            return "text-align"
        else:
            return "text-size"
    elif class_name.startswith("border-"):
        return class_name.split("-")[0] + "-" + class_name.split("-")[1]
    else:
        return class_name.split("-")[0]
    
    
def parse_tailwind_class(tailwind_class):
    # Define patterns for different class types
    patterns = [
        (r'^([a-z-]+)-(\d+)$', lambda m: {'property': m.group(1), 'value': m.group(2)}),  # e.g., border-l-4
        (r'^([a-z-]+)-([a-z]+)$', lambda m: {'property': m.group(1), 'value': m.group(2)}),  # e.g., text-blue
        (r'^([a-z-]+)-([a-z]+)-(\d+)$', lambda m: {'property': m.group(1), 'value': f"{m.group(2)}-{m.group(3)}"})  # e.g., bg-gray-200
    ]
    
    for pattern, handler in patterns:
        match = re.match(pattern, tailwind_class)
        if match:
            return handler(match)
    
    raise ValueError("Invalid Tailwind CSS class format")