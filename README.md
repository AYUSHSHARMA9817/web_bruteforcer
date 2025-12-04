# 🔐 Web Brute Force Tool

![Python](https://img.shields.io/badge/python-3.6%2B-blue) ![License](https://img.shields.io/badge/license-MIT-green)

A multi-threaded web brute force tool for testing login forms against password lists. Supports both `.txt` and `.csv` wordlists with dynamic POST parameter configuration.

## 🚀 Features

- **Multi-threaded**: Configurable thread count for fast brute forcing
- **Dynamic Parameters**: Interactive POST parameter setup
- **Multiple Formats**: Supports `.txt` and `.csv` password files
- **Session Persistence**: Uses `requests.Session()` for realistic attacks
- **Smart Detection**: Identifies successful logins via "logout" keyword
- **CSV Parsing**: Extracts passwords from all cells and comma-separated values

## 📋 Requirements

## 🛠️ Installation
- ``` git clone https://github.com/yourusername/web-brute.git ```
- ``` cd web-brute ```

## ⚡ Usage
- ``` python3 web_brute.py ```

### Interactive Setup

1. **Enter target URL**: `http://example.com/login`
2. **Enter thread count**: `1000` (recommended for speed)
3. **Enter password file**: `passwords.txt` or `passwords.csv`
4. **Add POST parameters**:
Parameter name: username
Value for 'username': admin

Parameter name: submit
Value for 'submit': Login

Parameter name: done

5. **Watch results**: Successful passwords display immediately

### Example Session

- Give request url: http://testphp.vulnweb.com/login.php
- Give number of threads: 500
- Enter filename with passwords (.txt or .csv): rockyou.txt
- Enter POST parameters (type 'done' when finished):
- Parameter name: uname
- Value for 'uname': admin
- Parameter name: passwd
- Value for 'passwd':
- Parameter name: done
- Parameters: {'uname': 'admin', 'passwd': ''}
- Logged in for password: admin123
- Scan complete!

## 📁 Password File Formats

### TXT (One password per line)
password123
admin
123456
qwerty

### CSV (Passwords in any cell)
admin,password123,guest
user1,secret,pass

## ⚙️ Customization

**Modify success detection** in `web_brute.py`:
Change this line for different login indicators
if "logout" in ``` out.content.decode() ```: # or "dashboard", "welcome", etc.

## 🎯 Attack Vectors

- Login forms with username/password fields
- API endpoints with auth tokens
- Admin panels with weak credentials
- Custom POST-based authentication

## ⚠️ Legal & Ethical Warning

🔴 CRITICAL: ONLY USE ON SYSTEMS YOU OWN OR HAVE EXPLICIT WRITTEN PERMISSION TO TEST

❌ Unauthorized use is illegal and unethical
✅ Authorized pentesting / security research
✅ CTF challenges / bug bounty programs
✅ Your own applications / lab environments

## 🔒 Rate Limiting & Detection Avoidance

- Use reasonable thread counts (500-2000)
- Add delays between requests if needed:
import time
time.sleep(0.1) # Add in login() function

- Rotate User-Agents and proxies for production use

## 📊 Performance

| Threads | Passwords/sec | Recommended for |
|---------|---------------|-----------------|
| 500     | ~300-500     | Local testing  |
| 1000    | ~600-1000    | Lab networks   |
| 2000+   | ~1200+       | High bandwidth |

## Future Enhancements

- [ ] Proxy support & User-Agent rotation
- [ ] Custom success/failure detection
- [ ] Progress bar & ETA
- [ ] Results export (JSON/CSV)
- [ ] Rate limiting & delays
- [ ] Multiple target support

## 📄 License

MIT License - see [LICENSE](LICENSE) for details.

## 🙌 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

---
**Built for authorized security testing only** ⚡
