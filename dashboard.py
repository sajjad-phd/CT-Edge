import streamlit as st
import plotly.graph_objects as go
from ct_reader import CTReader
import pandas as pd
import time
from datetime import datetime, timedelta

# Set page config
st.set_page_config(
    page_title="CT Monitor",
    page_icon="📊",
    layout="wide"
)

# Initialize session state
if 'reader' not in st.session_state:
    st.session_state.reader = CTReader()
    st.session_state.reader.start()

if 'data' not in st.session_state:
    st.session_state.data = {
        'timestamps': [],
        'voltages': []
    }

# Title
st.title("CT Monitor Dashboard")

# Create placeholder for the plot
plot_placeholder = st.empty()

# Create metrics
col1, col2, col3 = st.columns(3)
with col1:
    voltage_metric = st.empty()
with col2:
    sample_rate_metric = st.empty()
with col3:
    buffer_size_metric = st.empty()

# Main loop
while True:
    # Get new data
    new_data = st.session_state.reader.get_data()
    
    if new_data:
        # Update data
        st.session_state.data['timestamps'].extend(new_data['timestamps'])
        st.session_state.data['voltages'].extend(new_data['voltages'])
        
        # Keep only last 10000 points
        max_points = 10000
        if len(st.session_state.data['timestamps']) > max_points:
            st.session_state.data['timestamps'] = st.session_state.data['timestamps'][-max_points:]
            st.session_state.data['voltages'] = st.session_state.data['voltages'][-max_points:]
        
        # Create DataFrame
        df = pd.DataFrame({
            'timestamp': st.session_state.data['timestamps'],
            'voltage': st.session_state.data['voltages']
        })
        
        # Update metrics
        voltage_metric.metric("Latest Voltage", f"{df['voltage'].iloc[-1]:.3f} V")
        sample_rate_metric.metric("Sample Rate", f"{st.session_state.reader.sample_rate} Hz")
        buffer_size_metric.metric("Buffer Size", f"{st.session_state.reader.buffer_size}")
        
        # Create plot
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=df['timestamp'],
            y=df['voltage'],
            mode='lines',
            name='Voltage'
        ))
        
        fig.update_layout(
            title='Real-time CT Voltage',
            xaxis_title='Time',
            yaxis_title='Voltage (V)',
            height=600
        )
        
        # Update plot
        plot_placeholder.plotly_chart(fig, use_container_width=True)
    
    time.sleep(0.1)  # Small delay to prevent high CPU usage 