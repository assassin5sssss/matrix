from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components


APP_DIR = Path(__file__).resolve().parent
HTML_FILE = APP_DIR / "matrix_lab.html"

st.set_page_config(
    page_title="西电高代与矩阵实验室",
    page_icon="🧮",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# Make the embedded single-page application occupy the whole Streamlit canvas.
st.markdown(
    """
    <style>
      header[data-testid="stHeader"],
      div[data-testid="stToolbar"],
      footer {
        display: none !important;
      }
      .stApp,
      div[data-testid="stAppViewContainer"],
      div[data-testid="stMain"] {
        background: #f6f7fb;
      }
      div[data-testid="stMainBlockContainer"],
      .block-container {
        max-width: none !important;
        padding: 0 !important;
      }
      div[data-testid="stElementContainer"] {
        margin: 0 !important;
      }
      iframe[title="streamlit_components.v1.html"] {
        display: block;
        width: 100% !important;
        border: 0 !important;
      }
    </style>
    """,
    unsafe_allow_html=True,
)


@st.cache_data(show_spinner=False)
def load_embedded_app(path: str, modified_time: float) -> str:
    """Load the HTML and add a small bridge that resizes its Streamlit iframe."""
    del modified_time  # It is part of the cache key and invalidates on file updates.
    html = Path(path).read_text(encoding="utf-8")
    resize_bridge = r"""
    <script>
      (() => {
        const reportHeight = () => {
          const height = Math.max(
            document.documentElement?.scrollHeight || 0,
            document.body?.scrollHeight || 0,
            window.innerHeight || 0
          );
          window.parent.postMessage(
            {
              isStreamlitMessage: true,
              type: "streamlit:setFrameHeight",
              height: height
            },
            "*"
          );
        };

        window.addEventListener("load", () => {
          reportHeight();
          window.setTimeout(reportHeight, 150);
        });

        if (window.ResizeObserver) {
          new ResizeObserver(reportHeight).observe(document.documentElement);
        }

        window.setInterval(reportHeight, 1000);
      })();
    </script>
    """

    if "</body>" in html.lower():
        close_index = html.lower().rfind("</body>")
        return html[:close_index] + resize_bridge + html[close_index:]
    return html + resize_bridge


if not HTML_FILE.is_file():
    st.error("缺少 matrix_lab.html，无法启动矩阵实验室。")
    st.stop()

try:
    embedded_html = load_embedded_app(
        str(HTML_FILE),
        HTML_FILE.stat().st_mtime,
    )
except (OSError, UnicodeError) as exc:
    st.error(f"读取 matrix_lab.html 失败：{exc}")
    st.stop()

components.html(embedded_html, height=1000, scrolling=True)
