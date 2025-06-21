import streamlit as st
from PIL import Image
import base64


st.set_page_config(
    page_title="Picturam",
    page_icon="🩰",
    layout="wide",
    initial_sidebar_state="collapsed"
)


st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stButton > button {
        background-color: #ecf0f1 !important;
        color: black !important;
        border: none !important;
        border-radius: 25px !important;
        font-weight: bold !important;
        transition: all 0.3s ease !important;
    }
    
    .stButton > button:hover {
        background-color: #d5dbdb !important;
        transform: translateY(-1px) !important;
    }
    
    img {
        border-radius: 15px !important;
    }
    
    .block-container {
        padding-top: 0rem;
        }
    .main-header {
        text-align: center;
        font-size: 3.5em;
        font-weight: bold;
        color: #2c3e50;
        margin-bottom: 0.5em;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }

    .subtitle {
        text-align: center;
        font-size: 1.3em;
        color: #7f8c8d;
        margin-bottom: 1em;
        font-style: italic;
    }

    .nav-menu {
        display: flex;
        justify-content: center;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1em;
        border-radius: 10px;
        margin: 2em 0;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }

    .nav-button {
        background: rgba(255,255,255,0.2);
        color: white;
        border: none;
        padding: 0.8em 1.5em;
        margin: 0 0.5em;
        border-radius: 25px;
        cursor: pointer;
        font-size: 1em;
        font-weight: bold;
        transition: all 0.3s ease;
        text-decoration: none;
        display: inline-block;
    }

    .nav-button:hover {
        background: rgba(255,255,255,0.3);
        transform: translateY(-2px);
    }

    .nav-button.active {
        background: #e74c3c;
        box-shadow: 0 2px 10px rgba(231,76,60,0.3);
    }

    .section-header {
        font-size: 2em;
        color: #34495e;
        border-bottom: 3px solid #e74c3c;
        padding-bottom: 0.3em;
        margin-top: 2em;
        margin-bottom: 1em;
    }

    .info-box {
        background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%);
        padding: 1.5em;
        border-radius: 10px;
        margin: 1em 0;
        border-left: 5px solid #e74c3c;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
    }

    .team-member {
        background: #ffffff;
        padding: 1em;
        border-radius: 8px;
        margin: 0.5em 0;
        border: 1px solid #dee2e6;
        box-shadow: 0 1px 5px rgba(0,0,0,0.08);
    }

    .contact-info {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        padding: 2em;
        border-radius: 15px;
        margin: 2em 0;
        text-align: center;
    }

    .keywords {
        display: flex;
        flex-wrap: wrap;
        gap: 10px;
        margin: 1em 0;
    }

    .keyword-tag {
        background: #e74c3c;
        color: white;
        padding: 0.3em 0.8em;
        border-radius: 20px;
        font-size: 0.9em;
        font-weight: bold;
    }

    .photo-placeholder {
        width: 100%;
        height: 300px;
        background: linear-gradient(45deg, #f1f2f6, #ddd);
        border: 2px dashed #aaa;
        display: flex;
        align-items: center;
        justify-content: center;
        color: #666;
        font-size: 1.2em;
        border-radius: 10px;
        margin: 1em 0;
    }

    .hero-placeholder {
        width: 100%;
        height: 400px;
        background: linear-gradient(45deg, #2c3e50, #4a6741);
        border: 3px dashed #bdc3c7;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-size: 1.5em;
        border-radius: 15px;
        margin: 2em 0;
    }

    .content-section {
        display: none;
    }

    .content-section.active {
        display: block;
    }
</style>
""", unsafe_allow_html=True)


if 'current_section' not in st.session_state:
    st.session_state.current_section = 'uvod'


st.markdown('<div class="main-header">Picturam</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Současný tanec</div>', unsafe_allow_html=True)


col1, col2, col3, col4, col5, col6 = st.columns([1, 1, 1, 1, 1, 1])

with col1:
    if st.button("🏠 Úvod", key="uvod", use_container_width=True):
        st.session_state.current_section = 'uvod'

with col2:
    if st.button("🎭 O představení", key="o-predstaveni", use_container_width=True):
        st.session_state.current_section = 'o-predstaveni'

with col3:
    if st.button("👥 Tým", key="tym", use_container_width=True):
        st.session_state.current_section = 'tym'

with col4:
    if st.button("📞 Kontakt", key="kontakt", use_container_width=True):
        st.session_state.current_section = 'kontakt'

with col5:
    if st.button("🖼️ Galerie", key="galerie", use_container_width=True):
        st.session_state.current_section = 'galerie'
with col6:
    if st.button("📋 O autorce", key="cv", use_container_width=True):
        st.session_state.current_section = 'cv'

st.markdown("---")

# ÚVOD
if st.session_state.current_section == 'uvod':
    cols, colz = st.columns([1,2])
    with colz:
        st.image("images/int_1.jpg", use_container_width =True)
    with cols:
        st.markdown('<div class="section-header">Vítejte</div>', unsafe_allow_html=True)
        st.markdown('''
        <div class="info-box">
            <strong>Picturam</strong> je současné taneční představení inspirované slavným obrazem <strong>Leonarda Da Vinci 
            <em>Poslední večeře</em></strong> . Choreografie zkoumá převedení statického obrazu do živé jevištní podoby 
            a zasazuje historické téma do současného světa mužského společenství.
            <br><br>
            Představení trvá <strong>40 minut</strong> a interpretuje ho <strong>5 tanečníků</strong> pod vedením <strong>choreografky Evy Rezové</strong>.
        </div>
        ''', unsafe_allow_html=True)

        col1, col2, col3 = st.columns(3)
        with col1:
            st.markdown('''
            <div class="info-box">
                <strong>🎭 Žánr</strong><br>
                Současný tanec
            </div>
            ''', unsafe_allow_html=True)

        with col2:
            st.markdown('''
            <div class="info-box">
                <strong>⏱️ Délka</strong><br>
                40 minut
            </div>
            ''', unsafe_allow_html=True)

        with col3:
            st.markdown('''
            <div class="info-box">
                <strong>👥 Obsazení</strong><br>
                5 tanečníků
            </div>
            ''', unsafe_allow_html=True)
    st.markdown("---")
    st.image("images/int_2.jpg", use_container_width=True)
    st.markdown("---")
    st.image("images/int_3.jpg", use_container_width=True)

    st.markdown("""
    <div style="text-align: center; margin: 2em 0; padding: 1.5em; background: linear-gradient(135deg, #f8f9fa 0%, #e9ecef 100%); border-radius: 10px; border-left: 5px solid #e74c3c;">
        <p style="color: #34495e; font-size: 1.2em; margin-bottom: 0;">
            📸 <strong>Více fotografií z představení najdete v naší galerii</strong>
        </p>
    </div>
    """, unsafe_allow_html=True)
# O PŘEDSTAVENÍ
elif st.session_state.current_section == 'o-predstaveni':
    col_s1, cols_2 = st.columns([2,1 ])
    with col_s1:
        st.markdown('<div class="section-header">O představení</div>', unsafe_allow_html=True)

        st.markdown('''
        <div class="info-box">
            <strong>Premiéra inscenace:</strong><br>
            1. 5. 2023, PONEC - divadlo pro tanec, Praha
        </div>
        ''', unsafe_allow_html=True)

        st.markdown('<div class="section-header">Anotace</div>', unsafe_allow_html=True)
        st.markdown('''
        <div class="info-box">
            Choreografie vychází z výtvarného umění a zkoumá převedení statického obrazu do jevištní živé podoby. 
            Inspirací pro choreografii se stal známý obraz <strong>Poslední večeře</strong> slavného malíře Leonarda Da Vinci. 
            Téma se zabývá historickou podobou obrazu, jejím rozpracováním a zasazením do současného světa mužského společenství.
        </div>
        ''', unsafe_allow_html=True)

        st.markdown('<div class="section-header">Klíčová slova</div>', unsafe_allow_html=True)
        keywords = ["tanec", "mužská energie", "dynamika", "síla", "agrese", "napětí", "očištění"]
        keywords_html = "".join([f'<span class="keyword-tag">{keyword}</span>' for keyword in keywords])
        st.markdown(f'<div class="keywords">{keywords_html}</div>', unsafe_allow_html=True)


        st.markdown('<div class="section-header">Technické informace</div>', unsafe_allow_html=True)
        st.markdown('''
        <div class="info-box">
            <strong>Prostor:</strong> min. 12 × 12 × 6 m, černý baletizol, černé výkryty<br><br>
            <strong>Scénografie:</strong> 4× stůl o rozměrech 76 × 139 × 60 cm - kovová konstrukce a překližková deska, 
            během představení je s nimi manipulováno; dále několik drobnějších rekvizit<br><br>
            <strong>Zvuk:</strong> reprodukovaná hudba<br><br>
            <em>Lightplot a další detaily technických požadavků jsou k nalezení v 
            <a href="https://docs.google.com/document/d/1j46pklQYYJqYjDM6avl7JyuczVnZjuhz-93g9Sop0ic/edit?tab=t.0" target="_blank" style="color: #e74c3c; text-decoration: underline;">online technickém rideru</a>
            .</em>
        </div>
        ''', unsafe_allow_html=True)
    with cols_2:
        st.image("images/4.jpg", use_container_width =True)
        st.image("images/5.jpg", use_container_width=True)


# TÝM
elif st.session_state.current_section == 'tym':
    st.markdown('<div class="section-header">Tvůrčí tým</div>', unsafe_allow_html=True)

    team_info = [
        ("Choreografie a režie", "Eva Rezová"),
        ("Interpretace", "Adam Rameš, David Kodys, Jakub Kohout, Jakub Sedláček, Jan Drahokoupil"),
        ("Hudba", "Sarah Jedličková, Alesandro Marcello, G. B. Pergolesi, P. I. Tchaikovsky"),
        ("Scénografie", "Ivo Jedlička"),
        ("Kostým", "Polina Akhmetzhanova"),
        ("Light design", "Tomáš Morávek"),
        ("Produkce", "Natálie Matysková, Samuel Loj")
    ]

    for role, names in team_info:
        st.markdown(f'''
        <div class="team-member">
            <strong>{role}:</strong><br>
            {names}
        </div>
        ''', unsafe_allow_html=True)

   # st.markdown('<div class="section-header">Fotografie týmu</div>', unsafe_allow_html=True)
   # col1, col2 = st.columns(2)

elif st.session_state.current_section == 'kontakt':
    st.markdown('<div class="section-header">Kontakt</div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="info-box">
        <p>Pro objednání představení, technické dotazy nebo další informace nás neváhejte kontaktovat. 
        Rádi zodpovíme všechny vaše otázky týkající se představení Picturam.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="contact-info" style="padding: 0.8em; margin: 0.5em 0;">
        <h4 style="color: white; margin-bottom: 0.3em;">📧 Email projektu</h4>
        <p style="font-size: 1em; margin-bottom: 0.5em;">
            <a href="mailto:picturam.eva.rez@gmail.com" style="color: white; text-decoration: underline;">
                picturam.eva.rez@gmail.com
            </a>
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 📞 Telefonní kontakty")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="info-box">
            <h4 style="color: #e74c3c; margin-bottom: 0.5em;">Natálie Matysková</h4>
            <p><strong>Pozice:</strong> Produkce</p>
            <p><strong>Telefon:</strong> 
                <a href="tel:+420739740163" style="color: #2c3e50; text-decoration: none;">
                    +420 739 740 163
                </a>
            </p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="info-box">
            <h4 style="color: #e74c3c; margin-bottom: 0.5em;">Eva Rezová</h4>
            <p><strong>Pozice:</strong> Choreografka</p>
            <p><strong>Telefon:</strong> 
                <a href="tel:+420739748687" style="color: #2c3e50; text-decoration: none;">
                    +420 739 748 687
                </a>
            </p>
        </div>
        """, unsafe_allow_html=True)



# GALERIE
elif st.session_state.current_section == 'galerie':
    st.markdown('<div class="section-header">Galerie</div>', unsafe_allow_html=True)


    st.markdown("### Fotografie z představení")

    col1, col2= st.columns(2)

    with col1:

        st.image("images/gal_1.jpg", use_container_width =True)
        st.image("images/gal_3.jpg", use_container_width=True)
        st.image("images/gal_5.jpg", use_container_width=True)
    with col2:

        st.image("images/gal_2.jpg", use_container_width=True)
        st.image("images/gal_4.jpg", use_container_width=True)
        st.image("images/gal_6.jpg", use_container_width=True)


# CV
elif st.session_state.current_section == 'cv':
    st.markdown('<div class="section-header">CV - Eva Rezová</div>', unsafe_allow_html=True)

    st.markdown('''
    <div class="info-box">
        <p>Tanci se věnuje již od dětství. Během studia na konzervatoři Duncan Centre se účastnila projektu 
        <strong><em>Svěcení jara</em></strong> v nastudování Jiřího Bartovance, které slavilo úspěchy v Czech Center New York 
        i na českých festivalech. Dále se podílela na projektu japonské choreografky Yoshiko Chuma v rámci 
        pražské výstavy Secret Journey. Jako tanečnice a choreografka byla součástí projektu na festivalu 
        v Takaoka v Japonsku.
        <p>Vytvořila choreografii ke <strong><em>Koncertu pro Mr. Shakespeara</em></strong> s hudbou Daniela Fikejze v rámci 
        Letních shakespearovských slavností 2022. S divadlem J.K.Tyla spolupracovala jako choreografka na 
        muzikálu <strong><em>Kouzelné hodinky doktora Kronera</em>, <em>Kozí válka</em> a <em>Company</em></strong>.</p>
       <p>Zúčastnila se studijních pobytů na Royal Conservatoire Antwerp v Belgii a na National Taiwan 
        University of Arts. V současnosti se jako interpretka a choreografka účastní mnoha uměleckých 
        projektů a zároveň se věnuje pedagogické činnosti.</p>
    </div>
    ''', unsafe_allow_html=True)

st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #7f8c8d; margin-top: 2em;">
    <p>© 2025 Picturam - Současný tanec</p>
    <p><em>Inspirováno dílem Leonarda Da Vinci "Poslední večeře"</em></p>
</div>
""", unsafe_allow_html=True)
