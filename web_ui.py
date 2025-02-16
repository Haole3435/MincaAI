import streamlit as st
from agent.agent_setup import create_agent_executor
from config import PERPLEXITY_API_KEY, OPENAI_API_KEY
import time

st.set_page_config(
    page_title="MincaAI Analyst Agent",
    layout="centered"
)

@st.cache_resource
def load_agent():
    return create_agent_executor()

# main interface
def main():
    st.title("MincaAI Analysis Agent")
    st.markdown("""
    **Analyze any industry sector or company portfolio**  
    *Example inputs:*  
    - `Tech and AI sector: Nvidia, Meta, Amazon`  
    - `Renewable energy sector: Tesla, NextEra Energy`  
    """)
    
    # Input box
    user_input = st.text_area(
        "Enter your analysis request:",
        height=150,
        placeholder="Enter sector/companies here..."
    )
    
    # Xử lý khi nhấn nút
    if st.button("Analyze", type="primary"):
        if not user_input.strip():
            st.error("Please enter a valid input")
            return
            
        with st.spinner("Analyzing market trends..."):
            try:
                start_time = time.time()
                agent = load_agent()
                result = agent.invoke({"input": user_input})
                processing_time = time.time() - start_time
                
                st.success(f"Analysis completed in {processing_time:.1f} seconds")
                st.subheader("Analysis Report")
                st.markdown("---")
                st.markdown(result['output'])
                
                with st.expander("Detailed Insights"):
                    st.markdown("""
                    **Key Trend Breakdown**  
                    *Automatically generated insights from raw data*
                    """)
                    
            except Exception as e:
                st.error(f"Analysis failed: {str(e)}")
                st.exception(e)

if __name__ == "__main__":
    main()