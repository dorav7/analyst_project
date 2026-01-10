import pandas as pd
import random
import datetime

# הגדרות
NUM_ROWS = 500  
OUTPUT_FILE = "sensitive_sales_data_v2.csv" # שם קובץ חדש

# מאגרי נתונים
FIRST_NAMES = ["John", "Jane", "Michael", "Emily", "David", "Sarah", "Daniel", "Laura", "Robert", "Linda"]
LAST_NAMES = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez"]
DOMAINS = ["gmail.com", "yahoo.com", "hotmail.com", "company.net"]
STREETS = ["Main St", "Broadway", "Park Ave", "Oak Ln", "Cedar Dr", "Pine St"]
CITIES = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]
CATEGORIES = ["Electronics", "Fashion", "Home & Garden", "Books", "Toys & Games", "Sports", "Automotive"]
PAYMENT_METHODS = ["Credit Card", "PayPal", "Debit Card", "Bank Transfer"]

def generate_fake_data(num_rows):
    data = []
    
    # ניצור "מאגר לקוחות" כדי שללקוחות יהיו מספר רכישות (יותר ריאליסטי)
    customers = []
    for _ in range(50): # נניח שיש 50 לקוחות חוזרים
        first = random.choice(FIRST_NAMES)
        last = random.choice(LAST_NAMES)
        cust_id = f"CUST-{random.randint(1000, 9999)}" # המזהה הלא-רגיש שלך!
        
        customers.append({
            "Customer_ID": cust_id,
            "Customer_Name": f"{first} {last}",      # רגיש
            "Email": f"{first.lower()}.{last.lower()}{random.randint(1,99)}@{random.choice(DOMAINS)}", # רגיש
            "Phone_Number": f"555-{random.randint(100, 999)}-{random.randint(1000, 9999)}", # רגיש
            "Address": f"{random.randint(1, 999)} {random.choice(STREETS)}, {random.choice(CITIES)}, USA", # רגיש
            "Credit_Card": f"{random.randint(4000, 4999)}-{random.randint(1000, 9999)}-{random.randint(1000, 9999)}-{random.randint(1000, 9999)}" # רגיש
        })

    for i in range(num_rows):
        # בוחרים לקוח אקראי מהרשימה (כדי שיהיו לקוחות חוזרים לאנליזה)
        cust = random.choice(customers)
        
        row = {
            "Transaction_ID": f"TXN-{10000 + i}",
            "Date": (datetime.date(2025, 1, 1) + datetime.timedelta(days=random.randint(0, 365))).isoformat(),
            
            # --- השדה החדש והחשוב ---
            "Customer_ID": cust["Customer_ID"], 
            # ------------------------
            
            "Customer_Name": cust["Customer_Name"],       
            "Email": cust["Email"],                  
            "Phone_Number": cust["Phone_Number"],           
            "Address": cust["Address"],              
            "Credit_Card": cust["Credit_Card"],               
            
            "Category": random.choice(CATEGORIES),
            "Amount": round(random.uniform(15.00, 1500.00), 2),
            "Payment_Method": random.choice(PAYMENT_METHODS)
        }
        data.append(row)
        
    return pd.DataFrame(data)

# יצירה ושמירה
df = generate_fake_data(NUM_ROWS)
df.to_csv(OUTPUT_FILE, index=False)

print(f"File created successfully: {OUTPUT_FILE}")
print(f"Columns: {list(df.columns)}")