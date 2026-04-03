def explain_error(error_message, error_type, mode="beginner"):

    explanations = {
        "ZeroDivisionError": {
            "beginner": "You are dividing by zero. This is not allowed.",
            "pro": "Division by zero caused ZeroDivisionError."
        },
        "NameError": {
            "beginner": "You used a variable that is not defined.",
            "pro": "Variable not found in current scope."
        },
        "SyntaxError": {
            "beginner": "There is a syntax mistake.",
            "pro": f"SyntaxError: {error_message}"
        }
    }

    return explanations.get(error_type, {}).get(mode, "Unknown error")


def explain_why(error_type):
    reasons = {
        "ZeroDivisionError": "Denominator is zero.",
        "NameError": "Variable used before definition."
    }
    return reasons.get(error_type, "No reason available.")


def suggest_fix(error_type, code):

    fixes = []

    if error_type == "ZeroDivisionError":
        fixes.append("Check denominator before dividing.")
    elif error_type == "NameError":
        fixes.append("Define variable before using.")
    elif error_type == "SyntaxError":
        fixes.append("Check syntax carefully.")

    return fixes


def step_by_step_explanation(error_type):

    steps = {
        "ZeroDivisionError": [
            "Step 1: Division operation detected.",
            "Step 2: Denominator is zero.",
            "Step 3: Division by zero is invalid.",
            "Step 4: Change denominator."
        ],
        "NameError": [
            "Step 1: Variable used.",
            "Step 2: Not defined.",
            "Step 3: Python cannot find it.",
            "Step 4: Define it first."
        ]
    }

    return steps.get(error_type, ["No steps available."])


def auto_fix_code(code, language="Python"):

    fixed_code = code

    if language == "Python":
        fixed_code = fixed_code.replace("=", " = ")

        if "/ 0" in fixed_code:
            fixed_code = fixed_code.replace("/ 0", "/ 1  # fixed")

    elif language in ["C++", "Java"]:
        if ";" not in fixed_code:
            fixed_code += ";\n// Added missing semicolon"

    return fixed_code