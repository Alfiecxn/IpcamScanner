import socket

def scan_ip_range(ip_range):
  # Split the IP range into start and end IPs
  start, end = ip_range.split('-')
  # Get the start and end IPs in integer form
  start_ip = list(map(int, start.split('.')))
  end_ip = list(map(int, end.split('.')))

  # Initialize a list to store the IP addresses of the cameras
  cameras = []

  # Initialize a counter to keep track of the number of IPs scanned
  count = 0

  # Loop through all IPs in the range
  for i in range(start_ip[0], end_ip[0]+1):
    for j in range(start_ip[1], end_ip[1]+1):
      for k in range(start_ip[2], end_ip[2]+1):
        for l in range(start_ip[3], end_ip[3]+1):
          # Construct the IP address
          ip = f"{i}.{j}.{k}.{l}"
          # Check if the IP address is a camera
          if is_ip_camera(ip):
            cameras.append(ip)
          count += 1
          # Print progress every 100 IPs
          if count % 100 == 0:
            print(f"Scanned {count} IPs")
  return cameras

def is_ip_camera(ip):
  # Try to connect to the IP camera on port 80 (default port for HTTP)
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.settimeout(0.5)
  try:
    s.connect((ip, 80))
    s.close()
    return True
  except:
    return False

# Example usage
ip_range = "192.168.1.1-192.168.1.254"
cameras = scan_ip_range(ip_range)

# Write the list of cameras to a file
with open("cameras.txt", "w") as f:
  for camera in cameras:
    f.write(camera + "\n")

print(f"Found {len(cameras)} cameras. IP addresses written to cameras.txt")
