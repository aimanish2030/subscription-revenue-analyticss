# subscription-revenue-analyticss
Simple subscription revenue analytics project in Python

import pandas as pd

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

# 1. Monthly Recurring Revenue (MRR)
MRR = active_users["Monthly_Price"].sum()

# 2. Annual Recurring Revenue (ARR)
ARR = MRR * 12

# 3. Active Subscribers
active_count = len(active_users)

# 4. Total Subscribers
total_users = len(df)

# 5. Cancellations
cancelled_users = len(df[df["Status"] == "Cancelled"])

# 6. Churn Rate
churn_rate = (cancelled_users / total_users) * 100

# 7. Plan-wise Subscriber Distribution
plan_distribution = active_users["Plan"].value_counts()

# 8. ARPU (Average Revenue Per User)
ARPU = MRR / active_count

# 9. Simple Forecasted MRR (Assume 5% growth)
forecasted_MRR = MRR * 1.05

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

print("\nPlan-wise Active Subscribers:")
print(plan_distribution)
