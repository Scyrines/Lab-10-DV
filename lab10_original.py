import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Lab 10 | Data Story", layout="wide")

skills = ["Data storytelling", "Python", "Chart selection",
          "Color and labels", "Data cleaning"]
ratings = [2.4, 3.0, 3.2, 3.7, 4.1]
df = pd.DataFrame({"Skill": skills, "Average rating": ratings})

st.title("Plan a Workshop Around Students' Needs")
st.write("Audience: students who self-rated their data visualization skills.")
st.write("Takeaway: data storytelling is the main area for support.")

fig, ax = plt.subplots(figsize=(8, 4.5))
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
