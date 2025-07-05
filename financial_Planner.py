# import streamlit as st
# import pandas as pd
# import numpy as np
# import plotly.express as px
# import plotly.graph_objects as go
# from plotly.subplots import make_subplots
# from datetime import datetime, timedelta
# import io
# from openpyxl import Workbook
# from openpyxl.styles import Font, PatternFill, Alignment
# import base64

# # Page configuration
# st.set_page_config(
#     page_title="Financial Planner",
#     page_icon="💰",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )

# # Custom CSS for better styling
# st.markdown("""
# <style>
#    .main-header { 
#     font-size: 2.5rem;
#     font-weight: bold;
#     color: white; /* Text color */
#     text-align: center;
#     margin-bottom: 2rem;
# }

# .metric-container {
#     background-color: #121212; /* Dark background */
#     padding: 1rem;
#     border-radius: 10px;
#     margin: 0.5rem 0;
#     color: white; /* Ensure text inside is white */
# }

# .stMetric {
#     background-color: #1e1e1e; /* Slightly lighter dark for contrast */
#     color: white; /* Text color */
#     padding: 1rem;
#     border-radius: 8px;
#     box-shadow: 0 2px 4px rgba(255,255,255,0.1); /* Soft light shadow */
# }

# </style>
# """, unsafe_allow_html=True)

# # Helper functions
# def calculate_compound_interest(principal, rate, time, compound_freq=12):
#     """Calculate compound interest"""
#     amount = principal * (1 + rate / compound_freq) ** (compound_freq * time)
#     return amount

# def calculate_sip_returns(monthly_investment, annual_rate, years):
#     """Calculate SIP returns"""
#     monthly_rate = annual_rate / 12
#     months = years * 12
#     future_value = monthly_investment * (((1 + monthly_rate) ** months - 1) / monthly_rate)
#     return future_value

# def calculate_loan_emi(principal, rate, tenure):
#     """Calculate EMI for loan"""
#     monthly_rate = rate / 12
#     months = tenure * 12
#     emi = principal * (monthly_rate * (1 + monthly_rate) ** months) / ((1 + monthly_rate) ** months - 1)
#     return emi

# def create_downloadable_excel(data_dict, filename="financial_plan.xlsx"):
#     """Create downloadable Excel file"""
#     output = io.BytesIO()
#     wb = Workbook()
    
#     # Remove default sheet
#     wb.remove(wb.active)
    
#     for sheet_name, data in data_dict.items():
#         ws = wb.create_sheet(title=sheet_name)
        
#         # Add headers
#         if isinstance(data, pd.DataFrame):
#             for col_idx, col_name in enumerate(data.columns, 1):
#                 cell = ws.cell(row=1, column=col_idx, value=col_name)
#                 cell.font = Font(bold=True)
#                 cell.fill = PatternFill(start_color="366092", end_color="366092", fill_type="solid")
#                 cell.alignment = Alignment(horizontal="center")
            
#             # Add data
#             for row_idx, row in enumerate(data.itertuples(index=False), 2):
#                 for col_idx, value in enumerate(row, 1):
#                     ws.cell(row=row_idx, column=col_idx, value=value)
#         else:
#             # For dictionary data
#             row = 1
#             for key, value in data.items():
#                 ws.cell(row=row, column=1, value=key).font = Font(bold=True)
#                 ws.cell(row=row, column=2, value=value)
#                 row += 1
    
#     wb.save(output)
#     output.seek(0)
#     return output.getvalue()

# # Main app
# def main():
#     st.markdown('<h1 class="main-header">💰 Comprehensive Financial Planner</h1>', unsafe_allow_html=True)
    
#     # Sidebar for navigation
#     st.sidebar.title("🧭 Navigation")
#     planning_type = st.sidebar.selectbox(
#         "Select Planning Type",
#         ["Dashboard", "Investment Planning", "Retirement Planning", "Education Planning", 
#          "Loan Planning", "Budget Planning", "Tax Planning", "Emergency Fund Planning"]
#     )
    
#     # Initialize session state for data storage
#     if 'financial_data' not in st.session_state:
#         st.session_state.financial_data = {}
    
#     if planning_type == "Dashboard":
#         show_dashboard()
#     elif planning_type == "Investment Planning":
#         investment_planning()
#     elif planning_type == "Retirement Planning":
#         retirement_planning()
#     elif planning_type == "Education Planning":
#         education_planning()
#     elif planning_type == "Loan Planning":
#         loan_planning()
#     elif planning_type == "Budget Planning":
#         budget_planning()
#     elif planning_type == "Tax Planning":
#         tax_planning()
#     elif planning_type == "Emergency Fund Planning":
#         emergency_fund_planning()

# def show_dashboard():
#     st.header("📊 Financial Dashboard")
    
#     col1, col2, col3, col4 = st.columns(4)
    
#     with col1:
#         st.metric("Total Assets", "$0", "0%")
#     with col2:
#         st.metric("Total Liabilities", "$0", "0%")
#     with col3:
#         st.metric("Net Worth", "$0", "0%")
#     with col4:
#         st.metric("Monthly Savings", "$0", "0%")
    
#     # Sample portfolio chart
#     if st.button("Generate Sample Portfolio"):
#         portfolio_data = {
#             'Asset Class': ['Stocks', 'Bonds', 'Real Estate', 'Cash', 'Commodities'],
#             'Allocation': [40, 30, 20, 5, 5],
#             'Value': [40000, 30000, 20000, 5000, 5000]
#         }
#         df = pd.DataFrame(portfolio_data)
        
#         fig = px.pie(df, values='Value', names='Asset Class', title='Portfolio Allocation')
#         st.plotly_chart(fig, use_container_width=True)

# def investment_planning():
#     st.header("📈 Investment Planning")
    
#     col1, col2 = st.columns(2)
    
#     with col1:
#         st.subheader("Investment Parameters")
#         investment_type = st.selectbox("Investment Type", ["Lump Sum", "SIP (Monthly)", "Both"])
        
#         if investment_type in ["Lump Sum", "Both"]:
#             lump_sum = st.number_input("Lump Sum Amount ($)", min_value=0, value=10000)
#         else:
#             lump_sum = 0
            
