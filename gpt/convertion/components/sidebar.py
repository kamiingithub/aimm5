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
            "1. choose one type what you want to convert to\n"
            "2. enter your data\n"
        )

        st.markdown("---")
        st.markdown("# About")
        st.markdown(
            "转换成你想要的数据结构"
        )

        st.markdown("---")
        st.markdown("Made by [Kami_Lin]")
        st.markdown("Powered by gpt-3.5")
        st.markdown("---")

        # faq()
