import streamlit as st
import asyncio
import edge_tts
import time

# ================== Page Config ==================
st.set_page_config(
    page_title="Canonization Rosary Book – Elucia & Kettely",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ================== Styling ==================
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
    .footer {
        text-align: center;
        margin-top: 3rem;
        padding: 1rem;
        font-size: 0.8rem;
        opacity: 0.7;
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

# ================== Multilingual Prayer Texts ==================
# English (original)
prayer_elucia_en = """
Eternal Canonization Prayer for Elucia Antoine

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

Shi, shi, shi.
"""

prayer_kettely_en = """
Eternal Canonization Prayer for Kettely Auguste

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

Shi, shi, shi.
"""

# French translations
prayer_elucia_fr = """
Prière de canonisation éternelle pour Elucia Antoine

Elucian Antoine,
Merci d'avoir élevé Gesner Deslandes, Ti boul, votre unique petit‑fils.
Merci pour ma première communion,
Merci d'avoir donné naissance à Kettely Auguste et d'avoir travaillé dans une usine pour payer mon école.
Merci de m'avoir nourri, payé le loyer, donné à votre petit‑fils une maison pour être élevé comme un prince.
Merci de m'avoir accompagné à l'école quand j'étais un enfant innocent,
Merci de m'avoir protégé jour et nuit,
Merci de m'avoir emmené chez le docteur quand j'étais malade,
Merci de m'avoir défendu lors d'altercations avec d'autres enfants.

Je crois que ton âme est toujours vivante quelque part dans cet Univers,
Et tu te souviens encore de moi, et je me souviens encore de toi.

Elucia Antoine, lorsque Kettely Auguste est partie vers l'orient éternel,
Toi et moi sommes restés seuls en grande harmonie, quelles que soient les circonstances.
Nous avons lutté contre toutes les adversités de la vie.
Quand tu es partie, me laissant derrière, j'ai accepté, mais cela m'a fait mal en silence, brûlant à l'intérieur de moi.

Ainsi, en souvenir de ta grandeur,
Je dis : que ton âme éternelle soit avec moi dans cette vie et pour toujours,
Pour détruire mes adversités présentes, visibles et invisibles,
Au nom du 1 – l'Architecte de cet Univers.

Shi, shi, shi.
"""

prayer_kettely_fr = """
Prière de canonisation éternelle pour Kettely Auguste

Kettely Auguste,
Merci d'avoir élevé Gesner Deslandes, Ti boul, votre fils unique.
Merci pour ma première communion,
Merci d'avoir travaillé dans une usine pour payer mon école.
Merci de m'avoir nourri, payé le loyer, donné à votre fils une maison pour être élevé comme un prince.
Merci de m'avoir accompagné à l'école quand j'étais un enfant innocent,
Merci de m'avoir protégé jour et nuit,
Merci de m'avoir emmené chez le docteur quand j'étais malade,
Merci de m'avoir défendu lors d'altercations avec d'autres enfants.

Tu as toujours dit que deux femmes prenaient soin de moi, luttant pour faire de ma vie un paradis.

Je crois que ton âme est toujours vivante quelque part dans cet Univers,
Et tu te souviens encore de moi, et je me souviens encore de toi.

Ainsi, en souvenir de ta grandeur,
Je dis : que ton âme éternelle soit avec moi dans cette vie et pour toujours,
Pour détruire mes adversités présentes, visibles et invisibles,
Au nom du 1 – l'Architecte de cet Univers.

Shi, shi, shi.
"""

# Spanish translations
prayer_elucia_es = """
Oración de canonización eterna para Elucia Antoine

Elucian Antoine,
Gracias por criar a Gesner Deslandes, Ti boul, tu único nieto.
Gracias por mi primera comunión,
Gracias por dar a luz a Kettely Auguste y trabajar en una fábrica para pagar mi escuela.
Gracias por alimentarme, pagar el alquiler, darle a tu nieto un hogar para ser criado como un príncipe.
Gracias por acompañarme a la escuela cuando era un niño inocente,
Gracias por protegerme día y noche,
Gracias por llevarme al médico cuando estaba enfermo,
Gracias por defenderme en altercados con otros niños.

Creo que tu alma sigue viva en algún lugar de este Universo,
Y todavía me recuerdas, y yo todavía te recuerdo.

Elucia Antoine, cuando Kettely Auguste viajó al eterno oriente,
Tú y yo nos quedamos solos en gran armonía, sin importar las circunstancias.
Luchamos contra todas las adversidades de la vida.
Cuando viajaste, dejándome atrás, lo acepté, pero dolió silenciosamente, ardiendo dentro de mí.

Así, en recuerdo de tu grandeza,
Digo: que tu alma eterna esté conmigo en esta vida y para siempre,
Para destruir mis adversidades presentes, visibles e invisibles,
En el nombre del 1 – el Arquitecto de este Universo.

Shi, shi, shi.
"""

prayer_kettely_es = """
Oración de canonización eterna para Kettely Auguste

Kettely Auguste,
Gracias por criar a Gesner Deslandes, Ti boul, tu único hijo.
Gracias por mi primera comunión,
Gracias por trabajar en una fábrica para pagar mi escuela.
Gracias por alimentarme, pagar el alquiler, darle a tu hijo un hogar para ser criado como un príncipe.
Gracias por acompañarme a la escuela cuando era un niño inocente,
Gracias por protegerme día y noche,
Gracias por llevarme al médico cuando estaba enfermo,
Gracias por defenderme en altercados con otros niños.

Siempre dijiste que dos mujeres me cuidaban, luchando para hacer de mi vida un paraíso.

Creo que tu alma sigue viva en algún lugar de este Universo,
Y todavía me recuerdas, y yo todavía te recuerdo.

Así, en recuerdo de tu grandeza,
Digo: que tu alma eterna esté conmigo en esta vida y para siempre,
Para destruir mis adversidades presentes, visibles e invisibles,
En el nombre del 1 – el Arquitecto de este Universo.

Shi, shi, shi.
"""

# Chinese (Simplified) translations
prayer_elucia_zh = """
永恒的封圣祈祷文 – 埃卢西亚·安托万

埃卢西安·安托万，
感谢您抚养了 Gesner Deslandes，Ti boul，您唯一的孙子。
感谢我的第一次圣餐，
感谢您生下了 Kettely Auguste 并在一家工厂工作来支付我的学费。
感谢您喂养我，支付房租，给您的孙子一个像王子一样被抚养的家。
感谢您在我还是个天真的孩子时陪我去上学，
感谢您日夜保护我，
感谢您在我生病时带我去看医生，
感谢您在我与其他孩子发生争执时为我辩护。

我相信您的灵魂仍然存在于这个宇宙的某个地方，
您仍然记得我，我也仍然记得您。

埃卢西亚·安托万，当 Kettely Auguste 前往永恒的东方时，
无论 circumstances 如何，您和我独自一人，和谐共处。
我们与生活的所有逆境抗争。
当您离开，留下我时，我接受了，但它默默地伤害着我，在我内心燃烧。

因此，为了纪念您的伟大，
我说：愿您永恒的灵魂在此生及永远与我同在，
以摧毁我现在的逆境，可见与不可见，
奉 1 – 这个宇宙的建筑师之名。

Shi， shi， shi.
"""

prayer_kettely_zh = """
永恒的封圣祈祷文 – 凯特莉·奥古斯特

凯特莉·奥古斯特，
感谢您抚养了 Gesner Deslandes，Ti boul，您唯一的儿子。
感谢我的第一次圣餐，
感谢您在一家工厂工作来支付我的学费。
感谢您喂养我，支付房租，给您的儿子一个像王子一样被抚养的家。
感谢您在我还是个天真的孩子时陪我去上学，
感谢您日夜保护我，
感谢您在我生病时带我去看医生，
感谢您在我与其他孩子发生争执时为我辩护。

您总是说有两位女士在照顾我，努力让我的生活成为天堂。

我相信您的灵魂仍然存在于这个宇宙的某个地方，
您仍然记得我，我也仍然记得您。

因此，为了纪念您的伟大，
我说：愿您永恒的灵魂在此生及永远与我同在，
以摧毁我现在的逆境，可见与不可见，
奉 1 – 这个宇宙的建筑师之名。

Shi， shi， shi.
"""

# Map languages
prayers = {
    "English": {
        "elucia": prayer_elucia_en,
        "kettely": prayer_kettely_en,
        "voice": "en-US-ChristopherNeural"
    },
    "French": {
        "elucia": prayer_elucia_fr,
        "kettely": prayer_kettely_fr,
        "voice": "fr-FR-HenriNeural"
    },
    "Spanish": {
        "elucia": prayer_elucia_es,
        "kettely": prayer_kettely_es,
        "voice": "es-ES-AlvaroNeural"
    },
    "Chinese": {
        "elucia": prayer_elucia_zh,
        "kettely": prayer_kettely_zh,
        "voice": "zh-CN-YunxiNeural"
    }
}

# ================== Cached TTS Audio Generation ==================
@st.cache_data(show_spinner=False)
def get_audio_bytes(text, voice):
    async def _generate():
        communicate = edge_tts.Communicate(text, voice)
        audio_data = b""
        async for chunk in communicate.stream():
            if chunk["type"] == "audio":
                audio_data += chunk["data"]
        return audio_data
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    result = loop.run_until_complete(_generate())
    loop.close()
    return result

# ================== Sidebar Company Info & Language Selection ==================
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/circled.png", width=80)
    st.markdown("## GlobalInternet.py")
    st.markdown("**Gesner Deslandes**, Engineer-in-Chief")
    st.markdown("---")
    st.markdown("### 🌐 Language")
    language = st.selectbox("Choose language / Choisir la langue / Seleccionar idioma / 选择语言", list(prayers.keys()))
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

# ================== Rosary Counter (unchanged) ==================
def rosary_counter(person_name):
    st.markdown("---")
    st.subheader("📿 Interactive Rosary – Click each bead as you pray")
    beads = 10
    if f"beads_{person_name}" not in st.session_state:
        st.session_state[f"beads_{person_name}"] = [False] * beads
    
    cols = st.columns(beads)
    for i, col in enumerate(cols):
        with col:
            if st.button("●", key=f"{person_name}_bead_{i}", use_container_width=True):
                st.session_state[f"beads_{person_name}"][i] = not st.session_state[f"beads_{person_name}"][i]
                st.rerun()
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
    st.markdown(prayers[language]["elucia"])
    
    # Recite button with AI voice
    if st.button("🔊 Recite Prayer (Energy Activation)", key="elucia_pray"):
        with st.spinner("Generating sacred audio..."):
            audio_bytes = get_audio_bytes(prayers[language]["elucia"], prayers[language]["voice"])
            st.audio(audio_bytes, format="audio/mp3")
        st.balloons()
        st.markdown('<div style="background: radial-gradient(circle, gold, transparent); padding: 1rem; border-radius: 20px; text-align:center;">✨ The energy of Elucia Antoine fills this space. Shi, shi, shi. ✨</div>', unsafe_allow_html=True)
    
    rosary_counter("Elucia")
    st.markdown('</div>', unsafe_allow_html=True)

# ================== Tab 2: Kettely Auguste ==================
with tab2:
    st.markdown('<div class="prayer-card">', unsafe_allow_html=True)
    st.markdown('<div class="saint-title">🌺 Saint Kettely Auguste 🌺</div>', unsafe_allow_html=True)
    st.markdown("*The Mother who sacrificed everything*")
    st.markdown(prayers[language]["kettely"])
    
    if st.button("🔊 Recite Prayer (Energy Activation)", key="kettely_pray"):
        with st.spinner("Generating sacred audio..."):
            audio_bytes = get_audio_bytes(prayers[language]["kettely"], prayers[language]["voice"])
            st.audio(audio_bytes, format="audio/mp3")
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
