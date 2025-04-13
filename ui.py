import streamlit as st

def display_ui():
    # Centered Title and Subheader
    st.markdown("<h1 style='text-align: center; color:#4B8BBE;'>🎓 University Students and Courses</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center; color:#6C63FF;'>💬 Ask a question about students or courses</h3>", unsafe_allow_html=True)

    # Initialize session state for user input
    if 'user_prompt' not in st.session_state:
        st.session_state.user_prompt = ""  # Initialize if not present

    # Centered input box with a subtle layout
    st.markdown("<div style='display: flex; justify-content: center; padding: 10px;'>", unsafe_allow_html=True)
    user_prompt = st.text_input("📝 Type your question here:", value=st.session_state.user_prompt, label_visibility="collapsed")
    st.markdown("</div>", unsafe_allow_html=True)

    # Example question buttons with better alignment and spacing
    st.markdown("<br><h4 style='text-align: center; color:#FF6F61;'>✨ Try one of these examples:</h4>", unsafe_allow_html=True)

    example_questions = {
        "📚 Show All Courses": "List the distinct courses available.",
        "🧑‍💻 Students in Data Science": "Who is enrolled in the Data Science course?",
        "🔢 Total Number of Students": "How many students are there in total?",
    }

    # Evenly spaced buttons
    cols = st.columns(len(example_questions), gap="medium")
    for col, (label, example) in zip(cols, example_questions.items()):
        with col:
            if st.button(label):
                st.session_state.user_prompt = example
                st.rerun()

    return st.session_state.user_prompt
