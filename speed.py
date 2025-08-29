import streamlit as st
import speedtest

st.title("🚀 Internet Speed Test")

if st.button("Check Speed"):
    st.write("Testing... Please wait ⏳")
    st.write("quntum... computing..⏳")
    st.write("Roming in internet for YOU ⏳")
    stt = speedtest.Speedtest()
    download = stt.download() / 1_000_000  # Mbps
    upload = stt.upload() / 1_000_000      # Mbps
    ping = stt.results.ping

    st.metric("Download Speed", f"{download:.2f} Mbps")
    st.metric("Upload Speed", f"{upload:.2f} Mbps")
    st.metric("Ping", f"{ping} ms")
