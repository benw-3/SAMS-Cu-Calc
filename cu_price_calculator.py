import streamlit as st

# Set the title and page configuration
st.set_page_config(page_title="Copper Price Calculator", layout="wide")

# Custom CSS for styling
st.markdown(
    """
    <style>
    .title {
        color: #FCE205; /* Yellow */
        font-size: 36px;
    }
    .header {
        color: #74417C; /* Purple */
        font-size: 24px;
    }
    .result {
        color: #74417C; /* Purple */
        font-size: 20px;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<h1 class="title">Copper Price Calculator</h1>', unsafe_allow_html=True)

# Input fields
lme_price = st.number_input("Enter LME Price (USD):", value=9538.00)
cu_percentage = st.selectbox("Select Copper Concentration (%):", [12, 13, 14, 15, 16, 17, 18, 19, 20])
moisture_percentage = st.number_input("Enter Moisture Percentage (%):", value=1.5)

# Calculate price
if st.button("Calculate Price"):
    unit_price = lme_price * (cu_percentage + 40) / 100 * (1 - moisture_percentage / 100)
    st.markdown(f'<h3 class="result">Price per WMT: USD {unit_price:.2f}</h3>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("Made with ❤️ for the Copper Market", unsafe_allow_html=True)
