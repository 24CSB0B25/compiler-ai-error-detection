THREAT_CATEGORIES = {
    "gets": "Unsafe Function",
    "strcpy": "Unsafe Function",
    "scanf": "Unsafe Function",
    "buffer_decl": "Buffer Overflow Risk",
}

SEVERITY_LEVELS = {
    "Unsafe Function": "HIGH",
    "Buffer Overflow Risk": "MEDIUM",
    "Unknown": "LOW"
}

def analyze_token(token):
    category = THREAT_CATEGORIES.get(token, "Unknown")
    severity = SEVERITY_LEVELS.get(category, "LOW")
    return category, severity
