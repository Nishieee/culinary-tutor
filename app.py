import streamlit as st
from chef import ask_chef  # Import the chatbot function

def main():
    # Streamlit UI setup
    st.set_page_config(page_title="Chef Maestro", page_icon="🍳", layout="wide")
    st.title("👨‍🍳 Chef Maestro: Your Culinary Tutor")

    # Sidebar
    with st.sidebar:
        st.header("About Chef Maestro")
        st.write("""
        Chef Maestro is your personal culinary tutor! 
        Ask questions about cooking techniques, recipes, ingredient substitutions, 
        or food science, and get detailed, step-by-step answers.
        """)
        st.write("Type your question in the box below and let Chef Maestro guide you!")
        st.markdown("**Examples of questions:**")
        st.write("- How do I make a perfect soufflé?")
        st.write("- What’s the science behind caramelization?")
        st.write("- How can I replace eggs in baking?")
    
    # Initialize session state
    if "user_input" not in st.session_state:
        st.session_state.user_input = ""
    if "response" not in st.session_state:
        st.session_state.response = ""

    # Form for input and buttons
    with st.form(key="chef_form", clear_on_submit=False):
        # Input area for user questions
        user_input = st.text_input(
            "Ask Chef Maestro your culinary question:", 
            value=st.session_state.user_input, 
            key="user_input_box"
        )

        # Submit and Clear buttons in a row
        col1, col2 = st.columns([1, 1])  # Equal column widths
        with col1:
            submit = st.form_submit_button("Submit")
        with col2:
            clear = st.form_submit_button("Clear All")

    # Handle button clicks
    if submit:
        if user_input.strip() == "":
            st.warning("Please enter a question before submitting.")
        else:
            with st.spinner("Chef Maestro is cooking up an answer..."):
                st.session_state.response = ask_chef(user_input)
                st.session_state.user_input = user_input  # Store input in session state

    if clear:
        # Clear the session state variables directly
        st.session_state["user_input"] = ""
        st.session_state["response"] = ""

    # Display the response
    if st.session_state.response:
        st.success("Here’s your answer:")
        st.markdown(st.session_state.response)

    # Footer
    st.markdown("""
    ---
    Built with 💖 by Chef Maestro. 
    """)

if __name__ == "__main__":
    main()