#         if investment_type in ["SIP (Monthly)", "Both"]:
#             monthly_sip = st.number_input("Monthly SIP Amount ($)", min_value=0, value=500)
#         else:
#             monthly_sip = 0
        
#         expected_return = st.slider("Expected Annual Return (%)", min_value=1.0, max_value=30.0, value=12.0, step=0.1)
#         investment_period = st.slider("Investment Period (Years)", min_value=1, max_value=50, value=10)
        
#         if st.button("Calculate Investment Returns"):
#             # Calculate returns
#             lump_sum_future = calculate_compound_interest(lump_sum, expected_return/100, investment_period)
#             sip_future = calculate_sip_returns(monthly_sip, expected_return/100, investment_period)
            
#             total_investment = lump_sum + (monthly_sip * 12 * investment_period)
#             total_returns = lump_sum_future + sip_future
#             gains = total_returns - total_investment
            
#             # Store in session state
#             st.session_state.financial_data['investment'] = {
#                 'Total Investment': f"${total_investment:,.2f}",
#                 'Future Value': f"${total_returns:,.2f}",
#                 'Total Gains': f"${gains:,.2f}",
#                 'Return %': f"{((total_returns/total_investment - 1) * 100):.2f}%"
#             }
    
#     with col2:
#         st.subheader("Investment Results")
#         if 'investment' in st.session_state.financial_data:
#             data = st.session_state.financial_data['investment']
#             for key, value in data.items():
#                 st.metric(key, value)
            
#             # Create growth chart
#             years = list(range(investment_period + 1))
#             lump_sum_growth = [lump_sum * (1 + expected_return/100) ** year for year in years]
#             sip_growth = [calculate_sip_returns(monthly_sip, expected_return/100, year) if year > 0 else 0 for year in years]
#             total_growth = [ls + sip for ls, sip in zip(lump_sum_growth, sip_growth)]
            
#             df = pd.DataFrame({
#                 'Year': years,
#                 'Lump Sum Growth': lump_sum_growth,
#                 'SIP Growth': sip_growth,
#                 'Total Value': total_growth
#             })
            
#             fig = px.line(df, x='Year', y=['Lump Sum Growth', 'SIP Growth', 'Total Value'],
#                          title='Investment Growth Over Time')
#             st.plotly_chart(fig, use_container_width=True)

# def retirement_planning():
#     st.header("🏖️ Retirement Planning")
    
#     col1, col2 = st.columns(2)
    
#     with col1:
#         st.subheader("Retirement Parameters")
#         current_age = st.number_input("Current Age", min_value=18, max_value=100, value=30)
#         retirement_age = st.number_input("Retirement Age", min_value=current_age+1, max_value=100, value=60)
#         current_monthly_expenses = st.number_input("Current Monthly Expenses ($)", min_value=0, value=3000)
#         inflation_rate = st.slider("Inflation Rate (%)", min_value=1.0, max_value=10.0, value=6.0, step=0.1)
#         expected_return = st.slider("Expected Return on Investments (%)", min_value=1.0, max_value=20.0, value=10.0, step=0.1)
#         life_expectancy = st.number_input("Life Expectancy", min_value=retirement_age+1, max_value=120, value=80)
        
#         if st.button("Calculate Retirement Needs"):
#             years_to_retirement = retirement_age - current_age
#             retirement_years = life_expectancy - retirement_age
            
#             # Calculate future monthly expenses
#             future_monthly_expenses = current_monthly_expenses * (1 + inflation_rate/100) ** years_to_retirement
            
#             # Calculate retirement corpus needed
#             retirement_corpus = future_monthly_expenses * 12 * retirement_years / (1 + expected_return/100 - inflation_rate/100)
            
#             # Calculate monthly SIP required
#             monthly_return = expected_return / 12 / 100
#             months_to_retirement = years_to_retirement * 12
#             required_monthly_sip = retirement_corpus * monthly_return / ((1 + monthly_return) ** months_to_retirement - 1)
            
#             st.session_state.financial_data['retirement'] = {
#                 'Years to Retirement': years_to_retirement,
#                 'Future Monthly Expenses': f"${future_monthly_expenses:,.2f}",
#                 'Retirement Corpus Needed': f"${retirement_corpus:,.2f}",
#                 'Required Monthly SIP': f"${required_monthly_sip:,.2f}"
#             }
    
#     with col2:
#         st.subheader("Retirement Results")
#         if 'retirement' in st.session_state.financial_data:
#             data = st.session_state.financial_data['retirement']
#             for key, value in data.items():
#                 st.metric(key, value)
            
#             # Create retirement planning chart
#             years = list(range(current_age, life_expectancy + 1))
#             corpus_values = []
            
#             for year in years:
#                 if year <= retirement_age:
#                     # Accumulation phase
#                     years_invested = year - current_age
#                     if years_invested > 0:
#                         corpus = calculate_sip_returns(float(data['Required Monthly SIP'].replace('$', '').replace(',', '')), 
#                                                      expected_return/100, years_invested)
#                     else:
#                         corpus = 0
#                 else:
#                     # Withdrawal phase
#                     years_after_retirement = year - retirement_age
#                     corpus = float(data['Retirement Corpus Needed'].replace('$', '').replace(',', ''))
#                     corpus *= (1 - (inflation_rate - expected_return)/100) ** years_after_retirement
                
#                 corpus_values.append(corpus)
            
#             df = pd.DataFrame({
#                 'Age': years,
#                 'Corpus Value': corpus_values
#             })
            
#             fig = px.line(df, x='Age', y='Corpus Value', title='Retirement Corpus Over Time')
#             fig.add_vline(x=retirement_age, line_dash="dash", line_color="red", 
#                          annotation_text="Retirement Age")
#             st.plotly_chart(fig, use_container_width=True)

# def education_planning():
#     st.header("🎓 Education Planning")
    
#     col1, col2 = st.columns(2)
    
#     with col1:
#         st.subheader("Education Parameters")
#         child_age = st.number_input("Child's Current Age", min_value=0, max_value=25, value=5)
#         education_start_age = st.number_input("Education Start Age", min_value=child_age+1, max_value=30, value=18)
#         current_education_cost = st.number_input("Current Education Cost ($)", min_value=0, value=50000)
#         education_inflation = st.slider("Education Inflation Rate (%)", min_value=1.0, max_value=15.0, value=8.0, step=0.1)
#         expected_return = st.slider("Expected Return on Investment (%)", min_value=1.0, max_value=20.0, value=12.0, step=0.1)
        
