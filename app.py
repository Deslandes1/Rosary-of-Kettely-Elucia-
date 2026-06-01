import streamlit as st
import time

# ================== Page Config ==================
st.set_page_config(
    page_title="Canonization Rosary Book – Elucia & Kettely",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ================== Styling (Esoteric, glowing, mystical) ==================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;600;900&display=swap');
    .stApp {
        background: radial-gradient(circle at center, #0a0f2a, #020617);
        color: #f5e6d3;
    }
    h1, h2, h3 {
        font-family: 'Cinzel', serif;
        color: #ffd966;
        text-shadow: 0 0 10px #ffaa44;
    }
    .prayer-card {
        background: rgba(0,0,0,0.65);
        backdrop-filter: blur(8px);
        border-radius: 30px;
        padding: 2rem;
        margin: 1.5rem 0;
        border: 1px solid rgba(255,215,0,0.4);
        box-shadow: 0 0 20px rgba(255,215,0,0.2);
    }
    .bead {
        width: 45px;
        height: 45px;
        border-radius: 50%;
        background: radial-gradient(circle at 30% 30%, #ffd700, #b8860b);
        display: inline-block;
        margin: 5px;
        cursor: pointer;
        transition: all 0.3s ease;
        box-shadow: 0 0 10px gold;
    }
    .bead-clicked {
        background: radial-gradient(circle at 30% 30%, #ffaa44, #ff6600);
        box-shadow: 0 0 20px #ffaa44;
        transform: scale(1.1);
    }
    .footer {
        text-align: center;
        margin-top: 3rem;
        padding: 1rem;
        font-size: 0.8rem;
        opacity: 0.7;
    }
    .button-pray {
        background: linear-gradient(90deg, #ffaa44, #ff6600);
        color: #1e1e2a;
        border: none;
        border-radius: 40px;
        padding: 0.6rem 1.5rem;
        font-weight: bold;
        font-size: 1.1rem;
        cursor: pointer;
        transition: 0.2s;
    }
    .button-pray:hover {
        transform: scale(1.02);
        box-shadow: 0 0 25px #ffaa44;
    }
    .saint-title {
        font-size: 2.5rem;
        text-align: center;
        margin-bottom: 0;
    }
    .energy-orb {
        width: 150px;
        height: 150px;
        background: radial-gradient(circle, rgba(255,215,0,0.3), transparent);
        border-radius: 50%;
        margin: 20px auto;
        animation: pulse 3s infinite;
    }
    @keyframes pulse {
        0% { transform: scale(1); opacity: 0.6; }
        50% { transform: scale(1.2); opacity: 1; }
        100% { transform: scale(1); opacity: 0.6; }
    }
    
    /* New Avatar Styling */
    .avatar-img {
        border-radius: 50%;
        width: 90px;
        height: 90px;
        object-fit: cover;
        border: 2px solid #ffaa44;
        box-shadow: 0 0 20px rgba(255,170,68,0.6);
    }
</style>
""", unsafe_allow_html=True)

# ================== Prayer Texts ==================
prayer_elucia = f"""
**Eternal Canonization Prayer for Elucia Antoine**  

Elucian Antoine,  
Thank you for raising Gesner Deslandes, Ti boul, your only grandson.  
Thank you for my first communion,  
Thank you for giving birth to Kettely Auguste and working at a factory to pay for my school.  
Thank you for feeding me, paying the rent, giving your grandson a home to be raised like a prince.  
Thank you for accompanying me to school when I was an innocent child,  
Thank you for protecting me day and night,  
Thank you for taking me to the doctor when I was sick,  
Thank you for defending me in altercations with other kids.  

I believe your soul is still alive somewhere in this Universe,  
And you still remember me, and I still remember you.  

Elucia Antoine, when Kettely Auguste traveled to the eternal orient,  
You and I stood alone in great harmony, no matter the circumstances.  
We struggled against all life adversities.  
When you traveled, leaving me behind, I accepted, but it hurt silently, burning inside me.  

Thus, in remembrance of your greatness,  
I say: may your eternal soul be with me in this life and forever,  
To destroy my present adversities, visible and invisible,  
In the name of the 1 – the Architect of this Universe.  

*Shi, shi, shi.*  
"""

prayer_kettely = f"""
**Eternal Canonization Prayer for Kettely Auguste**  

Kettely Auguste,  
Thank you for raising Gesner Deslandes, Ti boul, your only son.  
Thank you for my first communion,  
Thank you for working at a factory to pay for my school.  
Thank you for feeding me, paying the rent, giving your son a home to be raised like a prince.  
Thank you for accompanying me to school when I was an innocent child,  
Thank you for protecting me day and night,  
Thank you for taking me to the doctor when I was sick,  
Thank you for defending me in altercations with other kids.  

You always said two women were taking care of me, struggling to make my life a paradise.  

I believe your soul is still alive somewhere in this Universe,  
And you still remember me, and I still remember you.  

Thus, in remembrance of your greatness,  
I say: may your eternal soul be with me in this life and forever,  
To destroy my present adversities, visible and invisible,  
In the name of the 1 – the Architect of this Universe.  

*Shi, shi, shi.*  
"""

# ================== Sidebar Company Info ==================
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/circled.png", width=80)
    st.markdown("## GlobalInternet.py")
    st.markdown("**Gesner Deslandes**, Engineer-in-Chief")
    st.markdown("---")
    st.markdown("### 📞 Contact")
    st.markdown("📱 (509)-47385663")
    st.markdown("✉️ deslandes78@gmail.com")
    st.markdown("🌐 [GlobalInternet.py](https://globalinternetsitepy-abh7v6tnmskxxnuplrdcgk.streamlit.app/)")
    st.markdown("---")
    st.markdown("### 💰 Offer a Donation")
    st.markdown("Support this eternal work: **$9.99 USD** (one‑time)")
    st.markdown("*All proceeds keep the energy alive*")
    st.markdown("---")
    st.caption("© 2025 GlobalInternet.py")

# ================== Main Interface with Avatar and Credit ==================
st.markdown('<div class="energy-orb"></div>', unsafe_allow_html=True)

# Two columns: title on left, avatar on right
col1, col2 = st.columns([3, 1])
with col1:
    st.title("✨ The Canonization Rosary Book ✨")
    st.markdown("### *Elucia Antoine & Kettely Auguste*")
with col2:
    avatar_url = "https://raw.githubusercontent.com/Deslandes1/Rosary-of-Kettely-Elucia-/refs/heads/main/Gesner%20Deslandes.png"
    st.markdown(f'<img src="{avatar_url}" class="avatar-img" style="float:right;">', unsafe_allow_html=True)

st.markdown("#### *Canonized by Gesner Deslandes – Eternal Light of the Universe*")
st.caption("Built by Gesner Deslandes at GlobalInternet.py")

# Tabs for each saint
tab1, tab2 = st.tabs(["🌸 Elucia Antoine (Grandmother)", "🌺 Kettely Auguste (Mother)"])

# ================== ROSARY COUNTER FUNCTIONALITY ==================
def rosary_counter(person_name):
    st.markdown("---")
    st.subheader("📿 Interactive Rosary – Click each bead as you pray")
    # 5 decades + 1 crucifix bead? We'll use 10 beads + 1 large bead for simplicity.
    beads = 10
    if f"beads_{person_name}" not in st.session_state:
        st.session_state[f"beads_{person_name}"] = [False] * beads
    
    cols = st.columns(beads)
    for i, col in enumerate(cols):
        with col:
            if st.button("●", key=f"{person_name}_bead_{i}", use_container_width=True):
                st.session_state[f"beads_{person_name}"][i] = not st.session_state[f"beads_{person_name}"][i]
                st.rerun()
            # Visual feedback
            if st.session_state[f"beads_{person_name}"][i]:
                st.markdown('<div style="color:#ffaa44; text-align:center;">✨</div>', unsafe_allow_html=True)
            else:
                st.markdown('<div style="color:#666; text-align:center;">○</div>', unsafe_allow_html=True)
    
    if all(st.session_state[f"beads_{person_name}"]):
        st.success(f"✨ You have completed the rosary for {person_name}! May the eternal light shine upon them. ✨")
        if st.button("Reset Rosary", key=f"reset_{person_name}"):
            st.session_state[f"beads_{person_name}"] = [False] * beads
            st.rerun()
    else:
        st.caption(f"{sum(st.session_state[f'beads_{person_name}'])} / {beads} beads prayed")

# ================== Tab 1: Elucia Antoine ==================
with tab1:
    st.markdown('<div class="prayer-card">', unsafe_allow_html=True)
    st.markdown('<div class="saint-title">🌸 Saint Elucia Antoine 🌸</div>', unsafe_allow_html=True)
    st.markdown("*The Grandmother who raised a prince*")
    st.markdown(prayer_elucia)
    
    # Audio option? Not required but nice. We'll add a simple "Pray" button that triggers a visual effect.
    if st.button("🔊 Recite Prayer (Energy Activation)", key="elucia_pray"):
        st.balloons()
        st.markdown('<div style="background: radial-gradient(circle, gold, transparent); padding: 1rem; border-radius: 20px; text-align:center;">✨ The energy of Elucia Antoine fills this space. Shi, shi, shi. ✨</div>', unsafe_allow_html=True)
    
    rosary_counter("Elucia")
    st.markdown('</div>', unsafe_allow_html=True)

# ================== Tab 2: Kettely Auguste ==================
with tab2:
    st.markdown('<div class="prayer-card">', unsafe_allow_html=True)
    st.markdown('<div class="saint-title">🌺 Saint Kettely Auguste 🌺</div>', unsafe_allow_html=True)
    st.markdown("*The Mother who sacrificed everything*")
    st.markdown(prayer_kettely)
    
    if st.button("🔊 Recite Prayer (Energy Activation)", key="kettely_pray"):
        st.balloons()
        st.markdown('<div style="background: radial-gradient(circle, gold, transparent); padding: 1rem; border-radius: 20px; text-align:center;">✨ The energy of Kettely Auguste embraces you. Shi, shi, shi. ✨</div>', unsafe_allow_html=True)
    
    rosary_counter("Kettely")
    st.markdown('</div>', unsafe_allow_html=True)

# ================== Footer ==================
st.markdown("""
<div class="footer">
    <p>🌌 *In the name of the 1 – the Architect of this Universe* 🌌</p>
    <p>May the eternal souls of Elucia Antoine and Kettely Auguste guide, protect, and destroy all adversities.</p>
    <p>Built by Gesner Deslandes – GlobalInternet.py | For canonization inquiries or to add names, contact above.</p>
</div>
""", unsafe_allow_html=True)
