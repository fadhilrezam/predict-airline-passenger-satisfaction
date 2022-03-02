import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def app():
    st.title('Prediksi Airline Passenger Satisfaction')
    df = pd.read_csv('train.csv')
    df.columns = df.columns.str.replace(' ','_')
    my_expander = st.expander("Telusuri Data Set", expanded=False)
    with my_expander:
        st.write(df)


#-------------------------------------------------------------------------------------------------------------------------------------------
    st.subheader('Deskripsi Dataset')
    st.write('Dataset yang akan di gunakan dalam pengerjaan Milestone 2 ini adalah dataset mengenai Airline Passenger Satisfaction, dimana berisikan data survey dari beberapa pengguna maskapai penerbangan terkait faktor apa saja yang menandakan kepuasan mereka masing-masing.')
    st.write('\n')
    st.write('\n')
    st.subheader('Tujuan Pengolahan Dataset')
    st.write('Tujuan dari pengerjaan Milestone 2 ini adalah untuk membuat suatu model yang mampu memprediksi bagaimana tingkat kepuasan seorang pengguna maskapai (satisfied atau dissatisfied/netral) berdasarkan beberapa data input yang mereka berikan.')
    st.write('\n')
    st.write('----------------------------------------------------------------------------------------------------------------------------')
#-------------------------------------------------------------------------------------------------------------------------------------------


#-------------------------------------------------------------------------------------------------------------------------------------------
    st.header('Exploratory Data Analysis (EDA)')
    st.write('\n')
    st.write('\n')
    col1, col2, col3= st.columns((1,1,1))
    with col1:
        st.subheader('Flight Passanger Satisfaction berdasarkan Jenis Customer')
        fig,ax=plt.subplots(figsize=(10,7))
        sns.countplot(x = df['Customer_Type'], hue= df['satisfaction'], color = 'red')
        st.pyplot(fig)
    with col2:
        st.subheader('Flight Passanger Satisfaction berdasarkan Tujuan Penerbangan')
        fig,ax=plt.subplots(figsize=(10,7))
        sns.countplot(x = df['Type_of_Travel'], hue= df['satisfaction'], color = 'red')
        st.pyplot(fig)
    with col3:
        st.subheader('Flight Passanger Satisfaction berdasarkan Tujuan Kelas')
        fig,ax=plt.subplots(figsize=(10,7))
        sns.countplot(x = df['Class'], hue= df['satisfaction'], color = 'red')
        st.pyplot(fig)
    
    st.subheader('Penjelasan')
    st.write('Grafik di atas menunjukan bagaimana kepuasan penumpang pesawat berdasarkan jenis pelanggan,tujuan penerbangan dan kelas penerbangan yang di ambil oleh penumpang. Terlihat bahwa penumpang-penumpang yang loyal, tujuan penerbangannya yaitu untuk melakukan business trip dan juga penumpang yang menggunakan Business Class lebih banyak yang merasa puas dengan layanan yang di berikan oleh maskapai selama penerbangan.')
    st.write('\n')
    st.write('\n')
#-------------------------------------------------------------------------------------------------------------------------------------------


#-------------------------------------------------------------------------------------------------------------------------------------------
    row1_spacer1, row1_1, row1_spacer2 = st.columns((.1, 3.2, .1))
    with row1_1:
        st.subheader('Hubungan Jarak Penerbangan dengan Jenis Perjalanan')
        fig1,ax=plt.subplots(figsize=(30,12))
        fig1=sns.catplot(kind='bar', col = 'Class', x='Flight_Distance', y='Type_of_Travel', hue='satisfaction', data = df)
        st.pyplot(fig1)
    st.subheader('Penjelasan')
    st.write('Grafik di atas menunjukan bagaimana hubungan jarak suatu penerbangan dengan jenis penerbangan yang di kelompokkan berdasarkan pemilihan kelas penerbangan (Eco, Eco Plus dan Business) dengan melihat bagaimana satisfaction mereka selama penerbangan. Didapatkan beberapa informasi sebagai berikut:') 
    st.write('1. Untuk konsumen dengan jenis penerbangan Personal Travel, baik di kelas Eco Plus, Eco, maupun Business lebih banyak merasa puas dengan layanan yang airline berikan.') 
    st.write('2. Untuk konsumen dengan jenis penerbangan Business Travel, mereka lebih puas melakukan penerbangan dengan kelas Business untuk jarak yang jauh, hal ini didasari dengan alasan mungkin karena jaraknya jauh, mereka melakukan penerbangan untuk urusan bisnis maka dengan memilih kelas Business, mereka akan lebih dimanjakan dengan fasilitas dan privacy yang lebih baik, sehingga ketika sampai di tempat tujuan tidak terlalu merasa kelelahan akibat penerbangan dan bisa lebih produktif untuk melakukan urusan bisnis kedepannya.')
    st.write('\n')
    st.write('\n')
#------------------------------------------------------------------------------------------------------------------------------------------- 


#-------------------------------------------------------------------------------------------------------------------------------------------
    row2_spacer1, row2_1, row2_spacer2 = st.columns((.1, 3.2, .1))
    with row2_1:
        st.subheader('Hubungan Satisfaction dengan Seat comfort')
        fig2,ax=plt.subplots(figsize=(30,12))
        fig2=sns.catplot(kind = 'count', x='satisfaction', col='Seat_comfort', data=df, height = 4, aspect=0.7)
        st.pyplot(fig2)

    row3_spacer1, row3_1, row3_spacer2 = st.columns((.1, 3.2, .1))
    with row3_1:
        st.subheader('Hubungan Satisfaction dengan Inflight entertainment')
        fig3,ax=plt.subplots(figsize=(30,12))
        fig3=sns.catplot(kind = 'count', x='satisfaction', col='Inflight_entertainment', data=df, height = 4, aspect=0.7)
        st.pyplot(fig3)

    row4_spacer1, row4_1, row4_spacer2 = st.columns((.1, 3.2, .1))
    with row4_1:
        st.subheader('Hubungan Satisfaction dengan Online boarding')
        fig4,ax=plt.subplots(figsize=(30,12))
        fig4 = sns.catplot(kind = 'count', x='satisfaction', col='Online_boarding', data=df, height = 4, aspect=0.7)
        st.pyplot(fig4)
    st.write('\n')
    st.subheader('Penjelasan')
    st.write('Dari grafik plot di atas dapat di simpulkan bagaimana hubungan ke tiga fitur tersebut dengan tingkat satisfaction konsumen selama penerbangan:')
    st.write('1. Terkait seat comfort, semakin nyaman tempat duduk selama penerbangan maka konsumen sudah merasakan bahwa airline ini memiliki tingkat kenyamanan penerbangan yang bagus.')
    st.write('2. Terkait inflight entertainment juga sama, mungkin semakin bervariasi fitur-fitur seperti film, musik atau mungkin ada fitur seperti POV dari berbagai sisi untuk melihat bagaimana keadaan di luar pesawat dapat meningkatkan kenyamanan mereka.')
    st.write('3. Terakhir terkait Online boarding, ini untuk keadaan sebelum penerbangan. Jadi mungkin apabila maskapai sudah semakin digital seperti dengan adanya fitur online boarding dimana konsumen hanya perlu melakukan check in melalui aplikasi ataupun website tanpa perlu melakukan check in secara tradisional di terminal bandara juga dapat meningkatkan tingkat kenyamanan mereka.')
 #-------------------------------------------------------------------------------------------------------------------------------------------       

        