#         if st.button("Calculate Education Fund"):
#             years_to_education = education_start_age - child_age
            
#             # Calculate future education cost
#             future_education_cost = current_education_cost * (1 + education_inflation/100) ** years_to_education
            
#             # Calculate monthly SIP required
#             monthly_return = expected_return / 12 / 100
#             months_to_education = years_to_education * 12
#             required_monthly_sip = future_education_cost * monthly_return / ((1 + monthly_return) ** months_to_education - 1)
            
#             st.session_state.financial_data['education'] = {
#                 'Years to Education': years_to_education,
#                 'Future Education Cost': f"${future_education_cost:,.2f}",
#                 'Required Monthly SIP': f"${required_monthly_sip:,.2f}",
#                 'Total Investment': f"${required_monthly_sip * months_to_education:,.2f}"
#             }
    
#     with col2:
#         st.subheader("Education Results")
#         if 'education' in st.session_state.financial_data:
#             data = st.session_state.financial_data['education']
#             for key, value in data.items():
#                 st.metric(key, value)

# def loan_planning():
#     st.header("🏠 Loan Planning")
    
#     col1, col2 = st.columns(2)
    
#     with col1:
#         st.subheader("Loan Parameters")
#         loan_amount = st.number_input("Loan Amount ($)", min_value=0, value=300000)
#         interest_rate = st.slider("Interest Rate (%)", min_value=1.0, max_value=30.0, value=8.5, step=0.1)
#         loan_tenure = st.slider("Loan Tenure (Years)", min_value=1, max_value=30, value=20)
        
#         if st.button("Calculate Loan Details"):
#             monthly_emi = calculate_loan_emi(loan_amount, interest_rate/100, loan_tenure)
#             total_payment = monthly_emi * loan_tenure * 12
#             total_interest = total_payment - loan_amount
            
#             st.session_state.financial_data['loan'] = {
#                 'Monthly EMI': f"${monthly_emi:,.2f}",
#                 'Total Payment': f"${total_payment:,.2f}",
#                 'Total Interest': f"${total_interest:,.2f}",
#                 'Interest %': f"{(total_interest/loan_amount * 100):.2f}%"
#             }
    
#     with col2:
#         st.subheader("Loan Results")
#         if 'loan' in st.session_state.financial_data:
#             data = st.session_state.financial_data['loan']
#             for key, value in data.items():
#                 st.metric(key, value)
            
#             # Create loan amortization chart
#             months = loan_tenure * 12
#             monthly_rate = interest_rate / 12 / 100
#             monthly_emi = float(data['Monthly EMI'].replace('$', '').replace(',', ''))
            
#             balance = loan_amount
#             principal_payments = []
#             interest_payments = []
#             balances = []
            
#             for month in range(1, months + 1):
#                 interest_payment = balance * monthly_rate
#                 principal_payment = monthly_emi - interest_payment
#                 balance -= principal_payment
                
#                 principal_payments.append(principal_payment)
#                 interest_payments.append(interest_payment)
#                 balances.append(max(0, balance))
            
#             df = pd.DataFrame({
#                 'Month': list(range(1, months + 1)),
#                 'Principal Payment': principal_payments,
#                 'Interest Payment': interest_payments,
#                 'Outstanding Balance': balances
#             })
            
#             fig = make_subplots(specs=[[{"secondary_y": True}]])
            
#             fig.add_trace(
#                 go.Scatter(x=df['Month'], y=df['Principal Payment'], name='Principal Payment'),
#                 secondary_y=False,
#             )
            
#             fig.add_trace(
#                 go.Scatter(x=df['Month'], y=df['Interest Payment'], name='Interest Payment'),
#                 secondary_y=False,
#             )
            
#             fig.add_trace(
#                 go.Scatter(x=df['Month'], y=df['Outstanding Balance'], name='Outstanding Balance'),
#                 secondary_y=True,
#             )
            
#             fig.update_layout(title_text="Loan Amortization Schedule")
#             fig.update_xaxes(title_text="Month")
#             fig.update_yaxes(title_text="Payment Amount ($)", secondary_y=False)
#             fig.update_yaxes(title_text="Outstanding Balance ($)", secondary_y=True)
            
#             st.plotly_chart(fig, use_container_width=True)

# def budget_planning():
#     st.header("📊 Budget Planning")
    
#     col1, col2 = st.columns(2)
    
#     with col1:
#         st.subheader("Income")
#         salary = st.number_input("Monthly Salary ($)", min_value=0, value=5000)
#         other_income = st.number_input("Other Monthly Income ($)", min_value=0, value=0)
#         total_income = salary + other_income
        
#         st.subheader("Expenses")
#         housing = st.number_input("Housing ($)", min_value=0, value=1500)
#         food = st.number_input("Food ($)", min_value=0, value=500)
#         transportation = st.number_input("Transportation ($)", min_value=0, value=300)
#         utilities = st.number_input("Utilities ($)", min_value=0, value=200)
#         entertainment = st.number_input("Entertainment ($)", min_value=0, value=300)
#         healthcare = st.number_input("Healthcare ($)", min_value=0, value=200)
#         other_expenses = st.number_input("Other Expenses ($)", min_value=0, value=200)
        
#         total_expenses = housing + food + transportation + utilities + entertainment + healthcare + other_expenses
        
#         if st.button("Analyze Budget"):
#             savings = total_income - total_expenses
#             savings_rate = (savings / total_income * 100) if total_income > 0 else 0
            
#             st.session_state.financial_data['budget'] = {
#                 'Total Income': f"${total_income:,.2f}",
#                 'Total Expenses': f"${total_expenses:,.2f}",
#                 'Monthly Savings': f"${savings:,.2f}",
#                 'Savings Rate': f"{savings_rate:.2f}%"
#             }
    
#     with col2:
#         st.subheader("Budget Analysis")
#         if 'budget' in st.session_state.financial_data:
#             data = st.session_state.financial_data['budget']
#             for key, value in data.items():
#                 st.metric(key, value)
            
