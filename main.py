import streamlit as st
from analyzer import analyze_code
from explainer import (
    explain_error,
    explain_why,
    suggest_fix,
    step_by_step_explanation,
    auto_fix_code
)
from quality_analyzer import analyze_quality, code_insights

# Page settings
st.set_page_config(
    page_title="AI Code Debugger",
    page_icon="🧠",
    layout="wide"
)

# Title
st.title("🧠 AI Code Debugger")
st.markdown("### Debug your code like a pro 🚀")

# Layout
col1, col2 = st.columns(2)

# LEFT SIDE
with col1:
    language = st.selectbox(
        "Select Language",
        ["Python", "C++", "Java"]
    )

    mode = st.selectbox("Choose Mode", ["beginner", "pro"])
    code = st.text_area("Paste your code here:", height=300)
    run = st.button("🚀 Analyze Code")

# RIGHT SIDE
with col2:
    if run:

        st.divider()

        # 🔥 MULTI-LANGUAGE HANDLING
        if language == "Python":
            result = analyze_code(code)

            st.subheader("🚨 Error Analysis")

            if result["status"] == "success":
                st.success("✅ No errors found!")
            else:
                st.error(f"❌ {result['type']} detected!")

                explanation = explain_error(
                    result["message"],
                    result["type"],
                    mode
                )

                st.info(explanation)

                st.write("### ❓ Why this happened")
                st.write(explain_why(result["type"]))

                st.write("### 🛠 Fix Suggestions")
                fixes = suggest_fix(result["type"], code)
                for fix in fixes:
                    st.write("- " + fix)

                st.write("### 📚 Step-by-Step Explanation")
                steps = step_by_step_explanation(result["type"])
                for step in steps:
                    st.write("- " + step)

                if mode == "pro":
                    st.code(result["message"])

        else:
            # 🔥 BASIC SUPPORT FOR C++ / JAVA
            st.subheader("⚠️ Limited Language Support")

            st.info("Basic analysis for non-Python languages")

            st.write("### 💡 Suggestions")

            if "cout" in code or "printf" in code:
                st.write("- Output statement detected")

            if ";" not in code:
                st.write("- Missing semicolon (C++/Java)")

            if "main" not in code:
                st.write("- Missing main function")

        # 📊 Code Quality
        st.divider()
        st.subheader("📊 Code Quality")

        score, issues = analyze_quality(code)
        st.metric("Score", f"{score}/100")

        if issues:
            for issue in issues:
                st.warning(issue)
        else:
            st.success("✅ Clean code!")

        # 💡 Insights
        st.divider()
        st.subheader("💡 Insights")

        insights = code_insights(code)
        if insights:
            for insight in insights:
                st.info(insight)

        # 🛠 Auto Fix
        st.divider()
        st.subheader("🛠 Auto Fixed Code")

        fixed_code = auto_fix_code(code, language)
        st.code(fixed_code, language="python")