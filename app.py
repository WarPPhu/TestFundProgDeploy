# -*- coding: utf-8 -*-

import streamlit as st


st.set_page_config(
             page_title="Fundamental Programming Project",
             layout="wide",
             initial_sidebar_state="expanded",
         )

class App:
    def __init__(self):

        self.column_name = ['Gross(M) $', 'Director', 'Actor', 'Writer', 'Rating', 'Genres',
                                                           'Country', 'Laguages', 'Filiming Locations', 'Run Times', 'Release Date',
                                                           'Have Official Site', 'Company']

  
    def MainPage(self):
        st.markdown("## Gross Prediction")
        st.write("\n")
        
        
    def PageAppendix(self):
        st.markdown("## Appendix")
        
        st.write('Ref Data')
        st.write('https://www.imdb.com/')
        
        st.write('Group Member')
        st.write('6480444026, ปภัช สุจิตรัตนันท์, Papat Sujitrattanun')
        st.write('6480448626, ปาลิตา เหลืองพัฒนผดุง, Palita Luengpattanapadung')
        st.write('6480459526, พิเชฐ ชาไชย, Pichet Chachai')
        st.write('6480469826, ภูริณัฐ จันทร์หอม, Phurinut Chanhom')
        st.write('6480484126, วัชรพล สร้างกุศล, Watcharapol Srangkusol')

    def start(self):
        st.title("Fundamental Programming Project")
        with st.sidebar:
            page = st.radio("Select page", tuple(self.page.keys()))
        self.page[page]()


if __name__ == "__main__":
    app = App()
    app.start()