#             # Create budget breakdown chart
#             expense_data = {
#                 'Category': ['Housing', 'Food', 'Transportation', 'Utilities', 'Entertainment', 'Healthcare', 'Other'],
#                 'Amount': [housing, food, transportation, utilities, entertainment, healthcare, other_expenses]
#             }
#             df = pd.DataFrame(expense_data)
            
#             fig = px.pie(df, values='Amount', names='Category', title='Expense Breakdown')
#             st.plotly_chart(fig, use_container_width=True)

# def tax_planning():
#     st.header("💼 Tax Planning")
    
#     col1, col2 = st.columns(2)
    
#     with col1:
#         st.subheader("Tax Information")
#         annual_income = st.number_input("Annual Income ($)", min_value=0, value=60000)
#         tax_bracket = st.selectbox("Tax Bracket (%)", [10, 15, 22, 24, 32, 35, 37])
        
#         # Tax-saving investments
#         st.subheader("Tax-Saving Investments")
#         retirement_contribution = st.number_input("401(k) Contribution ($)", min_value=0, value=6000)
#         ira_contribution = st.number_input("IRA Contribution ($)", min_value=0, value=6000)
#         hsa_contribution = st.number_input("HSA Contribution ($)", min_value=0, value=3000)
        
#         if st.button("Calculate Tax Savings"):
#             total_deductions = retirement_contribution + ira_contribution + hsa_contribution
#             taxable_income = annual_income - total_deductions
            
#             tax_without_planning = annual_income * tax_bracket / 100
#             tax_with_planning = taxable_income * tax_bracket / 100
#             tax_savings = tax_without_planning - tax_with_planning
            
#             st.session_state.financial_data['tax'] = {
#                 'Annual Income': f"${annual_income:,.2f}",
#                 'Total Deductions': f"${total_deductions:,.2f}",
#                 'Taxable Income': f"${taxable_income:,.2f}",
#                 'Tax Savings': f"${tax_savings:,.2f}"
#             }
    
#     with col2:
#         st.subheader("Tax Analysis")
#         if 'tax' in st.session_state.financial_data:
#             data = st.session_state.financial_data['tax']
#             for key, value in data.items():
#                 st.metric(key, value)

# def emergency_fund_planning():
#     st.header("🚨 Emergency Fund Planning")
    
#     col1, col2 = st.columns(2)
    
#     with col1:
#         st.subheader("Emergency Fund Parameters")
#         monthly_expenses = st.number_input("Monthly Expenses ($)", min_value=0, value=3000)
#         months_coverage = st.slider("Months of Coverage", min_value=3, max_value=12, value=6)
#         current_savings = st.number_input("Current Emergency Savings ($)", min_value=0, value=5000)
#         monthly_contribution = st.number_input("Monthly Contribution ($)", min_value=0, value=300)
        
#         if st.button("Calculate Emergency Fund"):
#             target_fund = monthly_expenses * months_coverage
#             shortfall = max(0, target_fund - current_savings)
            
#             if monthly_contribution > 0:
#                 months_to_target = shortfall / monthly_contribution
#             else:
#                 months_to_target = float('inf')
            
#             st.session_state.financial_data['emergency'] = {
#                 'Target Emergency Fund': f"${target_fund:,.2f}",
#                 'Current Savings': f"${current_savings:,.2f}",
#                 'Shortfall': f"${shortfall:,.2f}",
#                 'Months to Target': f"{months_to_target:.1f}" if months_to_target != float('inf') else "∞"
#             }
    
#     with col2:
#         st.subheader("Emergency Fund Results")
#         if 'emergency' in st.session_state.financial_data:
#             data = st.session_state.financial_data['emergency']
#             for key, value in data.items():
#                 st.metric(key, value)

# # Download functionality
# st.sidebar.markdown("---")
# st.sidebar.subheader("📥 Download Reports")

# if st.sidebar.button("Download Excel Report"):
#     if st.session_state.financial_data:
#         excel_data = create_downloadable_excel(st.session_state.financial_data)
#         st.sidebar.download_button(
#             label="📊 Download Excel File",
#             data=excel_data,
#             file_name=f"financial_plan_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx",
#             mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
#         )
#     else:
#         st.sidebar.warning("No data available to download. Please run some calculations first.")













# import streamlit as st
# import pandas as pd
# import numpy as np
# import plotly.express as px
# import plotly.graph_objects as go
# from plotly.subplots import make_subplots
# from datetime import datetime, timedelta
# import io
# from openpyxl import Workbook
# from openpyxl.styles import Font, PatternFill, Alignment
# import base64

# # Page configuration
# st.set_page_config(
#     page_title="Financial Planner",
#     page_icon="💰",
#     layout="wide",
#     initial_sidebar_state="expanded"
# )

# # Custom CSS for better styling
# st.markdown("""
# <style>
#     .main-header { 
#         font-size: 2.5rem;
#         font-weight: bold;
#         color: white; /* Text color */
#         text-align: center;
#         margin-bottom: 2rem;
#     }
#     .metric-container {
#         background-color: #121212; /* Dark background */
#         padding: 1rem;
#         border-radius: 10px;
#         margin: 0.5rem 0;
#         color: white; /* Ensure text inside is white */
#     }
#     .stMetric {
#         background-color: #1e1e1e; /* Slightly lighter dark for contrast */
#         color: white; /* Text color */
#         padding: 1rem;
#         border-radius: 8px;
#         box-shadow: 0 2px 4px rgba(255,255,255,0.1); /* Soft light shadow */
#     }
# </style>
# """, unsafe_allow_html=True)

# # Helper functions
# def format_inr(amount):
#     """Format amount in Indian currency with lakh/crore"""
#     if amount >= 10000000:  # 1 crore
#         return f"₹{amount/10000000:.2f} Cr"
#     elif amount >= 100000:  # 1 lakh
#         return f"₹{amount/100000:.2f} L"
#     else:
#         return f"₹{amount:,.0f}"

# def calculate_compound_interest(principal, rate, time, compound_freq=12):
#     """Calculate compound interest"""
#     amount = principal * (1 + rate / compound_freq) ** (compound_freq * time)
#     return amount

# def calculate_sip_returns(monthly_investment, annual_rate, years):
#     """Calculate SIP returns"""
#     monthly_rate = annual_rate / 12
#     months = years * 12
#     future_value = monthly_investment * (((1 + monthly_rate) ** months - 1) / monthly_rate)
#     return future_value

