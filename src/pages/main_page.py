import streamlit as st

SEASON = ["春", "夏", "秋", "冬"]
COLOR = ["ダークレッド", "緑系", "ブルー系", "ブラック", "白", "グレー"]
GENRE = ["シティ系", "ストリート", "アメカジ", "カジュアル", "きれいめ"]
SCENE = ["仕事", "デート", "ディナー", "ランチ", "古着巡り"]
HEIGHT = ["低身長(160cm以下)", "全ての身長"]
HAIR_COLOR = ["黒髪", "金髪", "茶髪"]
HAIR_STYLE = ["ショート", "ウルフカット", "マッシュ", "センターパート"]


def main_page() -> dict[str:str]:
    st.title("👚ファッション提案アプリデモ👕")
    st.write("探したいファッション情報を入力してください！")
    season = st.selectbox(label="季節（シーズン）を教えてください。", options=(SEASON))

    color = st.selectbox(label="色の系統を教えてください", options=(COLOR))

    genre = st.selectbox(label="服装のジャンルを教えてください", options=(GENRE))

    scene = st.selectbox(label="着用シーンを教えてください", options=(SCENE))

    height = st.selectbox(label="身長の特徴を教えてください", options=(HEIGHT))

    hair_color = st.selectbox(label="あなたの髪色を教えてください", options=(HAIR_COLOR))

    hair_style = st.selectbox(label="あなたの髪型を教えてください", options=(HAIR_STYLE))

    other_request = st.text_input(label="他にご要望があれば記述ください", value="")

    if st.button("おすすめを表示"):
        return {
            "season": season,
            "color": color,
            "genre": genre,
            "scene": scene,
            "height": height,
            "hair_color": hair_color,
            "hair_style": hair_style,
            "other_request": other_request,
        }
    else:
        return None


if __name__ == "__main__":
    main_page()
