import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# Create simple subscription data
# -----------------------------
data = {
    "User_ID": [1,2,3,4,5,6,7,8,9,10],
    "Plan": ["Basic","Standard","Premium","Basic","Standard",
             "Premium","Basic","Standard","Premium","Basic"],
    "Monthly_Price": [199,299,499,199,299,499,199,299,499,199],
    "Status": ["Active","Active","Cancelled","Active","Active",
               "Active","Cancelled","Active","Active","Active"]
}

df = pd.DataFrame(data)

# -----------------------------
# Active users
# -----------------------------
active_users = df[df["Status"] == "Active"]

# -----------------------------
# Metrics Calculation
# -----------------------------
MRR = active_users["Monthly_Price"].sum()
ARR = MRR * 12
active_count = len(active_users)
total_users = len(df)
cancelled_users = len(df[df["Status"] == "Cancelled"])
churn_rate = (cancelled_users / total_users) * 100
ARPU = MRR / active_count
forecasted_MRR = MRR * 1.05  # assume 5% growth

# -----------------------------
# Print Results
# -----------------------------
print("----- Subscription Revenue Analytics -----")
print("MRR:", MRR)
print("ARR:", ARR)
print("Active Subscribers:", active_count)
print("Total Subscribers:", total_users)
print("Cancelled Subscribers:", cancelled_users)
print("Churn Rate (%):", round(churn_rate, 2))
print("ARPU:", round(ARPU, 2))
print("Forecasted Next Month MRR:", round(forecasted_MRR, 2))

# -----------------------------
# Chart: Plan-wise Active Subscribers
# -----------------------------
plan_counts = active_users["Plan"].value_counts()

plan_counts.plot(kind="bar")
plt.title("Plan-wise Active Subscribers")
plt.xlabel("Subscription Plan")
plt.ylabel("Number of Users")
plt.show()