# def calculate_loan_emi(principal, rate, tenure):
#     """Calculate EMI for loan"""
#     monthly_rate = rate / 12
#     months = tenure * 12
#     emi = principal * (monthly_rate * (1 + monthly_rate) ** months) / ((1 + monthly_rate) ** months - 1)
#     return emi

# def calculate_indian_tax(income, regime="old"):
#     """Calculate Indian income tax"""
#     if regime == "old":
#         # Old tax regime (with standard deduction of ₹50,000)
#         taxable_income = max(0, income - 50000)
#         if taxable_income <= 250000:
#             tax = 0
#         elif taxable_income <= 500000:
#             tax = (taxable_income - 250000) * 0.05
#         elif taxable_income <= 1000000:
#             tax = 12500 + (taxable_income - 500000) * 0.20
#         else:
#             tax = 112500 + (taxable_income - 1000000) * 0.30
#     else:
#         # New tax regime (FY 2023-24 onwards)
#         if income <= 300000:
#             tax = 0
#         elif income <= 600000:
#             tax = (income - 300000) * 0.05
#         elif income <= 900000:
#             tax = 15000 + (income - 600000) * 0.10
#         elif income <= 1200000:
#             tax = 45000 + (income - 900000) * 0.15
#         elif income <= 1500000:
#             tax = 90000 + (income - 1200000) * 0.20
#         else:
#             tax = 150000 + (income - 1500000) * 0.30
    
#     # Add 4% cess
#     tax_with_cess = tax * 1.04
#     return tax_with_cess

# def create_downloadable_excel(data_dict, filename="financial_plan.xlsx"):
#     """Create downloadable Excel file"""
#     output = io.BytesIO()
#     wb = Workbook()
    
#     # Remove default sheet
#     wb.remove(wb.active)
    
#     for sheet_name, data in data_dict.items():
#         ws = wb.create_sheet(title=sheet_name)
        
#         # Add headers
#         if isinstance(data, pd.DataFrame):
#             for col_idx, col_name in enumerate(data.columns, 1):
#                 cell = ws.cell(row=1, column=col_idx, value=col_name)
#                 cell.font = Font(bold=True)
#                 cell.fill = PatternFill(start_color="366092", end_color="366092", fill_type="solid")
#                 cell.alignment = Alignment(horizontal="center")
            
#             # Add data
#             for row_idx, row in enumerate(data.itertuples(index=False), 2):
#                 for col_idx, value in enumerate(row, 1):
#                     ws.cell(row=row_idx, column=col_idx, value=value)
#         else:
#             # For dictionary data
#             row = 1
#             for key, value in data.items():
#                 ws.cell(row=row, column=1, value=key).font = Font(bold=True)
#                 ws.cell(row=row, column=2, value=value)
#                 row += 1
    
#     wb.save(output)
#     output.seek(0)
#     return output.getvalue()

# # Main app
# def main():
#     st.markdown('<h1 class="main-header">💰 Comprehensive Financial Planner</h1>', unsafe_allow_html=True)
    
#     # Sidebar for navigation
#     st.sidebar.title("🧭 Navigation")
#     planning_type = st.sidebar.selectbox(
#         "Select Planning Type",
#         ["Dashboard", "Investment Planning", "Retirement Planning", "Education Planning", 
#          "Loan Planning", "Budget Planning", "Tax Planning", "Emergency Fund Planning"]
#     )
    
#     # Initialize session state for data storage
#     if 'financial_data' not in st.session_state:
#         st.session_state.financial_data = {}
    
#     if planning_type == "Dashboard":
#         show_dashboard()
#     elif planning_type == "Investment Planning":
#         investment_planning()
#     elif planning_type == "Retirement Planning":
#         retirement_planning()
#     elif planning_type == "Education Planning":
#         education_planning()
#     elif planning_type == "Loan Planning":
#         loan_planning()
#     elif planning_type == "Budget Planning":
#         budget_planning()
#     elif planning_type == "Tax Planning":
#         tax_planning()
#     elif planning_type == "Emergency Fund Planning":
#         emergency_fund_planning()

# def show_dashboard():
#     st.header("📊 Financial Dashboard")
    
#     col1, col2, col3, col4 = st.columns(4)
    
#     with col1:
#         st.metric("Total Assets", "₹0", "0%")
#     with col2:
#         st.metric("Total Liabilities", "₹0", "0%")
#     with col3:
#         st.metric("Net Worth", "₹0", "0%")
#     with col4:
#         st.metric("Monthly Savings", "₹0", "0%")
    
#     # Sample portfolio chart
#     if st.button("Generate Sample Portfolio"):
#         portfolio_data = {
#             'Asset Class': ['Equity MF', 'Debt MF', 'PPF/EPF', 'FD/RD', 'Gold', 'Real Estate'],
#             'Allocation': [35, 25, 15, 10, 5, 10],
#             'Value': [350000, 250000, 150000, 100000, 50000, 100000]
#         }
#         df = pd.DataFrame(portfolio_data)
#         df['Formatted_Value'] = df['Value'].apply(format_inr)
        
#         fig = px.pie(df, values='Value', names='Asset Class', 
#                     title='Portfolio Allocation',
#                     hover_data=['Formatted_Value'])
#         st.plotly_chart(fig, use_container_width=True)

# def investment_planning():
#     st.header("📈 Investment Planning")
    
#     col1, col2 = st.columns(2)
    
#     with col1:
#         st.subheader("Investment Parameters")
#         investment_type = st.selectbox("Investment Type", ["Lump Sum", "SIP (Monthly)", "Both"])
        
#         if investment_type in ["Lump Sum", "Both"]:
#             lump_sum = st.number_input("Lump Sum Amount (₹)", min_value=0, value=500000, step=50000)
#         else:
#             lump_sum = 0
            
#         if investment_type in ["SIP (Monthly)", "Both"]:
#             monthly_sip = st.number_input("Monthly SIP Amount (₹)", min_value=0, value=10000, step=1000)
#         else:
#             monthly_sip = 0
        
#         expected_return = st.slider("Expected Annual Return (%)", min_value=1.0, max_value=30.0, value=12.0, step=0.1)
#         investment_period = st.slider("Investment Period (Years)", min_value=1, max_value=50, value=10)
        
