import streamlit as st

st.set_page_config(page_title="Parkinson's Spiral Screening", page_icon="🧠", layout="centered")

# ---------- look (dark purple) ----------
st.markdown(
    """
<style>
#MainMenu, footer, [data-testid="stToolbar"] {display:none !important;}
.stApp {background: radial-gradient(900px 500px at 85% -10%, rgba(124,58,237,.30), transparent 60%), #0a0714;}
html, body, [class*="css"] {color:#e8eefc;}
.badge {display:inline-block; font-size:.78rem; color:#c4b5fd; border:1px solid rgba(167,139,250,.4);
        background:rgba(124,58,237,.12); padding:5px 14px; border-radius:99px;}
.title {font-size:2.3rem; font-weight:700; line-height:1.15; margin:14px 0 10px 0;}
.grad {background:linear-gradient(90deg,#67e8f9,#a78bfa 55%,#c084fc); -webkit-background-clip:text;
       background-clip:text; color:transparent;}
.lead {color:#8b9ab8; margin-bottom:1.5rem;}
.notice {border-radius:14px; padding:16px 20px; margin:14px 0; border:1px solid rgba(167,139,250,.45);
          background:rgba(124,58,237,.10); color:#c4b5fd;}
.notice small {text-transform:uppercase; letter-spacing:.1em; font-size:.72rem; opacity:.85;}
.notice .label {font-size:1.4rem; font-weight:700; color:#e8eefc;}
.hdr {display:flex; align-items:center; gap:24px; flex-wrap:wrap; margin-bottom:1.2rem;}
.hdr .txt {flex:1 1 300px; min-width:0;}
.hdr .vid {flex:0 0 190px; width:190px; height:190px; border-radius:18px; overflow:hidden;
           border:1.5px solid rgba(167,139,250,.55); background:#0a0714;
           box-shadow:0 0 22px rgba(124,58,237,.45), inset 0 0 12px rgba(124,58,237,.25);}
.hdr .vid video {width:100%; height:100%; object-fit:cover; display:block; pointer-events:none;}
@media (max-width:640px){.hdr .vid{margin:0 auto;}}
.disc {margin-top:2rem; padding:12px 16px; border-radius:12px; font-size:.82rem; color:#d9c48a;
       background:rgba(251,191,36,.06); border:1px solid rgba(251,191,36,.25);}
</style>
""",
    unsafe_allow_html=True,
)


# ---------- header (text on the left, looping video on the right) ----------
st.markdown(
    '<div class="hdr"><div class="txt">'
    '<span class="badge">● Deep-learning powered</span>'
    '<div class="title">AI-Based Parkinson’s Disease Screening Using '
    '<span class="grad">Spiral Drawing Images</span></div>'
    '<div class="lead">Upload a hand-drawn spiral and the model will analyse it '
    "for tremor and smoothness patterns.</div></div>"
    '<div class="vid"><video autoplay loop muted playsinline disablepictureinpicture '
    'controlslist="nodownload nofullscreen noremoteplayback" '
    'src="app/static/brain.mp4"></video></div></div>',
    unsafe_allow_html=True,
)

# ---------- input ----------
uploaded = st.file_uploader("Upload a spiral image from your computer", type=["png", "jpg", "jpeg"])
if uploaded:
    st.image(uploaded, caption="Uploaded spiral", width=320)

# ---------- result ----------
if st.button("Analyze drawing", type="primary", disabled=uploaded is None):
    st.markdown(
        '<div class="notice"><small>Result</small>'
        '<div class="label">Model not trained yet</div>'
        "<div>No prediction can be given because the model has not been trained yet.</div></div>",
        unsafe_allow_html=True,
    )

st.markdown(
    '<div class="disc">⚠️ <b>Medical disclaimer:</b> educational research prototype, not a medical device. '
    "It cannot diagnose Parkinson’s disease.</div>",
    unsafe_allow_html=True,
)
