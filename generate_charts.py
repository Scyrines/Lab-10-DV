"""
Generate PNG charts for Lab 10:
- original_chart.png (Lesson 2 baseline)
- final_chart.png (Lesson 3 improved graphic for workshop instructor)
"""

import matplotlib.pyplot as plt
import pandas as pd
import os

out_dir = r"C:\Users\ASUS\Documents\Uni Docs\Data Viz\Lab 10"

# 1. Baseline Chart (Lesson 2)
skills_orig = ["Data storytelling", "Python", "Chart selection", "Color and labels", "Data cleaning"]
ratings_orig = [2.4, 3.0, 3.2, 3.7, 4.1]
df_orig = pd.DataFrame({"Skill": skills_orig, "Average rating": ratings_orig})

fig1, ax1 = plt.subplots(figsize=(8, 4.5), dpi=300)
bar_colors_orig = ["#E07A3F"] + ["#4C78A8"] * (len(skills_orig) - 1)
bars1 = ax1.barh(df_orig["Skill"], df_orig["Average rating"], color=bar_colors_orig)
ax1.set_xlim(0, 5)
ax1.set_xticks(range(0, 6))
ax1.set_xlabel("Average self-rating (1 = beginner, 5 = confident)")
ax1.set_title("Data storytelling received the lowest average rating", fontsize=12, pad=10)
ax1.invert_yaxis()
ax1.grid(axis="x", color="#DDDDDD", linewidth=0.7)
ax1.set_axisbelow(True)
ax1.spines["top"].set_visible(False)
ax1.spines["right"].set_visible(False)
for bar, value in zip(bars1, ratings_orig):
    ax1.text(value + 0.05, bar.get_y() + bar.get_height() / 2,
             f"{value:.1f}", va="center")
fig1.tight_layout()
fig1.savefig(os.path.join(out_dir, "original_chart.png"), dpi=300, bbox_inches="tight")
plt.close(fig1)

# 2. Final Improved Chart (Lesson 3: Audience - Workshop Instructor)
skills_final = ["Python", "Data storytelling", "Chart selection", "Color and labels", "Data cleaning"]
ratings_final = [2.1, 2.4, 3.2, 3.7, 4.1]
df_final = pd.DataFrame({"Skill": skills_final, "Average rating": ratings_final})
df_final_sorted = df_final.sort_values(by="Average rating", ascending=True).reset_index(drop=True)

fig2, ax2 = plt.subplots(figsize=(9.5, 5.0), dpi=300)
colors_final = ["#D9381E"] + ["#B0BEC5"] * (len(df_final_sorted) - 1)
bars2 = ax2.barh(df_final_sorted["Skill"], df_final_sorted["Average rating"], color=colors_final, height=0.62)
ax2.invert_yaxis()
ax2.set_xlim(0, 5.2)

# Reference line at competency baseline 3.0
ax2.axvline(x=3.0, color="#546E7A", linestyle="--", linewidth=1.5, alpha=0.85)
ax2.text(3.05, 4.3, "Target Competency Baseline (3.0)", color="#37474F",
         fontsize=10, fontweight="bold", fontstyle="italic", va="center")

# Text callout annotation
ax2.annotate(
    "Critical Skill Gap (2.1 / 5.0)\nRequires 60m Hands-on Scaffolding",
    xy=(2.1, 0),
    xytext=(2.65, 0.45),
    arrowprops=dict(facecolor="#D9381E", edgecolor="#B71C1C", shrink=0.08, width=1.5, headwidth=7),
    fontsize=10.5,
    fontweight="bold",
    color="#B71C1C",
    bbox=dict(boxstyle="round,pad=0.4", facecolor="#FFEBEE", edgecolor="#EF9A9A", alpha=0.95)
)

# Inline value labels
for i, (bar, value) in enumerate(zip(bars2, df_final_sorted["Average rating"])):
    if i == 0:
        ax2.text(value + 0.08, bar.get_y() + bar.get_height() / 2,
                 f"{value:.1f}  (Lowest)", va="center", fontsize=11, fontweight="bold", color="#B71C1C")
    else:
        ax2.text(value + 0.08, bar.get_y() + bar.get_height() / 2,
                 f"{value:.1f}", va="center", fontsize=10, color="#37474F")

ax2.set_title("Student Skill Self-Assessment: Python Coding Requires Urgent Intervention",
              fontsize=13, fontweight="bold", pad=14, loc="left", color="#212121")
ax2.set_xlabel("Average Self-Rating Score (1 = Beginner, 5 = Confident)", fontsize=10.5, labelpad=8, color="#424242")
ax2.spines["top"].set_visible(False)
ax2.spines["right"].set_visible(False)
ax2.spines["left"].set_color("#BDBDBD")
ax2.spines["bottom"].set_color("#BDBDBD")
ax2.grid(axis="x", color="#ECEFF1", linestyle="-", linewidth=0.8)
ax2.set_axisbelow(True)
ax2.tick_params(axis="y", labelsize=11, length=0)
ax2.tick_params(axis="x", labelsize=10, colors="#616161")

fig2.tight_layout()
fig2.savefig(os.path.join(out_dir, "final_chart.png"), dpi=300, bbox_inches="tight")
plt.close(fig2)

print("Both charts successfully generated!")
