LABORATORY PRACTICE III – SOURCE CODE PACKAGE
A.Y. 2026-27 | BE

This ZIP contains code for all numbered practicals in Groups A, B and C, excluding every Mini Project option.

Folders:
- Group_A_Algorithms: C++ programs (Practical 1 to 5)
- Group_B_Machine_Learning: Python programs (Practical 1 to 5)
- Group_C_Blockchain: Solidity contracts for Practical 3 and 4, plus step-by-step guides/report outline for non-coding practicals 1, 2 and 5.

Run C++:
  g++ filename.cpp -std=c++17 -O2 -o program
  ./program

Run Python:
  python -m pip install -r requirements.txt
  python filename.py

Machine Learning datasets:
- Uber practical reads uber.csv if present; otherwise it creates a demonstration dataset.
- Email practical reads emails.csv with columns text,label; otherwise it uses a small demo dataset.
- Bank churn practical reads bank.csv if present; otherwise it creates a synthetic demo dataset.
- Clustering practical reads sales_data_sample.csv if present; otherwise it creates a synthetic demo dataset.
Synthetic results are for learning and testing only, not real-world conclusions.

Solidity:
Open Remix IDE, create a .sol file, paste the code, compile using Solidity 0.8.20 or later, and deploy to a test environment. For BankAccount, use the deployed contract's deposit function with a small test value. Do not use real funds for practice.

IMPORTANT:
The original index has Mini Project choices in each group. They are intentionally excluded, as requested previously.
