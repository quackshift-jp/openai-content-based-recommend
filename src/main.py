import streamlit as st
from PIL import Image

from pages.main_page import main_page


def main():
    user_info_dict = main_page()


if __name__ == "__main__":
    main()