#         if st.button("Calculate Investment Returns"):
#             # Calculate returns
#             lump_sum_future = calculate_compound_interest(lump_sum, expected_return/100, investment_period)
#             sip_future = calculate_sip_returns(monthly_sip, expected_return/100, investment_period)
            
#             total_investment = lump_sum + (monthly_sip * 12 * investment_period)
#             total_returns = lump_sum_future + sip_future
#             gains = total_returns - total_investment
            
#             # Store in session state
#             st.session_state.financial_data['investment'] = {
#                 'Total Investment': format_inr(total_investment),
#                 'Future Value': format_inr(total_returns),
#                 'Total Gains': format_inr(gains),
#                 'Return %': f"{((total_returns/total_investment - 1) * 100):.2f}%"
#             }
    
#     with col2:
#         st.subheader("Investment Results")
#         if 'investment' in st.session_state.financial_data:
#             data = st.session_state.financial_data['investment']
#             for key, value in data.items():
#                 st.metric(key, value)
            
#             # Create growth chart
#             years = list(range(investment_period + 1))
#             lump_sum_growth = [lump_sum * (1 + expected_return/100) ** year for year in years]
#             sip_growth = [calculate_sip_returns(monthly_sip, expected_return/100, year) if year > 0 else 0 for year in years]
#             total_growth = [ls + sip for ls, sip in zip(lump_sum_growth, sip_growth)]
            
#             df = pd.DataFrame({
#                 'Year': years,
#                 'Lump Sum Growth': lump_sum_growth,
#                 'SIP Growth': sip_growth,
#                 'Total Value': total_growth
#             })
            
#             fig = px.line(df, x='Year', y=['Lump Sum Growth', 'SIP Growth', 'Total Value'],
#                          title='Investment Growth Over Time')
#             st.plotly_chart(fig, use_container_width=True)

# def retirement_planning():
#     st.header("🏖️ Retirement Planning")
    
#     col1, col2 = st.columns(2)
    
#     with col1:
#         st.subheader("Retirement Parameters")
#         current_age = st.number_input("Current Age", min_value=18, max_value=100, value=30)
#         retirement_age = st.number_input("Retirement Age", min_value=current_age+1, max_value=100, value=60)
#         current_monthly_expenses = st.number_input("Current Monthly Expenses (₹)", min_value=0, value=50000, step=5000)
#         inflation_rate = st.slider("Inflation Rate (%)", min_value=1.0, max_value=10.0, value=6.0, step=0.1)
#         expected_return = st.slider("Expected Return on Investments (%)", min_value=1.0, max_value=20.0, value=12.0, step=0.1)
#         life_expectancy = st.number_input("Life Expectancy", min_value=retirement_age+1, max_value=120, value=80)
        
#         if st.button("Calculate Retirement Needs"):
#             years_to_retirement = retirement_age - current_age
#             retirement_years = life_expectancy - retirement_age
            
#             # Calculate future monthly expenses
#             future_monthly_expenses = current_monthly_expenses * (1 + inflation_rate/100) ** years_to_retirement
            
#             # Calculate retirement corpus needed
#             retirement_corpus = future_monthly_expenses * 12 * retirement_years / (1 + expected_return/100 - inflation_rate/100)
            
#             # Calculate monthly SIP required
#             monthly_return = expected_return / 12 / 100
#             months_to_retirement = years_to_retirement * 12
#             required_monthly_sip = retirement_corpus * monthly_return / ((1 + monthly_return) ** months_to_retirement - 1)
            
#             st.session_state.financial_data['retirement'] = {
#                 'Years to Retirement': years_to_retirement,
#                 'Future Monthly Expenses': format_inr(future_monthly_expenses),
#                 'Retirement Corpus Needed': format_inr(retirement_corpus),
#                 'Required Monthly SIP': format_inr(required_monthly_sip)
#             }
    
#     with col2:
#         st.subheader("Retirement Results")
#         if 'retirement' in st.session_state.financial_data:
#             data = st.session_state.financial_data['retirement']
#             for key, value in data.items():
#                 st.metric(key, value)
            
#             # Create retirement planning chart
#             years = list(range(current_age, life_expectancy + 1))
#             corpus_values = []
            
#             for year in years:
#                 if year <= retirement_age:
#                     # Accumulation phase
#                     years_invested = year - current_age
#                     if years_invested > 0:
#                         corpus = calculate_sip_returns(float(data['Required Monthly SIP'].replace('₹', '').replace(' Cr', '').replace(' L', '').replace(',', '')) * (10000000 if 'Cr' in data['Required Monthly SIP'] else 100000 if 'L' in data['Required Monthly SIP'] else 1), 
#                                                      expected_return/100, years_invested)
#                     else:
#                         corpus = 0
#                 else:
#                     # Withdrawal phase
#                     years_after_retirement = year - retirement_age
#                     corpus_needed = float(data['Retirement Corpus Needed'].replace('₹', '').replace(' Cr', '').replace(' L', '').replace(',', '')) * (10000000 if 'Cr' in data['Retirement Corpus Needed'] else 100000 if 'L' in data['Retirement Corpus Needed'] else 1)
#                     corpus = corpus_needed * (1 - (inflation_rate - expected_return)/100) ** years_after_retirement
                
#                 corpus_values.append(corpus)
            
#             df = pd.DataFrame({
#                 'Age': years,
#                 'Corpus Value': corpus_values
#             })
            
#             fig = px.line(df, x='Age', y='Corpus Value', title='Retirement Corpus Over Time')
#             fig.add_vline(x=retirement_age, line_dash="dash", line_color="red", 
#                          annotation_text="Retirement Age")
#             st.plotly_chart(fig, use_container_width=True)

# def education_planning():
#     st.header("🎓 Education Planning")
    
#     col1, col2 = st.columns(2)
    
#     with col1:
#         st.subheader("Education Parameters")
#         child_age = st.number_input("Child's Current Age", min_value=0, max_value=25, value=5)
#         education_start_age = st.number_input("Education Start Age", min_value=child_age+1, max_value=30, value=18)
#         current_education_cost = st.number_input("Current Education Cost (₹)", min_value=0, value=1000000, step=100000)
#         education_inflation = st.slider("Education Inflation Rate (%)", min_value=1.0, max_value=15.0, value=10.0, step=0.1)
#         expected_return = st.slider("Expected Return on Investment (%)", min_value=1.0, max_value=20.0, value=12.0, step=0.1)
        
