import webbrowser as wb

def webauto():
    chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe %s" # Path of browser file in your pc
    URLS = (
        "gmail.com",
        "google.com",
        "github.com/ashish-garg18"
    ) # URLS to be opened
    for url in URLS:
        print("Opening : " + url)
        wb.get(chrome_path).open(url)
    
webauto()