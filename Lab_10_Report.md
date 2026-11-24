# TFB3133 / TEB3133 Data Visualization
# Lab 10: Framing the Data Story — Audience-Focused Graphic Report

---

## 1. Executive Summary & Context

- **Course:** TFB3133 / TEB3133 Data Visualization
- **Topic:** Lab 10 — Framing the Data Story & Audience-Centered Design
- **Source Material Reference:** Lecture 3, *"The Audience"*, covering:
  - The Five Questions for Explaining Data Graphics
  - Pre-attentive Attributes (Color, Position, Form)
  - Minimizing Cognitive Overload & Maximizing Retention
  - Communicating the Key Message & Actionable Takeaways

---

## 2. Reframing the Story (Lesson 3.1)

### 2.1 Original Graphic Context (Lesson 1 & 2)
- **Original Audience:** Students who completed a self-rating survey about data visualization skills.
- **Original Decision / Question:** *"Where do my peers and I feel least confident, and what general topic should we look at?"*
- **Original Title:** `Plan a Workshop Around Students' Needs`
- **Original Takeaway:** `Data storytelling is the main area for support.`
- **Limitations:** The initial chart presented general awareness for students without actionable urgency, specific intervention targets, or operational benchmarks.

### 2.2 Reframed Context for the Target Audience
- **Target Audience:** **Workshop Instructor / Curriculum Lead**
- **Decision / Question to Answer:** 
  > *"How should workshop instructional time (3 hours), hands-on lab exercises, and teaching assistant (TA) support be distributed to maximize student learning outcomes?"*
- **Reframed Title:** `Workshop Instructor Briefing: Prioritize Python Coding in Workshop Schedule`
- **Reframed Key Takeaway:** 
  > `Python programming received the lowest average rating (2.1 / 5.0), falling 0.9 points below the 3.0 target competency threshold. Allocate 60% of hands-on lab time and dedicated TAs to Python syntax and environment scaffolding.`
- **Reasoning for Changes:**
  An instructor needs decision-oriented operational intelligence rather than passive descriptive summaries. By shifting the perspective to the instructor, the visual must directly inform time allocation, syllabus weighting, and resource deployment.

---

## 3. The Five Questions About the Graphic (Lecture 3 Framework)

| Question | Assessment & Explanation |
| :--- | :--- |
| **1. What do the axes mean?** | The vertical category axis displays the five assessed Data Visualization domains (`Python`, `Data storytelling`, `Chart selection`, `Color and labels`, `Data cleaning`). The horizontal numeric axis represents average self-rating on a 1.0 to 5.0 Likert scale (1 = Beginner, 5 = Confident). |
| **2. What do the encodings mean?** | **Bar length** encodes the quantitative average rating. **Color hue** serves as a pre-attentive indicator: vivid crimson (`#D9381E`) highlights the critical bottleneck (`Python`), while neutral slate (`#B0BEC5`) encodes non-critical skills. A **vertical dashed line** marks the 3.0 competency baseline. |
| **3. What level of detail is shown?** | Aggregate summary means from $n = 65$ pre-workshop student responses. The display omits individual respondent scatter to minimize visual noise and emphasize overall curriculum trends. |
| **4. Which data points should the audience notice?** | The audience immediately notices the top bar (`Python` at 2.1) due to contrasting color, top spatial positioning, an explicit callout annotation badge, and its clear shortfall against the 3.0 dashed baseline. |
| **5. What is the key takeaway?** | Python fundamentals represent the single greatest learning barrier; the instructor must restructure the workshop agenda to provide 60 minutes of hands-on Python scaffolding before advancing to complex charting. |

---

## 4. Graphic Improvements & Design Modifications (Lesson 3.2)

1. **Updated Data & Narrative Shift:**
   - Modified `Python` self-rating from 3.0 down to **2.1** (reflecting fresh pre-course diagnostic data).
   - This update shifts the lowest-rated skill from Data Storytelling (2.4) to **Python (2.1)**, altering the primary takeaway and driving curriculum reprioritization.
2. **Pre-attentive Visual Emphasis:**
   - **Color Contrast:** Replaced the low-contrast dual palette with a high-salience crimson (`#D9381E`) on the target bar and muted grayish-slate (`#B0BEC5`) on secondary bars.
   - **Position Encoding:** Sorted bars in ascending order (`Python` at the top). In Western reading patterns (top-to-bottom), placing the primary issue first commands immediate attention.
