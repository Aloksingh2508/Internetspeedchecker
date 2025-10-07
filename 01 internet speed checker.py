import speedtest

def check_internet_speed():
    st = speedtest.Speedtest()
    
    print("Testing download speed...")
    download_speed = st.download() / 1_000_000  # Convert to Mbps
    
    print("Testing upload speed...")
    upload_speed = st.upload() / 1_000_000  # Convert to Mbps
    
    ping = st.results.ping
    
    print(f"\n🌐 Internet Speed Test Results:")
    print(f"Download Speed: {download_speed:.2f} Mbps")
    print(f"Upload Speed:   {upload_speed:.2f} Mbps")
    print(f"Ping:           {ping:.2f} ms")

# Run the function
check_internet_speed()
