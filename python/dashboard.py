import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Digital Banking Dashboard")

# загрузка данных
df_transactions = pd.read_csv("df/transactions.csv")
df_cards = pd.read_csv("df/cards.csv")

df_transactions['transaction_date'] = pd.to_datetime(df_transactions['transaction_date'])

# SIDEBAR
st.sidebar.header("Filters")

# фильтр даты
start_date = st.sidebar.date_input(
    "Start date",
    df_transactions['transaction_date'].min()
)

end_date = st.sidebar.date_input(
    "End date",
    df_transactions['transaction_date'].max()
)


# фильтр банков
banks = st.sidebar.multiselect(
    "Select banks",
    df_cards['bank_name'].unique(),
    default=df_cards['bank_name'].unique()
)

# фильтрация данных
filtered_tx = df_transactions[
    (df_transactions['transaction_date'] >= pd.to_datetime(start_date)) &
    (df_transactions['transaction_date'] <= pd.to_datetime(end_date))
]

filtered_cards = df_cards[df_cards['bank_name'].isin(banks)]

st.write("Filtered transactions:", len(filtered_tx))

# KPI метрики
col1, col2, col3 = st.columns(3)

col1.metric("Transactions", len(filtered_tx))
col2.metric("Total Volume", round(filtered_tx['amount'].sum(), 2))
col3.metric("Total Fees", round(filtered_tx['fee_amount'].sum(), 2))

# график транзакций
tx_type = (
    filtered_tx
    .groupby('transaction_type')
    .size()
    .reset_index(name='count')
)

fig = px.bar(
    tx_type,
    x='transaction_type',
    y='count',
    title="Transactions by Type"
)

st.plotly_chart(fig)

# график комиссий
fees = (
    filtered_tx
    .groupby('route_type')['fee_amount']
    .sum()
    .reset_index()
)

fig2 = px.bar(
    fees,
    x='route_type',
    y='fee_amount',
    title="Fees by Route"
)

st.plotly_chart(fig2)