3. **Cognitive Load Reduction:**
   - **Direct Data Labelling:** Replaced ambiguous axis tracing with bold, direct numeric labels (`2.1 (Lowest)`) at the end of each bar.
   - **De-cluttering:** Removed top and right chart spines, removed redundant x-axis ticks, and lightened the horizontal grid to reduce visual friction (data-ink ratio optimization).
4. **Contextual Benchmarking & Annotation:**
   - Introduced a prominent **Target Competency Baseline (3.0)** dashed line.
   - Added an annotated callout box with a directional pointer specifying the exact action: *"Critical Skill Gap (2.1 / 5.0) — Requires 60m Hands-on Scaffolding"*.

---

## 5. Peer Evaluation & Feedback Revision (Lesson 3.3)

During the peer evaluation phase, the chart was presented to a classmate without reading the takeaway aloud:

- **What the Peer Understood:**
  - The peer instantly recognized the horizontal bar layout and stated that `Python` was highlighted as the lowest-rated subject.
  - They understood that 1 represented beginner level and 5 represented confident mastery.
- **What Was Initially Unclear:**
  - The peer asked whether a score of 2.1 was considered an alarming deficiency or merely an expected average for novices, noting that without an explicit standard or target benchmark, it was difficult to evaluate the severity of the gap.
  - They also noted that having both x-axis numbers and bar labels created slight duplication.
- **Revision Implemented After Feedback:**
  - **Added the 3.0 Competency Threshold Reference Line:** An explicit vertical reference line (`--`) clearly separates adequate baseline proficiency ($\ge 3.0$) from sub-standard proficiency ($< 3.0$), making the 0.9 deficit immediately discernible.
  - **Added the Explicit Action Annotation Box:** Integrated an annotated callout directly detailing the required instructional remedy (60m lab allocation).

---

## 6. Visual Comparison

### 6.1 Baseline Graphic (Lesson 2 — Student Perspective)
*Original file: `original_chart.png`*
- Generic title (`Data storytelling received the lowest average rating`)
- No explicit competency reference line
- Category order not optimized for urgency
- No actionable guidance for curriculum planning

### 6.2 Improved Graphic (Lesson 3 — Instructor Perspective)
*Final file: `final_chart.png`*
- Decision-driven headline (`Student Skill Self-Assessment: Python Coding Requires Urgent Intervention`)
- Pre-attentive color highlighting and top-ranked position encoding
- Explicit 3.0 competency threshold and callout annotation badge
- Direct data labels with de-cluttered background

---

## 7. Reflection: Visual Emphasis and Explanatory Text (150–200 Words)

> Visual emphasis and explanatory text serve as the bridge between raw data representation and human cognition. By leveraging pre-attentive attributes—specifically high-contrast color hue and strategic spatial positioning—a data visualization directs immediate, automatic visual perception to the focal insight before conscious cognitive processing begins. In our redesigned chart, highlighting the critical Python deficit in vibrant crimson against desaturated slate-gray peers eliminates the need for exhaustive visual scanning, instantaneously anchoring the viewer's attention.
>
> Simultaneously, explanatory text and contextual benchmarks minimize extraneous cognitive load. When audiences encounter unannotated graphics, they must mentally calculate differences, interpret arbitrary scales, and deduce implications. Integrating an explicit competency threshold line alongside direct value labels and an actionable callout directly answers the audience's five core questions. Rather than wondering whether a 2.1 rating is acceptable, the workshop instructor immediately understands the severity of the deficit and the necessary intervention. This dual synergy of selective visual contrast and concise explanatory framing prevents cognitive overload, enhances working memory retention, and transforms passive data viewing into decisive instructional action.

*(Word Count: 177 words)*

---

## 8. File Deliverables in `Lab 10` Folder

1. **`lab10.py`**: The complete, interactive Streamlit application containing the improved audience-focused visualization, toggleable baseline view, dynamic metrics, and five graphic question breakdown.
2. **`lab10_original.py`**: The baseline implementation from Lesson 2 for comparison.
3. **`generate_charts.py`**: Python script that renders and exports both charts at 300 DPI.
4. **`final_chart.png`**: High-resolution image of the finalized, improved chart for submission.
5. **`original_chart.png`**: High-resolution image of the baseline chart.
6. **`Lab_10_Report.md`**: Complete, structured assignment report and reflection.
