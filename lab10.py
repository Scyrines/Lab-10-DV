"""
TFB3133/TEB3133 Data Visualization
Lab 10: Framing the Data Story
Audience-Focused Data Storytelling Application

Audience: Workshop Instructor / Curriculum Lead
Takeaway: Python received the lowest average rating (2.1/5.0).
Allocate 60% of lab time and dedicated TAs to Python coding fundamentals.
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

# Set page configuration
st.set_page_config(
    page_title="Lab 10 | Audience-Focused Data Story",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------------------------
# Sidebar Controls & Context
# ---------------------------------------------------------
st.sidebar.title("Lab 10: Story Framing Controls")
st.sidebar.markdown(
    """
    **Audience Context:**  
    *Target Audience:* Workshop Instructor  
    *Decision Goal:* How to allocate workshop agenda, instructional hours, and teaching assistants.
    """
)

mode = st.sidebar.radio(
    "Select Display Version:",
    ["Improved (Audience: Workshop Instructor)", "Original Baseline (Audience: Students)"]
)

# ---------------------------------------------------------
# Data Preparation
# ---------------------------------------------------------
if mode == "Original Baseline (Audience: Students)":
    # Original Lesson 2 baseline data
    skills = ["Data storytelling", "Python", "Chart selection", "Color and labels", "Data cleaning"]
    ratings = [2.4, 3.0, 3.2, 3.7, 4.1]
    df = pd.DataFrame({"Skill": skills, "Average rating": ratings})
    
    # Baseline Page Content
    st.title("Plan a Workshop Around Students' Needs")
    st.info("**Audience:** Students who self-rated their data visualization skills.\n\n"
            "**Takeaway:** Data storytelling is the main area for support.")
    
    fig, ax = plt.subplots(figsize=(9, 4.8))
    bar_colors = ["#E07A3F"] + ["#4C78A8"] * (len(skills) - 1)
    bars = ax.barh(df["Skill"], df["Average rating"], color=bar_colors)
    ax.set_xlim(0, 5)
    ax.set_xticks(range(0, 6))
    ax.set_xlabel("Average self-rating (1 = beginner, 5 = confident)")
    ax.set_title("Data storytelling received the lowest average rating")
    ax.invert_yaxis()
    ax.grid(axis="x", color="#DDDDDD", linewidth=0.7)
    ax.set_axisbelow(True)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    
    for bar, value in zip(bars, ratings):
        ax.text(value + 0.05, bar.get_y() + bar.get_height() / 2,
                f"{value:.1f}", va="center")
    
    fig.tight_layout()
    st.pyplot(fig, clear_figure=True)
    st.caption("Fictional practice values. Ratings are averages on a 1-5 scale.")

else:
    # ---------------------------------------------------------
    # Lesson 3: Improved Display for Workshop Instructor
    # ---------------------------------------------------------
    # Updated rating: Python rating updated from 3.0 to 2.1
    # Demonstrating how changing one rating shifts the key takeaway to Python
    skills = ["Python", "Data storytelling", "Chart selection", "Color and labels", "Data cleaning"]
    ratings = [2.1, 2.4, 3.2, 3.7, 4.1]
    df = pd.DataFrame({"Skill": skills, "Average rating": ratings})
    
    # Sort data by rating ascending so lowest rating appears at the top
    df_sorted = df.sort_values(by="Average rating", ascending=True).reset_index(drop=True)
    
    st.title("Workshop Instructor Briefing: Prioritize Python Scaffolding")
    
    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown(
            """
            ### Executive Takeaway
            > **Actionable Directive:** **Python programming** emerged as the single largest competency deficit 
            > (**2.1 / 5.0**, well below the **3.0 minimum competency baseline**).  
            > **Recommendation:** Restructure the 3-hour workshop to dedicate **60 minutes** to guided 
            > Python syntax and environment setup, and pair each student group with a dedicated Lab TA.
            """
        )
    with col2:
        st.metric(label="Primary Focus Area", value="Python (2.1 / 5.0)", delta="-0.9 below baseline", delta_color="inverse")
        st.metric(label="Secondary Focus Area", value="Data Storytelling", delta="2.4 / 5.0", delta_color="off")

    st.markdown("---")

    # Matplotlib Visualization
    fig, ax = plt.subplots(figsize=(9.5, 5.0), dpi=150)
    
    # Pre-attentive feature: High contrast crimson (#D9381E) for target, muted slate (#B0BEC5) for others
    colors = ["#D9381E"] + ["#B0BEC5"] * (len(df_sorted) - 1)
    
    bars = ax.barh(df_sorted["Skill"], df_sorted["Average rating"], color=colors, height=0.62)
    
    # Invert y-axis so the lowest (top priority) is at the top
    ax.invert_yaxis()
    
    # Limits & styling
    ax.set_xlim(0, 5.2)
    
    # Explanatory reference line at competency benchmark (3.0)
    ax.axvline(x=3.0, color="#546E7A", linestyle="--", linewidth=1.5, alpha=0.85)
    ax.text(3.05, 4.3, "Target Competency Baseline (3.0)", color="#37474F",
            fontsize=10, fontweight="bold", fontstyle="italic", va="center")
    
    # Text annotation callout highlighting the main point
    ax.annotate(
        "Critical Skill Gap (2.1 / 5.0)\nRequires 60m Hands-on Scaffolding",
        xy=(2.1, 0),
        xytext=(2.65, 0.45),
        arrowprops=dict(facecolor="#D9381E", edgecolor="#B71C1C", shrink=0.08, width=1.5, headwidth=7),
        fontsize=10.5,
        fontweight="bold",
        color="#B71C1C",
        bbox=dict(boxstyle="round,pad=0.4", facecolor="#FFEBEE", edgecolor="#EF9A9A", alpha=0.95)
    )
    
    # Add value labels directly on the bars
    for i, (bar, value) in enumerate(zip(bars, df_sorted["Average rating"])):
        # Highlighted bar gets bold colored text
        if i == 0:
            ax.text(value + 0.08, bar.get_y() + bar.get_height() / 2,
                    f"{value:.1f}  (Lowest)", va="center", fontsize=11, fontweight="bold", color="#B71C1C")
        else:
            ax.text(value + 0.08, bar.get_y() + bar.get_height() / 2,
                    f"{value:.1f}", va="center", fontsize=10, color="#37474F")

    # Titles and labels revised for instructor audience
    ax.set_title("Student Skill Self-Assessment: Python Coding Requires Urgent Intervention",
                 fontsize=13, fontweight="bold", pad=14, loc="left", color="#212121")
    ax.set_xlabel("Average Self-Rating Score (1 = Beginner, 5 = Confident)", fontsize=10.5, labelpad=8, color="#424242")
    
    # Remove clutter: top and right spines, redundant vertical ticks
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color("#BDBDBD")
    ax.spines["bottom"].set_color("#BDBDBD")
    
    # Subtle background grid on x-axis
    ax.grid(axis="x", color="#ECEFF1", linestyle="-", linewidth=0.8)
    ax.set_axisbelow(True)
    
    # Format tick labels
    ax.tick_params(axis="y", labelsize=11, length=0)
    ax.tick_params(axis="x", labelsize=10, colors="#616161")
    
    fig.tight_layout()
    st.pyplot(fig, clear_figure=False)
    
    # Save chart image for submission
    chart_output_path = os.path.join(os.path.dirname(__file__), "final_chart.png")
    fig.savefig(chart_output_path, dpi=300, bbox_inches="tight")
    
    st.caption("Fictional student survey data (n = 65). Pre-workshop readiness assessment.")

    # ---------------------------------------------------------
    # Audience & Story Framework Summary (Assignment Lesson 3)
    # ---------------------------------------------------------
    with st.expander("View Lesson 3 Analysis & Five Graphic Questions", expanded=True):
        st.markdown(
            """
            #### 1. The Five Graphic Questions
            - **Axes Meaning:** The vertical axis lists 5 assessed Data Visualization skills. The horizontal axis represents the mean self-rating on a 1–5 Likert scale (1 = Beginner, 5 = Confident).
            - **Encoding Meaning:** Bar length encodes the average self-assessment score. The bright crimson bar encodes the target priority (lowest rating), while muted slate bars encode non-priority areas. The vertical dashed line encodes the required 3.0 competency threshold.
            - **Level of Detail:** Aggregate mean values across all surveyed students ($n = 65$).
            - **Noticeable Data Point:** The Python bar (2.1), accentuated via pre-attentive color contrast, top position, and an explicit callout annotation.
            - **Key Takeaway:** Python programming is the primary hurdle; workshop curriculum must be reallocated toward hands-on Python exercises.

            #### 2. Design Improvements Implemented
            - **Reframed for Workshop Instructor:** Shifted tone from general informational awareness to an actionable instructional decision.
            - **Pre-attentive Visual Hierarchy:** Used contrasting red hue against muted grey bars, plus position encoding (sorted lowest-to-highest).
            - **Reduced Overload:** Removed superfluous chart borders, added inline direct value labels, and provided an explicit threshold marker to avoid mental calculations.
            - **Iteration After Peer Feedback:** Added the **3.0 Competency Threshold Line** and an annotated callout box after classmate review confirmed that raw numbers alone lacked decision context.
            """
        )
