import streamlit as st

# from faq import faq

def set_openai_api_key(api_key: str):
    st.session_state["OPENAI_API_KEY"] = api_key

def sidebar():
    with st.sidebar:
        st.markdown(
            "# 欢迎来到🤖AI妙妙屋🏠"
        )
        st.markdown("---")

        st.markdown(
            "## How to use\n"
            "1. Upload a pdf, docx, or txt file📄\n"
            "2. Ask a question about the document💬\n"
        )

        st.markdown("---")
        st.markdown("# About")
        st.markdown(
            "📖 allows you to ask questions about your "
            "documents and get accurate answers with instant citations. "
        )
        st.markdown(
            "This tool is a work in progress. "
        )
        st.markdown("---")

        st.markdown("Made by [Kami_Lin]")
        st.markdown("Powered by gpt-3.5")
        st.markdown("---")
        # faq()
