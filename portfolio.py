import streamlit as st
from streamlit_option_menu import option_menu
import requests
from streamlit_lottie import st_lottie
from PIL import Image

st.set_page_config(page_title="Iqbal's portfolio", page_icon=":rocket:",layout= "wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()



lottie_coder = load_lottieurl("https://lottie.host/310e5446-8eec-44f7-9b20-ca6cfe74c30e/ffOZNWqZIl.json")
lottie_coder2 = load_lottieurl("https://lottie.host/e75f8fa2-6b9d-4ff3-b9ae-f7b4cddd8811/nkFbs2xPbh.json")
image = Image.open("Images/Khabila.png")
image2 = Image.open("Images/SIMPLE.png")
image3 = Image.open("Images/Sistem Pakar.png")
image4 = Image.open("Images/instagram.png")
image5 = Image.open("Images/Linkedin.png")
image6 = Image.open("Images/Gmail.png")
image7 = Image.open("Images/FAQ.png")
image8 = Image.open("Images/COLLEGE.png")
image9 = Image.open("Images/COMMERCE.png")
image10 = Image.open("Images/FINMAP.png")
image11 = Image.open("Images/MANAJE.png")
image = image.resize((150, 100))
image2 = image2.resize((150, 100))
image3 = image3.resize((150, 100))
image7 = image7.resize((150, 100))
image8 = image8.resize((150, 100))
image9 = image9.resize((150, 100))
image10 = image10.resize((150, 100))
image11 = image11.resize((150, 100))
#image4 = image4.resize((150, 150))
#image5 = image5.resize((150, 150))
#image6 = image6.resize((250, 150))

with st.container():
    col8, col9 = st.columns(2)
    with col8:
        st.subheader("Hello It's Me :wave:")
        st.title("Iqbal Kurriana Putra")
        st.write("*Membantu perusahaan dan individu mewujudkan potensi mereka melalui solusi teknologi yang inovatif.*")
        st.markdown("[Readmore on CV](https://drive.google.com/file/d/1G66VK9bzYOq3u6w6jrIWAo_ZDMX9Fe_q/view?usp=sharing)")
    with col9:
        st_lottie(lottie_coder, height=320)

st.write('---')

with st.container():
    selected = option_menu(
        menu_title = None,
        options = ['About','Projects','Contact'],
        icons = ['person','code-slash','chat-left-text-fill'],
        orientation= 'horizontal'
    )
if selected == 'About':

    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            st.subheader("I am Iqbal Kurriana Putra")
            st.header('Business Application Solution Architect')
            st.title('PT ASDP Indonesia Ferry')
            st.write("Saya pengembang tekun dan antusias dengan perancangan sistem. Saya juga memiliki passion tentang latar belakang yang kuat dalam Python dan Machine Learning.")
        with col2:
            st_lottie(lottie_coder2, height=120)
    
    st.write("---")

    with st.container():
        col3,col4 = st.columns(2)
        with col3:
            st.subheader("""
            Education
                         """)
            st.info("""
            - Universitas Jember (2019-2024)
                - Fakultas Ilmu Komputer - S1 Sistem Informasi
                - IPK: 3.81
            """)
        with col4:
            st.subheader("""
            Achivement
            """)
            st.info("""
            - Juara 1 Tingkat Nasional bidang Bisnis TIK IT Convert 2020 Universitas Jember
            - Juara 1 Best Presentation dan Best Poster Program Kreativitas Mahasiswa 2021 Universitas Jember
            - Juara 2 dan 3 Tingkat Fakultas bidang Bisnis TIK Fakultas Ilmu Komputer, Universitas Jember
            - Juara 1 PKM-PI Tingkat Fakultas Ekonomi dan Bisnis 2021
            - Poster Terbaik IT Convert 2022 Bidang Bisnis TIK
            """)
    with st.container():
        st.subheader("""
        Experience
        """)
        st.info(""" 
        - Universitas Jember
            - Juri Lomba Proposal BISNIS TIK Fortran 2021 OSPEK Fakultas Ilmu Komputer
            - Juri Lomba Proposal BISNIS TIK Fortran 3.0 (2022) OSPEK Fakultas Ilmu Komputer
            - Juri Pelatihan Public Speaking UKM MUSTIKA 2023
            - Koordinator Desa Wisata Arjasa(Ketua Kelompok KKN MBKM 2022)
            - Narasumber WEBINAR NGOPI SELASA #53 (NGOBROL PAGI SELARASKAN ASA UNTUK DESA) LP2M, Universtas Jember 2023
            - Pemateri Video dan Desain Grafis dalam Kegiatan Innovate Ideals Annual Competition(INDIUM) 2023 Himpunan Mahasiswa Teknik Kimia, Universitas Jember
        - Software Engineer Practicum Assistant 2020 - 2022
        - Enterprise Resources Planning Specialist(Internship) - PT Andromedia Indonesia
        - Junior Digital Trainer and Mentor(Internship) - PT Gemilang Media Wisatama(Travelxism)
            - Supreme Leader
            - Most Active Student
            - Pemateri Pelatihan Pembuatan Konten Digital di Desa Wisata Jatirejo, Bantul, DIY
            - Pemateri Pelatihan Pemasaran/Marketing Kalurahan Tlogoadi Sleman, DIY
        - System Analyst(Internship) - PT Wesclic Indonesia Neotech
        - Business Application Solution Architect - PT ASDP Indonesia Ferry
        """)

if selected =='Projects':
    with st.container():
        st.title("My Projects")
        st.write("##")
        st.header("System Analyst")
        col6, col7 = st.columns((1,5))
        with col6:
            st.image(image)
        with col7:
            st.subheader("E-Commerce UMKM Khabila")
            st.write("""Software Requirement Spesification E-Commerce UMKM Khabila
            """)
            st.markdown("[Readmore](https://drive.google.com/file/d/10FTQ3mIPrNSR8A4cxNEpYBGWxpXOa-yz/view)")

    with st.container():
        col10, col11 = st.columns((1,5))
        with col10:
            st.image(image2)
        with col11:
            st.subheader("Sistem Informasi Management Pengadaan Elektronik Pemerintah")
            st.write("""Software Requirement Spesification Sistem Informasi Management Pengadaan Elektronik Pemerintah
            """)
            st.markdown("[Readmore](https://drive.google.com/file/d/1LUFJrqW7_udCk6RtoEdUIBQIjgJohPXw/view?usp=sharing)")

    with st.container():
        col19, col20 = st.columns((1,5))
        with col19:
            st.image(image7)
        with col20:
            st.subheader("Sistem Informasi Management Pengadaan Elektronik Pemerintah")
            st.write("""Frequently Asked Questions Sistem Informasi Management Pengadaan Elektronik Pemerintah
            """)
            st.markdown("[Readmore](https://drive.google.com/file/d/1mz2CiR269us4Pwf4TCy6ZXngNfarBEnr/view?usp=drive_link)")

    with st.container():
        col21, col22 = st.columns((1,5))
        with col21:
            st.image(image8)
        with col22:
            st.subheader("Sistem Informasi Manajemen Tracer Alumni")
            st.write("""Dokumen End User Sistem Informasi Manajemen Tracer Alumni
            """)
            st.markdown("[Readmore](https://drive.google.com/file/d/1DVekC1OlnTN15DFMBgCZ__kPrxuSa6L3/view?usp=drive_link)")

    with st.container():
        col23, col24 = st.columns((1,5))
        with col23:
            st.image(image9)
        with col24:
            st.subheader("Manaje Store - E-commerce Website Builder")
            st.write("""Dokumen End User Manaje Store - E-commerce Website Builder
            """)
            st.markdown("[Readmore](https://drive.google.com/file/d/1qfV0M6ZlLBCnYdV-uz5iFIqOwQseNIo7/view?usp=drive_link)")

    with st.container():
        col25, col26 = st.columns((1,5))
        with col25:
            st.image(image10)
        with col26:
            st.subheader("Mobile App - FINMAP")
            st.write("""Dokumen End User Mobile App - FINMAP
            """)
            st.markdown("[Readmore](https://drive.google.com/file/d/127pgBk-UDGRce6KIPo9XPZZtUoAXZzTW/view?usp=drive_link)")

    with st.container():
        col21, col22 = st.columns((1,5))
        with col21:
            st.image(image11)
        with col22:
            st.subheader("Website Manaje LPX Studio")
            st.write("""Diagram Penambahan Fitur SRS LPX
            """)
            st.markdown("[Readmore](https://drive.google.com/file/d/1CVmhpdY8QeSS2MNV2ZkrG5d-Ab_XkIox/view?usp=drive_link)")
            st.markdown("**Next Project Soon*")
    st.write('---')

    with st.container():
        st.header("Software Engineer")
        col12, col13 = st.columns((1,5))
        with col12:
            st.image(image3)
        with col13:
            st.subheader("Sistem Pakar Diagnosa Penyakit Ayam Pedaging")
            st.write("""Sistem Pakar Diagnosa Penyakit Ayam Pedaging Menggunakan Metode FK-NN Studi Kasus Peternakan PT. Cemerlang Unggas Lestari
            """)
            st.markdown("[Visit Expert System](https://sistem-pakar-penyakit-ayam-192410101033.streamlit.app/)")
            st.markdown("[Visit Github Repo](https://github.com/192410101033/sistem-pakar-penyakit-ayam.git)")
            st.markdown("**Next Project Soon*")

if selected == 'Contact':
    st.title("Get in touch!")
    st.write('##')
    st.write('##')
    with st.container():
        col12, col13, col14, col15, col16, col17, col18 = st.columns((1, 1, 1,1,1,1.7,1))
    
        with col12:
            st.write("")

        with col13:
            st.image(image4, width=150)
            st.markdown('<div style="text-align: center;">'
                        '<h3>INSTAGRAM</h3>'
                        '<a href="https://www.instagram.com/iqbalkurrianaputra/">iqbalkurrianaputra</a>'
                        '</div>', unsafe_allow_html=True)
        with col14:
            st.write("")

        with col15:
            st.image(image5, width=150)
            st.markdown('<div style="text-align: center;">'
                        '<h3>LINKEDIN</h3>'
                        '<a href="https://www.linkedin.com/in/iqbalkurrianaputra">Iqbal Kurriana Putra</a>'
                        '</div>', unsafe_allow_html=True)
        
        with col16:
            st.write("")

        with col17:
            st.image(image6, width=250)
            st.markdown('<div style="text-align: center;">'
                        '<h3>GMAIL</h3>'
                        '<a href="https://iqbalkurrianaputra@gmail.com">iqbalkurrianaputra@gmail.com</a>'
                        '</div>', unsafe_allow_html=True)
        
        with col18:
            st.write("")
