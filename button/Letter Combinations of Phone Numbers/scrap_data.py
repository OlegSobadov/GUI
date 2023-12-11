import tkinter as tk
from tkinter import ttk
import string
import random
from random import randint
import re


def generate_random_data():
    file = f"""
            T{randint(1, 9)}tle: Image Recognition Report {randint(1, 100)}

            F{randint(1, 9)}rst name: John
            Last name: Doe
            """
    return file

def generate_random_email():
    username = ''.join(random.choice(string.ascii_letters) for _ in range(random.randint(5, 10)))
    domain = ''.join(random.choice(string.ascii_lowercase) for _ in range(random.randint(3, 6)))
    extension = random.choice(["com", "net", "org"])
    return f"{username}@{domain}.{extension}"

def generate_file():
    file_data = generate_random_data()
    with open(file_path, 'w') as f:
        f.write(file_data)
    status_label.config(text="File 'sample.txt' has been generated.")

def generate_email_file(num_emails):
    with open(file_path, 'w') as f:
        for _ in range(num_emails):
            email = generate_random_email()
            f.write(f"Title: Scraping Data\n")
            f.write(f"Email: {email}\n")
            f.write(f"First Name: Job\n")
            f.write(f"Last Name: Doe\n\n")
    status_label.config(text="File 'sample.txt' has been generated.")

def generate_custom_file():
    unit = var_extract.get() # Get t selected unit (name or email)
    if unit == 'names':
        generate_file()

    elif unit == 'email':
        try:
            num_emails = int(num_emails_entry.get()) # TODO: move to validate email_entry to isdecimal() or isdigit() and < 9:;
        except Exception as exc:
            num_emails = 5
        if num_emails < 10:
            generate_email_file(num_emails)
        else: 
            generate_email_file(num_emails=5) # if field empty - default 5;

def recognize_data():
    try:
        data = read_file()
        title, first_name, last_name = extract_data(data)
        display_data(title, first_name, last_name)
    except FileNotFoundError:
        status_label.config(text="File not found.")
    except Exception as exc:
        status_label.config(text=str(exc))

def recognize_email():
    try:
        data = read_file()
        emails = scrape_emails(data)
        display_email(emails)
    except FileNotFoundError:
        status_label.config(text="File not found.")
    except Exception as exc:
        status_label.config(text=str(exc))

def custom_recognize_data():
    unit = var_extract.get() # Get t selected unit (name or email)
    if unit == 'names':
        recognize_data()
    elif unit == 'email':
        recognize_email()
    else:
        ...

def read_file():
    with open(file_path, 'r') as f:
        return f.read()

def extract_data(data):
    pattern = re.compile(r'(\w\d)tle: (.+) (\w\d)rst name: (.+) Last name: (.+)', re.I | re.DOTALL)
    result = pattern.search(data)
    if result:
        return result.group(2).strip(), result.group(4).strip(), result.group(5).strip()
    else:
        raise Exception('No data found.')

def scrape_emails(content): # same extract email/data
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = re.findall(pattern, content)

    print("Scraped emails:")
    for email in emails:
        print(email)

    return emails

def display_data(title=None, first_name=None, last_name=None):
    status_label.config(text=f"Title: {title}\nFirst name: {first_name}\nLast name: {last_name}")

def display_email(emails):
    top = tk.Toplevel(window)
    top.geometry(f"+{int(window.winfo_width() + window.winfo_rootx())}+{int(window.winfo_height() * .9)}")
    frame = tk.Frame(top)
    frame.pack()
    for i, email in enumerate(emails):
        label = ttk.Label(frame, text=f'Email: {email}')
        label.grid(row=i, column=0, sticky='w')

    frame.update_idletasks()
    frame.place(relx=0.7, rely=0.6, anchor='center') 


# initialization
file_path = 'data/sample.txt'

# create the gui
window = tk.Tk()
window.title("File Generator")
window.geometry('250x200')


num_emails_label = tk.Label(window, text='Choice numbers of emails (1-9)') # add validation to entry no more than len(num_emails) < 10;
num_emails_label.pack()
num_emails_entry = tk.Entry(window)
num_emails_entry.pack()

generate_button = tk.Button(window, text="Generate File", command=generate_custom_file)
generate_button.pack()

recognize_button = tk.Button(window, text="Recognize Data", command=custom_recognize_data)
recognize_button.pack()


# radiobutton to choice name/email or both if email exists
var_extract = tk.StringVar()
var_extract.set('names') # default selection

radio_names = tk.Radiobutton(window, text='names', variable=var_extract, value='names')
radio_names.pack()
radio_email = tk.Radiobutton(window, text='email', variable=var_extract, value='email')
radio_email.pack()


status_label = tk.Label(window, text="")
status_label.pack()

window.mainloop()