#         if st.button("Calculate Education Fund"):
#             years_to_education = education_start_age - child_age
            
#             # Calculate future education cost
#             future_education_cost = current_education_cost * (1 + education_inflation/100) ** years_to_education
            
#             # Calculate monthly SIP required
#             monthly_return = expected_return / 12 / 100
#             months_to_education = years_to_education * 12
#             required_monthly_sip = future_education_cost * monthly_return / ((1 + monthly_return) ** months_to_education - 1)
            
#             st.session_state.financial_data['education'] = {
#                 'Years to Education': years_to_education,
#                 'Future Education Cost': format_inr(future_education_cost),
#                 'Required Monthly SIP': format_inr(required_monthly_sip),
#                 'Total Investment': format_inr(required_monthly_sip * months_to_education)
#             }
    
#     with col2:
#         st.subheader("Education Results")
#         if 'education' in st.session_state.financial_data:
#             data = st.session_state.financial_data['education']
#             for key, value in data.items():
#                 st.metric(key, value)

# def loan_planning():
#     st.header("🏠 Loan Planning")
    
#     col1, col2 = st.columns(2)
    
#     with col1:
#         st.subheader("Loan Parameters")
#         loan_type = st.selectbox("Loan Type", ["Home Loan", "Personal Loan", "Car Loan", "Education Loan"])
#         loan_amount = st.number_input("Loan Amount (₹)", min_value=0, value=5000000, step=100000)
        
#         # Set default interest rates based on loan type
#         if loan_type == "Home Loan":
#             default_rate = 8.5
#         elif loan_type == "Personal Loan":
#             default_rate = 12.0
#         elif loan_type == "Car Loan":
#             default_rate = 9.0
#         else:  # Education Loan
#             default_rate = 10.5
            
#         interest_rate = st.slider("Interest Rate (%)", min_value=1.0, max_value=30.0, value=default_rate, step=0.1)
#         loan_tenure = st.slider("Loan Tenure (Years)", min_value=1, max_value=30, value=20)
        
#         if st.button("Calculate Loan Details"):
#             monthly_emi = calculate_loan_emi(loan_amount, interest_rate/100, loan_tenure)
#             total_payment = monthly_emi * loan_tenure * 12
#             total_interest = total_payment - loan_amount
            
#             st.session_state.financial_data['loan'] = {
#                 'Monthly EMI': format_inr(monthly_emi),
#                 'Total Payment': format_inr(total_payment),
#                 'Total Interest': format_inr(total_interest),
#                 'Interest %': f"{(total_interest/loan_amount * 100):.2f}%"
#             }
    
#     with col2:
#         st.subheader("Loan Results")
#         if 'loan' in st.session_state.financial_data:
#             data = st.session_state.financial_data['loan']
#             for key, value in data.items():
#                 st.metric(key, value)
            
#             # Create loan amortization chart
#             months = loan_tenure * 12
#             monthly_rate = interest_rate / 12 / 100
            
#             # Extract numeric value from formatted EMI
#             emi_str = data['Monthly EMI'].replace('₹', '').replace(' Cr', '').replace(' L', '').replace(',', '')
#             monthly_emi = float(emi_str) * (10000000 if 'Cr' in data['Monthly EMI'] else 100000 if 'L' in data['Monthly EMI'] else 1)
            
#             balance = loan_amount
#             principal_payments = []
#             interest_payments = []
#             balances = []
            
#             for month in range(1, months + 1):
#                 interest_payment = balance * monthly_rate
#                 principal_payment = monthly_emi - interest_payment
#                 balance -= principal_payment
                
#                 principal_payments.append(principal_payment)
#                 interest_payments.append(interest_payment)
#                 balances.append(max(0, balance))
            
#             df = pd.DataFrame({
#                 'Month': list(range(1, months + 1)),
#                 'Principal Payment': principal_payments,
#                 'Interest Payment': interest_payments,
#                 'Outstanding Balance': balances
#             })
            
#             fig = make_subplots(specs=[[{"secondary_y": True}]])
            
#             fig.add_trace(
#                 go.Scatter(x=df['Month'], y=df['Principal Payment'], name='Principal Payment'),
#                 secondary_y=False,
#             )
            
#             fig.add_trace(
#                 go.Scatter(x=df['Month'], y=df['Interest Payment'], name='Interest Payment'),
#                 secondary_y=False,
#             )
            
#             fig.add_trace(
#                 go.Scatter(x=df['Month'], y=df['Outstanding Balance'], name='Outstanding Balance'),
#                 secondary_y=True,
#             )
            
#             fig.update_layout(title_text="Loan Amortization Schedule")
#             fig.update_xaxes(title_text="Month")
#             fig.update_yaxes(title_text="Payment Amount (₹)", secondary_y=False)
#             fig.update_yaxes(title_text="Outstanding Balance (₹)", secondary_y=True)
            
#             st.plotly_chart(fig, use_container_width=True)principal_payment)
#                 interest_payments.append(interest_payment)
#                 balances.append(max(0, balance))
            
#             df = pd.DataFrame({
#                 'Month': list(range(1, months + 1)),
#                 'Principal Payment': principal_payments,
#                 'Interest Payment': interest_payments,
#                 'Outstanding Balance': balances
#             })
            
#             fig = make_subplots(specs=[[{"secondary_y": True}]])
            
#             fig.add_trace(
#                 go.Scatter(x=df['Month'], y=df['Principal Payment'], name='Principal Payment'),
#                 secondary_y=False,
#             )
            
#             fig.add_trace(
#                 go.Scatter(x=df['Month'], y=df['Interest Payment'], name='Interest Payment'),
#                 secondary_y=False,
#             )
            
#             fig.add_trace(
#                 go.Scatter(x=df['Month'], y=df['Outstanding Balance'], name='Outstanding Balance'),
#                 secondary_y=True,
#             )
            
#             fig.update_layout(title_text="Loan Amortization Schedule")
#             fig.update_xaxes(title_text="Month")
#             fig.update_yaxes(title_text="Payment Amount ($)", secondary_y=False)
#             fig.update_yaxes(title_text="Outstanding Balance ($)", secondary_y=True)
            
