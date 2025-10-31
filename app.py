"""
Manufacturer Finder - Professional Web Application
Corporate-friendly interface for finding credible manufacturers
"""

import streamlit as st
import pandas as pd
import os
import sys
from datetime import datetime
import logging
from manufacturer_finder import ManufacturerFinder
from excel_exporter import ExcelExporter

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Page configuration
st.set_page_config(
    page_title="Manufacturer Credibility Analyzer | DynaPrice",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Professional Corporate CSS
st.markdown("""
<style>
    /* Global Styles */
    .main {
        background-color: #f8f9fa;
    }
    
    /* Header Styles */
    .corporate-header {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
        padding: 2rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    
    .corporate-header h1 {
        font-size: 2.5rem;
        font-weight: 700;
        margin: 0;
        color: white;
    }
    
    .corporate-header p {
        font-size: 1.1rem;
        margin-top: 0.5rem;
        opacity: 0.95;
        color: #e8f4f8;
    }
    
    /* Card Styles */
    .info-card {
        background: white;
        padding: 1.5rem;
        border-radius: 8px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.08);
        margin: 1rem 0;
        border-left: 4px solid #2a5298;
    }
    
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 8px;
        color: white;
        text-align: center;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    
    .metric-value {
        font-size: 2.5rem;
        font-weight: 700;
        margin: 0.5rem 0;
    }
    
    .metric-label {
        font-size: 0.9rem;
        opacity: 0.9;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    
    /* Status Messages */
    .status-success {
        background-color: #d4edda;
        border-left: 4px solid #28a745;
        padding: 1rem;
        border-radius: 4px;
        margin: 1rem 0;
    }
    
    .status-warning {
        background-color: #fff3cd;
        border-left: 4px solid #ffc107;
        padding: 1rem;
        border-radius: 4px;
        margin: 1rem 0;
    }
    
    .status-info {
        background-color: #d1ecf1;
        border-left: 4px solid #17a2b8;
        padding: 1rem;
        border-radius: 4px;
        margin: 1rem 0;
    }
    
    /* Button Styles */
    .stButton>button {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
        color: white;
        border: none;
        padding: 0.75rem 2rem;
        font-weight: 600;
        border-radius: 6px;
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(30, 60, 114, 0.3);
    }
    
    /* Sidebar Styles */
    .sidebar .sidebar-content {
        background-color: #ffffff;
    }
    
    /* Data Table Styles */
    .dataframe {
        border: 1px solid #dee2e6;
        border-radius: 6px;
    }
    
    /* Progress Bar */
    .stProgress > div > div > div {
        background: linear-gradient(90deg, #1e3c72 0%, #2a5298 100%);
    }
    
    /* Footer */
    .footer {
        text-align: center;
        padding: 2rem;
        color: #6c757d;
        font-size: 0.9rem;
        margin-top: 3rem;
        border-top: 1px solid #dee2e6;
    }
</style>
""", unsafe_allow_html=True)

def main():
    """Main application function"""
    
    # Corporate Header
    st.markdown("""
    <div class="corporate-header">
        <h1>📊 Manufacturer Credibility Analyzer</h1>
        <p>AI-Powered Supply Chain Intelligence for Strategic Procurement</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Sidebar Configuration
    with st.sidebar:
        st.image("https://img.icons8.com/fluency/96/factory.png", width=80)
        st.markdown("### ⚙️ Configuration")
        
        # API Key Configuration
        st.markdown("---")
        api_key_source = st.radio(
            "API Key Source",
            ["Environment Variable", "Enter Manually"],
            help="Choose how to provide your OpenAI API key"
        )
        
        if api_key_source == "Enter Manually":
            api_key = st.text_input(
                "OpenAI API Key",
                type="password",
                help="Your OpenAI API key will not be stored"
            )
        else:
            api_key = os.getenv('OPENAI_API_KEY', '')
            if api_key:
                st.success("✓ API key loaded from environment")
            else:
                st.warning("⚠️ No API key in environment")
        
        st.markdown("---")
        
        # Analysis Settings
        st.markdown("### 📋 Analysis Settings")
        max_manufacturers = st.slider(
            "Manufacturers per Part",
            min_value=1,
            max_value=5,
            value=3,
            help="Number of manufacturer recommendations"
        )
        
        st.markdown("---")
        
        # Information Panel
        with st.expander("ℹ️ About This Tool"):
            st.markdown("""
            **Manufacturer Credibility Analyzer**
            
            This enterprise tool uses advanced AI to evaluate 
            and recommend credible manufacturers based on:
            
            - Industry reputation
            - Product quality standards
            - Supply chain reliability
            - Market presence
            
            *Powered by OpenAI GPT-4*
            """)
        
        with st.expander("📖 Data Requirements"):
            st.markdown("""
            **Excel File Format:**
            
            Your file should contain:
            - **MPN** (Manufacturing Part Number)
            - **Description** (Product details)
            - **Quantity** (Required amount)
            
            Column names are auto-detected.
            """)
        
        # Footer
        st.markdown("---")
        st.markdown("""
        <div style='text-align: center; color: #6c757d; font-size: 0.8rem;'>
            <p><strong>DynaPrice</strong><br>
            Manufacturing Intelligence<br>
            Version 1.0</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Main Content Area
    tab1, tab2, tab3 = st.tabs(["📤 Upload & Analyze", "📊 Results Dashboard", "📈 Analytics"])
    
    # TAB 1: Upload & Analyze
    with tab1:
        col1, col2 = st.columns([2, 1])
        
        with col1:
            st.markdown("### Upload Manufacturing Parts Data")
            st.markdown("Upload your Excel file containing manufacturing part information for AI-powered analysis.")
        
        with col2:
            st.markdown("### Quick Stats")
            if 'results_df' in st.session_state:
                st.metric("Parts Analyzed", len(st.session_state['results_df']))
        
        st.markdown("---")
        
        # File Upload Section
        uploaded_file = st.file_uploader(
            "Choose Excel File (.xlsx, .xls)",
            type=['xlsx', 'xls'],
            help="Upload an Excel file with MPN, Description, and Quantity columns"
        )
        
        if uploaded_file is not None:
            try:
                # Save uploaded file temporarily
                temp_path = f"temp_upload_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
                with open(temp_path, 'wb') as f:
                    f.write(uploaded_file.getbuffer())
                
                # Load and preview data
                df = pd.read_excel(temp_path)
                
                # Clean column names
                df = df.rename(columns={
                    'Oracle MPN': 'MPN',
                    'description': 'Model_Description',
                    'Qty On Hand': 'Quantity'
                })
                
                # Handle missing columns
                if 'MPN' not in df.columns:
                    possible_mpn_cols = [col for col in df.columns if 'mpn' in col.lower() or 'part' in col.lower()]
                    if possible_mpn_cols:
                        df['MPN'] = df[possible_mpn_cols[0]]
                
                if 'Model_Description' not in df.columns:
                    possible_desc_cols = [col for col in df.columns if 'desc' in col.lower() or 'model' in col.lower()]
                    if possible_desc_cols:
                        df['Model_Description'] = df[possible_desc_cols[0]]
                
                if 'Quantity' not in df.columns:
                    possible_qty_cols = [col for col in df.columns if 'qty' in col.lower() or 'quant' in col.lower()]
                    if possible_qty_cols:
                        df['Quantity'] = df[possible_qty_cols[0]]
                    else:
                        df['Quantity'] = 1
                
                # Filter required columns
                df = df[['MPN', 'Model_Description', 'Quantity']].copy()
                df = df.dropna(subset=['MPN', 'Model_Description'])
                df['Quantity'] = df['Quantity'].fillna(1).astype(int)
                df.insert(0, 'ID', range(1, len(df) + 1))
                
                # Display success message
                st.markdown(f"""
                <div class="status-success">
                    ✓ <strong>File loaded successfully!</strong><br>
                    Found {len(df)} valid parts ready for analysis
                </div>
                """, unsafe_allow_html=True)
                
                # Data Preview
                st.markdown("### 📋 Data Preview")
                st.dataframe(df.head(10), use_container_width=True, height=300)
                
                if len(df) > 10:
                    st.info(f"Showing first 10 of {len(df)} parts")
                
                st.markdown("---")
                
                # Analysis Controls
                col1, col2, col3 = st.columns([1, 2, 1])
                
                with col2:
                    analyze_button = st.button(
                        "🚀 Start AI Analysis",
                        use_container_width=True,
                        type="primary"
                    )
                
                if analyze_button:
                    if not api_key:
                        st.error("⚠️ Please provide an OpenAI API key in the sidebar")
                    else:
                        # Run analysis
                        st.markdown("### 🔍 Analysis in Progress")
                        
                        with st.spinner("Initializing AI analysis engine..."):
                            try:
                                finder = ManufacturerFinder(api_key=api_key)
                                
                                # Progress tracking
                                progress_bar = st.progress(0)
                                status_text = st.empty()
                                results_container = st.container()
                                
                                # Process items
                                results = []
                                for idx, row in df.iterrows():
                                    progress = (idx + 1) / len(df)
                                    progress_bar.progress(progress)
                                    status_text.markdown(f"""
                                    <div class="status-info">
                                        Processing {idx + 1}/{len(df)}: <strong>{row['MPN']}</strong>
                                    </div>
                                    """, unsafe_allow_html=True)
                                    
                                    try:
                                        manufacturer_info = finder._query_manufacturers(
                                            mpn=row['MPN'],
                                            description=row['Model_Description'],
                                            quantity=row['Quantity'],
                                            max_results=max_manufacturers
                                        )
                                        
                                        result_row = row.to_dict()
                                        result_row.update(manufacturer_info)
                                        results.append(result_row)
                                        
                                    except Exception as e:
                                        logger.error(f"Error processing {row['MPN']}: {str(e)}")
                                        result_row = row.to_dict()
                                        result_row.update({
                                            'Top_Manufacturer': 'Analysis Error',
                                            'All_Manufacturers': '',
                                            'Avg_Credibility_Score': 0,
                                            'Recommendation': f'Error: {str(e)}',
                                            'Detailed_Analysis': '',
                                            'Additional_Info': ''
                                        })
                                        results.append(result_row)
                                
                                results_df = pd.DataFrame(results)
                                
                                # Clear progress indicators
                                progress_bar.empty()
                                status_text.empty()
                                
                                # Store results in session state
                                st.session_state['results_df'] = results_df
                                st.session_state['analysis_complete'] = True
                                st.session_state['analysis_timestamp'] = datetime.now()
                                
                                # Export to Excel
                                output_path = f"manufacturer_analysis_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
                                exporter = ExcelExporter(output_path=output_path)
                                output_file = exporter.create_summary_sheet(results_df)
                                st.session_state['output_file'] = output_file
                                
                                # Success message
                                st.markdown("""
                                <div class="status-success">
                                    ✅ <strong>Analysis Completed Successfully!</strong><br>
                                    All parts have been analyzed and results are ready for review.
                                </div>
                                """, unsafe_allow_html=True)
                                
                                # Display summary metrics
                                st.markdown("### 📊 Analysis Summary")
                                
                                col1, col2, col3, col4 = st.columns(4)
                                
                                with col1:
                                    st.markdown("""
                                    <div class="metric-card">
                                        <div class="metric-label">Total Parts</div>
                                        <div class="metric-value">{}</div>
                                    </div>
                                    """.format(len(results_df)), unsafe_allow_html=True)
                                
                                with col2:
                                    avg_score = results_df['Avg_Credibility_Score'].mean()
                                    st.markdown("""
                                    <div class="metric-card">
                                        <div class="metric-label">Avg Score</div>
                                        <div class="metric-value">{:.1f}</div>
                                    </div>
                                    """.format(avg_score), unsafe_allow_html=True)
                                
                                with col3:
                                    high_cred = len(results_df[results_df['Avg_Credibility_Score'] >= 80])
                                    st.markdown("""
                                    <div class="metric-card">
                                        <div class="metric-label">High Quality</div>
                                        <div class="metric-value">{}</div>
                                    </div>
                                    """.format(high_cred), unsafe_allow_html=True)
                                
                                with col4:
                                    low_cred = len(results_df[results_df['Avg_Credibility_Score'] < 60])
                                    st.markdown("""
                                    <div class="metric-card">
                                        <div class="metric-label">Need Review</div>
                                        <div class="metric-value">{}</div>
                                    </div>
                                    """.format(low_cred), unsafe_allow_html=True)
                                
                                st.markdown("---")
                                
                                # Download button
                                with open(output_file, 'rb') as f:
                                    st.download_button(
                                        label="📥 Download Complete Report (Excel)",
                                        data=f,
                                        file_name=os.path.basename(output_file),
                                        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                                        use_container_width=True
                                    )
                                
                                # Redirect to results tab
                                st.info("💡 Switch to the 'Results Dashboard' tab to explore detailed findings")
                                
                            except Exception as e:
                                st.error(f"❌ Error during analysis: {str(e)}")
                                logger.error(f"Analysis error: {str(e)}", exc_info=True)
                            
                            finally:
                                # Cleanup temp file
                                if os.path.exists(temp_path):
                                    os.remove(temp_path)
                
            except Exception as e:
                st.error(f"❌ Error loading file: {str(e)}")
                logger.error(f"File loading error: {str(e)}", exc_info=True)
    
    # TAB 2: Results Dashboard
    with tab2:
        if 'analysis_complete' in st.session_state and st.session_state['analysis_complete']:
            results_df = st.session_state['results_df']
            
            # Header with timestamp
            col1, col2 = st.columns([3, 1])
            with col1:
                st.markdown("### 📊 Analysis Results Dashboard")
            with col2:
                if 'analysis_timestamp' in st.session_state:
                    ts = st.session_state['analysis_timestamp']
                    st.caption(f"Analyzed: {ts.strftime('%Y-%m-%d %H:%M')}")
            
            st.markdown("---")
            
            # Summary Metrics
            col1, col2, col3, col4, col5 = st.columns(5)
            
            with col1:
                st.metric("Total Parts", len(results_df))
            
            with col2:
                avg_score = results_df['Avg_Credibility_Score'].mean()
                st.metric("Avg Credibility", f"{avg_score:.1f}/100")
            
            with col3:
                high_cred = len(results_df[results_df['Avg_Credibility_Score'] >= 80])
                st.metric("High Quality (≥80)", high_cred)
            
            with col4:
                medium_cred = len(results_df[(results_df['Avg_Credibility_Score'] >= 60) & 
                                             (results_df['Avg_Credibility_Score'] < 80)])
                st.metric("Medium (60-79)", medium_cred)
            
            with col5:
                low_cred = len(results_df[results_df['Avg_Credibility_Score'] < 60])
                st.metric("Need Review (<60)", low_cred)
            
            st.markdown("---")
            
            # Filters
            st.markdown("### 🔍 Filter Results")
            col1, col2 = st.columns(2)
            
            with col1:
                score_filter = st.selectbox(
                    "Filter by Credibility Score",
                    ["All Parts", "High Quality (≥80)", "Medium Quality (60-79)", "Low Quality (<60)"]
                )
            
            with col2:
                search_term = st.text_input("Search by MPN or Description", "")
            
            # Apply filters
            filtered_df = results_df.copy()
            
            if score_filter == "High Quality (≥80)":
                filtered_df = filtered_df[filtered_df['Avg_Credibility_Score'] >= 80]
            elif score_filter == "Medium Quality (60-79)":
                filtered_df = filtered_df[(filtered_df['Avg_Credibility_Score'] >= 60) & 
                                          (filtered_df['Avg_Credibility_Score'] < 80)]
            elif score_filter == "Low Quality (<60)":
                filtered_df = filtered_df[filtered_df['Avg_Credibility_Score'] < 60]
            
            if search_term:
                mask = filtered_df['MPN'].astype(str).str.contains(search_term, case=False) | \
                       filtered_df['Model_Description'].astype(str).str.contains(search_term, case=False)
                filtered_df = filtered_df[mask]
            
            st.markdown(f"### 📋 Results ({len(filtered_df)} parts)")
            
            # Display results
            display_cols = ['ID', 'MPN', 'Model_Description', 'Top_Manufacturer', 'Avg_Credibility_Score', 'Recommendation']
            display_df = filtered_df[display_cols].copy()
            display_df['Avg_Credibility_Score'] = display_df['Avg_Credibility_Score'].round(2)
            
            st.dataframe(
                display_df,
                use_container_width=True,
                height=500,
                column_config={
                    "ID": st.column_config.NumberColumn("ID", width="small"),
                    "MPN": st.column_config.TextColumn("MPN", width="medium"),
                    "Model_Description": st.column_config.TextColumn("Description", width="large"),
                    "Top_Manufacturer": st.column_config.TextColumn("Top Manufacturer", width="medium"),
                    "Avg_Credibility_Score": st.column_config.ProgressColumn(
                        "Score",
                        format="%.1f",
                        min_value=0,
                        max_value=100,
                        width="small"
                    ),
                    "Recommendation": st.column_config.TextColumn("Recommendation", width="large")
                }
            )
            
            # Download filtered results
            if 'output_file' in st.session_state:
                st.markdown("---")
                with open(st.session_state['output_file'], 'rb') as f:
                    st.download_button(
                        label="📥 Download Full Report (Excel)",
                        data=f,
                        file_name=os.path.basename(st.session_state['output_file']),
                        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                        use_container_width=True
                    )
        else:
            st.info("👈 Upload and analyze an Excel file in the 'Upload & Analyze' tab to see results here")
    
    # TAB 3: Analytics
    with tab3:
        if 'analysis_complete' in st.session_state and st.session_state['analysis_complete']:
            results_df = st.session_state['results_df']
            
            st.markdown("### 📈 Analytics & Insights")
            st.markdown("---")
            
            # Score distribution
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("#### Credibility Score Distribution")
                score_ranges = {
                    '90-100': len(results_df[results_df['Avg_Credibility_Score'] >= 90]),
                    '80-89': len(results_df[(results_df['Avg_Credibility_Score'] >= 80) & 
                                           (results_df['Avg_Credibility_Score'] < 90)]),
                    '70-79': len(results_df[(results_df['Avg_Credibility_Score'] >= 70) & 
                                           (results_df['Avg_Credibility_Score'] < 80)]),
                    '60-69': len(results_df[(results_df['Avg_Credibility_Score'] >= 60) & 
                                           (results_df['Avg_Credibility_Score'] < 70)]),
                    '<60': len(results_df[results_df['Avg_Credibility_Score'] < 60])
                }
                st.bar_chart(score_ranges)
            
            with col2:
                st.markdown("#### Top 10 Manufacturers by Frequency")
                # Extract all manufacturers
                all_manufacturers = []
                for mfrs in results_df['All_Manufacturers']:
                    all_manufacturers.extend([m.strip() for m in str(mfrs).split('|')])
                
                mfr_counts = pd.Series(all_manufacturers).value_counts().head(10)
                st.bar_chart(mfr_counts)
            
            st.markdown("---")
            
            # Key insights
            st.markdown("#### 🎯 Key Insights")
            
            col1, col2, col3 = st.columns(3)
            
            with col1:
                st.markdown("""
                <div class="info-card">
                    <h4>Highest Rated Part</h4>
                    <p><strong>Score:</strong> {:.1f}/100</p>
                    <p><strong>MPN:</strong> {}</p>
                </div>
                """.format(
                    results_df['Avg_Credibility_Score'].max(),
                    results_df.loc[results_df['Avg_Credibility_Score'].idxmax(), 'MPN']
                ), unsafe_allow_html=True)
            
            with col2:
                st.markdown("""
                <div class="info-card">
                    <h4>Most Common Manufacturer</h4>
                    <p><strong>{}</strong></p>
                    <p>Appears {} times</p>
                </div>
                """.format(
                    mfr_counts.index[0] if len(mfr_counts) > 0 else 'N/A',
                    mfr_counts.values[0] if len(mfr_counts) > 0 else 0
                ), unsafe_allow_html=True)
            
            with col3:
                st.markdown("""
                <div class="info-card">
                    <h4>Average Score</h4>
                    <p><strong>{:.1f}/100</strong></p>
                    <p>Across all parts</p>
                </div>
                """.format(results_df['Avg_Credibility_Score'].mean()), unsafe_allow_html=True)
        else:
            st.info("👈 Upload and analyze an Excel file to see analytics")
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div class="footer">
        <p><strong>Manufacturer Credibility Analyzer</strong> | Powered by OpenAI GPT-4</p>
        <p>DynaPrice © 2025 | Manufacturing Intelligence Solutions</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()
