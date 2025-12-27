from pathlib import Path

file_path_input = input("Please enter your File Path: ")
log_path = Path(file_path_input)

if log_path.exists():
    failed_attempts = {}
    THRESHOLD = 5

    with open(log_path, "r") as log:
        for line in log:
            if "FAILED_LOGIN" in line:
                # Splitting more carefully to avoid trailing/leading characters
                # Extracts 'jdoe' from 'user=jdoe'
                user = line.split("user=")[1].split()[0]
                # Extracts '192.168.1.50' from 'ip=192.168.1.50'
                ip = line.split("ip=")[1].strip()
                
                key = (user, ip)  # Use a tuple as a key for better reliability
                failed_attempts[key] = failed_attempts.get(key, 0) + 1

    # Check for alerts
    found_alerts = False
    for (user, ip), count in failed_attempts.items():
        if count >= THRESHOLD:
            print(f"[ALERT] Possible brute-force attack on user '{user}' from IP {ip} ({count} failed attempts)")
            found_alerts = True
            
    if not found_alerts:
        print(f"No brute-force attempts detected (Threshold: {THRESHOLD}).")
else:
    print(f"Error: File not found at {log_path}")
