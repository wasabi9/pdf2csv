from PIL import Image
import os
from tqdm import tqdm
import pandas as pd

import pytesseract

all_emails = ""
for i in tqdm(range(len(os.listdir("pages")))):
    all_emails += pytesseract.image_to_string(Image.open('pages/page_'+str(i+1)+'.jpg'))

emails_list = all_emails.split("\n")
emails_list = [email for email in emails_list if '@' in email]
df = pd.DataFrame(columns=["emails"])
df["emails"] = emails_list
df.to_csv("All_emails.csv", index=False)

