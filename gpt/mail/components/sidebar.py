import streamlit as st

# import faq


def sidebar():
    with st.sidebar:
        st.markdown(
            "# 欢迎来到🤖AI妙妙屋🏠"
        )
        st.markdown("---")

        st.markdown(
            "## How to use\n"
            "Just enter the email you want to send\n"
        )

        st.markdown("---")
        st.markdown("# About")
        st.markdown(
            "为你生成正式的邮件内容"
        )

        st.markdown("---")
        st.markdown("Made by [Kami_Lin]")
        st.markdown("Powered by gpt-3.5")
        st.markdown("---")

        # faq()
