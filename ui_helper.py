
import streamlit as st

def apply_custom_style():
    """
    Applies professional custom CSS to the Streamlit app.
    Features:
    - Increased Font Sizes for readability.
    - Bold Headings.
    - Healthcare gradient background.
    - Modern Card styling.
    - Special Summary Card styling.
    """
    st.markdown("""
        <style>
        /* Import Google Font - Outfit */
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@400;500;600;700&display=swap');

        html, body, [class*="css"] {
            font-family: 'Outfit', sans-serif;
            font-size: 18px; /* Increased Base Font Size */
        }
        
        /* Streamlit Input Labels */
        .stNumberInput label, .stSelectbox label, .stTextInput label {
            font_size: 1.1rem !important;
            font_weight: 600 !important;
        }

        /* 1. Main Background Gradient - Healthcare Theme */
        .stApp {
            background: linear-gradient(135deg, #e0f7fa 0%, #e8f5e9 100%);
        }

        /* 2. Headers - Bolder and Larger */
        h1 {
            font-size: 3rem !important;
            font-weight: 800 !important;
            color: #004d40;
            margin-bottom: 0.5rem;
        }
        
        h2 {
            font-size: 2.2rem !important;
            font-weight: 700 !important;
            color: #00695c;
            margin-top: 1.5rem;
        }
        
        h3 {
            font-size: 1.6rem !important;
            font-weight: 700 !important;
            color: #00796b;
        }
        
        h4 {
             font-size: 1.3rem !important;
             font-weight: 600 !important;
        }

        /* 3. Measurement Cards */
        .measurement-card {
            background-color: #ffffff;
            border-radius: 16px;
            padding: 24px; /* More padding */
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05);
            transition: transform 0.2s;
            text-align: center;
            border: 1px solid rgba(0,0,0,0.02);
            height: 100%;
        }
        
        .measurement-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 30px rgba(0, 0, 0, 0.08);
        }

        .measurement-label {
            font-size: 1rem;
            text-transform: uppercase;
            letter-spacing: 1.2px;
            color: #7f8c8d;
            font-weight: 600;
            margin-bottom: 15px;
        }

        .measurement-value {
            font-size: 2.8rem; /* Larger Value */
            font-weight: 800;
            margin-bottom: 8px;
        }
        
        .measurement-status {
            font-size: 1rem;
            font-weight: 700;
            padding: 6px 16px;
            border-radius: 30px;
            display: inline-block;
        }
        
        /* 4. Summary Card - Special Highlight */
        .summary-card {
            background: linear-gradient(135deg, #ffffff 0%, #f9fbfd 100%);
            border: 2px solid #e0e0e0;
            border-radius: 20px;
            padding: 40px;
            text-align: center;
            box-shadow: 0 10px 40px rgba(0,0,0,0.08);
            margin-top: 30px;
            margin-bottom: 40px;
        }
        
        .summary-title {
            font-size: 1.8rem;
            font-weight: 800;
            color: #2c3e50;
            margin-bottom: 20px;
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        
        .summary-risk {
            font-size: 4.5rem;
            font-weight: 900;
            line-height: 1.1;
        }
        
        .summary-subtitle {
            font-size: 1.5rem;
            color: #555;
            margin-top: 15px;
        }

        /* Status Colors */
        .status-green { color: #2ecc71; background-color: #e8f8f5; }
        .status-blue { color: #3498db; background-color: #eaf2f8; }
        .status-orange { color: #f39c12; background-color: #fef5e7; }
        .status-red { color: #c0392b; background-color: #fceceb; } /* Darker red */
        .status-yellow { color: #f1c40f; background-color: #fcf9e7; }
        
        /* Buttons */
        .stButton>button {
            background: linear-gradient(90deg, #00b09b 0%, #96c93d 100%);
            color: white;
            border: none;
            padding: 16px 32px; /* Bigger button */
            font-size: 1.2rem;
            border-radius: 40px;
            width: 100%;
            font-weight: 700;
            box-shadow: 0 4px 15px rgba(0,0,0,0.1);
            margin-top: 20px;
        }
        
        .stButton>button:hover {
            box-shadow: 0 6px 20px rgba(0,0,0,0.2);
            transform: scale(1.02);
        }
        
        /* Disclaimer */
        .medical-disclaimer {
            font-size: 0.9rem;
            color: #95a5a6;
            text-align: center;
            margin-top: 50px;
            padding: 20px;
            border-top: 1px solid #eee;
            font-style: italic;
        }

        </style>
    """, unsafe_allow_html=True)

def card_component(label, value, status, status_color="green", sub_text=""):
    """
    Renders a clean modern card.
    """
    color_map = {
        "green": "#2ecc71",
        "blue": "#3498db",
        "orange": "#f39c12",
        "red": "#c0392b",
        "yellow": "#f1c40f"
    }
    
    text_color = color_map.get(status_color, "#2c3e50")
    bg_class = f"status-{status_color}"
    
    html = f"""
    <div class="measurement-card">
        <div class="measurement-label">{label}</div>
        <div class="measurement-value" style="color: {text_color}">{value}</div>
        <div class="measurement-status {bg_class}">{status}</div>
        <div style="font-size: 0.95rem; color: #7f8c8d; margin-top: 10px; font-weight: 500;">{sub_text}</div>
    </div>
    """
    st.markdown(html, unsafe_allow_html=True)
