import speedtest   
st = speedtest.Speedtest()      #object created

print("Current Downloading Speed", st.download()) 

print("Current Uploading Speed", st.upload()) 

st.get_servers([])       #used to get current ping
print(st.results.ping)
