import streamlit as st

st.set_page_config(
    page_title="HighGrow Global Trade | Connecting Markets Worldwide",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="collapsed",
)

st.markdown(
    """
    <style>
    :root {
        --navy: #071a2b;
        --navy2: #0d2b43;
        --green: #18a36b;
        --green2: #0d6d4b;
        --light: #f5f8fa;
        --text: #182532;
        --muted: #617080;
        --white: #ffffff;
        --border: #e4eaee;
    }
    .stApp { background: #ffffff; color: var(--text); }
    [data-testid="stHeader"] { background: rgba(255,255,255,0); }
    .block-container { padding-top: 1.5rem; max-width: 1180px; }
    .hero {
        min-height: 560px;
        padding: 80px 7%;
        border-radius: 24px;
        display: flex;
        align-items: center;
        background: linear-gradient(110deg, rgba(5,20,34,.97), rgba(8,43,64,.88)),
                    radial-gradient(circle at 80% 30%, rgba(24,163,107,.28), transparent 30%);
        color: white;
        margin-bottom: 55px;
    }
    .badge {
        display: inline-block;
        color: #bff0d9;
        border: 1px solid rgba(191,240,217,.35);
        background: rgba(24,163,107,.12);
        padding: 7px 13px;
        border-radius: 30px;
        font-size: 13px;
        font-weight: 700;
        letter-spacing: .4px;
        margin-bottom: 18px;
    }
    .hero h1 {
        font-size: clamp(42px, 6vw, 72px);
        line-height: 1.03;
        letter-spacing: -2px;
        margin: 0 0 20px 0;
    }
    .hero h1 span { color: #54d99e; }
    .hero p { font-size: 19px; color: #d7e2e9; max-width: 760px; line-height: 1.6; }
    .section-kicker { color: var(--green); font-weight: 800; font-size: 13px; text-transform: uppercase; letter-spacing: 1.4px; }
    .section-title { font-size: 38px; line-height: 1.15; color: var(--navy); margin: 8px 0 12px; }
    .muted { color: var(--muted); }
    .card {
        background: white;
        border: 1px solid var(--border);
        border-radius: 16px;
        padding: 24px;
        height: 100%;
        box-shadow: 0 8px 24px rgba(10,35,55,.05);
    }
    .card h3 { color: var(--navy); margin: 8px 0; }
    .card p { color: var(--muted); font-size: 14px; }
    .icon {
        width: 52px; height: 52px; border-radius: 12px;
        background: #eaf8f2; display: grid; place-items: center;
        font-size: 25px;
    }
    .dark-panel {
        background: linear-gradient(145deg, var(--navy), var(--navy2));
        padding: 34px; border-radius: 18px; color: white;
    }
    .dark-panel h3 { color: white; font-size: 24px; }
    .dark-panel p { color: #d5e0e7; }
    .stat { background: rgba(255,255,255,.07); padding: 16px; border-radius: 10px; }
    .stat strong { display: block; font-size: 24px; color: #5fe0a8; }
    .stat small { color: #c7d4dd; }
    .market-box {
        background: linear-gradient(135deg, #f7faf9, #eef6f3);
        padding: 30px;
        border-radius: 18px;
    }
    .market-pill {
        background: white;
        padding: 13px 16px;
        border-radius: 8px;
        border: 1px solid #e1ebe7;
        font-weight: 700;
        color: var(--navy);
        margin-bottom: 10px;
    }
    .footer {
        margin-top: 50px;
        padding: 24px 0 10px;
        border-top: 1px solid var(--border);
        color: var(--muted);
        font-size: 13px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Navigation
nav_cols = st.columns([3, 1, 1, 1, 1, 1, 1])
with nav_cols[0]:
    st.markdown("### 🟩 HighGrow Global Trade")
for i, label in enumerate(["Home", "About", "Products", "Services", "Markets", "Contact"], start=1):
    with nav_cols[i]:
        if st.button(label, key=f"nav_{label}", use_container_width=True):
            st.session_state["section"] = label.lower()

st.markdown(
    """
    <div class="hero">
      <div>
        <div class="badge">INDIA • GLOBAL TRADE • TRUSTED SOURCING</div>
        <div class="hero h1"><h1>Connecting <span>Quality</span><br>Products to Global Markets.</h1></div>
        <p>HighGrow Global Trade is an India-based import-export and global sourcing business connecting Indian agricultural products with international buyers.</p>
      </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# About
st.markdown('<div class="section-kicker">About HighGrow</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Trade that grows with trust.</div>', unsafe_allow_html=True)
about_cols = st.columns([1.15, 0.85])
with about_cols[0]:
    st.markdown(
        """
        <p class="muted">HighGrow Global Trade works to make international trade simpler, reliable and transparent. We focus on sourcing Indian products, coordinating export processes and building long-term relationships with buyers and suppliers.</p>
        <p class="muted">Our focus begins with agricultural products and can expand according to buyer requirements, quantity, destination and sourcing capability.</p>
        """,
        unsafe_allow_html=True,
    )
with about_cols[1]:
    st.markdown(
        """
        <div class="dark-panel">
          <h3>Founded by</h3>
          <p><strong>Sumedh Thombare</strong><br><strong>Omkar Zinjurde</strong></p>
          <p>Ahilyanagar, Maharashtra, India</p>
          <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin-top:18px">
            <div class="stat"><strong>01</strong><small>Core mission</small></div>
            <div class="stat"><strong>24/7</strong><small>Communication</small></div>
            <div class="stat"><strong>∞</strong><small>Global potential</small></div>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown("<br>", unsafe_allow_html=True)

# Products
st.markdown('<div class="section-kicker">Our Products</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Indian agricultural products for global markets.</div>', unsafe_allow_html=True)
st.markdown('<p class="muted">Wholesale and export enquiries are welcome. Final specifications, packaging, quantity and availability are confirmed with the buyer.</p>', unsafe_allow_html=True)

products = [
    ("🍚", "Kolam Rice", "Indian Kolam Rice for wholesale and export enquiries."),
    ("🌾", "Wheat", "Indian wheat for bulk trade and export enquiries."),
    ("🌾", "Bajra", "Indian pearl millet (Bajra) for wholesale and export enquiries."),
    ("🌍", "Custom Sourcing", "Additional products sourced according to quantity, specification and destination."),
]
product_cols = st.columns(4)
for col, (icon, name, desc) in zip(product_cols, products):
    with col:
        st.markdown(f'<div class="card"><div class="icon">{icon}</div><h3>{name}</h3><p>{desc}</p></div>', unsafe_allow_html=True)
        if st.button(f"Request {name} Quote", key=f"quote_{name}", use_container_width=True):
            st.session_state["selected_product"] = name
            st.session_state["section"] = "contact"

st.markdown("<br>", unsafe_allow_html=True)

# Services
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
for row in range(2):
    cols = st.columns(3)
    for j in range(3):
        title, desc = services[row * 3 + j]
        with cols[j]:
            st.markdown(f'<div class="card"><h3>{title}</h3><p>{desc}</p></div>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

# Process
st.markdown('<div class="section-kicker">Our Process</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Simple. Clear. Reliable.</div>', unsafe_allow_html=True)
steps = [
    ("1", "Inquiry", "Share your requirement."),
    ("2", "Quotation", "Receive product & price details."),
    ("3", "Confirmation", "Finalize quantity and terms."),
    ("4", "Shipment", "Documentation & logistics."),
    ("5", "Delivery", "Goods reach destination."),
]
step_cols = st.columns(5)
for col, (num, title, desc) in zip(step_cols, steps):
    with col:
        st.markdown(f'<div class="card" style="text-align:center"><div style="width:45px;height:45px;border-radius:50%;background:#18a36b;color:white;display:grid;place-items:center;margin:0 auto 12px;font-weight:800">{num}</div><h3>{title}</h3><p>{desc}</p></div>', unsafe_allow_html=True)

# Markets
st.markdown("<br>", unsafe_allow_html=True)
st.markdown('<div class="market-box"><div class="section-kicker">Global Reach</div><div class="section-title">Building connections beyond borders.</div><p class="muted">Our target markets include Africa, the Middle East, Asia and other international destinations.</p></div>', unsafe_allow_html=True)
market_cols = st.columns(4)
for col, text in zip(market_cols, ["🌍 Africa", "🕌 Middle East", "🌏 Asia", "🚢 Global Markets"]):
    with col:
        st.markdown(f'<div class="market-pill">{text}</div>', unsafe_allow_html=True)

# Contact
st.markdown("<br>", unsafe_allow_html=True)
st.markdown('<div class="section-kicker">Contact Us</div>', unsafe_allow_html=True)
st.markdown('<div class="section-title">Let\'s talk global trade.</div>', unsafe_allow_html=True)
contact_left, contact_right = st.columns([0.85, 1.15])
with contact_left:
    st.markdown(
        """
        <div class="card">
          <h3>HighGrow Global Trade</h3>
          <p><strong>Founders:</strong><br>Sumedh Thombare<br>Omkar Zinjurde</p>
          <p><strong>Email:</strong><br><a href="mailto:highgrowglobaltrade@gmail.com">highgrowglobaltrade@gmail.com</a></p>
          <p><strong>Address:</strong><br>Ahilyanagar, Maharashtra, India</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
with contact_right:
    selected = st.session_state.get("selected_product", "")
    with st.form("inquiry_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Email Address")
        company = st.text_input("Company Name")
        product = st.selectbox("Product / Requirement", ["Kolam Rice", "Wheat", "Bajra", "Custom Sourcing"], index=["Kolam Rice", "Wheat", "Bajra", "Custom Sourcing"].index(selected) if selected in ["Kolam Rice", "Wheat", "Bajra", "Custom Sourcing"] else 0)
        quantity = st.text_input("Quantity (e.g. 20 MT)")
        destination = st.text_input("Destination Country / Port")
        message = st.text_area("Requirements / Message")
        submitted = st.form_submit_button("Send Inquiry", use_container_width=True)
    if submitted:
        if not name or not email or not message:
            st.error("Please provide your name, email and message.")
        else:
            st.success("Your enquiry has been prepared. Please email highgrowglobaltrade@gmail.com with these details.")
            st.info(f"Product: {product} | Quantity: {quantity or 'Not specified'} | Destination: {destination or 'Not specified'}")
            st.code(f"Name: {name}\nEmail: {email}\nCompany: {company}\nProduct: {product}\nQuantity: {quantity}\nDestination: {destination}\nMessage: {message}")

st.markdown(
    """
    <div class="footer">
      <strong style="color:#182532">HighGrow Global Trade</strong> — Connecting quality products to global markets.<br>
      Founded by Sumedh Thombare & Omkar Zinjurde • Ahilyanagar, Maharashtra, India • highgrowglobaltrade@gmail.com<br>
      © 2026 HighGrow Global Trade. All rights reserved.
    </div>
    """,
    unsafe_allow_html=True,
)