#             st.plotly_chart(fig, use_container_width=True)

# def budget_planning():
#     st.header("📊 Budget Planning")
    
#     col1, col2 = st.columns(2)
    
#     with col1:
#         st.subheader("Income")
#         salary = st.number_input("Monthly Salary ($)", min_value=0, value=5000)
#         other_income = st.number_input("Other Monthly Income ($)", min_value=0, value=0)
#         total_income = salary + other_income
        
#         st.subheader("Expenses")
#         housing = st.number_input("Housing ($)", min_value=0, value=1500)
#         food = st.number_input("Food ($)", min_value=0, value=500)
#         transportation = st.number_input("Transportation ($)", min_value=0, value=300)
#         utilities = st.number_input("Utilities ($)", min_value=0, value=200)
#         entertainment = st.number_input("Entertainment ($)", min_value=0, value=300)
#         healthcare = st.number_input("Healthcare ($)", min_value=0, value=200)
#         other_expenses = st.number_input("Other Expenses ($)", min_value=0, value=200)
        
#         total_expenses = housing + food + transportation + utilities + entertainment + healthcare + other_expenses
        
#         if st.button("Analyze Budget"):
#             savings = total_income - total_expenses
#             savings_rate = (savings / total_income * 100) if total_income > 0 else 0
            
#             st.session_state.financial_data['budget'] = {
#                 'Total Income': f"${total_income:,.2f}",
#                 'Total Expenses': f"${total_expenses:,.2f}",
#                 'Monthly Savings': f"${savings:,.2f}",
#                 'Savings Rate': f"{savings_rate:.2f}%"
#             }
    
#     with col2:
#         st.subheader("Budget Analysis")
#         if 'budget' in st.session_state.financial_data:
#             data = st.session_state.financial_data['budget']
#             for key, value in data.items():
#                 st.metric(key, value)
            
#             # Create budget breakdown chart
#             expense_data = {
#                 'Category': ['Housing', 'Food', 'Transportation', 'Utilities', 'Entertainment', 'Healthcare', 'Other'],
#                 'Amount': [housing, food, transportation, utilities, entertainment, healthcare, other_expenses]
#             }
#             df = pd.DataFrame(expense_data)
            
#             fig = px.pie(df, values='Amount', names='Category', title='Expense Breakdown')
#             st.plotly_chart(fig, use_container_width=True)

# def tax_planning():
#     st.header("💼 Tax Planning")
    
#     col1, col2 = st.columns(2)
    
#     with col1:
#         st.subheader("Tax Information")
#         annual_income = st.number_input("Annual Income ($)", min_value=0, value=60000)
#         tax_bracket = st.selectbox("Tax Bracket (%)", [10, 15, 22, 24, 32, 35, 37])
        
#         # Tax-saving investments
#         st.subheader("Tax-Saving Investments")
#         retirement_contribution = st.number_input("401(k) Contribution ($)", min_value=0, value=6000)
#         ira_contribution = st.number_input("IRA Contribution ($)", min_value=0, value=6000)
#         hsa_contribution = st.number_input("HSA Contribution ($)", min_value=0, value=3000)
        
#         if st.button("Calculate Tax Savings"):
#             total_deductions = retirement_contribution + ira_contribution + hsa_contribution
#             taxable_income = annual_income - total_deductions
            
#             tax_without_planning = annual_income * tax_bracket / 100
#             tax_with_planning = taxable_income * tax_bracket / 100
#             tax_savings = tax_without_planning - tax_with_planning
            
#             st.session_state.financial_data['tax'] = {
#                 'Annual Income': f"${annual_income:,.2f}",
#                 'Total Deductions': f"${total_deductions:,.2f}",
#                 'Taxable Income': f"${taxable_income:,.2f}",
#                 'Tax Savings': f"${tax_savings:,.2f}"
#             }
    
#     with col2:
#         st.subheader("Tax Analysis")
#         if 'tax' in st.session_state.financial_data:
#             data = st.session_state.financial_data['tax']
#             for key, value in data.items():
#                 st.metric(key, value)

# def emergency_fund_planning():
#     st.header("🚨 Emergency Fund Planning")
    
#     col1, col2 = st.columns(2)
    
#     with col1:
#         st.subheader("Emergency Fund Parameters")
#         monthly_expenses = st.number_input("Monthly Expenses ($)", min_value=0, value=3000)
#         months_coverage = st.slider("Months of Coverage", min_value=3, max_value=12, value=6)
#         current_savings = st.number_input("Current Emergency Savings ($)", min_value=0, value=5000)
#         monthly_contribution = st.number_input("Monthly Contribution ($)", min_value=0, value=300)
        
#         if st.button("Calculate Emergency Fund"):
#             target_fund = monthly_expenses * months_coverage
#             shortfall = max(0, target_fund - current_savings)
            
#             if monthly_contribution > 0:
#                 months_to_target = shortfall / monthly_contribution
#             else:
#                 months_to_target = float('inf')
            
#             st.session_state.financial_data['emergency'] = {
#                 'Target Emergency Fund': f"${target_fund:,.2f}",
#                 'Current Savings': f"${current_savings:,.2f}",
#                 'Shortfall': f"${shortfall:,.2f}",
#                 'Months to Target': f"{months_to_target:.1f}" if months_to_target != float('inf') else "∞"
#             }
    
#     with col2:
#         st.subheader("Emergency Fund Results")
#         if 'emergency' in st.session_state.financial_data:
#             data = st.session_state.financial_data['emergency']
#             for key, value in data.items():
#                 st.metric(key, value)

# # Download functionality
# st.sidebar.markdown("---")
# st.sidebar.subheader("📥 Download Reports")

# if st.sidebar.button("Download Excel Report"):
#     if st.session_state.financial_data:
#         excel_data = create_downloadable_excel(st.session_state.financial_data)
#         st.sidebar.download_button(
#             label="📊 Download Excel File",
#             data=excel_data,
#             file_name=f"financial_plan_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx",
#             mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
#         )
#     else:
#         st.sidebar.warning("No data available to download. Please run some calculations first.")

# if __name__ == "__main__":
#     main()


















# if __name__ == "__main__":
#     main()











