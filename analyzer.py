import ast

def analyze_code(code):
    try:
        ast.parse(code)
        exec(code, {})
        return {
            "status": "success",
            "error": None,
            "type": None
        }

    except SyntaxError as e:
        return {
            "status": "error",
            "type": "SyntaxError",
            "message": str(e)
        }

    except Exception as e:
        return {
            "status": "error",
            "type": type(e).__name__,
            "message": str(e)
        }