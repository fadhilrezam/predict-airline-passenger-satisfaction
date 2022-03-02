import streamlit as st
# import requests

def app():
#     URL = 'http://127.0.0.1:5000/'

    st.title('Aplikasi Prediksi Airline Passenger Satisfaction')
    ct = st.number_input('Customer_Type (0: Loyal, 1: Disloyal)')
    age = st.number_input('Umur Penumpang')
    tot = st.number_input('Tujuan Penerbangan (0: Personal Trip, 1: Business Trip)')
    kelas = st.number_input('Kelas penerbangan (0: Business, 1: Eco, 2:Eco Plus)')
    fd = st.number_input('Jarak Penerbangan (Miles)')
    wifi = st.number_input('Tingkat Layanan Wifi (0:tidak ada, 1-5)')
    booking = st.number_input('Bagaimana Kemudahan Dalam Online Booking (0:susah, 1-5)')
    boarding = st.number_input('Bagaimana Kemudahan Dalam Online Boarding (0:susah, 1-5)')
    seat = st.number_input('Tingkat Kenyamanan Kursi Pesawat (0:tidak nyaman, 1-5)')
    entertain = st.number_input('Tingkat Kenyamanan Layanan Entertainment Pesawat (0: tidak menarik, 1-5)')
    onboard = st.number_input('Layanan On Board Maskapai (0:buruk, 1-5)')
    leg = st.number_input('Kenyamanan Leg Room (0:sangat sempit, 1-5)')
    service = st.number_input('Layanan Inflight Maskapai (0:buruk, 1-5)')
    clean = st.number_input('Kebersihan Interior Pesawat: (0:kotor, 1-5)')

    #param input
    #URL = URL+ f'?ct={ct}&age={age}&tot={tot}&kelas={kelas}&fd={fd}&wifi={wifi}&booking={booking}&boarding={boarding}&seat={seat}&entertain={entertain}&onboard={onboard}&leg={leg}&service={service}&clean={clean}'
    data = {'ct':ct,
            'age':age,
            'tot':tot,
            'kelas':kelas,
            'fd':fd,
            'wifi':wifi,
            'booking':booking,
            'boarding':boarding,
            'seat':seat,
            'entertain':entertain,
            'onboard':onboard,
            'leg':leg,
            'service':service,
            'clean':clean}

#     #Komunikasi
#     r = requests.get(URL, json=data)
#     res = r.json()
#     st.write(f"Hasil Prediksi : {res['data']['result']}")

