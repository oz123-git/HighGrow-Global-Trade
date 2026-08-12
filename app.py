import base64
from pathlib import Path

import streamlit as st

st.set_page_config(
    page_title="HighGrow Global Trade",
    page_icon="🌿",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ---------- Assets ----------
def load_b64_image(path: str):
    p = Path(path)
    if not p.exists():
        return None
    try:
        return base64.b64decode(p.read_text(encoding="utf-8").strip())
    except Exception:
        return None

hero_image = load_b64_image("assets/hero_agri.b64")

# ---------- Styling ----------
st.markdown(
    """
    <style>
    :root { --navy:#071726; --navy2:#0a2435; --green:#43d89b; --green-dark:#18a36b; --muted:#b9c8d2; }
    .stApp { background:#fff; color:#152331; }
    [data-testid="stHeader"] { background:transparent; }
    .block-container { max-width:1400px; padding:1.2rem 1.4rem 3rem; }
    .brand { display:flex; align-items:center; gap:14px; margin:0 0 10px 4px; }
    .brand-logo { width:52px; height:52px; border-radius:9px; background:linear-gradient(145deg,#55dda2,#1aa56d); display:grid; place-items:center; color:white; font-size:30px; box-shadow:0 5px 16px rgba(24,163,107,.18); }
    .brand-name { font-size:29px; line-height:1.03; font-weight:800; color:#0d1d2c; letter-spacing:-.7px; }
    .brand-name span { display:block; }
    .navbtn button { background:#0c1320 !important; color:white !important; border:1px solid #253142 !important; border-radius:9px !important; font-weight:650 !important; height:46px !important; }
    .hero-wrap { background:linear-gradient(120deg,#061421 0%,#092333 55%,#071923 100%); border:1px solid #19384b; border-radius:28px; padding:70px 5.2%; overflow:hidden; box-shadow:0 14px 45px rgba(5,20,35,.12); }
    .eyebrow { display:inline-block; border:1px solid #347c68; color:#69e4ae; background:rgba(31,135,97,.12); border-radius:30px; padding:9px 16px; font-size:13px; font-weight:800; letter-spacing:.5px; }
    .hero-title { font-size:clamp(42px,5vw,70px); line-height:1.04; letter-spacing:-2.5px; font-weight:850; color:#fff; margin:42px 0 18px; }
    .hero-title .green { color:#4bdc9e; }
    .hero-copy { color:#d1dce3; font-size:18px; line-height:1.65; max-width:650px; }
    .hero-line { width:65px; height:2px; background:#22b77c; margin:26px 0; }
    .feature { display:flex; gap:10px; align-items:center; color:#fff; margin-top:24px; }
    .feature-icon { width:40px; height:40px; border-radius:50%; background:rgba(24,163,107,.18); border:1px solid rgba(69,218,157,.25); display:grid; place-items:center; color:#5ce2a9; }
    .feature strong { display:block; font-size:14px; }
    .feature small { color:#aebdc7; font-size:12px; }
    .hero-image { width:100%; max-height:560px; object-fit:contain; display:block; }
    .cta-row { margin-top:34px; }
    .section-kicker { color:#18a36b; font-size:13px; font-weight:850; text-transform:uppercase; letter-spacing:1.4px; margin-top:58px; }
    .section-title { color:#071a2b; font-size:38px; line-height:1.15; font-weight:800; margin:7px 0 12px; letter-spacing:-1px; }
    .muted { color:#667583; line-height:1.65; }
    .card { background:#fff; border:1px solid #e3eaee; border-radius:17px; padding:24px; min-height:190px; box-shadow:0 8px 26px rgba(10,35,55,.055); }
    .card h3 { color:#0a2032; margin:10px 0 8px; }
    .card p { color:#667583; font-size:14px; line-height:1.6; }
    .icon { width:52px; height:52px; border-radius:13px; background:#eaf8f2; display:grid; place-items:center; font-size:25px; }
    .dark-panel { background:linear-gradient(145deg,#071a2b,#0d2d45); padding:32px; border-radius:18px; color:#fff; }
    .dark-panel h3 { color:#fff; font-size:24px; }
    .dark-panel p { color:#d2dfe7; }
    .market-box { background:linear-gradient(135deg,#f7faf9,#eef6f3); padding:30px; border-radius:18px; }
    .market-pill { background:#fff; padding:14px 16px; border-radius:9px; border:1px solid #e0eae6; font-weight:750; color:#0a2032; margin-top:12px; }
    .footer { margin-top:58px; padding:26px 0 8px; border-top:1px solid #e4eaee; color:#667583; font-size:13px; }
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------- Header ----------
head = st.columns([3.0, 1, 1, 1, 1, 1, 1])
with head[0]:
    st.markdown('<div class="brand"><div class="brand-logo">🌿</div><div class="brand-name">HighGrow Global<span>Trade</span></div></div>', unsafe_allow_html=True)
for i, (label, icon) in enumerate([
    ("Home", "⌂"), ("About", "👥"), ("Products", "◈"),
    ("Services", "⚙"), ("Markets", "◎"), ("Contact", "✉")
], start=1):
    with head[i]:
        st.markdown('<div class="navbtn">', unsafe_allow_html=True)
        st.button(f"{icon}  {label}", key=f"nav_{label}", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

# ---------- Hero ----------
st.markdown('<div class="hero-wrap">', unsafe_allow_html=True)
hero_left, hero_right = st.columns([1.04, .96], gap="large")
with hero_left:
    st.markdown('<div class="eyebrow">INDIA • GLOBAL TRADE • TRUSTED SOURCING</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-title">India\'s Finest<br><span class="green">Agricultural Products,</span><br>Delivered Worldwide.</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-line"></div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-copy">HighGrow Global Trade connects the richness of Indian farms with the needs of the world. We supply quality agricultural products with trust, transparency and timely delivery.</div>', unsafe_allow_html=True)
    f1, f2, f3, f4 = st.columns(4)
    features = [("♧", "Quality", "Carefully sourced"), ("◉", "Trusted", "Reliable partner"), ("◎", "Global Reach", "Serving worldwide"), ("▣", "Delivery", "On-time support")]
    for c, (ico, title, sub) in zip([f1,f2,f3,f4], features):
        with c:
            st.markdown(f'<div class="feature"><div class="feature-icon">{ico}</div></div><div style="margin-left:2px"><strong style="color:white;font-size:13px">{title}</strong><br><small style="color:#aebdc7">{sub}</small></div>', unsafe_allow_html=True)
    st.markdown('<div class="cta-row"></div>', unsafe_allow_html=True)
    b1, b2 = st.columns(2)
    with b1:
        if st.button("➜  Explore Products", key="hero_products", use_container_width=True):
            st.session_state["selected_product"] = "Kolam Rice"
    with b2:
        if st.button("☎  Start an Inquiry", key="hero_inquiry", use_container_width=True):
            st.session_state["inquiry_open"] = True
with hero_right:
    if hero_image:
        st.image(hero_image, width="stretch")
    else:
        st.markdown('<div style="height:500px;display:grid;place-items:center;color:#8fa4b1">Hero image asset not found.</div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# ---------- About ----------
st.markdown('<div class="section-kicker">About HighGrow</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Trade that grows with trust.</div>', unsafe_allow_html=True)
a, b = st.columns([1.15,.85])
with a:
    st.markdown('<p class="muted">HighGrow Global Trade is an India-based import-export and sourcing business focused on connecting Indian agricultural products with international buyers.</p><p class="muted">We aim to build long-term trade relationships through clear communication, dependable sourcing and professional coordination.</p>', unsafe_allow_html=True)
with b:
    st.markdown('<div class="dark-panel"><h3>Founded by</h3><p><strong>Sumedh Thombare</strong><br><strong>Omkar Zinjurde</strong></p><p>Ahilyanagar, Maharashtra, India</p></div>', unsafe_allow_html=True)

# ---------- Products ----------
st.markdown('<div class="section-kicker">Our Products</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Indian agricultural products for global markets.</div>', unsafe_allow_html=True)
st.markdown('<p class="muted">Wholesale and export enquiries are welcome. Final specifications, packaging, quantity and availability are confirmed with the buyer.</p>', unsafe_allow_html=True)
products = [
    ("🍚", "Kolam Rice", "Indian Kolam Rice for wholesale and export enquiries."),
    ("🌾", "Wheat", "Indian wheat for bulk trade and export enquiries."),
    ("🌾", "Bajra", "Indian pearl millet (Bajra) for wholesale and export enquiries."),
    ("🌍", "Custom Sourcing", "Additional products sourced according to quantity, specification and destination."),
]
cols = st.columns(4)
for c, (ico, name, desc) in zip(cols, products):
    with c:
        st.markdown(f'<div class="card"><div class="icon">{ico}</div><h3>{name}</h3><p>{desc}</p></div>', unsafe_allow_html=True)
        if st.button(f"Request {name} Quote", key=f"quote_{name}", use_container_width=True):
            st.session_state["selected_product"] = name
            st.session_state["inquiry_open"] = True

# ---------- Services ----------
st.markdown('<div class="section-kicker">Our Services</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">From sourcing to shipment.</div>', unsafe_allow_html=True)
services = [
    ("Global Sourcing", "Identify suitable suppliers and products according to buyer requirements."),
    ("Import & Export", "Coordinate international trade transactions and export processes."),
    ("Documentation", "Support for commercial and shipping documentation required for trade."),
    ("Logistics Coordination", "Coordinate with logistics and freight partners for movement of goods."),
    ("Buyer Support", "Clear communication, quotation support and order coordination."),
    ("Supplier Network", "Build dependable sourcing relationships for consistent business."),
]
for r in range(2):
    row = st.columns(3)
    for c, (title, desc) in zip(row, services[r*3:(r+1)*3]):
        with c:
            st.markdown(f'<div class="card"><h3>{title}</h3><p>{desc}</p></div>', unsafe_allow_html=True)

# ---------- Process ----------
st.markdown('<div class="section-kicker">Our Process</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Simple. Clear. Reliable.</div>', unsafe_allow_html=True)
steps = [("1","Inquiry","Share your requirement."),("2","Quotation","Receive product & price details."),("3","Confirmation","Finalize quantity and terms."),("4","Shipment","Documentation & logistics."),("5","Delivery","Goods reach destination.")]
row = st.columns(5)
for c,(num,title,desc) in zip(row,steps):
    with c:
        st.markdown(f'<div class="card" style="text-align:center;min-height:155px"><div style="width:44px;height:44px;border-radius:50%;background:#18a36b;color:white;display:grid;place-items:center;margin:auto;font-weight:800">{num}</div><h3>{title}</h3><p>{desc}</p></div>',unsafe_allow_html=True)

# ---------- Markets ----------
st.markdown('<div class="market-box"><div class="section-kicker" style="margin-top:0">Global Reach</div><div class="section-title">Building connections beyond borders.</div><p class="muted">Our target markets include Africa, the Middle East, Asia and other international destinations.</p></div>', unsafe_allow_html=True)
markets = st.columns(4)
for c,text in zip(markets,["🌍 Africa","🕌 Middle East","🌏 Asia","🚢 Global Markets"]):
    with c: st.markdown(f'<div class="market-pill">{text}</div>',unsafe_allow_html=True)

# ---------- Contact ----------
st.markdown('<div class="section-kicker">Contact Us</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Let\'s talk global trade.</div>', unsafe_allow_html=True)
left,right = st.columns([.8,1.2])
with left:
    st.markdown('<div class="card"><h3>HighGrow Global Trade</h3><p><strong>Founders:</strong><br>Sumedh Thombare<br>Omkar Zinjurde</p><p><strong>Email:</strong><br><a href="mailto:highgrowglobaltrade@gmail.com">highgrowglobaltrade@gmail.com</a></p><p><strong>Address:</strong><br>Ahilyanagar, Maharashtra, India</p></div>',unsafe_allow_html=True)
with right:
    selected = st.session_state.get("selected_product", "Kolam Rice")
    choices = ["Kolam Rice","Wheat","Bajra","Custom Sourcing"]
    with st.form("inquiry_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Email Address")
        company = st.text_input("Company Name")
        product = st.selectbox("Product / Requirement", choices, index=choices.index(selected) if selected in choices else 0)
        quantity = st.text_input("Quantity (e.g. 20 MT)")
        destination = st.text_input("Destination Country / Port")
        message = st.text_area("Requirements / Message")
        submitted = st.form_submit_button("Send Inquiry", use_container_width=True)
    if submitted:
        if not name or not email or not message:
            st.error("Please provide your name, email and message.")
        else:
            st.success("Inquiry details captured. Please send the details to highgrowglobaltrade@gmail.com to complete the enquiry.")
            st.code(f"Name: {name}\nEmail: {email}\nCompany: {company}\nProduct: {product}\nQuantity: {quantity}\nDestination: {destination}\nMessage: {message}")

st.markdown('<div class="footer"><strong>HighGrow Global Trade</strong> — Connecting quality Indian agricultural products to global markets.<br>Founded by Sumedh Thombare & Omkar Zinjurde • Ahilyanagar, Maharashtra, India • highgrowglobaltrade@gmail.com<br>© 2026 HighGrow Global Trade. All rights reserved.</div>',unsafe_allow_html=True)
