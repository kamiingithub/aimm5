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
            "1. Just enter your angry words\n"
            "2. Keep calm and friendly❤\n"
        )

        st.markdown("---")
        st.markdown("# About")
        st.markdown(
            "将气愤、责备😡的语言转换为平和友善的对话"
        )

        st.markdown("---")
        st.markdown("Made by [Kami_Lin]")
        st.markdown("Powered by gpt-3.5")
        st.markdown("---")

        # faq()
