
logFiles = [
    "report.pdf",
    "pmYojana.apk",
    "data.txt",
    "student.text",
    "cmYojana.pdf",
    "example.apk",
    "demo.bat"
]

for file in logFiles:
    if file.endswith(".apk"):
        print("Warning..!!")
        print("Check this file:",file)