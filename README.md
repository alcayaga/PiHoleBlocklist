# Pi-hole Blocklists

A collection of domain-based blocklists and filters optimized for Pi-hole to block ads, tracking, phishing, gambling, and malware, with a focus on Chilean domains and Smart TV telemetry.

## Available Blocklists

| List File | Description | Format |
| :--- | :--- | :--- |
| **[Chile-Ads.txt](file:///Users/pablo/Documents/GitHub/PiHoleBlocklist/Chile-Ads.txt)** | Filters for Chile-specific advertisement, telemetry, and tracking domains. | Domain List |
| **[Chile-Gambling.txt](file:///Users/pablo/Documents/GitHub/PiHoleBlocklist/Chile-Gambling.txt)** | Filters for Chilean gambling and online betting domains. | Adblock Plus (ABP) Format |
| **[Chile-Phishing.txt](file:///Users/pablo/Documents/GitHub/PiHoleBlocklist/Chile-Phishing.txt)** | Blocklist for Chilean phishing, scam, and fraudulent websites. | Domain List |
| **[Smart-TV.txt](file:///Users/pablo/Documents/GitHub/PiHoleBlocklist/Smart-TV.txt)** | Filters targeting Smart TV telemetry (specifically LG Smart TVs) and advertising. | Adblock Plus (ABP) Format |
| **[World-Phishing.txt](file:///Users/pablo/Documents/GitHub/PiHoleBlocklist/World-Phishing.txt)** | Global phishing and malware tracking sites. | Mixed Format |
| **[World-Tracking.txt](file:///Users/pablo/Documents/GitHub/PiHoleBlocklist/World-Tracking.txt)** | Global telemetry and user activity tracking servers. | Domain List |

---

## How to Install in Pi-hole

To use these blocklists in your Pi-hole setup, follow these step-by-step instructions:

### 1. Copy the Raw URL
Choose the blocklist you want to add and copy its raw URL. For example:
* **Chile Ads & Tracking:**
  `https://raw.githubusercontent.com/alcayaga/PiHoleBlocklist/main/Chile-Ads.txt`
* **Chile Gambling:**
  `https://raw.githubusercontent.com/alcayaga/PiHoleBlocklist/main/Chile-Gambling.txt`
* **Chile Phishing:**
  `https://raw.githubusercontent.com/alcayaga/PiHoleBlocklist/main/Chile-Phishing.txt`
* **Smart TV Telemetry:**
  `https://raw.githubusercontent.com/alcayaga/PiHoleBlocklist/main/Smart-TV.txt`
* **World Phishing:**
  `https://raw.githubusercontent.com/alcayaga/PiHoleBlocklist/main/World-Phishing.txt`
* **World Tracking:**
  `https://raw.githubusercontent.com/alcayaga/PiHoleBlocklist/main/World-Tracking.txt`

*(Note: Replace `alcayaga` with your GitHub username if you have customized these lists in your own fork).*

### 2. Add to Pi-hole Web Interface
1. Open and log in to your **Pi-hole Admin Console** (typically at `http://pi.hole/admin` or `http://<IP_ADDRESS>/admin`).
2. In the sidebar menu, navigate to **Group Management** and click on **Adlists**.
3. Under **Add a new adlist**:
   * **Address:** Paste the copied Raw URL from Step 1.
   * **Comment:** Enter a descriptive name (e.g., `PiHoleBlocklist - Chile Ads`).
4. Click the **Add** button.

### 3. Update the Gravity Database
After adding new lists, you must update Pi-hole's database for the blocklist changes to take effect.
* **Via Web Interface:** Go to **Tools** -> **Gravity** and click the **Update** button.
* **Via Terminal (SSH):** Run the following command on your Pi-hole host machine:
  ```bash
  pihole -g
  ```

---

## Validating Lists using Python

This repository includes a utility script `checkdns.py` to verify whether the domains listed in the blocklists are still active and resolving. This helps keep lists clean by identifying dead/expired domains.

### Prerequisites
Make sure you have Python 3 and the `dnspython` package installed:
```bash
pip install dnspython
```

### Running the Verification Script
You can run the script directly:
```bash
python checkdns.py
```

By default, the script checks the `Chile-Phishing.txt` file. You can open `checkdns.py` and modify the input file parameter on line 31 to check other lists:
```python
active, inactive = check_domains('Chile-Ads.txt')
```

The script will query Google's public DNS (`8.8.8.8`) for each domain and output:
* Active domains (currently resolving)
* Inactive domains (unresolving/dead)

---

## Contributing

If you encounter an ad, tracker, or phishing attempt that isn't blocked, feel free to contribute!
1. Fork this repository.
2. Add the domains to the appropriate `.txt` file (one domain per line).
3. Open a Pull Request with a clear description of the domains added.